# P08｜PeptideCLM：环肽通透性预测

Peptide-Aware Chemical Language Model Successfully Predicts Membrane Diffusion of Cyclic Peptides

Aaron L. Feller、Claus O. Wilke；2025；Journal of Chemical Information and Modeling。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC11971985/)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

研究将肽化学结构纳入语言模型预训练，是否有助于预测环肽通过膜的能力，尤其关注与训练数据不同的化学簇。

## 2. 用了什么模型

PeptideCLM约4,400万参数，以肽和小分子SMILES预训练，下游做通透性回归；五个模型取均值，并按logPexp=-5.5派生可通透/不可通透类别。

## 3. 用了什么数据集

约2,300万条肽与小分子用于混合预训练；下游使用CycPeptMPDB的PAMPA子集，移除检测下限为-10的记录。总库规模不等于筛选后的训练规模。

## 4. 最后结果怎么样

对应混合预训练设置，论文报告AUROC=0.781±0.067、AUPRC=0.738±0.161、RMSE=0.742±0.214；评价采用六簇轮流留出，分数波动也随测试簇变化。 [依据：论文来源](https://pmc.ncbi.nlm.nih.gov/articles/PMC11971985/)

## 5. 贡献是什么（阅读归纳）

把小分子与肽化学表示结合，并使用留簇评价检验环肽通透性的结构外推，比只报告随机测试更贴近化学空间迁移问题。

## 6. 缺陷与局限是什么（阅读判断）

PAMPA是人工膜实验，不能直接等同细胞摄取或肠屏障保护。排除检测下限记录会改变目标人群；不同簇间波动较大。作者预训练数据存在后续修正版，阅读时需区分数据版本。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P07](P07_Deep2Pep.md) · [返回逐篇索引](README.md) · [下一篇 P09 →](P09_PepLand.md)
