# P11｜AOP-DRL：抗氧化肽预测

AOP-DRL: A deep representation learning framework for the computational prediction of antioxidant peptides

Yongzhu Zhou、Wanlin Liu、Qiao Liu 等；2025；Computational and Structural Biotechnology Journal。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800373/) · [已归档PDF](../pdfs/P11_2025_AOP_DRL.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

利用蛋白预训练表示识别抗氧化肽，同时利用卷积捕捉可能与功能相关的局部序列模式。

## 2. 用了什么模型

AOP-DRL使用ESM-2 650M模型的1,280维残基表征，结合TextCNN和分类头，输出抗氧化/非抗氧化概率。

## 3. 用了什么数据集

来自AnOxPePred的1,404条肽：687阳性，其中456条自由基清除、231条螯合；717阴性。论文评价P60/P70/P80/P90等相似性设置，并使用分层留出及交叉验证。

## 4. 最后结果怎么样

作者摘要报告，相对所比较抗氧化专用模型的平均accuracy，P60、P70、P80、P90分别提高7.26%、2.57%、2.59%、4.20%。这是四种设置的增幅，不能当成最终准确率；也不能把ESM单独基线分数当作AOP-DRL结果。 [依据：论文原文](../pdfs/P11_2025_AOP_DRL.pdf)

## 5. 贡献是什么（阅读归纳）

将大型蛋白模型提供的序列表示与局部卷积结合，检验预训练特征用于小规模抗氧化肽筛选的可行性。

## 6. 缺陷与局限是什么（阅读判断）

阳性包含不同抗氧化作用类型，统一二分类不能区分具体机制与强度。正文对冻结范围和学习方式的描述不完全一致，且不同数据划分之间的关系仍需澄清；本轮只整理论文报告。

证据位置：摘要与模型/数据方法。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P10](P10_Peptide_generalization.md) · [返回逐篇索引](README.md) · [下一篇 P12 →](P12_MFP_MFL.md)
