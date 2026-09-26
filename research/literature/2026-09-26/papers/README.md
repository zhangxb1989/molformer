# 每篇文献速读分析

**28篇均已单独成文：27篇近三年文献＋1篇2022年基础论文。** 每篇按同样六项阅读：研究、模型、数据集、结果、贡献、缺陷。点击文献名即可查看，并可在文末切换前后篇。

当前优先完成逐篇阅读整理。第三阶段跨论文详细比较与创新判断按用户要求留待以后；本轮不开展作者代码核查。已有历史研究文件仍保留。

本次补读8篇：F01、P03、P22、P27已补到正文关键部分（所读版本见表）；P20已补正式SI；P06、P07、P18仍为摘要与片段。

“正文关键部分”表示已读与本笔记相关的方法/结果，不等于逐页全文精读。“摘要／部分内容”仍有明确缺口；文档齐全不代表全文证据全部齐全。贡献和缺陷是阅读归纳，缺少证据会另注明。

| 文献（点击打开） | 研究主题 | 主要模型或方法 | 阅读范围 |
|---|---|---|---|
| [F01 · MoLFormer：分子语言模型基础（2022）](F01_MoLFormer.md) | 小分子性质预测 | MoLFormer | 预印本v3关键部分 |
| [P01 · 小分子表征学习的局限：评论文章（2023）](P01_Representation_limits_comment.md) | 模型评价与研究观点 | 讨论指纹、描述符和学习表征 | 正文关键部分 |
| [P02 · PeptideBERT：三类肽性质预测（2023）](P02_PeptideBERT.md) | 溶血、溶解性、抗污损 | ProtBERT＋分类头 | 正文关键部分 |
| [P03 · ActFound：少样本化合物活性预测（2024）](P03_ActFound.md) | 跨实验的定量活性回归 | 成对学习＋元学习 | 作者公开稿关键部分 |
| [P04 · AutoPeptideML：更可信的肽活性建模（2024）](P04_AutoPeptideML.md) | 阴性样本、相似性划分与自动建模 | 蛋白表征＋RF/LightGBM/KNN集成 | 正文关键部分 |
| [P05 · PepNet：抗炎与抗菌肽预测（2024）](P05_PepNet.md) | 抗炎肽、抗菌肽二分类 | ProtT5＋理化特征＋CNN/Transformer | 正文关键部分 |
| [P06 · DeepAIP：预训练特征识别抗炎肽（2024）](P06_DeepAIP.md) | 抗炎肽二分类 | ProtT5＋上下文自注意力 | 摘要＋流程片段 |
| [P07 · Deep2Pep：四种肽活性的多标签预测（2024）](P07_Deep2Pep.md) | 抗菌、降压、抗氧化、降血糖 | BiLSTM＋注意力残差＋BERT编码器 | 摘要＋数据片段 |
| [P08 · PeptideCLM：环肽通透性预测（2025）](P08_PeptideCLM.md) | PAMPA膜通透性回归与派生分类 | 肽/小分子SMILES预训练模型 | 正文关键部分 |
| [P09 · PepLand：典型与修饰肽的图表征（2025）](P09_PepLand.md) | 穿膜、溶解性与结合性质 | 多视图异构图预训练模型 | 正文关键部分 |
| [P10 · 从标准肽外推到修饰肽：模型比较（2025）](P10_Peptide_generalization.md) | 插值与标准→修饰外推 | 指纹、化学/蛋白语言模型＋SVM/LightGBM | 正文关键部分 |
| [P11 · AOP-DRL：抗氧化肽预测（2025）](P11_AOP_DRL.md) | 抗氧化肽二分类 | ESM-2＋TextCNN | 正文关键部分 |
| [P12 · MFP-MFL：多特征融合识别多功能肽（2025）](P12_MFP_MFL.md) | 五种活性多标签预测 | ESM-2/ProtT5/RoBERTa＋图注意力 | 正文关键部分 |
| [P13 · BPFun：七种肽功能联合预测（2025）](P13_BPFun.md) | 七功能多标签分类 | 多尺度CNN＋BiLSTM＋Transformer/注意力 | 正文关键部分 |
| [P14 · PeptiVerse：治疗肽多性质预测平台（2026）](P14_PeptiVerse.md) | 七类治疗肽开发性质 | 冻结ESM-2/PeptideCLM/ChemBERTa＋预测器 | 正文关键部分 |
| [P15 · PeptideCLM-2：扩展肽化学语言模型（2026）](P15_PeptideCLM2.md) | 肽通透性、归巢与相关性质 | SMILES语言模型：MLM/MTR/混合目标 | 预印本＋正式补充材料 |
| [P16 · LANTERN：TCR与肽结合预测（2026）](P16_LANTERN.md) | 免疫受体—肽配对二分类 | ESM＋MoLFormer＋交叉注意力 | 正文关键部分 |
| [P17 · PepBenchmark：统一肽机器学习基准（2026）](P17_PepBenchmark.md) | 数据、处理流程与模型评价标准化 | 指纹、GNN、蛋白/SMILES模型四类基线 | 正文关键部分 |
| [P18 · 酚类抗氧化预测：CDFT与决策树（2024）](P18_Phenols_CDFT.md) | 酚类DPPH抗氧化分类 | 量子描述符＋J48/RandomTree/JCHAID | 摘要＋结论片段 |
| [P19 · 抗氧化QSAR：预测小分子DPPH强度（2025）](P19_Antioxidant_QSAR.md) | DPPH pIC50回归 | Mordred描述符＋树模型集成 | 正文关键部分 |
| [P20 · 肠屏障功能障碍的代谢组预测（2026）](P20_Barrier_metabolomics.md) | 生物样本屏障功能指数回归 | 生物信息约束筛选＋五类回归模型 | 正式摘要＋正式补充材料 |
| [P21 · HELM-BERT：保留修饰肽拓扑的表示（2026）](P21_HELM_BERT.md) | 环肽通透性与肽—蛋白相互作用 | HELM-BERT；配对任务加ESM-2 | 正文关键部分 |
| [P22 · GP-MoLFormer：生成新分子（2025）](P22_GP_MoLFormer.md) | 分子生成、骨架修饰与性质优化 | 自回归Transformer＋pair-tuning | 预印本v2关键部分 |
| [P23 · 分子性质预测：关键因素的系统比较（2023）](P23_Systematic_molecular_benchmark.md) | 表示、数据规模、噪声与活性悬崖 | RF/XGB/SVM与SMILES/GNN模型 | 正文关键部分 |
| [P24 · 植物化学物：Papp、TEER与外排比预测（2026）](P24_Phytochemical_QSPR.md) | Caco-2通透与屏障相关性质 | 分子描述符＋Stacking回归 | 正文关键部分 |
| [P25 · TIDE：双编码器融合TCR与肽信息（2025会议／2026在线）](P25_TIDE.md) | TCR—肽结合二分类 | ESM＋MoLFormer＋交叉注意力 | 正文关键部分 |
| [P26 · NPCLM：天然产物领域化学语言模型（2026）](P26_NPCLM.md) | 天然产物生成与性质分类 | Mamba/Mamba-2/GPT；对照MoLFormer等 | 预印本v1关键部分 |
| [P27 · 食品任务中的基础模型与迁移学习（2025）](P27_Food_foundation_models.md) | 肽运输、分子味觉与图像质地 | ESMC、MoLFormer及视觉模型 | 正式正文关键部分 |

常用指标：accuracy为正确率，但多标签文章可能使用不同定义；F1综合精确率与召回率；MCC综合混淆矩阵信息；AUROC衡量连续分数区分两类的能力；R²通常衡量回归拟合表现，但ActFound的r²特指截断后的Pearson相关系数平方；RMSE/MAE衡量误差。不同任务和划分的数字不能直接排名。

[研究总入口](../README.md) · [进度日志](../work_log.md) · [续接记录](../CONTINUE_HERE.md) · [原结构化长表](../structured_review.md)
