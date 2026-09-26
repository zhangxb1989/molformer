# P22｜GP-MoLFormer：生成新分子

GP-MoLFormer: a foundation model for molecular generation

Jerret Ross、Brian Belgodere、Samuel C. Hoffman 等；2025；Digital Discovery。

[论文入口](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00122f) · [正式发表摘要](https://pubs.rsc.org/en-gb/content/articlelanding/2025/dd/d5dd00122f) · [本次补读原文/材料](https://arxiv.org/html/2405.04912v2)

**阅读范围：预印本v2的正文关键部分；2025正式发表信息保留，正式主文尚未逐表对照。** 更新：2026-09-26。

## 1. 做了什么研究

研究从头分子生成、指定骨架修饰和目标性质优化，并分析训练数据重复与记忆对生成新颖性的影响。

## 2. 用了什么模型

4680万参数的自回归Transformer解码器，使用线性注意力和旋转位置编码。Pair-tuning冻结主体，只训练少量提示嵌入，学习把性质较差的分子转为较优分子。

## 3. 用了什么数据集

PubChem/ZINC约11亿条SMILES；去重版Uniq为6.5亿条。预印本Methods列QED、penalized logP、DRD2训练分子对分别为70,644、60,227、34,404；前两项测试各800个分子，DRD2为1000个。 [来源](https://arxiv.org/html/2405.04912v2)

## 4. 最后结果怎么样

v2 Table 1：Uniq生成3万个分子时IntDiv=0.8655、FCD=0.0591。Table 4：每个种子生成125次的QED最高0.948、有效率94.7%。Table 5：DRD2平均预测活性分数由种子的0.007升至生成物0.844（每种子20次选最高），并非实测活性。 [来源](https://arxiv.org/html/2405.04912v2)

## 5. 贡献是什么（阅读归纳）

用统一分子生成器配合参数较少的pair-tuning处理多种生成任务，同时明确考察记忆、重复数据和生成规模。

## 6. 缺陷与局限是什么（阅读判断）

生成有效性、新颖性和预测器高分不能证明可合成性或真实药效；不同基线的训练/参考分布或种子不同，不能仅凭表中数字排名。预印本对无约束优化的高分，也不代表保留原结构。正式版数值尚未逐表比对。

证据位置：arXiv v2：Results的Table 1/4/5；Methods的Datasets and tokenization、Pair-tuning。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P21](P21_HELM_BERT.md) · [返回逐篇索引](README.md) · [下一篇 P23 →](P23_Systematic_molecular_benchmark.md)
