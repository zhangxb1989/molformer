# P07｜Deep2Pep：四种肽活性的多标签预测

Deep2Pep: A deep learning method in multi-label classification of bioactive peptide

Lihua Chen、Zhenkang Hu、Yuzhi Rong 等；2024；Computational Biology and Chemistry。

[论文入口](https://www.sciencedirect.com/science/article/pii/S1476927124000094) · [PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/38308955/) · [本次补读原文/材料](https://www.sciencedirect.com/science/article/pii/S1476927124000094)

**阅读范围：正式摘要及出版社数据/序列分析片段；尚未完整阅读正文。** 更新：2026-09-26。

## 1. 做了什么研究

允许同一条肽同时具有多种活性，联合预测抗菌、抗高血压、抗氧化和抗高血糖四个标签。

## 2. 用了什么模型

BiLSTM、注意力残差模块与BERT encoder联合预测四类活性；Highlights说明使用加权focal loss应对标签不平衡。BiLSTM起主要作用；尚未确认BERT来自大规模预训练权重。

## 3. 用了什么数据集

来源为UniProt、APD、AHTPDB、DFBP、BIOPEP-UWM、BGI-marine。可见Sequence analysis列出抗菌3014、降压2597、抗氧化1202、降血糖516个阳性标签，另称活性阳性6772、阴性863；多标签计数会重叠，不能把各功能阳性相加当成独立肽数。UniProt阴性取自缺少功能注释的序列。 [来源](https://www.sciencedirect.com/science/article/pii/S1476927124000094)

## 4. 最后结果怎么样

摘要报告subset accuracy=0.737、Macro F1=0.734、Hamming loss=0.095，并称优于所比较模型。Subset accuracy要求一条肽的标签集合全部匹配，不能当作普通二分类正确率。 [来源](https://www.sciencedirect.com/science/article/pii/S1476927124000094)

## 5. 贡献是什么（阅读归纳）

把四类肽活性组织为联合多标签任务，利用序列上下文及标签共同学习，使多功能肽不必被强制归入单一类别。

## 6. 缺陷与局限是什么（阅读判断）

缺注释不等于实验确认无活性；抗高血糖阳性标签明显较少，汇总分数不能代替逐标签表现。完整去重、集合划分与阈值仍未取得。

证据位置：ScienceDirect的Highlights、Dataset、Sequence analysis、Conclusion；PubMed 38308955摘要。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P06](P06_DeepAIP.md) · [返回逐篇索引](README.md) · [下一篇 P08 →](P08_PeptideCLM.md)
