# P27｜食品任务中的基础模型与迁移学习

Leveraging foundation models and transfer learning for peptide transport prediction, molecular taste classification, and visual texture analysis

Yizhou Ma、Qing Ren、Kasper Hettinga 等；2025；Innovative Food Science & Emerging Technologies。

[论文入口](https://www.sciencedirect.com/science/article/pii/S1466856425003315)

**阅读范围：摘要／部分内容。** 更新：2026-09-26。 未取得的细节会明确留空，不代表原文没有报告。

## 1. 做了什么研究

在三类食品相关任务中考察基础模型的迁移使用：肽运输预测、小分子味觉分类、图像质地分析。三者是不同输入和标签的任务。

## 2. 用了什么模型

ESMC用于肽运输，MoLFormer用于小分子味觉，视觉模型用于图像任务；不能把论文概括成“MoLFormer预测肽运输”。

## 3. 用了什么数据集

分别使用肽序列、分子SMILES和图像数据。当前可见摘要不足以确认各数据集的准确样本量、来源、重复样本和划分方式。

## 4. 最后结果怎么样

摘要报告味觉任务accuracy达到0.99。该成绩只对应味觉实验；肽运输和图像任务的完整结果尚未核对，不能把0.99套用于这些任务。 [依据：论文来源](https://www.sciencedirect.com/science/article/pii/S1466856425003315)

## 5. 贡献是什么（阅读归纳）

展示了不同基础模型在食品研究中的迁移方向，帮助区分模型、输入模态与应用任务之间的对应关系。

## 6. 缺陷与局限是什么（阅读判断）

只有摘要与可见页面支持当前笔记，尚不能判断高准确率是否在独立化合物或外部来源上保持。三个任务并列展示，不代表已经建立统一的多模态肽活性模型。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P26](P26_NPCLM.md) · [返回逐篇索引](README.md)
