# P18｜酚类抗氧化预测：CDFT与决策树

Accurate & simple open-sourced no-code machine learning and CDFT predictive models for the antioxidant activity of phenols

Andrés Halabi Diaz、Franco Galdames、Patricia Velásquez；2024；Computational and Theoretical Chemistry。

[论文入口](https://researchers.unab.cl/en/publications/accurate-amp-simple-open-sourced-no-code-machine-learning-and-cdf/) · [作者机构收录的论文摘要](https://researchers.unab.cl/en/publications/accurate-amp-simple-open-sourced-no-code-machine-learning-and-cdf/) · [本次补读原文/材料](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)

**阅读范围：正式摘要、Highlights和可见结论段落；尚缺完整方法与结果表。** 更新：2026-09-26。

## 1. 做了什么研究

用酚类分子的电子反应性与结构特征预测DPPH抗氧化活性，强调无需编程的建模流程和可解释规则。

## 2. 用了什么模型

在GFN1-xTB、GFN2-xTB层面计算概念密度泛函理论（CDFT）描述符；结合PCA、InfoGain等筛选方法，训练J48、RandomTree、JCHAID等树模型。

## 3. 用了什么数据集

202种酚类化合物的抗DPPH数据。出版社结论段落提到留一交叉验证（LOOCV）与90%/10%划分；具体类别阈值、各类数量及筛选流程仍未取得。 [来源](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)

## 4. 最后结果怎么样

摘要报告各决策树在内部与外部验证中accuracy超过85%；可见结论提到LOOCV与90/10划分。“外部”不宜直接理解为另一个独立来源队列，逐模型分数仍未取得。 [来源](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219)

## 5. 贡献是什么（阅读归纳）

将电子反应性描述符与容易阅读的决策树规则连接，为酚类抗氧化结构—活性关系提供简单且可解释的建模路线。

## 6. 缺陷与局限是什么（阅读判断）

202个样本规模有限；可见材料不足以确认特征筛选是否在验证折内完成。DPPH清除能力不等同细胞抗氧化或肠屏障保护，当前也不能确认对新骨架的泛化。

证据位置：ScienceDirect摘要、Highlights、Conclusion；Universidad Andrés Bello作者机构摘要。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P17](P17_PepBenchmark.md) · [返回逐篇索引](README.md) · [下一篇 P19 →](P19_Antioxidant_QSAR.md)
