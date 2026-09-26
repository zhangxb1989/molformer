# P06｜DeepAIP：预训练特征识别抗炎肽

DeepAIP: Deep learning for anti-inflammatory peptide prediction using pre-trained protein language model features based on contextual self-attention network

Lun Zhu、Qingguo Yang、Sen Yang；2024；International Journal of Biological Macromolecules。

[论文入口](https://pubmed.ncbi.nlm.nih.gov/39357724/) · [PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/39357724/)

**阅读范围：摘要／部分内容。** 更新：2026-09-26。 未取得的细节会明确留空，不代表原文没有报告。

## 1. 做了什么研究

利用预训练蛋白语言模型从序列提取信息，预测肽是否具有抗炎活性，并比较不同预训练特征的效果。

## 2. 用了什么模型

DeepAIP使用ProtT5嵌入，结合上下文自注意力和多尺度卷积；作者比较后选择ProtT5作为特征输入。

## 3. 用了什么数据集

使用抗炎肽基准数据，并另外评价17条新收集的抗炎阳性序列。主数据集精确规模、负例来源与划分细节，现有摘要证据不足以确认。

## 4. 最后结果怎么样

摘要报告，相对次优比较方法，MCC和accuracy分别提高16.35%和6.91%；另将17条阳性肽全部识别为抗炎肽。这些是作者报告的增幅和阳性识别结果，不是可直接代换的绝对MCC/accuracy。 [依据：PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/39357724/)

## 5. 贡献是什么（阅读归纳）

展示上下文注意力对预训练肽序列特征的再加工方式，并比较特征来源，而非只更换一个分类器。

## 6. 缺陷与局限是什么（阅读判断）

17条外部序列全部为阳性，无法评价特异度或误报率。阅读限制：未取得完整方法和结果表，增幅的计算口径、同源性控制及主测试集表现仍需全文说明。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P05](P05_PepNet.md) · [返回逐篇索引](README.md) · [下一篇 P07 →](P07_Deep2Pep.md)
