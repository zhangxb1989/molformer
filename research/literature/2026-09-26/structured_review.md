# 阶段 2：逐篇结构化分析

**快速阅读请打开[每篇独立分析索引](papers/README.md)**：28篇已分别整理为研究、模型、数据、结果、贡献、缺陷六项。本文件保留较细的历史提取。当前优先逐篇整理，第三阶段留待以后，不继续代码核查。

NR = 本轮未取得足够证据，不等于原文没有报告。全文关键部分阅读不等于已经运行作者代码；性能数字主要为作者报告；P15另含既有公开预测核对记录，已单独注明。本轮仅整理文献。正文与预印本版本严格区分。

术语：AA=氨基酸序列；SMILES=分子线性表示；AIP=抗炎肽；AMP=抗菌肽；PAMPA=人工膜通透性实验。

质量复核及保留限制见 [quality_check.md](quality_check.md)。

## F01 · MoLFormer（2022）

Large-scale chemical language representations capture molecular structure and properties

来源：[10.1038/s42256-022-00580-7](https://www.nature.com/articles/s42256-022-00580-7)；[本次阅读材料](https://arxiv.org/pdf/2106.09553v3)。阅读：full_text_key_sections；arXiv v3 (2022-12-14), methods and Tables 1–2; formal 2022 publication metadata retained; final-version identity not assumed。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 小分子性质预测的基础表征；不在三年主窗口。 |
| 数据集与标签 | 最大预训练约11亿条PubChem/ZINC分子SMILES。分类：BBBP/Tox21/ClinTox/HIV/BACE/SIDER；回归：QM9/QM8/ESOL/FreeSolv/Lipophilicity。 |
| 输入与表示 | SMILES。 |
| 模型与预训练 | 12层、12头、隐藏维度768的线性注意力Transformer编码器，使用旋转位置编码；以MoLFormer-XL原论文预训练规模为准，不混用其他权重版本。 |
| Loss | 预训练为遮盖语言建模；下游分类/回归各接相应监督目标。 |
| Inference | 最后一层token表示均值池化后接预测头；比较冻结特征与整体微调。 |
| Metrics | 所读v3中，MoLFormer-XL在BBBP、ClinTox、SIDER的AUROC分别为93.7%、94.8%、69.0%；ESOL、FreeSolv、Lipophilicity的RMSE分别为0.2787、0.2308、0.5289，误差单位依各端点。分类采用骨架划分，回归采用随机划分，不能合并为一个准确率。 |
| 划分与泄漏控制 | 所读v3补充Section C明确：分类骨架划分，回归随机划分；不能自动等同于用户数据协议。 |
| 限制与可比性 | 本次已读arXiv v3正文关键部分；未逐项对照正式版。部分基线成绩引自其他工作，且预训练规模不同；不将原文结果视为用户任务实测结果。 |
| 证据位置 | arXiv v3：Methods；PDF第10—11页Table 1/2及表注；第21—22页补充数据与划分说明。 |

[打开本篇六项速读分析](papers/F01_MoLFormer.md)


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

[打开本篇六项速读分析](papers/P01_Representation_limits_comment.md)


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

[打开本篇六项速读分析](papers/P02_PeptideBERT.md)


## P03 · ActFound（2024）

A bioactivity foundation model using pairwise meta-learning

来源：[10.1038/s42256-024-00876-w](https://www.nature.com/articles/s42256-024-00876-w)；[本次阅读材料](https://www.researchgate.net/publication/383120443_A_bioactivity_foundation_model_using_pairwise_meta-learning)。阅读：full_text_key_sections；author-uploaded publisher-layout manuscript (Bin Feng, 2024-09-20), Methods/Results/Discussion; proof contains an online-date placeholder; final typeset identity not assumed。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 少样本 assay 内定量生物活性回归。 |
| 数据集与标签 | ChEMBL含35,644个assays；正式摘要写约160万活性记录，作者公开稿Methods写约140万、70万独立化合物，两种口径保留。评估包括ChEMBL、BindingDB、FS-Mol、pQSAR-ChEMBL、KIBA、Davis，另有FEP与GDSC实验。 |
| 输入与表示 | 2048维Morgan指纹；同一assay内构建化合物对。 |
| 模型与预训练 | 共享两层感知机编码器（隐藏维度2048）＋线性层的孪生网络；成对元学习，内循环适应最后线性层；kNN-MAML利用近邻assays。未使用分子语言模型。 |
| Loss | Methods：绝对活性均方误差与加权成对活性差均方误差相加；内/外循环使用各自支持/查询集合。 |
| Inference | 相对活性差加支持化合物的已知活性，按嵌入注意力与Tanimoto掩码融合为绝对预测；新assay需支持样本。 |
| Metrics | ChEMBL/BindingDB的16-shot实验中，作者报告r²和RMSE均优于所比方法；每个assay用16个已测化合物微调。FEP实验中使用40%实测数据、平均约12个化合物微调后，作者报告超过FEP+(OPLS4)。这里的r²定义为max(Pearson相关系数,0)²，不是通常的回归决定系数。 |
| 划分与泄漏控制 | Fig. 2的ChEMBL/BindingDB为16-shot，每库500个测试assays；Fig. 3含跨库及KIBA/Davis迁移；FEP实验另报告排除与基准重叠的预训练化合物。补充实验全表尚未整理。 |
| 限制与可比性 | 作者指出未使用靶蛋白序列或实验文字描述，输入仍为简单分子指纹。FEP结果依赖目标assay支持标签，不能理解为无标签替代物理计算；数据量的摘要/正文差异尚未解决。 |
| 证据位置 | 作者公开稿：Fig. 1—4；Methods的Problem setting、Pairwise learning、Training data curation、Implementation details；Discussion。 |

[打开本篇六项速读分析](papers/P03_ActFound.md)


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
| Metrics | 论文发现，不控制同源性会高估泛化表现；蛋白预训练特征整体优于简单编码，但所比较预训练模型之间并非越大越好。优化后的传统模型集成可与复杂网络竞争。各任务以MCC评价，没有一个适用于全库的统一准确率。 |
| 划分与泄漏控制 | 对比 Original/NegSearch/NegSearch+HP；CCPart 30% 局部序列相似性约束，20% 测试，训练内 10 折。 |
| 限制与可比性 | 排除相关活性的负池与长度匹配有参考价值；缺失功能标签仍不等于真阴性。 |
| 证据位置 | Methods: datasets、negative sampling、homology partition、AutoPeptideML；IBM/AutoPeptideML。 |

[打开本篇六项速读分析](papers/P04_AutoPeptideML.md)


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
| 证据位置 | Methods: Data preparation、architecture；Results/Table；Statistics and reproducibility。 本轮复核原 PDF p.3–4 性能、p.10 数据准备与 p.11 Statistics。 |

[打开本篇六项速读分析](papers/P05_PepNet.md)


## P06 · DeepAIP（2024）

DeepAIP: Deep learning for anti-inflammatory peptide prediction using pre-trained protein language model features based on contextual self-attention network

来源：[10.1016/j.ijbiomac.2024.136172](https://pubmed.ncbi.nlm.nih.gov/39357724/)；[本次阅读材料](https://www.sciencedirect.com/science/article/pii/S0141813024069812)。阅读：abstract_or_partial；published abstract and publicly visible workflow excerpts; full methods and result tables remain incomplete。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 抗炎肽二分类。 |
| 数据集与标签 | 出版社流程段落说明：合并PreAIP、AIPpred、IF-AIP所用数据，经CD-HIT阈值0.9处理后按80%/20%分为训练/测试；另有17条抗炎阳性序列。主集合准确样本量和阴性构造仍未取得。 |
| 输入与表示 | Prot-T5-XL-Uniref50隐藏特征与平均池化，来自肽氨基酸序列。 |
| 模型与预训练 | 使用Prot-T5-XL-Uniref50提取并平均池化序列特征，再结合上下文自注意力与多尺度卷积。作者在八种预训练特征中比较后选择ProtT5。 |
| Loss | NR：摘要不足以确认。 |
| Inference | 输出 AIP 预测；阈值 NR。 |
| Metrics | 摘要报告，相对次优比较方法，MCC和accuracy分别提高16.35%和6.91%；另将17条阳性肽全部识别为抗炎肽。这些是作者报告的增幅和阳性识别结果，不是可直接代换的绝对MCC/accuracy。 |
| 划分与泄漏控制 | 出版社可见流程：合并数据后CD-HIT阈值0.9处理，80%训练/20%测试；是否按同源簇隔离划分，NR。 |
| 限制与可比性 | 17条外部序列全为阳性，不能估计特异度。0.9去冗余阈值不能自动证明严格跨同源簇外推。完整结果表、绝对分数与增幅计算口径仍待补读。 |
| 证据位置 | PubMed 39357724摘要；ScienceDirect Highlights及DeepAIP construction process条目1—5。 |

[打开本篇六项速读分析](papers/P06_DeepAIP.md)


## P07 · Deep2Pep（2024）

Deep2Pep: A deep learning method in multi-label classification of bioactive peptide

来源：[10.1016/j.compbiolchem.2024.108021](https://www.sciencedirect.com/science/article/pii/S1476927124000094)；[本次阅读材料](https://www.sciencedirect.com/science/article/pii/S1476927124000094)。阅读：abstract_or_partial；published abstract, Highlights, Dataset and Sequence analysis excerpts; full split and deduplication details remain incomplete。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 抗菌、抗高血压、抗氧化、抗高血糖四功能多标签。 |
| 数据集与标签 | 来源为UniProt、APD、AHTPDB、DFBP、BIOPEP-UWM、BGI-marine。可见Sequence analysis列出抗菌3014、降压2597、抗氧化1202、降血糖516个阳性标签，另称活性阳性6772、阴性863；多标签计数会重叠，不能把各功能阳性相加当成独立肽数。UniProt阴性取自缺少功能注释的序列。 |
| 输入与表示 | 序列编码、embedding 与语言 tokenizer。 |
| 模型与预训练 | BiLSTM、注意力残差模块与BERT encoder联合预测四类活性；Highlights说明使用加权focal loss应对标签不平衡。BiLSTM起主要作用；尚未确认BERT来自大规模预训练权重。 |
| Loss | 出版社Highlights明确为加权focal loss；完整公式、类别权重和超参数尚未取得。 |
| Inference | 多标签输出；逐标签阈值 NR。 |
| Metrics | 摘要报告subset accuracy=0.737、Macro F1=0.734、Hamming loss=0.095，并称优于所比较模型。Subset accuracy要求一条肽的标签集合全部匹配，不能当作普通二分类正确率。 |
| 划分与泄漏控制 | 去重、同源性、划分 NR。 |
| 限制与可比性 | 缺注释不等于实验确认无活性；抗高血糖阳性标签明显较少，汇总分数不能代替逐标签表现。完整去重、集合划分与阈值仍未取得。 |
| 证据位置 | ScienceDirect的Highlights、Dataset、Sequence analysis、Conclusion；PubMed 38308955摘要。 |

[打开本篇六项速读分析](papers/P07_Deep2Pep.md)


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

[打开本篇六项速读分析](papers/P08_PeptideCLM.md)


## P09 · PepLand（2025）

PepLand: a large-scale pre-trained peptide representation model for a comprehensive landscape of both canonical and non-canonical amino acids

来源：[10.1093/bib/bbaf367](https://pmc.ncbi.nlm.nih.gov/articles/PMC12315545/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 典型与非典型肽的穿膜、溶解性、结合等性质。 |
| 数据集与标签 | 五个主要基准：canonical CPP/Sol/Binding 与 noncanonical CPP/Binding；预训练为大规模典型肽再适应修饰肽。 |
| 输入与表示 | SMILES 分子图，原子/片段信息及 AdaFrag。 |
| 模型与预训练 | PepLand：多视图异构图神经网络，两阶段预训练，结合原子/片段表示与任务预测头；可探针或微调。 |
| Loss | 遮盖属性预测；具体目标和各任务 loss 本轮未完整核实，NR。 |
| Inference | 表征池化后分类/回归。 |
| Metrics | 主表按任务用 AUC 或 Spearman；ncCPP 0.628、ncBinding 0.768 为相应 Spearman 设置。 |
| 划分与泄漏控制 | 按其各数据基准；不能推定所有集合均同源/骨架分离。 |
| 限制与可比性 | 图模型，不等同 SMILES 语言模型；图注与表的指标描述须按具体任务核对。 |
| 证据位置 | Main Table 1；Methods: pretraining、datasets；PMC12315545。 |

[打开本篇六项速读分析](papers/P09_PepLand.md)


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
| Metrics | 作者报告，标准肽内插时表示差别不大；修饰肽内插时化学语言模型更有优势。标准到修饰外推时性能明显下降，摘要概括约下降50%，其中化学指纹和ChemBERTa-2相对较好；该增减不是某个统一准确率。 |
| 划分与泄漏控制 | 相似性分割 CCPart；训练内 5 折 HPO、Optuna 最多 200 steps（含 early stopping）、5 seeds；外推用全部标准肽训练、修饰肽测试。 |
| 限制与可比性 | 负例有“其他活性”来源，不必然真阴性；直接证明已有 MolFormer 肽任务先例。 |
| 证据位置 | Methods datasets/representations/partition；Figs 4–6；IBM/PeptideGeneralizationBenchmarks。 本轮复核原 PDF p.3 Table 1、p.4 HPO。 |

[打开本篇六项速读分析](papers/P10_Peptide_generalization.md)


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
| Metrics | 作者摘要报告，相对所比较抗氧化专用模型的平均accuracy，P60、P70、P80、P90分别提高7.26%、2.57%、2.59%、4.20%。这是四种设置的增幅，不能当成最终准确率；也不能把ESM单独基线分数当作AOP-DRL结果。 |
| 划分与泄漏控制 | 80/20 分层、P60/70/80/90 相似性设置与 5 折；相互嵌套关系须代码确认。 |
| 限制与可比性 | 文本对全量训练/部分冻结及对比学习描述不完全一致，不能直接沿用全部宣传语。 |
| 证据位置 | Methods: Dataset、ESM-2/TextCNN、Evaluation；PMC12800373。 |

[打开本篇六项速读分析](papers/P11_AOP_DRL.md)


## P12 · MFP_MFL（2025）

MFP-MFL: Leveraging Graph Attention and Multi-Feature Integration for Superior Multifunctional Bioactive Peptide Prediction

来源：[10.3390/ijms26031317](https://pmc.ncbi.nlm.nih.gov/articles/PMC11818429/)。阅读：full_text_key_sections；published PDF plus static audit of author code commit 1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 五功能多标签：AMP/AIP/AHP/ACP/ADP。 |
| 数据集与标签 | 表 2：单功能 5,719，双功能 198；据此为 5,917 独立序列，标签条目不能当独立样本。 |
| 输入与表示 | ESM-2、ProtT5、RoBERTa 多特征融合。 |
| 模型与预训练 | 论文 MFP-MFL：GAT、FGM 对抗训练、多特征集成；所核公开推理快照对 30 模型等权平均。 |
| Loss | 原 PDF p.19 式 (10)–(11) 只印正类项；作者代码 1f7b35f 的 GAT.py 使用完整 BCEWithLogitsLoss，无显式类别权重。训练入口对初始与对抗 loss 各反传一次、系数均为 1；FGM 源文件未见，扰动实现仍未核实。 |
| Inference | 公开 predict.py 对 30 个模型 sigmoid 概率取算术平均；用被评分数据的真实标签在 0.30–0.69 中选最优阈值（全零得分回退 0），不是固定 0.5。 |
| Metrics | 多标签 precision、coverage、accuracy、exact match、absolute false；主表 accuracy 0.786、precision 0.799。公开代码 Accuracy 是样本平均标签集合 Jaccard。 |
| 划分与泄漏控制 | 公开训练/集成推理入口用 test 标签选阈值后在同批 test 数据计分，存在测试集参与调参；论文表格与该提交的对应尚未证实。未认定严格同源外推。 |
| 限制与可比性 | 结论部分交换指标，采用主表；多标签 Jaccard 不能与二分类 accuracy 等同。已核代码的阈值相关成绩不视作独立测试估计；静态核查不等于复现。 |
| 证据位置 | 原 PDF p.5 特征集成结果表、p.14–15 数据计数、p.19 式 (10)–(11) 与结论；已核对公式页图像。 作者仓库固定提交 1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de 的 GAT.py/GAT_train.py/predict.py/threshold.py/evaluation.py；逐行证据见 code_audit.md。 |

[打开本篇六项速读分析](papers/P12_MFP_MFL.md)


## P13 · BPFun（2025）

BPFun: a deep learning framework for bioactive peptide function prediction using multi-label strategy by transformer-driven and sequence rich intrinsic information

来源：[10.1186/s12859-025-06190-5](https://link.springer.com/article/10.1186/s12859-025-06190-5)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 七功能多标签，含抗氧化与抗炎等。 |
| 数据集与标签 | 各标签计数可重叠：AMP 2409、ACP 646、ADP 514、AHP 868、AIP 1678、AAP 134、AOP 318；154 个双标签。 |
| 输入与表示 | 序列及丰富内在特征。 |
| 模型与预训练 | BPFun：Transformer、BiLSTM、注意力；不能仅因 Transformer 就归为预训练大模型。 |
| Loss | 主文 p.12 式 (17) 明示 MSE；网络另含 L2 正则化，不能默认写成 BCE。 |
| Inference | 七个 sigmoid 输出，阈值 >0.5。 |
| Metrics | 原文摘要及Table 7报告多标签accuracy=0.6577、absolute true=0.6573；后者描述整组标签完全匹配的比例。作者在所用七功能测试集上报告优于比较方法。 |
| 划分与泄漏控制 | CD-HIT 0.9 去冗余、长度≥5，再随机 80/20。 |
| 限制与可比性 | 先去冗余后随机分割不等于相似性隔离；序列遮盖增强需限制在训练内。 |
| 证据位置 | Methods: model/loss、dataset；BMC 主文。 本轮核对原 PDF p.11 sigmoid/0.5 阈值与 p.12 式 (17) 图像。 |

[打开本篇六项速读分析](papers/P13_BPFun.md)


## P14 · PeptiVerse（2026）

PeptiVerse: A unified platform for therapeutic peptide property prediction

来源：[10.1038/s41467-026-74167-w](https://pmc.ncbi.nlm.nih.gov/articles/PMC13388690/)。阅读：full_text_key_sections；published full text or author manuscript。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 七类治疗肽性质：溶血、溶解性、nonfouling、毒性、通透性、半衰期、亲和力。 |
| 数据集与标签 | 例：溶血 6,076；修饰肽通透性合计 7,475，其中 PAMPA 6,869、Caco-2 606；典型 CPP 2,324；半衰期按 AA/SMILES 为 130/245。各通透端点需分清。 |
| 输入与表示 | AA 与 SMILES 两类输入。 |
| 模型与预训练 | 冻结 ESM-2、PeptideCLM、ChemBERTa，加传统或深度预测器；结合任务用交叉注意力。 |
| Loss | 各算法不同；回归包括 MSE/Huber 等设置，不能写一个统一 loss。 |
| Inference | 单性质预测；可用集成和熵估计不确定性，不代表已证明概率校准。 |
| Metrics | 自有实验分类 F1/AUROC；回归 r、rho、R²、RMSE/MAE。Table 1 移用的 PepLand 分类分数与原论文指标名不一致，不能将整列都作为同指标 F1 排名。 |
| 划分与泄漏控制 | 序列/SMILES 聚类 80/20；结合按亲和力分布匹配，不能称严格冷靶点；半衰期 5 折。 |
| 限制与可比性 | 正式版 2026-07-16。p.5 Table 1 将 PepLand 的 c-CPP 0.838、c-Sol 0.662 列在 Best F1 下，但 P09 原 Table 1 标为 AUC；且历史分数来自不同划分。该表不能证明同协议、同指标的优势。冻结特征流程可参考。 |
| 证据位置 | 原 PDF p.5 Table 1、p.7–8 数据/训练方法；另与 PepLand 原 Table 1 对照：https://academic.oup.com/view-large/527864395 。 |

[打开本篇六项速读分析](papers/P14_PeptiVerse.md)


## P15 · PeptideCLM2（2026）

Scaling SMILES-Based Chemical Language Models for Therapeutic Peptide Engineering

来源：[10.1021/acs.jcim.6c00652](https://pubs.acs.org/doi/10.1021/acs.jcim.6c00652)。阅读：preprint_full_text_and_final_supplement；bioRxiv preprint v5, 2026-06-23, plus final journal Supporting Information v1, 2026-07-14; final main article Methods not fully verified。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 治疗肽通透性、半衰期及相关功能预测。 |
| 数据集与标签 | CycPeptMPDB、THPep、CellPPD、AmpHGT、PepMSND；预训练含逾亿小分子与肽。公开 THPep 源表 609 行，class 0/1 为 433/176；609 个 SMILES 字符串不同，不代表已完成化学规范化或同源性审计。 |
| 输入与表示 | SMILES。 |
| 模型与预训练 | PeptideCLM-2 多个规模/预训练目标变体，约 32–337M 参数。 |
| Loss | 预印本/作者启动示例：25% span 掩码、99 RDKit 属性、0.6 token CE+0.4 MTR MSE。代码 labels 仅忽略 padding，CE 并非仅在掩码位计算。公开分类入口 BCEWithLogitsLoss；专用回归入口及正式补充表 S5/S6 均确认 MSE。 |
| Inference | 正式补充 S5 分类采用 rank-16 LoRA；当前代码 r=16、alpha=32、dropout=0.1。S6 回归为内折 checkpoints 均值集成。THPep 公开预测为 logits；评估 notebook 同时有测试标签择优阈值与固定 logit 0 两条路径，正式表 S8 的阈值相关指标匹配前者。 |
| Metrics | 正式补充 S8：MLM MCC/AUROC/F1 为 0.756±0.019/0.949±0.006/0.826±0.012；Hybrid 为 0.747±0.036/0.940±0.019/0.818±0.022；MTR 为 0.698±0.036/0.924±0.016/0.784±0.029。按测试标签最大化 MCC 阈值重算，18 个均值/样本 SD 均匹配三位小数；固定 logit 0 的 MCC 为 0.693±0.062、0.667±0.066、0.623±0.047。仅为已发布预测的计算核对，未训练模型。 |
| 划分与泄漏控制 | 正式补充 S5：固定划分优先，否则 5 折。找回历史 prepare_thpep 脚本：两次按标签分层的 20% 随机留出，609 行重建为训练389/验证98/测试122。三个 seeds×三种模型的9份测试导出，样本、标签、行序全部匹配；THPep 函数未实施按簇分组，不能从 manifest 名称推定隔离。未取得完整训练日志，未审计 main90 上游同源性处理；不能概括为统一3×5折。 |
| 限制与可比性 | 正式主文方法仍访问受限；现已直接读取正式补充 S5/S6/S8。THPep 表 S8 的 MCC/F1 与测试集择优阈值计算一致，不应作完全独立测试估计；AUROC 不受该阈值改变，不表示其他步骤已无泄漏。结论只限9份THPep导出，未重算基线或其他任务。预印本 CC BY 与正式补充 CC BY-NC 分别记录。 |
| 证据位置 | PMC12803269 v5；正式 SI DOI 10.1021/acs.jcim.6c00652.s001，S5/S6/S8（PDF S5–S7）。当前作者提交6b9708d4cb05717307d310daaf1c0f88c71ff084；历史划分脚本4740c70c3f5246c4be66cc54de11d7cb3a1c8b2a。固定链接/哈希见 thpep_evidence.json，9份预测重算见 thpep_protocol_audit.md 与 thpep_audit_results.json。 |

[打开本篇六项速读分析](papers/P15_PeptideCLM2.md)


## P16 · LANTERN（2026）

LANTERN: TCR-peptide binding prediction via large language model representations

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

[打开本篇六项速读分析](papers/P16_LANTERN.md)


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

[打开本篇六项速读分析](papers/P17_PepBenchmark.md)


## P18 · Phenols_CDFT（2024）

Accurate & simple open-sourced no-code machine learning and CDFT predictive models for the antioxidant activity of phenols

来源：[10.1016/j.comptc.2024.114782](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)；[本次阅读材料](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)。阅读：abstract_or_partial；published abstract, Highlights and conclusion excerpts, plus author-institution abstract; full methods remain incomplete。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 酚类 DPPH 抗氧化分类。 |
| 数据集与标签 | 202种酚类化合物的抗DPPH数据。出版社结论段落提到留一交叉验证（LOOCV）与90%/10%划分；具体类别阈值、各类数量及筛选流程仍未取得。 |
| 输入与表示 | 量子 CDFT 与分子描述符。 |
| 模型与预训练 | 在GFN1-xTB、GFN2-xTB层面计算概念密度泛函理论（CDFT）描述符；结合PCA、InfoGain等筛选方法，训练J48、RandomTree、JCHAID等树模型。 |
| Loss | 各树模型目标；精确设置 NR。 |
| Inference | 抗氧化类别预测；阈值 NR。 |
| Metrics | 摘要报告各决策树在内部与外部验证中accuracy超过85%；可见结论提到LOOCV与90/10划分。“外部”不宜直接理解为另一个独立来源队列，逐模型分数仍未取得。 |
| 划分与泄漏控制 | 出版社Conclusion报告LOOCV与90/10划分；具体集合数量、独立来源验证和嵌套特征筛选仍NR。 |
| 限制与可比性 | 202个样本规模有限；可见材料不足以确认特征筛选是否在验证折内完成。DPPH清除能力不等同细胞抗氧化或肠屏障保护，当前也不能确认对新骨架的泛化。 |
| 证据位置 | ScienceDirect摘要、Highlights、Conclusion；Universidad Andrés Bello作者机构摘要。 |

[打开本篇六项速读分析](papers/P18_Phenols_CDFT.md)


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
| 证据位置 | Methods: data preparation/modeling；Results tables；PMC12194667。 本轮复核官方原 PDF p.1、p.4、p.7–9；归档字节版本差异见 manifest。 |

[打开本篇六项速读分析](papers/P19_Antioxidant_QSAR.md)


## P20 · Barrier_metabolomics（2026）

A Biologically Informed Machine Learning Pipeline Uncovers Metabolic Features of Intestinal Barrier Dysfunction

来源：[10.1021/acs.analchem.6c00178](https://pubmed.ncbi.nlm.nih.gov/41854110/)；[本次阅读材料](https://acs.figshare.com/articles/journal_contribution/A_Biologically_Informed_Machine_Learning_Pipeline_Uncovers_Metabolic_Features_of_Intestinal_Barrier_Dysfunction/31812620)。阅读：abstract_and_final_supplement；published abstract plus formal Supporting Information s001 v1 (2026-03-19), Sections S1/S4/S6 and Tables S6/S7; main article remains access-limited。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 从代谢组预测连续肠屏障功能指数。 |
| 数据集与标签 | 小鼠实验S1报告七组、每组10只，最终清洗后建模数未确认；筛出10个功能相关代谢物。临床Table S7列健康/AP/IBD样本数：队列1为41/50/56，队列2为10/10/20；分别采血与采粪，用途不同，不当作同一回归测试集。 |
| 输入与表示 | 生物样本的代谢物特征，非单分子 SMILES。 |
| 模型与预训练 | LASSO、XGBoost和随机森林用于集成特征筛选；最终五种回归器为线性回归、Bayesian Ridge、ElasticNet、PLS和SVR，辅以SHAP解释。 |
| Loss | SI S4分别给出线性回归平方误差、ElasticNet正则化回归、Bayesian Ridge、PLS和SVR目标；不归并成一个神经网络loss。 |
| Inference | 输出样本屏障指数。 |
| Metrics | 正式SI Table S6中，10特征方案测试R²/MAE分别为：ElasticNet 0.620/0.350、Bayesian Ridge 0.642/0.329、线性回归0.604/0.352、PLS 0.654/0.319、SVR 0.643/0.329。这是同一方案跨回归器的表现，不能写成临床诊断准确率。 |
| 划分与泄漏控制 | SI S4.3：特征筛选调参用5折；最终回归调参用Repeated K-Fold（5折×5次）。最终训练/测试比例与预处理、特征筛选的嵌套边界尚未由主文确认。 |
| 限制与可比性 | 主文缺口仍影响对屏障指数定义、最终建模样本与训练/测试划分的判断；SI调参采用重复5折，但未据此确认所有预处理/筛选均在折内。临床组间存在BMI或年龄差异；代谢关联与体外转化不能单独证明体内保护因果。 |
| 证据位置 | ACS正式SI（DOI 10.1021/acs.analchem.6c00178.s001）：S1/S4/S6；S24页Table S6、S25页Table S7。数值表已视觉确认。 |

[打开本篇六项速读分析](papers/P20_Barrier_metabolomics.md)


## P21 · HELM_BERT（2026）

HELM-BERT: Topology-Aware Representations for Chemically Modified Peptides

来源：[10.1021/acs.jcim.6c00451](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417886/)。阅读：full_text_key_sections；2026 journal final; supersedes early preprint extraction。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 修饰肽通透性回归、肽–蛋白相互作用分类。 |
| 数据集与标签 | 预训练 39,079 独立肽；通透性 7,715；Propedia 配对分组 20,057 正配对，蛋白簇分组筛选后 20,055；另有 ChEMBL PPI。 |
| 输入与表示 | HELM 化学单体与连接表示。 |
| 模型与预训练 | HELM-BERT；对比 MolFormer-XL/PeptideCLM；PPI 加冻结 ESM-2。 |
| Loss | 通透性 MSE；PPI BCE，阳性权重 4。 |
| Inference | 全微调、仅头微调和线性探针分别评估。 |
| Metrics | 正式版摘要报告，随机划分通透性R²=0.668，在Murcko骨架划分下也保持最佳平均表现；同架构SMILES对照在全微调时缩小差距，而冻结表示时HELM优势更清楚。 |
| 划分与泄漏控制 | 最终版加入随机/10 折 Murcko 分组；PPI 5 折配对/蛋白分组，1:4 阴性采样。 |
| 限制与可比性 | 以 2026 正式版为准：不能把旧预印本的样本比矛盾或缺少 scaffold 检验套用最终版；检查预训练重叠消融。 |
| 证据位置 | PMC13417886 Methods: downstream tasks、ChEMBL benchmark、overlap ablation。 本轮用正式版 ACS/PMC 已索引方法再次核对计数、1:4 采样与 BCE 阳性权重 4。 |

[打开本篇六项速读分析](papers/P21_HELM_BERT.md)


## P22 · GP_MoLFormer（2025）

GP-MoLFormer: a foundation model for molecular generation

来源：[10.1039/D5DD00122F](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00122f)；[本次阅读材料](https://arxiv.org/html/2405.04912v2)。阅读：full_text_key_sections；arXiv v2 (2025-03-31), Results/Methods and Tables 1/4/5; 2025 Digital Discovery publication retained, final main text not verified。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 分子生成及条件优化，非直接活性识别。 |
| 数据集与标签 | PubChem/ZINC约11亿条SMILES；去重版Uniq为6.5亿条。预印本Methods列QED、penalized logP、DRD2训练分子对分别为70,644、60,227、34,404；前两项测试各800个分子，DRD2为1000个。 |
| 输入与表示 | SMILES 自回归序列。 |
| 模型与预训练 | 4680万参数的自回归Transformer解码器，使用线性注意力和旋转位置编码。Pair-tuning冻结主体，只训练少量提示嵌入，学习把性质较差的分子转为较优分子。 |
| Loss | 自回归下一token交叉熵；pair-tuning对性质排序的分子对进行条件生成交叉熵训练，只更新提示嵌入。 |
| Inference | 无条件自回归采样、以骨架SMILES续写，或给定输入分子及软提示进行性质优化。 |
| Metrics | v2 Table 1：Uniq生成3万个分子时IntDiv=0.8655、FCD=0.0591。Table 4：每个种子生成125次的QED最高0.948、有效率94.7%。Table 5：DRD2平均预测活性分数由种子的0.007升至生成物0.844（每种子20次选最高），并非实测活性。 |
| 划分与泄漏控制 | Table 1用3万生成物和17.5万参考分子，但不同模型参考分布不同；DRD2基线种子也不同。Methods将SMILES规范化且不保留异构信息。 |
| 限制与可比性 | 生成有效性、新颖性和预测器高分不能证明可合成性或真实药效；不同基线的训练/参考分布或种子不同，不能仅凭表中数字排名。预印本对无约束优化的高分，也不代表保留原结构。正式版数值尚未逐表比对。 |
| 证据位置 | arXiv v2：Results的Table 1/4/5；Methods的Datasets and tokenization、Pair-tuning。 |

[打开本篇六项速读分析](papers/P22_GP_MoLFormer.md)


## P23 · Systematic_molecular_benchmark（2023）

A systematic study of key elements underlying molecular property prediction

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

[打开本篇六项速读分析](papers/P23_Systematic_molecular_benchmark.md)


## P24 · Phytochemical_QSPR（2026）

Molecular descriptor driven QSPR modeling of Papp, TEER and Efflux Ratio from Caco‐2 cells using machine learning for various phytochemicals

来源：[10.1002/jsfa.70701](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/jsfa.70701)。阅读：full_text_key_sections；published PDF; Abstract, Methods and Table 2 key sections, not a complete page-by-page review。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 植物化学物的 Caco-2 Papp、TEER、ER 回归。 |
| 数据集与标签 | 83 种植物化学物，三重复形成 249 行；候选描述符 5,003。 |
| 输入与表示 | SMILES 计算 PaDEL/alvaDesc 描述符。 |
| 模型与预训练 | 十类回归器；CatBoost/LightGBM/GB 加线性元模型的 stacking。 |
| Loss | 各回归器目标不同；精确 loss 未列全，NR。 |
| Inference | 输出三类连续指标。 |
| Metrics | 原Table 2的Stacking测试R²：Papp 0.9550±0.0399；TEER 0.5435±0.4556；ER 0.9289±0.0602。对应NRMSE为0.0312、0.0781、0.0593（均值）。Papp和ER较好，TEER明显更不稳定。 |
| 划分与泄漏控制 | 重复 5 折×6；标准化只拟合训练集；有相关筛选/RFECV。 |
| 限制与可比性 | 三重复是否按化合物分组未明确；相关筛选范围与按 test 选模型表述需审计。249 行不等于 249 独立化合物；方法称 polyphenols，但列出混合类别，按 phytochemicals 记录。 |
| 证据位置 | Wiley 正文 Materials and Methods；2026-05-08 在线 DOI 10.1002/jsfa.70701。 本轮重新核对 Wiley 方法中的 249 个测量样本与结果中的 5,003 描述符；83 才是独立化合物数。 本次补读原PDF第8页Table 2，并渲染核对Stacking测试R²/NRMSE。 |

[打开本篇六项速读分析](papers/P24_Phytochemical_QSPR.md)


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
| Metrics | 作者机构保存的摘要报告，在TCHard的未见肽及少样本设置下，TIDE相对ChemBERTa、TITAN、NetTCR等基线取得更好的预测表现和稳健性。具体各组AUROC尚未逐表整理，因此保留作者定性结论，不补写提升幅度。 |
| 划分与泄漏控制 | 训练验证与独立测试，zero/few-shot 设定须按未见肽理解。 |
| 限制与可比性 | 与 LANTERN 同作者/同类数据和架构，不能作为两个独立数据来源的复现证据；作为另一正式文献条目保留。 |
| 证据位置 | PMC13159490 Methods/Experiments；BIBM 2025 proceedings，在线元数据 2026-01-29。 |

[打开本篇六项速读分析](papers/P25_TIDE.md)


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
| Metrics | 作者摘要报告：随机划分下Mamba系列比GPT高约0.02—0.04 MCC，骨架划分下表现接近；Mamba生成的有效性/独特性较好，GPT生成的新颖性略高。领域预训练可在所测任务上接近更大通用语料模型。 |
| 划分与泄漏控制 | 随机与 Murcko 划分、重复 5×5 折；作者报告移除预训练和下游重叠分子。 |
| 限制与可比性 | 本轮仅确认 2026 arXiv v1，不能写已接收；提供天然产物领域适应已有先例。 |
| 证据位置 | arXiv2602.13958v1 Methods 3.1–3.4；作者 rozariwang/CLMs-for-NPs。 |

[打开本篇六项速读分析](papers/P26_NPCLM.md)


## P27 · Food_foundation_models（2025）

Leveraging foundation models and transfer learning for peptide transport prediction, molecular taste classification, and visual texture analysis

来源：[10.1016/j.ifset.2025.104247](https://www.sciencedirect.com/science/article/pii/S1466856425003315)；[本次阅读材料](https://edepot.wur.nl/702069)。阅读：full_text_key_sections；publisher-layout 2025 article deposited in Wageningen institutional repository; Sections 2–3, Tables 1/2 and Figure 6。

| 字段 | 抽取内容 |
|---|---|
| 任务定义 | 食品任务：肽运输、分子味觉及图像质地。 |
| 数据集与标签 | 5183条山羊乳肽；ChemTastesDB三种味觉子集，Methods列甜1313、苦1615、鲜220；80张肉类似物、鸡肉与豆腐图像。Methods均写80%/20%训练/测试。 |
| 输入与表示 | 肽序列、分子 SMILES、图像分别处理。 |
| 模型与预训练 | 肽任务：ESMC嵌入＋MLP或BiLSTM，最好方案加入修饰位点特征；味觉：MoLFormer或ChemBERTa2嵌入＋MLP；图像：CLIP嵌入＋MLP。三个任务分别建模。 |
| Loss | 肽与味觉分类用交叉熵；图像回归段也写cross-entropy，与连续回归描述存在疑点，按原文保留、不自行更正。 |
| Inference | 分别以肽嵌入/修饰、SMILES嵌入、图像嵌入接预测头；MoLFormer只用于味觉实验。 |
| Metrics | 肽运输：修饰增强BiLSTM准确率0.89、AUC 0.952，二肽组成基线为0.79/0.853。味觉：MoLFormer准确率0.99、ChemBERTa2为0.98；Table 2测试集为323苦＋263甜＋44鲜。图像纤维度：Fig. 6C报告R²=0.81、RMSE=8.03。 |
| 划分与泄漏控制 | Methods三任务均写80/20；未见独立来源、分子骨架或肽同源簇隔离验证的充分说明。图像总数80与Fig. 6C测试n=20并不符合所述比例。 |
| 限制与可比性 | 图像仅来自一项既有研究，样本少；文中留出测试不足以证明跨研究或新骨架泛化。原文有口径差异：甜味数量Methods为1313、Results为1331；图像Methods写80/20，但Fig. 6C写测试n=20，需保留而不自行统一。 |
| 证据位置 | 机构PDF第2—3页Methods；第4页Table 1、第5页Table 2、第6页Fig. 6C、第7页Discussion。表格与图注已视觉确认。 |

[打开本篇六项速读分析](papers/P27_Food_foundation_models.md)

