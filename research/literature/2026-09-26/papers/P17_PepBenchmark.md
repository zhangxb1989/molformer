# P17｜PepBenchmark：统一肽机器学习基准

PepBenchmark: A Standardized Benchmark for Peptide Machine Learning

Jiahui Zhang、Rouyi Wang、Kuangqi Zhou 等；2026；International Conference on Learning Representations 2026。

[论文入口](https://arxiv.org/html/2604.10531v1) · [正式会议论文](https://openreview.net/attachment?id=NskQgtSdll&name=pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

针对不同肽研究的数据清洗、负例构建、划分和指标不统一问题，建立共同的数据集、处理流程和评价体系。

## 2. 用了什么模型

没有提出一个单一的新预测网络，而是统一比较指纹、图神经网络、蛋白语言模型和SMILES模型四类方法，形成公共基线与排行榜。

## 3. 用了什么数据集

35个数据集：29个典型肽、6个非典型肽；27个分类、8个回归，覆盖7组用途。按任务提供一致的清洗、表示和划分流程。

## 4. 最后结果怎么样

主要成果是PepBenchData、PepBenchPipeline、PepBenchLeaderboard三部分及统一基线。分类按AUROC、回归按MAE评价，并汇总多个划分；不能以一个跨任务总分代替具体任务结果。 [依据：正式会议论文](https://openreview.net/attachment?id=NskQgtSdll&name=pdf)

## 5. 贡献是什么（阅读归纳）

使模型可以在共同数据和规则下比较，降低每项研究重新整理数据的成本，也为判断改进是否来自模型本身提供条件。

## 6. 缺陷与局限是什么（阅读判断）

统一流程不能自动消除原始标签质量和负例语义问题；典型与非典型肽采用不同相似性处理，仍需按具体任务解释外推难度。正式状态为ICLR 2026会议论文。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P16](P16_LANTERN.md) · [返回逐篇索引](README.md) · [下一篇 P18 →](P18_Phenols_CDFT.md)
