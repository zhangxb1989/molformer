# P13｜BPFun：七种肽功能联合预测

BPFun: a deep learning framework for bioactive peptide function prediction using multi-label strategy by transformer-driven and sequence rich intrinsic information

Lun Zhu、Hao Sun、Sen Yang；2025；BMC Bioinformatics。

[论文入口](https://link.springer.com/article/10.1186/s12859-025-06190-5) · [已归档PDF](../pdfs/P13_2025_BPFun.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

同时识别肽的七种活性，包括抗菌、抗癌、抗糖尿病、抗高血压、抗炎、抗血管生成和抗氧化，并处理功能标签不平衡。

## 2. 用了什么模型

融合五类序列及理化特征，通过多尺度卷积、BiLSTM及注意力提取信息，配合数据增强，输出七个标签概率。使用Transformer模块不等于使用预训练大模型。

## 3. 用了什么数据集

标签记录数分别为2,409、646、514、868、1,678、134、318，存在154条双标签肽，不能把各标签直接相加当独立样本数。CD-HIT 0.9去冗余后随机80%/20%分割。

## 4. 最后结果怎么样

原文摘要及Table 7报告多标签accuracy=0.6577、absolute true=0.6573；后者描述整组标签完全匹配的比例。作者在所用七功能测试集上报告优于比较方法。 [依据：论文原文](../pdfs/P13_2025_BPFun.pdf)

## 5. 贡献是什么（阅读归纳）

整合多种生物与理化信息，把更多肽功能放入同一多标签模型，并尝试通过增强缓解标签不平衡。

## 6. 缺陷与局限是什么（阅读判断）

小类别如抗血管生成只有134条标签记录，总体指标可能掩盖弱势类别。去冗余后随机分割不等于训练测试相似性隔离；数据增强的作用应与真实新样本泛化区分。

证据位置：摘要及Table 7（PDF第21页）。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P12](P12_MFP_MFL.md) · [返回逐篇索引](README.md) · [下一篇 P14 →](P14_PeptiVerse.md)
