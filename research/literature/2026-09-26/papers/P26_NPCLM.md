# P26｜NPCLM：天然产物领域化学语言模型

Chemical Language Models for Natural Products: A State-Space Model Approach

Ho-Hsuan Wang、Afnan Sultan、Andrea Volkamer 等；2026；arXiv。

[论文入口](https://arxiv.org/html/2602.13958v1) · [arXiv v1摘要与正文](https://arxiv.org/html/2602.13958v1)

**阅读范围：预印本v1关键部分。** 更新：2026-09-26。 当前仅确认arXiv v1，未确认正式接收。

## 1. 做了什么研究

研究面向天然产物预训练的模型，比较状态空间模型与Transformer，以及不同tokenizer对生成和性质预测的影响。

## 2. 用了什么模型

从头训练Mamba、Mamba-2和GPT，比较八种tokenizer；另以MoLFormer-XL、ChemBERTa-2等作对照，并考察领域适应。生成与分类分别评价。

## 3. 用了什么数据集

预训练1,030,273种天然产物；下游包括6,651条肽通透性数据、4,431条FourTastes味觉数据，以及约2.6万条抗癌活性数据。

## 4. 最后结果怎么样

作者摘要报告：随机划分下Mamba系列比GPT高约0.02—0.04 MCC，骨架划分下表现接近；Mamba生成的有效性/独特性较好，GPT生成的新颖性略高。领域预训练可在所测任务上接近更大通用语料模型。 [依据：arXiv v1摘要与正文](https://arxiv.org/html/2602.13958v1)

## 5. 贡献是什么（阅读归纳）

将天然产物领域数据、架构和tokenization放在共同实验中比较，显示数据领域匹配可能比单纯增大通用预训练规模更值得研究。

## 6. 缺陷与局限是什么（阅读判断）

随机划分优势在骨架划分下减弱，说明泛化结论依赖评价设置；只覆盖少数性质任务。当前仅确认2026-02-15的arXiv v1，不能写成已正式接收论文。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P25](P25_TIDE.md) · [返回逐篇索引](README.md) · [下一篇 P27 →](P27_Food_foundation_models.md)
