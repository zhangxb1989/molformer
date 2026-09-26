# P23｜分子性质预测：关键因素的系统比较

A systematic study of key elements underlying molecular property prediction

Jianyuan Deng、Zhibo Yang、Hehe Wang 等；2023；Nature Communications。

[论文入口](https://www.nature.com/articles/s41467-023-41948-6) · [已归档PDF](../pdfs/P23_2023_Systematic_molecular_benchmark.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

系统比较分子性质预测中的表示方式和模型，检验数据规模、噪声、分布以及活性悬崖等因素如何改变模型表现。

## 2. 用了什么模型

比较描述符/指纹上的RF、XGBoost、SVM，与GRU、MolBERT、图神经网络等学习表示模型。

## 3. 用了什么数据集

包括MoleculeNet、阿片类相关数据及其他活性数据，并构造不同规模的实验。总计训练62,820个模型实例：这是模型数量，不是分子样本量。

## 4. 最后结果怎么样

在所测试的多数数据条件下，学习表示没有稳定表现出相对传统表示的优势；活性悬崖显著影响预测，足够数据规模是学习表示发挥优势的重要条件。没有一个跨所有数据集的统一准确率。 [依据：论文原文](../pdfs/P23_2023_Systematic_molecular_benchmark.pdf)

## 5. 贡献是什么（阅读归纳）

以大量受控比较把讨论从“哪个网络更新”转向表示、数据和评价条件，为设置有竞争力的传统基线提供实验依据。

## 6. 缺陷与局限是什么（阅读判断）

结论受当时所选模型、数据及训练方案限制，不能推导为后来所有预训练模型都无效。P01是对相关问题的评论，不能视为另一项独立复现实验。

证据位置：摘要及Results。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P22](P22_GP_MoLFormer.md) · [返回逐篇索引](README.md) · [下一篇 P24 →](P24_Phytochemical_QSPR.md)
