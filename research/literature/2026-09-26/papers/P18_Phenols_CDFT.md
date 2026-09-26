# P18｜酚类抗氧化预测：CDFT与决策树

Accurate & simple open-sourced no-code machine learning and CDFT predictive models for the antioxidant activity of phenols

Andrés Halabi Diaz、Franco Galdames、Patricia Velásquez；2024；Computational and Theoretical Chemistry。

[论文入口](https://researchers.unab.cl/en/publications/accurate-amp-simple-open-sourced-no-code-machine-learning-and-cdf/) · [作者机构收录的论文摘要](https://researchers.unab.cl/en/publications/accurate-amp-simple-open-sourced-no-code-machine-learning-and-cdf/)

**阅读范围：摘要／部分内容。** 更新：2026-09-26。 未取得的细节会明确留空，不代表原文没有报告。

## 1. 做了什么研究

用酚类分子的电子反应性与结构特征预测DPPH抗氧化活性，强调无需编程的建模流程和可解释规则。

## 2. 用了什么模型

在GFN1-xTB、GFN2-xTB层面计算概念密度泛函理论（CDFT）描述符；结合PCA、InfoGain等筛选方法，训练J48、RandomTree、JCHAID等树模型。

## 3. 用了什么数据集

作者机构保存的论文摘要明确为202种酚类化合物的抗DPPH数据。精确类别阈值、各集合数量和数据清洗后的分布，本笔记尚未取得。

## 4. 最后结果怎么样

摘要报告决策树在内部与外部验证中accuracy均超过85%。这里的“外部”沿用作者称谓，尚不能确认它是独立来源还是原数据池的留出集合，也未取得各模型完整结果表。 [依据：作者机构收录的论文摘要](https://researchers.unab.cl/en/publications/accurate-amp-simple-open-sourced-no-code-machine-learning-and-cdf/)

## 5. 贡献是什么（阅读归纳）

将电子反应性描述符与容易阅读的决策树规则连接，为酚类抗氧化结构—活性关系提供简单且可解释的建模路线。

## 6. 缺陷与局限是什么（阅读判断）

样本规模较小，标签阈值与划分会明显影响结果；DPPH化学清除活性不等同细胞抗氧化或肠屏障保护。阅读限制：主要依据作者机构摘要，尚未完成全文分析。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P17](P17_PepBenchmark.md) · [返回逐篇索引](README.md) · [下一篇 P19 →](P19_Antioxidant_QSAR.md)
