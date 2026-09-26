# P06｜DeepAIP：预训练特征识别抗炎肽

DeepAIP: Deep learning for anti-inflammatory peptide prediction using pre-trained protein language model features based on contextual self-attention network

Lun Zhu、Qingguo Yang、Sen Yang；2024；International Journal of Biological Macromolecules。

[论文入口](https://pubmed.ncbi.nlm.nih.gov/39357724/) · [PubMed摘要](https://pubmed.ncbi.nlm.nih.gov/39357724/) · [本次补读原文/材料](https://www.sciencedirect.com/science/article/pii/S0141813024069812)

**阅读范围：正式摘要及出版社可见流程段落；尚缺完整结果表。** 更新：2026-09-26。

## 1. 做了什么研究

利用预训练蛋白语言模型从序列提取信息，预测肽是否具有抗炎活性，并比较不同预训练特征的效果。

## 2. 用了什么模型

使用Prot-T5-XL-Uniref50提取并平均池化序列特征，再结合上下文自注意力与多尺度卷积。作者在八种预训练特征中比较后选择ProtT5。

## 3. 用了什么数据集

出版社流程段落说明：合并PreAIP、AIPpred、IF-AIP所用数据，经CD-HIT阈值0.9处理后按80%/20%分为训练/测试；另有17条抗炎阳性序列。主集合准确样本量和阴性构造仍未取得。 [来源](https://www.sciencedirect.com/science/article/pii/S0141813024069812)

## 4. 最后结果怎么样

摘要报告，相对次优比较方法，MCC和accuracy分别提高16.35%和6.91%；另将17条阳性肽全部识别为抗炎肽。这些是作者报告的增幅和阳性识别结果，不是可直接代换的绝对MCC/accuracy。 [来源](https://www.sciencedirect.com/science/article/pii/S0141813024069812)

## 5. 贡献是什么（阅读归纳）

展示上下文注意力对预训练肽序列特征的再加工方式，并比较特征来源，而非只更换一个分类器。

## 6. 缺陷与局限是什么（阅读判断）

17条外部序列全为阳性，不能估计特异度。0.9去冗余阈值不能自动证明严格跨同源簇外推。完整结果表、绝对分数与增幅计算口径仍待补读。

证据位置：PubMed 39357724摘要；ScienceDirect Highlights及DeepAIP construction process条目1—5。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P05](P05_PepNet.md) · [返回逐篇索引](README.md) · [下一篇 P07 →](P07_Deep2Pep.md)
