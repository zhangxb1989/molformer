# 阶段 2：逐篇结构化分析

NR = 本轮未取得足够证据，不等于原文没有报告。全文关键部分阅读不等于已经运行作者代码；所有性能数字都是作者报告，非本轮复现实验。正文与预印本版本严格区分。

术语：AA=氨基酸序列；SMILES=分子线性表示；AIP=抗炎肽；AMP=抗菌肽；PAMPA=人工膜通透性实验。

## F01 · MoLFormer（2022）

Large-scale chemical language representations capture molecular structure and properties

来源：[10.1038/s42256-022-00580-7](https://www.nature.com/articles/s42256-022-00580-7)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 小分子性质预测的基础表征；不在三年主窗口。 |
| 数据集与标签 | PubChem/ZINC 无标签预训练；下游多种分子分类/回归基准。 |
| 输入与表示 | SMILES。 |
| 模型与预训练 | 线性注意力、旋转位置编码的 MolFormer；原论文最大约 11 亿分子，公开 fork checkpoint 约 1 亿。 |
| Loss | 预训练 MLM；各下游目标须按配置区分。 |
| Inference | 分子编码器加性质预测头；具体权重须核对。 |
| Metrics | 分类 AUROC、回归误差等随任务变化，不是用户任务实测分数。 |
| 划分与泄漏控制 | 原论文基准协议不能自动等同于用户划分。 |
| 限制与可比性 | 本轮主要核对摘要、官方代码与 checkpoint 说明；不声称逐项复现原论文。 |
| 证据位置 | 出版社摘要；IBM/molformer README pretrained models。 |


## P01 · Representation_limits_comment（2023）

Limitations of representation learning in small molecule property prediction

来源：[10.1038/s41467-023-41967-3](https://pmc.ncbi.nlm.nih.gov/articles/PMC10575963/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 分子表征局限的评论，非独立预测模型。 |
| 数据集与标签 | 讨论相关评估研究，没有新的独立任务数据集。 |
| 输入与表示 | 指纹、描述符与学习表征的适用边界。 |
| 模型与预训练 | 无新增训练模型。 |
| Loss | 不适用。 |
| Inference | 不适用。 |
| Metrics | 不产生可与用户实验比较的新成绩。 |
| 划分与泄漏控制 | 关注数据、划分和模型复杂度的解释。 |
| 限制与可比性 | 应与 P23 原始研究分开引用；不把评论计为一次独立基准实验。 |
| 证据位置 | 正文评论全文。 |


## P02 · PeptideBERT（2023）

PeptideBERT: A Language Model Based on Transformers for Peptide Property Prediction

来源：[10.1021/acs.jpclett.3c02398](https://pmc.ncbi.nlm.nih.gov/articles/PMC10683064/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 溶血、溶解性、nonfouling 三个独立二分类任务。 |
| 数据集与标签 | DBAASP v3 溶血 9,316 条、约 19.6% 阳性；PROSO II 溶解性 18,453；nonfouling 3,600 阳性和 13,585 阴性。 |
| 输入与表示 | 氨基酸序列。 |
| 模型与预训练 | ProtBERT 预训练编码器加分类头，分别微调。 |
| Loss | 二元交叉熵 BCE。 |
| Inference | sigmoid，阈值 0.5；各任务独立预测。 |
| Metrics | accuracy；溶血 86.051%，溶解性增强设置 70.018%，nonfouling 88.365%，不可跨任务排名。 |
| 划分与泄漏控制 | 随机 81/9/10；增强在训练集。 |
| 限制与可比性 | 溶血数据存在重复/冲突序列，需重做分组去重；不是 MolFormer 或多酚模型。 |
| 证据位置 | Methods: Datasets、Model architecture/training；Results。 |


## P03 · ActFound（2024）

A bioactivity foundation model using pairwise meta-learning

来源：[10.1038/s42256-024-00876-w](https://www.nature.com/articles/s42256-024-00876-w)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 少样本 assay 内定量生物活性回归。 |
| 数据集与标签 | 约 160 万活性记录、35,644 个 ChEMBL assays；多组 ChEMBL/BindingDB 等评估。 |
| 输入与表示 | 化合物与 assay 内成对活性关系。 |
| 模型与预训练 | ActFound：跨 assay 元学习及成对活性差学习；不能因为 foundation model 就称其为语言模型。 |
| Loss | 成对学习目标；完整公式本轮未核实，NR。 |
| Inference | 用支持化合物适应 assay，再预测查询化合物。 |
| Metrics | 以定量回归表现为主；各基准指标与数值未逐项核实，NR。 |
| 划分与泄漏控制 | assay 内/跨 assay 协议需据全文或代码进一步确认。 |
| 限制与可比性 | 只读出版社摘要及官方项目说明；不能作为现有二分类的分数对手。 |
| 证据位置 | 出版社摘要；BFeng14/ActFound 官方 README。 |


## P04 · AutoPeptideML（2024）

AutoPeptideML: a study on how to build more trustworthy peptide bioactivity predictors

来源：[10.1093/bioinformatics/btae555](https://pmc.ncbi.nlm.nih.gov/articles/PMC11438549/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 18 个多肽二分类任务的可信评估与自动建模。 |
| 数据集与标签 | 单任务约 200–20,000；APML-Peptipedia 阴性候选池 92,092 肽、128 活性。 |
| 输入与表示 | 序列的 PLM 表征或 one-hot。 |
| 模型与预训练 | RF、LightGBM、KNN 调参并集成。 |
| Loss | 算法各自训练目标；模型选择最大化交叉验证 MCC，无统一神经 loss。 |
| Inference | 3 类模型×10 折共 30 模型概率均值，阈值 >0.5。 |
| Metrics | MCC 为核心，3 次重复；不把不同任务分数合成用户项目结论。 |
| 划分与泄漏控制 | 对比 Original/NegSearch/NegSearch+HP；CCPart 30% 局部序列相似性约束，20% 测试，训练内 10 折。 |
| 限制与可比性 | 排除相关活性的负池与长度匹配有参考价值；缺失功能标签仍不等于真阴性。 |
| 证据位置 | Methods: datasets、negative sampling、homology partition、AutoPeptideML；IBM/AutoPeptideML。 |


## P05 · PepNet（2024）

PepNet: an interpretable neural network for anti-inflammatory and antimicrobial peptides prediction using a pre-trained protein language model

来源：[10.1038/s42003-024-06911-1](https://www.nature.com/articles/s42003-024-06911-1)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | AIP 抗炎与 AMP 抗菌分别二分类。 |
| 数据集与标签 | 数据准备节：AIP 4,194（2,516/629/1,049）；AMP 8,346（5,340/1,336/1,670）；IEDB、APD3/DADP 等。 |
| 输入与表示 | one-hot、14 理化特征、ProtT5 表征；固定长度 40。 |
| 模型与预训练 | 预训练特征加残差膨胀 CNN、Transformer、池化和 MLP。 |
| Loss | 已读主文未明确核实具体训练损失，NR，不能默认写 CE。 |
| Inference | 两类 softmax 输出。 |
| Metrics | ACC、P/R、F1、MCC；AMP F1 0.951、MCC 0.901。 |
| 划分与泄漏控制 | 训练/验证/测试预划分，未建立严格结构外推证据。 |
| 限制与可比性 | 后面的 Statistics 节把 AIP/AMP 数据名对调；此处按数据准备节记录，复现须核对实际文件。 |
| 证据位置 | Methods: Data preparation、architecture；Results/Table；Statistics and reproducibility。 |


## P06 · DeepAIP（2024）

DeepAIP: Deep learning for anti-inflammatory peptide prediction using pre-trained protein language model features based on contextual self-attention network

来源：[10.1016/j.ijbiomac.2024.136172](https://pubmed.ncbi.nlm.nih.gov/39357724/)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 抗炎肽二分类。 |
| 数据集与标签 | 基准 AIP 数据；另报告 17 个新增阳性肽；精确主数据规模与负例构造 NR。 |
| 输入与表示 | 肽序列的 ProtT5 嵌入。 |
| 模型与预训练 | DeepAIP，结合上下文自注意力和多尺度卷积。 |
| Loss | NR：摘要不足以确认。 |
| Inference | 输出 AIP 预测；阈值 NR。 |
| Metrics | 摘要报告 ACC/MCC 改善；未核对完整表，不搬用增幅作为统一指标。 |
| 划分与泄漏控制 | 训练测试与同源性约束 NR。 |
| 限制与可比性 | 仅摘要/官方代码入口；17 个全阳性外部样本不能估计特异度。 |
| 证据位置 | PubMed 39357724 摘要；YangQingGuoCCZU/DeepAIP。 |


## P07 · Deep2Pep（2024）

Deep2Pep: A deep learning method in multi-label classification of bioactive peptide

来源：[10.1016/j.compbiolchem.2024.108021](https://www.sciencedirect.com/science/article/pii/S1476927124000094)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 抗菌、抗高血压、抗氧化、抗高血糖四功能多标签。 |
| 数据集与标签 | 数据量、每类计数和负标签定义本轮未核实。 |
| 输入与表示 | 序列编码、embedding 与语言 tokenizer。 |
| 模型与预训练 | Deep2Pep：BiLSTM/注意力残差及 BERT encoder；摘要不能证明使用大规模预训练 BERT。 |
| Loss | NR。 |
| Inference | 多标签输出；逐标签阈值 NR。 |
| Metrics | 指标详细定义与结果 NR。 |
| 划分与泄漏控制 | 去重、同源性、划分 NR。 |
| 限制与可比性 | 仅摘要可得；可作多功能任务参考，不是单标签屏障活性的直接基线。 |
| 证据位置 | 出版社/PubMed 38308955 摘要。 |


## P08 · PeptideCLM（2025）

Peptide-Aware Chemical Language Model Successfully Predicts Membrane Diffusion of Cyclic Peptides

来源：[10.1021/acs.jcim.4c01441](https://pmc.ncbi.nlm.nih.gov/articles/PMC11971985/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 环肽膜扩散/通透性回归及派生分类。 |
| 数据集与标签 | CycPeptMPDB 的 PAMPA 子集，移除检测下限 -10；不能把约 7,500 条总库规模当最终训练样本数。 |
| 输入与表示 | 肽与小分子 SMILES，长度 768。 |
| 模型与预训练 | 44M 参数 PeptideCLM；约 2,300 万肽/小分子混合预训练。 |
| Loss | 下游回归 MSE。 |
| Inference | 五模型均值；由 logPexp 阈值 -5.5 派生类别。 |
| Metrics | AUROC 0.781±0.067、AUPRC 0.738±0.161、RMSE 0.742±0.214（对应文中混合预训练设置）。 |
| 划分与泄漏控制 | PCA 后 K-means 六簇，轮流留一簇测试，其余数据建五折集成。 |
| 限制与可比性 | 不是 TJ 活性。作者预训练数据有后续修正版，复现应核对 Zenodo 15042141 说明及版本。 |
| 证据位置 | Methods、Table results；PMC11971985；作者数据发布说明。 |


## P09 · PepLand（2025）

PepLand: a large-scale pre-trained peptide representation model for a comprehensive landscape of both canonical and non-canonical amino acids

来源：[10.1093/bib/bbaf367](https://pmc.ncbi.nlm.nih.gov/articles/PMC12315545/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 典型与非典型肽的穿膜、溶解性、结合等性质。 |
| 数据集与标签 | 五个主要基准：canonical CPP/Sol/Binding 与 noncanonical CPP/Binding；预训练为大规模典型肽再适应修饰肽。 |
| 输入与表示 | SMILES 分子图，原子/片段信息及 AdaFrag。 |
| 模型与预训练 | PepLand 两阶段预训练，GRU/预测头；可探针或微调。 |
| Loss | 遮盖属性预测；具体目标和各任务 loss 本轮未完整核实，NR。 |
| Inference | 表征池化后分类/回归。 |
| Metrics | 主表按任务用 AUC 或 Spearman；ncCPP 0.628、ncBinding 0.768 为相应 Spearman 设置。 |
| 划分与泄漏控制 | 按其各数据基准；不能推定所有集合均同源/骨架分离。 |
| 限制与可比性 | 图模型，不等同 SMILES 语言模型；图注与表的指标描述须按具体任务核对。 |
| 证据位置 | Main Table 1；Methods: pretraining、datasets；PMC12315545。 |


## P10 · Peptide_generalization（2025）

How to build machine learning models able to extrapolate from standard to modified peptides

来源：[10.1186/s13321-025-01115-z](https://pmc.ncbi.nlm.nih.gov/articles/PMC12751563/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 标准肽内、修饰肽内插值以及标准→修饰外推。 |
| 数据集与标签 | 八数据集：结合 1,002/299；穿膜 2,324/480；抗菌 9,855/1,880；抗病毒 4,754/444（标准/修饰）。 |
| 输入与表示 | 指纹、SMILES 化学模型、蛋白模型、PepLand 等表征。 |
| 模型与预训练 | MolFormer、ChemBERTa-2、PeptideCLM、ESM/ProtT5 等固定表征接 SVM/LightGBM。 |
| Loss | 各下游算法原生目标，无统一深度 loss。 |
| Inference | 分类分数或定量结合预测。 |
| Metrics | 分类 MCC、回归 Spearman（文中 SPCC）；相似性阈值与表现也做相关分析。 |
| 划分与泄漏控制 | 相似性分割 CCPart；5 折、200 Optuna trials、5 seeds；外推用全部标准肽训练、修饰肽测试。 |
| 限制与可比性 | 负例有“其他活性”来源，不必然真阴性；直接证明已有 MolFormer 肽任务先例。 |
| 证据位置 | Methods datasets/representations/partition；Figs 4–6；IBM/PeptideGeneralizationBenchmarks。 |


## P11 · AOP_DRL（2025）

AOP-DRL: A deep representation learning framework for the computational prediction of antioxidant peptides

来源：[10.1016/j.csbj.2025.08.014](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800373/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 抗氧化肽二分类。 |
| 数据集与标签 | AnOxPePred 来源 1,404：687 阳性（456 清除自由基、231 螯合）和 717 阴性。 |
| 输入与表示 | ESM-2 650M 残基表征，1,280 维。 |
| 模型与预训练 | AOP-DRL：ESM-2 加 TextCNN 和分类头。 |
| Loss | 已读正文未清楚确定完整损失，NR。 |
| Inference | softmax、阈值 0.5。 |
| Metrics | ACC、MCC、Recall、F1、AUROC；不把 ESM 单独基线的 AUROC 误报为最终模型。 |
| 划分与泄漏控制 | 80/20 分层、P60/70/80/90 相似性设置与 5 折；相互嵌套关系须代码确认。 |
| 限制与可比性 | 文本对全量训练/部分冻结及对比学习描述不完全一致，不能直接沿用全部宣传语。 |
| 证据位置 | Methods: Dataset、ESM-2/TextCNN、Evaluation；PMC12800373。 |


## P12 · MFP_MFL（2025）

MFP-MFL: Leveraging Graph Attention and Multi-Feature Integration for Superior Multifunctional Bioactive Peptide Prediction

来源：[10.3390/ijms26031317](https://pmc.ncbi.nlm.nih.gov/articles/PMC11818429/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 五功能多标签：AMP/AIP/AHP/ACP/ADP。 |
| 数据集与标签 | 表 2：单功能 5,719，双功能 198；据此为 5,917 独立序列，标签条目不能当独立样本。 |
| 输入与表示 | ESM-2、ProtT5、RoBERTa 多特征融合。 |
| 模型与预训练 | MFP-MFL：GAT、FGM 对抗训练、加权集成。 |
| Loss | Linit+Ladv；印刷公式仅列 y log p 项，完整 BCE 的负类项须检查代码。 |
| Inference | 每功能 sigmoid，集成输出；阈值未核实。 |
| Metrics | 多标签 precision、coverage、accuracy、exact match、absolute false；主表 accuracy 0.786、precision 0.799。 |
| 划分与泄漏控制 | 文中训练/验证流程须结合数据文件确认；未认定严格同源外推。 |
| 限制与可比性 | 结论部分交换部分指标对应关系，采用主表；不能把多标签 accuracy 与二分类 accuracy 等同。 |
| 证据位置 | Methods/Data preparation、Loss；Tables 1–2；PMC11818429。 |


## P13 · BPFun（2025）

BPFun: a deep learning framework for bioactive peptide function prediction using multi-label strategy by transformer-driven and sequence rich intrinsic information

来源：[10.1186/s12859-025-06190-5](https://link.springer.com/article/10.1186/s12859-025-06190-5)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 七功能多标签，含抗氧化与抗炎等。 |
| 数据集与标签 | 各标签计数可重叠：AMP 2409、ACP 646、ADP 514、AHP 868、AIP 1678、AAP 134、AOP 318；154 个双标签。 |
| 输入与表示 | 序列及丰富内在特征。 |
| 模型与预训练 | BPFun：Transformer、BiLSTM、注意力；不能仅因 Transformer 就归为预训练大模型。 |
| Loss | 主文明示 MSE，而非假定 BCE。 |
| Inference | 七个 sigmoid 输出，阈值 >0.5。 |
| Metrics | 多标签 precision/coverage/accuracy、absolute true/false、F1。 |
| 划分与泄漏控制 | CD-HIT 0.9 去冗余、长度≥5，再随机 80/20。 |
| 限制与可比性 | 先去冗余后随机分割不等于相似性隔离；序列遮盖增强需限制在训练内。 |
| 证据位置 | Methods: model/loss、dataset；BMC 主文。 |


## P14 · PeptiVerse（2026）

PeptiVerse: A unified platform for therapeutic peptide property prediction

来源：[10.1038/s41467-026-74167-w](https://pmc.ncbi.nlm.nih.gov/articles/PMC13388690/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 七类治疗肽性质：溶血、溶解性、nonfouling、毒性、通透性、半衰期、亲和力。 |
| 数据集与标签 | 例：溶血 6,076；修饰肽通透性 7,475；典型 CPP 2,324；半衰期按 AA/SMILES 为 130/245。 |
| 输入与表示 | AA 与 SMILES 两类输入。 |
| 模型与预训练 | 冻结 ESM-2、PeptideCLM、ChemBERTa，加传统或深度预测器；结合任务用交叉注意力。 |
| Loss | 各算法不同；回归包括 MSE/Huber 等设置，不能写一个统一 loss。 |
| Inference | 单性质预测；可用集成和熵估计不确定性，不代表已证明概率校准。 |
| Metrics | 分类 F1/AUROC；回归 r、rho、R²、RMSE/MAE；深度模型重复 seeds。 |
| 划分与泄漏控制 | 序列/SMILES 聚类 80/20；结合按亲和力分布匹配，不能称严格冷靶点；半衰期 5 折。 |
| 限制与可比性 | 正式版 2026-07-16；早期预印本归并；小样本冻结特征流程值得复用。 |
| 证据位置 | Methods: data splitting、model training、evaluation；PMC13388690 正式版。 |


## P15 · PeptideCLM2（2026）

Scaling SMILES-Based
Chemical Language Models for
Therapeutic Peptide Engineering

来源：[10.1021/acs.jcim.6c00652](https://pubs.acs.org/doi/10.1021/acs.jcim.6c00652)。阅读：preprint_full_text；bioRxiv preprint v5, 2026-06-23; final metadata verified separately。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 治疗肽通透性、半衰期及相关功能预测。 |
| 数据集与标签 | CycPeptMPDB、THPep、CellPPD、AmpHGT、PepMSND；预训练含逾亿小分子与肽。 |
| 输入与表示 | SMILES。 |
| 模型与预训练 | PeptideCLM-2 多个规模/预训练目标变体，约 32–337M 参数。 |
| Loss | 所读预印本：MLM 掩码 25%、99 个 RDKit 属性 MTR、混合 0.6MLM+0.4MTR；下游精确 loss NR。 |
| Inference | 更换预测头后微调；与 RDKit/Morgan 集成基线比较。 |
| Metrics | 各任务分类/回归指标不同；本轮不逐项抄录未核对的最终版数值。 |
| 划分与泄漏控制 | 使用基准划分；THPep 随机 5 折；3 seeds；文中有预训练重叠审计。 |
| 限制与可比性 | 正式版 DOI 已核实，但方法阅读的是 2026-06-23 预印本 v5，不能声称所有细节已与正式版一致。 |
| 证据位置 | PMC12803269 预印本 Methods/Table 2；正式 DOI 10.1021/acs.jcim.6c00652。 |


## P16 · LANTERN（2026）

LANTERN: TCR-peptide binding prediction
                    <i>via</i>
                    large language model representations

来源：[10.7717/peerj.20980](https://pmc.ncbi.nlm.nih.gov/articles/PMC13045841/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | TCR β 链与肽是否结合的二分类。 |
| 数据集与标签 | TCHard 的 NA/RN/GenNA/GenRN；约 160k TCR、1,341 独立肽；不同 fold 配对数不同。 |
| 输入与表示 | TCR 氨基酸序列，肽转 SMILES。 |
| 模型与预训练 | LANTERN：ESM + MolFormer，multi-head cross-attention 与 MLP。 |
| Loss | BCE；可加入 MSE 对齐项。 |
| Inference | 输出配对结合概率；冻结/微调配置随实验变化。 |
| Metrics | 主指标 AUROC，另 ACC、Recall、Precision、F1、AUPRC；5 folds×3 seeds。 |
| 划分与泄漏控制 | 按肽分组训练/验证，测试评估未见肽，区分随机负例与参考负例。 |
| 限制与可比性 | “zero-shot”指该设置中的未见肽，不是无监督且无需任务训练；不能支持首次 MolFormer 肽建模。 |
| 证据位置 | Methods/Loss；Benchmark evaluation；PMC13045841。 |


## P17 · PepBenchmark（2026）

PepBenchmark: A Standardized Benchmark for Peptide Machine Learning

来源：[正式入口](https://proceedings.iclr.cc/paper_files/paper/2026/hash/56a225639da77e8f7c0409f6d5ba996b-Abstract-Conference.html)。阅读：full_text_key_sections；arXiv full text and official proceedings PDF。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 标准化肽机器学习基准。 |
| 数据集与标签 | 35 数据集：29 典型、6 非典型；27 分类、8 回归；7 组用途。 |
| 输入与表示 | 指纹、GNN、蛋白语言模型、SMILES 模型。 |
| 模型与预训练 | PepBenchmark 统一数据、流水线和模型比较。 |
| Loss | 随具体模型/任务而变，无单一基准 loss。 |
| Inference | 按共同数据处理与评估接口输出分类/回归结果。 |
| Metrics | 分类 AUROC、回归 MAE；跨 5 个划分汇总均值/标准差。 |
| 划分与泄漏控制 | 8/1/1；典型肽 k-mer/MMseqs2 约 0.3；非典型 ECFP 相似性约 0.95；配对任务蛋白冷划分。 |
| 限制与可比性 | 特征匹配阴性仍需审查语义；已确认 ICLR 2026 正式会议论文，不仅是 arXiv。 |
| 证据位置 | 官方 proceedings 与论文正文；ZGCI-AI4S-Pep/PepBenchmark。 |


## P18 · Phenols_CDFT（2024）

Accurate &amp; simple open-sourced no-code machine learning and CDFT predictive models for the antioxidant activity of phenols

来源：[10.1016/j.comptc.2024.114782](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 酚类 DPPH 抗氧化分类。 |
| 数据集与标签 | 酚类定量/分类资料；精确清洗后数量与标签界值 NR。 |
| 输入与表示 | 量子 CDFT 与分子描述符。 |
| 模型与预训练 | J48、RandomTree、JCHAID 等树模型及特征选择。 |
| Loss | 各树模型目标；精确设置 NR。 |
| Inference | 抗氧化类别预测；阈值 NR。 |
| Metrics | 摘要及页面片段不足以完整核对结果，NR。 |
| 划分与泄漏控制 | 训练测试划分、嵌套特征筛选 NR。 |
| 限制与可比性 | 化学对象接近，DPPH 不等于肠屏障作用；仅摘要/页面片段，不能视作全文阅读。 |
| 证据位置 | DOI 10.1016/j.comptc.2024.114782 出版社摘要。 |


## P19 · Antioxidant_QSAR（2025）

QSAR Models for Predicting the Antioxidant Potential of Chemical Substances

来源：[10.3390/jox15030080](https://pmc.ncbi.nlm.nih.gov/articles/PMC12194667/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 小分子 DPPH 抗氧化强度回归。 |
| 数据集与标签 | AODB 清理后 1,911 独立化合物，30 min 测量转 pIC50；不包含肽。 |
| 输入与表示 | 规范 SMILES、Mordred 描述符；F-test/MI 选特征。 |
| 模型与预训练 | 11 回归器，ExtraTrees/GB/XGB 等三模型集成。 |
| Loss | 各回归器目标不同；网格选择以 R² 等评价。 |
| Inference | 输出连续 pIC50。 |
| Metrics | 测试集集成 R² 约 0.78；最佳单模型 ExtraTrees R² 约 0.77、RMSE 约 0.45。 |
| 划分与泄漏控制 | 随机 80/20、训练内 10 折；按 InChI 去重和冲突过滤。 |
| 限制与可比性 | 文中 external 指同一数据池随机留出，不是前瞻外部集；筛特征是否每折拟合需审查。 |
| 证据位置 | Methods: data preparation/modeling；Results tables；PMC12194667。 |


## P20 · Barrier_metabolomics（2026）

A Biologically Informed Machine Learning Pipeline Uncovers Metabolic Features of Intestinal Barrier Dysfunction

来源：[10.1021/acs.analchem.6c00178](https://pubmed.ncbi.nlm.nih.gov/41854110/)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 从代谢组预测连续肠屏障功能指数。 |
| 数据集与标签 | 小鼠相关表型/代谢组，筛出 10 个核心代谢物；完整样本量本轮 NR。 |
| 输入与表示 | 生物样本的代谢物特征，非单分子 SMILES。 |
| 模型与预训练 | 生物信息约束特征选择加五类回归模型。 |
| Loss | 精确算法 loss NR。 |
| Inference | 输出样本屏障指数。 |
| Metrics | 摘要 R² 0.604–0.654、MAE 0.319–0.352。 |
| 划分与泄漏控制 | 完整划分、重复与泄漏控制 NR。 |
| 限制与可比性 | 只读摘要；相似关键词不构成同任务先例或直接基线。 |
| 证据位置 | PubMed 41854110/ACS 摘要。 |


## P21 · HELM_BERT（2026）

HELM-BERT: Topology-Aware
Representations for Chemically
Modified Peptides

来源：[10.1021/acs.jcim.6c00451](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417886/)。阅读：full_text_key_sections；2026 journal final; supersedes early preprint extraction。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 修饰肽通透性回归、肽–蛋白相互作用分类。 |
| 数据集与标签 | 预训练 39,079 肽；通透性 7,715；Propedia 20,057 正配对；另有 ChEMBL PPI。 |
| 输入与表示 | HELM 化学单体与连接表示。 |
| 模型与预训练 | HELM-BERT；对比 MolFormer-XL/PeptideCLM；PPI 加冻结 ESM-2。 |
| Loss | 通透性 MSE；PPI BCE，阳性权重 4。 |
| Inference | 全微调、仅头微调和线性探针分别评估。 |
| Metrics | 回归 R²/r/RMSE/MAE；PPI AUROC 等。 |
| 划分与泄漏控制 | 最终版加入随机/10 折 Murcko 分组；PPI 5 折配对/蛋白分组，1:4 阴性采样。 |
| 限制与可比性 | 以 2026 正式版为准：不能把旧预印本的样本比矛盾或缺少 scaffold 检验套用最终版；检查预训练重叠消融。 |
| 证据位置 | PMC13417886 Methods: downstream tasks、ChEMBL benchmark、overlap ablation。 |


## P22 · GP_MoLFormer（2025）

GP-MoLFormer: a foundation model for molecular generation

来源：[10.1039/D5DD00122F](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00122f)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 分子生成及条件优化，非直接活性识别。 |
| 数据集与标签 | 大规模小分子 SMILES；规模随模型版本。 |
| 输入与表示 | SMILES 自回归序列。 |
| 模型与预训练 | GP-MoLFormer 生成式化学语言模型。 |
| Loss | 语言建模目标；本轮未逐项核实各适应目标。 |
| Inference | 采样/条件生成分子。 |
| Metrics | 生成有效性、独特性、新颖性及优化任务指标。 |
| 划分与泄漏控制 | 生成训练语料与条件任务协议不可直接转为活性二分类划分。 |
| 限制与可比性 | 背景项；正式发表 2025，2024 预印本归并；非本项目直接预测基线。 |
| 证据位置 | Digital Discovery DOI 10.1039/D5DD00122F；作者预印本摘要。 |


## P23 · Systematic_molecular_benchmark（2023）

A systematic study of key elements underlying molecular property prediction

来源：[10.1038/s41467-023-41948-6](https://www.nature.com/articles/s41467-023-41948-6)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 分子性质预测关键因素的系统比较。 |
| 数据集与标签 | 共 62,820 个模型实例；多类 MoleculeNet/ChEMBL 等性质数据与规模实验。 |
| 输入与表示 | 描述符、指纹、SMILES 和图表示。 |
| 模型与预训练 | RF/XGB/SVM 与 GRU/MolBERT/GNN 等。 |
| Loss | 各模型/任务原生目标，不能指定统一 loss。 |
| Inference | 分类或回归预测。 |
| Metrics | 依数据集分别评价分类/回归与统计差异，本轮不跨数据集汇总一个“准确率”。 |
| 划分与泄漏控制 | 比较样本规模、噪声、分布及表示影响。 |
| 限制与可比性 | 支持强传统基线和受控评估；P01 是相关评论，不是同一项独立研究结果。 |
| 证据位置 | Nature Communications 正文 Methods/Results；原 PDF。 |


## P24 · Phytochemical_QSPR（2026）

Molecular descriptor driven
                    <scp>QSPR</scp>
                    modeling of Papp,
                    <scp>TEER</scp>
                    and Efflux Ratio from Caco‐2 cells using machine learning for various phytochemicals

来源：[10.1002/jsfa.70701](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/jsfa.70701)。阅读：publisher_methods_and_partial_results；Wiley published HTML。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 植物化学物的 Caco-2 Papp、TEER、ER 回归。 |
| 数据集与标签 | 83 种植物化学物，三重复形成 249 行；候选描述符 5,003。 |
| 输入与表示 | SMILES 计算 PaDEL/alvaDesc 描述符。 |
| 模型与预训练 | 十类回归器；CatBoost/LightGBM/GB 加线性元模型的 stacking。 |
| Loss | 各回归器目标不同；精确 loss 未列全，NR。 |
| Inference | 输出三类连续指标。 |
| Metrics | NRMSE、R²；TEER 表现波动较大，不挪用 Papp 成绩说明屏障效果。 |
| 划分与泄漏控制 | 重复 5 折×6；标准化只拟合训练集；有相关筛选/RFECV。 |
| 限制与可比性 | 三重复是否按化合物分组未明确；相关筛选范围与按 test 选模型表述需审计。249 行不等于 249 独立化合物；方法称 polyphenols，但列出混合类别，按 phytochemicals 记录。 |
| 证据位置 | Wiley 正文 Materials and Methods；2026-05-08 在线 DOI 10.1002/jsfa.70701。 |


## P25 · TIDE（2026）

Modeling TCR-pMHC Binding with Dual Encoders and Cross-Attention Fusion

来源：[10.1109/bibm66473.2025.11356540](https://pmc.ncbi.nlm.nih.gov/articles/PMC13159490/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | TCR–肽结合二分类。 |
| 数据集与标签 | TCHard，参考/随机阴性与未见肽评估；未将配对数量当独立肽数。 |
| 输入与表示 | TCR 序列与肽 SMILES；不直接输入 MHC。 |
| 模型与预训练 | TIDE：ESM + MolFormer、交叉注意力和分类头。 |
| Loss | BCE + λ 对齐正则。 |
| Inference | 配对结合概率，冻结/微调配置分实验。 |
| Metrics | AUROC 为主及分类指标。 |
| 划分与泄漏控制 | 训练验证与独立测试，zero/few-shot 设定须按未见肽理解。 |
| 限制与可比性 | 与 LANTERN 同作者/同类数据和架构，不能作为两个独立数据来源的复现证据；作为另一正式文献条目保留。 |
| 证据位置 | PMC13159490 Methods/Experiments；BIBM 2025 proceedings，在线元数据 2026-01-29。 |


## P26 · NPCLM（2026）

Chemical Language Models for Natural Products: A State-Space Model Approach

来源：[10.48550/arXiv.2602.13958](https://arxiv.org/html/2602.13958v1)。阅读：full_text_key_sections；arXiv v1, 2026-02-15。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 天然产物生成与肽通透、味觉、抗癌分类。 |
| 数据集与标签 | 预训练 1,030,273 NP；肽 6,651，FourTastes 4,431，抗癌约 26k。 |
| 输入与表示 | SMILES，八种 tokenizer。 |
| 模型与预训练 | NPCLM：Mamba/Mamba-2/GPT；对比 MolFormer-XL-both-10pct 与 ChemBERTa-2，含领域适应。 |
| Loss | 预训练 CE；味觉加权 CE，肽/抗癌 BCEWithLogitsLoss。 |
| Inference | 换分类头；生成用自回归采样，两个任务单独评价。 |
| Metrics | 分类 MCC/AUROC；生成有效性/独特性/新颖性。 |
| 划分与泄漏控制 | 随机与 Murcko 划分、重复 5×5 折；作者报告移除预训练和下游重叠分子。 |
| 限制与可比性 | 本轮仅确认 2026 arXiv v1，不能写已接收；提供天然产物领域适应已有先例。 |
| 证据位置 | arXiv2602.13958v1 Methods 3.1–3.4；作者 rozariwang/CLMs-for-NPs。 |


## P27 · Food_foundation_models（2025）

Leveraging foundation models and transfer learning for peptide transport prediction, molecular taste classification, and visual texture analysis

来源：[10.1016/j.ifset.2025.104247](https://www.sciencedirect.com/science/article/pii/S1466856425003315)。阅读：abstract_or_partial；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 食品任务：肽运输、分子味觉及图像质地。 |
| 数据集与标签 | 三种不同模态数据；具体肽运输样本量与来源 NR。 |
| 输入与表示 | 肽序列、分子 SMILES、图像分别处理。 |
| 模型与预训练 | ESMC 用于肽运输；MolFormer 用于小分子味觉；另有视觉模型。 |
| Loss | NR：本轮仅摘要可用。 |
| Inference | 各任务预测，不能误写为 MolFormer 预测肽运输。 |
| Metrics | 摘要味觉 accuracy 0.99，未经划分复核不能作为性能结论。 |
| 划分与泄漏控制 | 去重、划分与外推协议 NR。 |
| 限制与可比性 | 2025 正式论文，作为应用边界对照；不把三个任务合并成一个多模态肽活性模型。 |
| 证据位置 | 出版社摘要/Highlights，DOI 10.1016/j.ifset.2025.104247。 |

