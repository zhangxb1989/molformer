# P16｜LANTERN：TCR与肽结合预测

LANTERN: TCR-peptide binding prediction via large language model representations

Cong Qi、Hanzhang Fang、Siqi Jiang 等；2026；PeerJ。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC13045841/) · [已归档PDF](../pdfs/P16_2026_LANTERN.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

预测T细胞受体TCR与肽是否结合，重点评价对训练中未见肽及少样本情境的泛化。

## 2. 用了什么模型

使用ESM编码TCR氨基酸序列，MoLFormer编码肽的SMILES，多头交叉注意力融合两侧表示，再经MLP预测结合概率。

## 3. 用了什么数据集

TCHard基准，包括NA、RN、GenNA、GenRN等设置，约16万TCR和1,341种独立肽。配对记录数不等于独立肽数量；评价区分参考负例和随机负例。

## 4. 最后结果怎么样

论文报告在TCHard上有竞争力的AUROC表现，尤其在随机对照负例及未见表位设置下；使用5折、3个随机种子。当前笔记保留按情境的定性结论，不将多组实验合为一个准确率。 [依据：论文原文](../pdfs/P16_2026_LANTERN.pdf)

## 5. 贡献是什么（阅读归纳）

融合蛋白序列与肽化学表示，通过交叉注意力建模配对信息，是MoLFormer进入多肽相关任务的明确应用。

## 6. 缺陷与局限是什么（阅读判断）

阴性配对的构建方式会影响任务难度。文中的zero-shot指未见肽测试，不是整个模型无需任务训练；TCR—肽结合成绩也不能外推为其他肽活性或完整免疫反应的预测能力。

证据位置：摘要与TCHard实验。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P15](P15_PeptideCLM2.md) · [返回逐篇索引](README.md) · [下一篇 P17 →](P17_PepBenchmark.md)
