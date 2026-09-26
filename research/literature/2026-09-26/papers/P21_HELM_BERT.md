# P21｜HELM-BERT：保留修饰肽拓扑的表示

HELM-BERT: Topology-Aware Representations for Chemically Modified Peptides

Seungeon Lee、Takuto Koyama、Itsuki Maeda 等；2026；Journal of Chemical Information and Modeling。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417886/) · [已归档PDF](../pdfs/P21_2026_HELM_BERT.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

研究显式写出单体、化学修饰和共价连接的HELM表示，能否比普通氨基酸序列或原子级SMILES更好地表达修饰肽及环肽。

## 2. 用了什么模型

直接在HELM字符串上预训练编码器式Transformer；比较全微调、仅预测头训练及线性探针。肽—蛋白任务结合冻结的ESM-2蛋白表示。

## 3. 用了什么数据集

预训练39,079条独立肽；通透性7,715条；Propedia配对分组含20,057个阳性配对，蛋白簇分组筛选后20,055；另使用ChEMBL相互作用基准。

## 4. 最后结果怎么样

正式版摘要报告，随机划分通透性R²=0.668，在Murcko骨架划分下也保持最佳平均表现；同架构SMILES对照在全微调时缩小差距，而冻结表示时HELM优势更清楚。 [依据：论文原文](../pdfs/P21_2026_HELM_BERT.pdf)

## 5. 贡献是什么（阅读归纳）

让分子表示本身显式保留修饰和连接拓扑，并通过架构匹配对照区分表示格式与模型架构的影响。

## 6. 缺陷与局限是什么（阅读判断）

HELM输入依赖正确的单体与连接注释；结果仍受数据覆盖和预训练重叠影响。相互作用负例采用构造方式，不等同全部实验确认无结合。采用2026正式版结论，不能把早期预印本缺口继续套用。

证据位置：正式版摘要与Methods。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P20](P20_Barrier_metabolomics.md) · [返回逐篇索引](README.md) · [下一篇 P22 →](P22_GP_MoLFormer.md)
