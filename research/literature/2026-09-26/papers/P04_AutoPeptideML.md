# P04｜AutoPeptideML：更可信的肽活性建模

AutoPeptideML: a study on how to build more trustworthy peptide bioactivity predictors

Raúl Fernández-Díaz、Rodrigo Cossio-Pérez、Clement Agoni 等；2024；Bioinformatics。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC11438549/) · [已归档PDF](../pdfs/P04_2024_AutoPeptideML.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

研究肽活性预测的整个建模流程：阴性样本怎么选、训练测试怎么分、预训练特征是否有用，以及传统模型能否达到复杂网络的效果。

## 2. 用了什么模型

提取蛋白语言模型表征或one-hot特征，优化随机森林、LightGBM、KNN，再将交叉验证模型的预测概率平均。

## 3. 用了什么数据集

18个肽二分类任务，单任务约200—20,000条；用于选负例的APML-Peptipedia候选池含92,092条肽、128类活性。比较原划分、改进负例、再加同源性隔离等设置。

## 4. 最后结果怎么样

论文发现，不控制同源性会高估泛化表现；蛋白预训练特征整体优于简单编码，但所比较预训练模型之间并非越大越好。优化后的传统模型集成可与复杂网络竞争。各任务以MCC评价，没有一个适用于全库的统一准确率。 [依据：论文原文](../pdfs/P04_2024_AutoPeptideML.pdf)

## 5. 贡献是什么（阅读归纳）

把负例构建、相似性隔离和自动建模整理成完整流程，使评价更贴近新序列应用，也降低了建立任务模型的门槛。

## 6. 缺陷与局限是什么（阅读判断）

从其他活性肽中挑出的负例仍可能只是没有目标活性记录，未必被实验确认无活性。结论依赖这18个任务，不能推定对所有修饰肽或所有实验体系同样成立。

证据位置：摘要；Methods/Results。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P03](P03_ActFound.md) · [返回逐篇索引](README.md) · [下一篇 P05 →](P05_PepNet.md)
