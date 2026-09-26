# P07｜Deep2Pep：四种肽活性的多标签预测

Deep2Pep: A deep learning method in multi-label classification of bioactive peptide

Lihua Chen、Zhenkang Hu、Yuzhi Rong 等；2024；Computational Biology and Chemistry。

[论文入口](https://www.sciencedirect.com/science/article/pii/S1476927124000094) · [PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/38308955/)

**阅读范围：摘要／部分内容。** 更新：2026-09-26。 未取得的细节会明确留空，不代表原文没有报告。

## 1. 做了什么研究

允许同一条肽同时具有多种活性，联合预测抗菌、抗高血压、抗氧化和抗高血糖四个标签。

## 2. 用了什么模型

结合序列编码、embedding和tokenizer，使用BiLSTM、注意力残差模块及BERT encoder。作者摘要认为BiLSTM起主要作用；仅出现BERT名称不能认定使用了大规模预训练权重。

## 3. 用了什么数据集

出版社数据段列出UniProt、APD、AHTPDB、DFBP、BIOPEP-UWM、BGI-marine等来源，并称负例取自缺少功能信息的UniProt序列。本笔记未确认去重后的独立样本数与完整标签分布。

## 4. 最后结果怎么样

摘要报告subset accuracy=0.737、Macro F1=0.734、Hamming loss=0.095，并称优于所比较模型。Subset accuracy要求一条肽的标签集合全部匹配，不能当作普通二分类正确率。 [依据：PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/38308955/)

## 5. 贡献是什么（阅读归纳）

把四类肽活性组织为联合多标签任务，利用序列上下文及标签共同学习，使多功能肽不必被强制归入单一类别。

## 6. 缺陷与局限是什么（阅读判断）

缺少功能注释不代表真正无活性，负标签可能含未被研究的阳性肽。阅读限制：目前为摘要与出版社可见段落，去重、分割及预训练来源尚未完整确认。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P06](P06_DeepAIP.md) · [返回逐篇索引](README.md) · [下一篇 P08 →](P08_PeptideCLM.md)
