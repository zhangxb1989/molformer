# P22｜GP-MoLFormer：生成新分子

GP-MoLFormer: a foundation model for molecular generation

Jerret Ross、Brian Belgodere、Samuel C. Hoffman 等；2025；Digital Discovery。

[论文入口](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00122f) · [正式发表摘要](https://pubs.rsc.org/en-gb/content/articlelanding/2025/dd/d5dd00122f)

**阅读范围：摘要／部分内容。** 更新：2026-09-26。 未取得的细节会明确留空，不代表原文没有报告。

## 1. 做了什么研究

把化学语言预训练用于生成分子，覆盖从头生成、限定骨架的分子修饰，以及按目标性质优化三类任务。

## 2. 用了什么模型

GP-MoLFormer为约4,680万参数的自回归Transformer解码器，使用线性注意力和旋转位置编码；性质优化采用按性质排序的分子对进行pair-tuning。

## 3. 用了什么数据集

正式论文摘要报告训练语料超过11亿条化学SMILES；下游是生成及优化任务，不是一个活性二分类数据集。

## 4. 最后结果怎么样

作者报告三类任务表现优于或接近所比基线，并产生较高多样性的分子；同时发现明显的训练数据记忆，训练重复会降低生成新颖性。此处保留任务层面的结论，不换算成活性准确率。 [依据：正式发表摘要](https://pubs.rsc.org/en-gb/content/articlelanding/2025/dd/d5dd00122f)

## 5. 贡献是什么（阅读归纳）

将通用化学语言模型扩展为多种生成任务的基础，并提出pair-tuning；另外把训练记忆、新颖性与生成规模之间的关系纳入分析。

## 6. 缺陷与局限是什么（阅读判断）

有效SMILES和新骨架不代表可合成、无毒或有真实生物活性；生成可能重复训练数据。阅读限制：本篇以2025正式摘要为依据，尚未逐项整理生成基准数值。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P21](P21_HELM_BERT.md) · [返回逐篇索引](README.md) · [下一篇 P23 →](P23_Systematic_molecular_benchmark.md)
