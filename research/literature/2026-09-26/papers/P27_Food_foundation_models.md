# P27｜食品任务中的基础模型与迁移学习

Leveraging foundation models and transfer learning for peptide transport prediction, molecular taste classification, and visual texture analysis

Yizhou Ma、Qing Ren、Kasper Hettinga 等；2025；Innovative Food Science & Emerging Technologies。

[论文入口](https://www.sciencedirect.com/science/article/pii/S1466856425003315) · [本次补读原文/材料](https://edepot.wur.nl/702069)

**阅读范围：Wageningen机构公开正式论文的正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

用预训练表征分别解决山羊乳肽Caco-2运输分类、分子甜/苦/鲜味分类和食品图像纤维度回归。

## 2. 用了什么模型

肽任务：ESMC嵌入＋MLP或BiLSTM，最好方案加入修饰位点特征；味觉：MoLFormer或ChemBERTa2嵌入＋MLP；图像：CLIP嵌入＋MLP。三个任务分别建模。

## 3. 用了什么数据集

5183条山羊乳肽；ChemTastesDB三种味觉子集，Methods列甜1313、苦1615、鲜220；80张肉类似物、鸡肉与豆腐图像。Methods均写80%/20%训练/测试。 [来源](https://edepot.wur.nl/702069)

## 4. 最后结果怎么样

肽运输：修饰增强BiLSTM准确率0.89、AUC 0.952，二肽组成基线为0.79/0.853。味觉：MoLFormer准确率0.99、ChemBERTa2为0.98；Table 2测试集为323苦＋263甜＋44鲜。图像纤维度：Fig. 6C报告R²=0.81、RMSE=8.03。 [来源](https://edepot.wur.nl/702069)

## 5. 贡献是什么（阅读归纳）

展示如何把已有食品实验标签接到不同基础模型表征上，并证明肽修饰信息在本数据上具有额外价值。

## 6. 缺陷与局限是什么（阅读判断）

图像仅来自一项既有研究，样本少；文中留出测试不足以证明跨研究或新骨架泛化。原文有口径差异：甜味数量Methods为1313、Results为1331；图像Methods写80/20，但Fig. 6C写测试n=20，需保留而不自行统一。

证据位置：机构PDF第2—3页Methods；第4页Table 1、第5页Table 2、第6页Fig. 6C、第7页Discussion。表格与图注已视觉确认。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P26](P26_NPCLM.md) · [返回逐篇索引](README.md)
