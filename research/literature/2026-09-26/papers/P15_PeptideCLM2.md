# P15｜PeptideCLM-2：扩展肽化学语言模型

Scaling SMILES-Based Chemical Language Models for Therapeutic Peptide Engineering

Aaron L. Feller、Maxim Secor、Sebastian Swanson 等；2026；Journal of Chemical Information and Modeling。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12803269/) · [已归档PDF](../pdfs/P15_2026_PeptideCLM2_preprint_v5.pdf) · [正式补充材料S8](../pdfs/P15_2026_PeptideCLM2_final_supporting.pdf#page=7)

**阅读范围：预印本＋正式补充材料。** 更新：2026-09-26。 所读主文为2026-06-23预印本v5；正式补充材料另读，正式主文未完整取得。

## 1. 做了什么研究

扩展肽化学语言模型的规模与预训练目标，比较遮盖语言学习、分子描述符预测及两者混合，评价对治疗肽性质的迁移效果。

## 2. 用了什么模型

PeptideCLM-2包含约3,200万—3.37亿参数的不同规模；以SMILES为输入，分类使用LoRA与预测头，通透性回归使用多模型集成。

## 3. 用了什么数据集

预训练包含逾亿小分子及肽；下游包括CycPeptMPDB、THPep、CellPPD、AmpHGT、PepMSND。公开THPep表为609条，阴/阳性433/176；其他任务不能套用这个规模。

## 4. 最后结果怎么样

正式补充表S8的THPep结果：MLM的MCC/AUROC/F1为0.756/0.949/0.826；Hybrid为0.747/0.940/0.818；MTR为0.698/0.924/0.784，均为三个随机种子的均值。这一任务上MLM较好，不代表混合目标在所有任务都更优。 [依据：正式补充材料S8](../pdfs/P15_2026_PeptideCLM2_final_supporting.pdf#page=7)

## 5. 贡献是什么（阅读归纳）

系统比较模型规模与预训练目标，拓展SMILES肽模型在多种治疗相关性质上的使用，并报告分类、回归等不同下游路径。

## 6. 缺陷与局限是什么（阅读判断）

THPep阈值相关成绩受测试标签参与选择的已知限制，不能直接作为完全独立测试估计；具体历史核查另存，不在本篇展开。阅读范围为预印本v5及正式补充S5/S6/S8，正式主文尚未完整取得。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P14](P14_PeptiVerse.md) · [返回逐篇索引](README.md) · [下一篇 P16 →](P16_LANTERN.md)
