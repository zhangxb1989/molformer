"""Independent audit of released PeptideCLM-2 THPep predictions.

Requires NumPy and pandas. Tested with NumPy 2.3.5 and pandas 3.0.1.
Split reconstruction follows scikit-learn 1.7.2's documented stratified-shuffle
allocation and permutation order; references are in ../thpep_evidence.json.
This is independently written analysis, not execution of author training code.
All source CSV bytes must match pinned Git blob IDs before they are processed.
See ../thpep_protocol_audit.md for interpretation and scope limits.
"""
import json,math,pathlib,hashlib,collections
import numpy as np
import pandas as pd
import argparse, urllib.request

parser = argparse.ArgumentParser(description="Audit released THPep predictions; no training.")
parser.add_argument('--input-dir', type=pathlib.Path, required=True)
parser.add_argument('--output', type=pathlib.Path, required=True)
parser.add_argument('--download', action='store_true', help='Download 10 public CSV files at the pinned author commit.')
args = parser.parse_args()
root = args.input_dir
evidence_path = pathlib.Path(__file__).resolve().parents[1] / 'thpep_evidence.json'
evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
input_files = [evidence['source_data']] + evidence['predictions']
input_hashes = []
for entry in input_files:
    path = root / entry['local_name']
    if args.download:
        path.parent.mkdir(parents=True, exist_ok=True)
        request = urllib.request.Request(entry['raw_url'], headers={'User-Agent': 'Literature-evidence-audit/1.0'})
        with urllib.request.urlopen(request, timeout=90) as response:
            content = response.read()
        # Validate before saving or processing any downloaded input.
        blob = hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
        if blob != entry['git_blob_sha']:
            raise ValueError('Unexpected download bytes: '+entry['local_name'])
        path.write_bytes(content)
    content = path.read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    if blob != entry['git_blob_sha']:
        raise ValueError('Unexpected input bytes: '+entry['local_name'])
    input_hashes.append({'file': entry['local_name'], 'bytes': len(content), 'git_blob_sha': blob, 'sha256': hashlib.sha256(content).hexdigest()})
source = pd.read_csv(root/'THPep_source.csv')


def allocation(counts,n,rng):
    expected=counts/counts.sum()*n; result=np.floor(expected); left=int(n-result.sum())
    if left:
        fractions=expected-result
        for remainder in np.sort(np.unique(fractions))[::-1]:
            candidates=np.where(fractions==remainder)[0]; take=min(len(candidates),left)
            chosen=rng.choice(candidates,size=take,replace=False);result[chosen]+=1;left-=take
            if left==0:break
    return result.astype(int)

def stratified_holdout(frame,seed):
    y=frame['class'].to_numpy();_,inverse=np.unique(y,return_inverse=True)
    counts=np.bincount(inverse); groups=np.split(np.argsort(inverse,kind='mergesort'),np.cumsum(counts)[:-1])
    ntest=math.ceil(len(frame)*0.2);ntrain=len(frame)-ntest;rng=np.random.RandomState(seed)
    n=allocation(counts,ntrain,rng);t=allocation(counts-n,ntest,rng);tr=[];te=[]
    for i,group in enumerate(groups):
        shuffled=group[rng.permutation(counts[i])];tr.extend(shuffled[:n[i]]);te.extend(shuffled[n[i]:n[i]+t[i]])
    tr=rng.permutation(tr);te=rng.permutation(te)
    return frame.iloc[tr],frame.iloc[te]

def metrics(y,score,threshold):
    pred=score>=threshold;pos=y==1;neg=~pos
    tp=int((pred&pos).sum());tn=int((~pred&neg).sum());fp=int((pred&neg).sum());fn=int((~pred&pos).sum())
    den=math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn));mcc=(tp*tn-fp*fn)/den if den else 0.0
    f1=2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0.0
    p=score[pos];n=score[neg];auc=float(((p[:,None]>n).sum()+0.5*(p[:,None]==n).sum())/(len(p)*len(n)))
    return {'mcc':mcc,'f1':f1,'auroc':auc,'threshold':float(threshold),'confusion':{'tn':tn,'fp':fp,'fn':fn,'tp':tp}}

result={'method':'Independent NumPy implementation of stratified shuffle allocation/permutation as documented in scikit-learn 1.7.2; no author training code executed. Metrics recalculated from released predictions only.','numpy_version':np.__version__,'pandas_version':pd.__version__,'source_rows':len(source),'unique_smiles':source['smiles'].nunique(),'class_counts':{str(k):int(v) for k,v in source['class'].value_counts().items()},'runs':[]}
for seed in [101,202,303]:
    trainval,test=stratified_holdout(source,seed*45671);train,val=stratified_holdout(trainval,seed*52984)
    for path in sorted(root / f'THPep_{model}_{seed}.csv' for model in ['hybrid', 'mlm', 'mtr']):
        model=path.stem.split('_')[1];pred=pd.read_csv(path); y=pred['true_label'].to_numpy().astype(int);score=pred['predicted_label'].to_numpy()
        assert pred[['true_label','predicted_label']].notna().all().all()
        assert set(y)=={0,1} and np.isfinite(score).all()
        expected=list(zip(test['smiles'],test['class']));actual=list(zip(pred['smiles'],pred['true_label']))
        candidates=[]
        for t in np.unique(score):
            if len(np.unique(score>=t))==2:candidates.append(metrics(y,score,t))
        optimum=max(candidates,key=lambda x:x['mcc'])
        result['runs'].append({'seed':seed,'model':model,'rows':len(pred),'reconstructed_counts':{'train':len(train),'validation':len(val),'test':len(test)},'test_multiset_matches':collections.Counter(expected)==collections.Counter(actual),'test_order_matches':expected==actual,'test_class_counts':{str(k):int(v) for k,v in pred['true_label'].value_counts().items()},'score_min':float(score.min()),'score_max':float(score.max()),'fixed_logit_zero':metrics(y,score,0.0),'test_optimized_threshold':optimum})
models=sorted(set(r['model'] for r in result['runs']));result['summary']={}
for model in models:
    runs=[r for r in result['runs'] if r['model']==model];result['summary'][model]={}
    for kind in ['fixed_logit_zero','test_optimized_threshold']:
        result['summary'][model][kind]={m:{'mean':float(np.mean([r[kind][m] for r in runs])),'sample_sd':float(np.std([r[kind][m] for r in runs],ddof=1)),'population_sd':float(np.std([r[kind][m] for r in runs],ddof=0))} for m in ['mcc','auroc','f1']}

# Independent hand-checks for confusion-matrix signs and AUC ties.
check_y = np.array([0, 0, 1, 1])
assert metrics(check_y, np.array([-2., -1., 1., 2.]), 0)['mcc'] == 1
assert metrics(check_y, np.array([2., 1., -1., -2.]), 0)['mcc'] == -1
assert metrics(check_y, np.ones(4), 0)['auroc'] == .5
assert metrics(check_y, np.array([-1., 1., -1., 1.]), 0)['f1'] == .5
assert len(result['runs']) == 9
assert all(r['test_multiset_matches'] and r['test_order_matches'] for r in result['runs'])
# Official final SI Table S8, PDF page S7. Mean +/- sample SD, printed to 3 decimals.
published = {
    'mlm': {'mcc': [.756,.019], 'auroc': [.949,.006], 'f1': [.826,.012]},
    'hybrid': {'mcc': [.747,.036], 'auroc': [.940,.019], 'f1': [.818,.022]},
    'mtr': {'mcc': [.698,.036], 'auroc': [.924,.016], 'f1': [.784,.029]},
}
comparisons = []
for model, row in published.items():
    for metric, numbers in row.items():
        for stat, expected in zip(['mean', 'sample_sd'], numbers):
            actual = result['summary'][model]['test_optimized_threshold'][metric][stat]
            matches = f'{actual:.3f}' == f'{expected:.3f}'
            comparisons.append({'model':model, 'metric':metric, 'statistic':stat, 'published':expected, 'recomputed':actual, 'matches_at_3_decimals':matches})
assert all(c['matches_at_3_decimals'] for c in comparisons)
result['input_hashes'] = input_hashes
result['published_table_s8_comparison'] = comparisons
result['verification'] = {'input_blobs_verified':len(input_hashes), 'test_exports_exactly_matched':9, 'table_s8_values_matched':len(comparisons), 'metric_hand_checks_passed':True, 'trained_models':0, 'author_code_executed':False}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2)+'\n').encode('utf-8'))
print(json.dumps(result['verification']))
