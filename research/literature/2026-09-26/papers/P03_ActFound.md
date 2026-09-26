# P03｜ActFound：少样本化合物活性预测

A bioactivity foundation model using pairwise meta-learning

Bin Feng、Zequn Liu、Nanlan Huang 等；2024；Nature Machine Intelligence。

[论文入口](https://www.nature.com/articles/s42256-024-00876-w) · [正式摘要与数据说明](https://www.nature.com/articles/s42256-024-00876-w) · [本次补读原文/材料](https://www.researchgate.net/publication/383120443_A_bioactivity_foundation_model_using_pairwise_meta-learning)

**阅读范围：作者公开稿的正文关键部分；版式稿仍有上线日期占位符，不冒充已核对的最终排版版。** 更新：2026-09-26。

## 1. 做了什么研究

面向每个实验仅有少量已测化合物的活性回归，学习同一assay内的活性差，缓解跨实验测量尺度不一致的问题。

## 2. 用了什么模型

2048维Morgan指纹输入共享的两层感知机，再接线性层构成孪生网络；结合成对学习、元学习和相邻assay辅助微调。它没有使用分子语言模型作编码器。

## 3. 用了什么数据集

ChEMBL含35,644个assays；正式摘要写约160万活性记录，作者公开稿Methods写约140万、70万独立化合物，两种口径保留。评估包括ChEMBL、BindingDB、FS-Mol、pQSAR-ChEMBL、KIBA、Davis，另有FEP与GDSC实验。 [来源](https://www.researchgate.net/publication/383120443_A_bioactivity_foundation_model_using_pairwise_meta-learning)

## 4. 最后结果怎么样

ChEMBL/BindingDB的16-shot实验中，作者报告r²和RMSE均优于所比方法；每个assay用16个已测化合物微调。FEP实验中使用40%实测数据、平均约12个化合物微调后，作者报告超过FEP+(OPLS4)。这里的r²定义为max(Pearson相关系数,0)²，不是通常的回归决定系数。 [来源](https://www.researchgate.net/publication/383120443_A_bioactivity_foundation_model_using_pairwise_meta-learning)

## 5. 贡献是什么（阅读归纳）

把同一实验内可比较的活性差与跨实验元学习结合，使大量零散实验标签能够支持新assay的少样本建模。

## 6. 缺陷与局限是什么（阅读判断）

作者指出未使用靶蛋白序列或实验文字描述，输入仍为简单分子指纹。FEP结果依赖目标assay支持标签，不能理解为无标签替代物理计算；数据量的摘要/正文差异尚未解决。

证据位置：作者公开稿：Fig. 1—4；Methods的Problem setting、Pairwise learning、Training data curation、Implementation details；Discussion。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P02](P02_PeptideBERT.md) · [返回逐篇索引](README.md) · [下一篇 P04 →](P04_AutoPeptideML.md)
