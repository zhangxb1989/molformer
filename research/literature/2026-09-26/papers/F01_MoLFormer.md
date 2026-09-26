# F01｜MoLFormer：分子语言模型基础

Large-scale chemical language representations capture molecular structure and properties

Jerret Ross、Brian Belgodere、Vijil Chenthamarakshan 等；2022；Nature Machine Intelligence。

[论文入口](https://www.nature.com/articles/s42256-022-00580-7) · [本次补读原文/材料](https://arxiv.org/pdf/2106.09553v3)

**阅读范围：预印本v3的正文关键部分；保留2022年正式发表信息，未逐项比对正式版。** 更新：2026-09-26。

## 1. 做了什么研究

从大量分子的SMILES学习通用表征，再迁移到性质分类和回归。2022年基础论文，单列在近三年文献之外。

## 2. 用了什么模型

MoLFormer编码器：12层、每层12个注意力头、768维隐藏表示，结合线性注意力与旋转位置编码。遮盖语言建模预训练后，接性质预测头，可冻结或整体微调。

## 3. 用了什么数据集

最大预训练语料约11亿条，来自PubChem与ZINC。下游分类包括BBBP、Tox21、ClinTox、HIV、BACE、SIDER；回归包括QM9、QM8、ESOL、FreeSolv、Lipophilicity。 [来源](https://arxiv.org/pdf/2106.09553v3)

## 4. 最后结果怎么样

所读v3中，MoLFormer-XL在BBBP、ClinTox、SIDER的AUROC分别为93.7%、94.8%、69.0%；ESOL、FreeSolv、Lipophilicity的RMSE分别为0.2787、0.2308、0.5289，误差单位依各端点。分类采用骨架划分，回归采用随机划分，不能合并为一个准确率。 [来源](https://arxiv.org/pdf/2106.09553v3)

## 5. 贡献是什么（阅读归纳）

展示了大规模SMILES预训练的迁移价值，并用高效注意力降低训练成本；学习到的表示还包含与分子结构相关的信息。

## 6. 缺陷与局限是什么（阅读判断）

所读表格中的部分基线成绩引用既有文献，训练规模也不同；结果不能单独证明架构优越性。小分子基准成绩尚不能证明多肽或肠屏障端点效果。当前数值来自v3，未等同于正式版逐表核验。

证据位置：arXiv v3：Methods；PDF第10—11页Table 1/2及表注；第21—22页补充数据与划分说明。 数值为作者报告；贡献和局限为阅读归纳。

[返回逐篇索引](README.md) · [下一篇 P01 →](P01_Representation_limits_comment.md)
