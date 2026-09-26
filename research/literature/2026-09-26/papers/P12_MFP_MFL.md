# P12｜MFP-MFL：多特征融合识别多功能肽

MFP-MFL: Leveraging Graph Attention and Multi-Feature Integration for Superior Multifunctional Bioactive Peptide Prediction

Fang Ge、Jianren Zhou、Ming Zhang 等；2025；International Journal of Molecular Sciences。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC11818429/) · [已归档PDF](../pdfs/P12_2025_MFP_MFL.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

预测同一条肽的抗菌、抗炎、抗高血压、抗癌、抗糖尿病五类功能，利用不同预训练表示的互补信息。

## 2. 用了什么模型

融合ESM-2、ProtT5、RoBERTa特征，使用图注意力网络，并引入对抗训练和模型集成。这里按论文层面的模型设计概括。

## 3. 用了什么数据集

论文Table 2列出5,719条单功能肽、198条双功能肽，合计5,917条独立序列；双功能肽会在两个标签中出现，不能重复计作两个独立样本。

## 4. 最后结果怎么样

采用原文主表：多标签accuracy=0.786、precision=0.799。这里的accuracy对应标签集合重合程度，不能理解为78.6%的样本全部预测正确，也不能与普通二分类accuracy直接比较。 [依据：论文原文](../pdfs/P12_2025_MFP_MFL.pdf)

## 5. 贡献是什么（阅读归纳）

把多种预训练表示、图注意力与集成用于多功能肽识别，重点是特征融合和多标签任务建模。

## 6. 缺陷与局限是什么（阅读判断）

单功能与双功能样本很不均衡，少量多功能肽的表现不能仅由总体分数代表；结论段与主表有指标对调。既有记录提示阈值选择可能影响独立评价，应谨慎使用相关分数；本篇不展开代码细节，也不新增核查。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P11](P11_AOP_DRL.md) · [返回逐篇索引](README.md) · [下一篇 P13 →](P13_BPFun.md)
