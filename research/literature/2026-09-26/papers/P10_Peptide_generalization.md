# P10｜从标准肽外推到修饰肽：模型比较

How to build machine learning models able to extrapolate from standard to modified peptides

Raúl Fernández-Díaz、Rodrigo Ochoa、Thanh Lam Hoang 等；2025；Journal of Cheminformatics。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12751563/) · [已归档PDF](../pdfs/P10_2025_Peptide_generalization.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

直接研究在标准肽上训练的模型，能否预测修饰肽，并比较表示方式和相似性分割对结论的影响。

## 2. 用了什么模型

比较化学指纹、MoLFormer、ChemBERTa-2、PeptideCLM、ESM、ProtT5、PepLand等表示，下游使用SVM或LightGBM；并非提出单一新大型网络。

## 3. 用了什么数据集

四类任务形成八个标准/修饰数据集：结合1,002/299，穿膜2,324/480，抗菌9,855/1,880，抗病毒4,754/444。以相似性约束划分，并重复多个随机种子。

## 4. 最后结果怎么样

作者报告，标准肽内插时表示差别不大；修饰肽内插时化学语言模型更有优势。标准到修饰外推时性能明显下降，摘要概括约下降50%，其中化学指纹和ChemBERTa-2相对较好；该增减不是某个统一准确率。 [依据：论文原文](../pdfs/P10_2025_Peptide_generalization.pdf)

## 5. 贡献是什么（阅读归纳）

把容易混淆的内插和化学修饰外推分开评价，指出化学相似性与表示选择应按应用情境判断，并给出可比较的数据资源。

## 6. 缺陷与局限是什么（阅读判断）

修饰肽数据明显较少，外推结论受活性和修饰类型覆盖限制；部分负例来自其他活性来源，不一定是真阴性。四个任务上的相对优劣不能推广为某个模型总是最好。

证据位置：摘要Scientific contribution；Table 1。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P09](P09_PepLand.md) · [返回逐篇索引](README.md) · [下一篇 P11 →](P11_AOP_DRL.md)
