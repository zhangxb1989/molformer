# P25｜TIDE：双编码器融合TCR与肽信息

Modeling TCR-pMHC Binding with Dual Encoders and Cross-Attention Fusion

Wenbo Wang、Cong Qi、Zhi Wei；2025会议／2026在线；2025 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC13159490/) · [作者机构收录的论文摘要](https://researchwith.njit.edu/en/publications/modeling-tcr-pmhc-binding-with-dual-encoders-and-cross-attention-/)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

用蛋白和分子两侧信息预测TCR与肽的结合，关注数据不足及未见肽情境。虽然题目提到pMHC，现有模型记录不包含MHC的直接输入。

## 2. 用了什么模型

TIDE采用ESM编码TCR序列，MoLFormer编码肽SMILES，以交叉注意力融合，再输出结合概率；训练结合分类目标与表示对齐。

## 3. 用了什么数据集

使用TCHard基准，涉及参考/随机阴性以及未见肽测试；配对记录不能当作独立肽数量。会议为BIBM 2025，在线元数据日期为2026-01-29。

## 4. 最后结果怎么样

作者机构保存的摘要报告，在TCHard的未见肽及少样本设置下，TIDE相对ChemBERTa、TITAN、NetTCR等基线取得更好的预测表现和稳健性。具体各组AUROC尚未逐表整理，因此保留作者定性结论，不补写提升幅度。 [依据：作者机构收录的论文摘要](https://researchwith.njit.edu/en/publications/modeling-tcr-pmhc-binding-with-dual-encoders-and-cross-attention-/)

## 5. 贡献是什么（阅读归纳）

将蛋白序列和肽化学表示结合，通过跨注意力与对齐学习组织配对信息，为受体—肽识别提供另一种融合方案。

## 6. 缺陷与局限是什么（阅读判断）

与LANTERN存在作者、数据及架构重合，不能当作两个独立数据来源的重复验证；未显式输入MHC也限制了对完整TCR—pMHC机制的解释。当前笔记仍缺逐表结果摘要。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P24](P24_Phytochemical_QSPR.md) · [返回逐篇索引](README.md) · [下一篇 P26 →](P26_NPCLM.md)
