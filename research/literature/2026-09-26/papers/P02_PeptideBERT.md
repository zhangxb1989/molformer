# P02｜PeptideBERT：三类肽性质预测

PeptideBERT: A Language Model Based on Transformers for Peptide Property Prediction

Chakradhar Guntuboina、Adrita Das、Parisa Mollaei 等；2023；The Journal of Physical Chemistry Letters。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC10683064/) · [已归档PDF](../pdfs/P02_2023_PeptideBERT.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

分别预测肽是否溶血、是否可溶、是否具有nonfouling性质（减少非特异性附着）。三个任务各自训练二分类模型，并非一个统一的多标签活性模型。

## 2. 用了什么模型

以预训练蛋白语言模型ProtBERT编码氨基酸序列，再加分类头微调；用二元交叉熵训练，输出概率。

## 3. 用了什么数据集

溶血：DBAASP v3，9,316条，阳性约19.6%；溶解性：PROSO II，18,453条；nonfouling：3,600阳性、13,585阴性。采用随机81%/9%/10%训练、验证、测试划分。

## 4. 最后结果怎么样

论文报告accuracy：溶血86.051%；溶解性在增强设置下70.018%；nonfouling 88.365%。三个数字对应不同任务，不能据此比较哪种性质更有应用价值。 [依据：论文原文](../pdfs/P02_2023_PeptideBERT.pdf)

## 5. 贡献是什么（阅读归纳）

将蛋白语言模型迁移到肽的开发性质评价，展示了同一预训练编码器可分别服务多个肽分类任务，减少手工设计特征的需求。

## 6. 缺陷与局限是什么（阅读判断）

溶血数据存在相同序列的重复或冲突测量，随机划分可能受到相近样本影响；类别不平衡时accuracy也不足以概括筛选能力。对未见家族或化学修饰肽的外推仍需额外证据。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P01](P01_Representation_limits_comment.md) · [返回逐篇索引](README.md) · [下一篇 P03 →](P03_ActFound.md)
