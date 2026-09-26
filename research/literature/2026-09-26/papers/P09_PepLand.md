# P09｜PepLand：典型与修饰肽的图表征

PepLand: a large-scale pre-trained peptide representation model for a comprehensive landscape of both canonical and non-canonical amino acids

Ruochi Zhang、Haoran Wu、Chang Liu 等；2025；Briefings in Bioinformatics。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12315545/) · [已归档PDF](../pdfs/P09_2025_PepLand.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

统一表示典型肽和包含非典型氨基酸的修饰肽，使模型能保留普通氨基酸序列难以表达的化学结构信息。

## 2. 用了什么模型

PepLand把SMILES转成分子图，结合原子、片段信息及AdaFrag，通过两阶段预训练获得表示，再接任务预测头。它是图表征模型。

## 3. 用了什么数据集

主要包括典型肽穿膜、溶解性、结合，以及非典型肽穿膜、结合五组基准；预训练先利用大规模典型肽，再适应修饰肽。各任务规模应分别记录。

## 4. 最后结果怎么样

原Table 1中典型CPP、溶解性对应AUC为0.838、0.662；非典型CPP、结合任务的0.628、0.768是Spearman相关系数。这些数字不能全部称为F1或准确率。 [依据：论文原文](../pdfs/P09_2025_PepLand.pdf)

## 5. 贡献是什么（阅读归纳）

通过原子与片段层面的联合表示，拓展了对非典型残基、化学修饰肽的建模能力，提供了与序列模型不同的路线。

## 6. 缺陷与局限是什么（阅读判断）

各基准的任务和指标不同，不能拼成一个统一性能排序；也未据现有记录确认所有基准都采用同源性或骨架隔离。结果支持特定数据上的表示价值，不能自动说明对任意修饰都能外推。

证据位置：摘要及Table 1。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P08](P08_PeptideCLM.md) · [返回逐篇索引](README.md) · [下一篇 P10 →](P10_Peptide_generalization.md)
