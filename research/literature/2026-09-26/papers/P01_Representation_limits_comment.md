# P01｜小分子表征学习的局限：评论文章

Limitations of representation learning in small molecule property prediction

Ana Laura Dias、Latimah Bustillo、Tiago Rodrigues；2023；Nature Communications。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC10575963/) · [已归档PDF](../pdfs/P01_2023_Representation_limits_comment.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

讨论分子性质预测中，复杂的表征学习方法为什么未必稳定优于指纹、描述符等传统表示，强调正确理解数据条件与评估结果。文章属于评论。

## 2. 用了什么模型

没有提出或训练新的预测模型；讨论传统分子表示与神经网络学习表示的优劣和适用范围。

## 3. 用了什么数据集

没有新增独立实验数据集，主要围绕已有分子预测研究展开讨论，与本库P23系统比较论文相关。

## 4. 最后结果怎么样

产出是方法学判断，而非新的准确率或排行榜。其核心意思是：不能仅凭模型更复杂，就推定分子预测一定更好，结论要依赖具体数据和合理比较。 [依据：论文原文](../pdfs/P01_2023_Representation_limits_comment.pdf)

## 5. 贡献是什么（阅读归纳）

提供了理解表征学习局限的视角，帮助读者区分模型宣传、数据条件与真实实验支持。适合作为研究动机和讨论部分的参考。

## 6. 缺陷与局限是什么（阅读判断）

评论不提供新的独立验证，不能和P23算作两项互相复现的实验；也不能据此得出所有深度学习模型都无效的结论。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 F01](F01_MoLFormer.md) · [返回逐篇索引](README.md) · [下一篇 P02 →](P02_PeptideBERT.md)
