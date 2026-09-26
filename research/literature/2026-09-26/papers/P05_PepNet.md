# P05｜PepNet：抗炎与抗菌肽预测

PepNet: an interpretable neural network for anti-inflammatory and antimicrobial peptides prediction using a pre-trained protein language model

Jiyun Han、Tongxin Kong、Juntao Liu；2024；Communications Biology。

[论文入口](https://www.nature.com/articles/s42003-024-06911-1) · [已归档PDF](../pdfs/P05_2024_PepNet.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

分别预测抗炎肽和抗菌肽，尝试同时利用预训练语义、序列局部模式和理化性质，并辅助解释哪些位置与活性相关。

## 2. 用了什么模型

融合ProtT5表征、one-hot编码和14种理化特征，经残差膨胀CNN、Transformer、池化及MLP输出类别；序列按固定长度40处理。

## 3. 用了什么数据集

按数据准备节记录：抗炎4,194条，训练/验证/测试为2,516/629/1,049；抗菌8,346条，对应5,340/1,336/1,670。数据来自IEDB、APD3/DADP等来源。

## 4. 最后结果怎么样

抗菌任务报告F1=0.951、MCC=0.901。论文同时开展抗炎预测和解释分析；这里不把抗菌成绩当作抗炎成绩。 [依据：论文原文](../pdfs/P05_2024_PepNet.pdf)

## 5. 贡献是什么（阅读归纳）

将预训练蛋白特征与可解释的理化特征融合，结合局部卷积和序列注意力，覆盖两类生物活性筛选任务。

## 6. 缺陷与局限是什么（阅读判断）

固定长度处理可能损失长序列信息；已有划分不能直接证明远距离序列外推。正文后部与数据准备节存在抗炎/抗菌数据名对调，本笔记采用数据准备节口径；不据此猜测未核实的实验设置。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P04](P04_AutoPeptideML.md) · [返回逐篇索引](README.md) · [下一篇 P06 →](P06_DeepAIP.md)
