# P15 THPep：历史划分与正式补充表 S8 的证据核查

核查日期：2026-09-26。范围仅为 PeptideCLM-2 的 THPep 公开预测，3 种 large 模型（MLM、Hybrid、MTR）× 3 个 seeds（101、202、303）。本次独立重建划分、重算已发布预测；未训练模型，也未执行作者训练脚本或 notebook。

**结论：9 份测试集的样本、标签及行序均与历史脚本的分层随机留出完全一致；正式补充表 S8 的 MCC、F1、AUROC 均值及标准差共 18 个数值，与使用测试标签选择最大 MCC 阈值的计算结果一致到表中三位小数。** 固定 logit 阈值 0 的 MCC、F1 与该表不同。因此不能把表 S8 的这些阈值相关指标直接作为完全独立的测试估计，也不能将这组结果概括为统一的 3×5 折或已证实的按簇隔离评估。

## 1. 正式补充材料已取得

由 [ACS Figshare 官方条目](https://acs.figshare.com/articles/journal_contribution/Scaling_SMILES-Based_Chemical_Language_Models_for_Therapeutic_Peptide_Engineering/32979761) 取得正式补充文件，DOI `10.1021/acs.jcim.6c00652.s001`，version 1，发布日期 2026-07-14。文件共 9 页，原样归档为 [P15 正式补充 PDF](pdfs/P15_2026_PeptideCLM2_final_supporting.pdf)。[官方元数据](https://api.figshare.com/v2/articles/32979761) 给出 CC BY-NC 4.0；下载 MD5 与官方记录一致，GitHub 读回 SHA-256/大小/Git blob SHA 也一致，详见 [补充文件清单](supplement_manifest.json)。

- Table S5（p. S5）：分类任务优先使用固定划分，否则使用 5 折；分类 LoRA rank 16，最多 10 epochs，patience 5。CycPeptMPDB 回归使用 MSE、外层留出和内层集成。
- Table S6（p. S6）：回归 MSE、学习率 3e-4、batch 16、内折 checkpoints 均值集成，3 次重复。
- Table S8（p. S7）：THPep 三个随机 seeds 的 mean±SD；本次逐项核对三种 PeptideCLM-2 的 MCC、AUROC、F1。

这使部分正式方法与指标得到直接核对。正式论文主文仍受访问限制；不能据此声称已完成正式主文与预印本 v5 的全部方法对照。原预印本和正式补充材料是不同文件，许可分别记录。

## 2. 找回被删除的划分脚本

当前作者快照为 `6b9708d4cb05717307d310daaf1c0f88c71ff084`。其中已没有划分准备脚本，但历史中最后可读版本位于 [4740c70… 的 prepare_benchmark_data.py L20–44](https://github.com/AaronFeller/PeptideCLM-2/blob/4740c70c3f5246c4be66cc54de11d7cb3a1c8b2a/training/prepare_benchmark_data.py#L20)，随后被 [ea5cbc5…](https://github.com/AaronFeller/PeptideCLM-2/commit/ea5cbc59c27c739c8eeab305c074f128b29e6683) 删除。

THPep 函数读取 `THPep_main90_smiles_classes.csv`，先按 class 分层留出 20% 测试集，random_state=seed×45671；再在剩余数据内按 class 分层留出 20% 验证集，random_state=seed×52984。名义比例为训练/验证/测试 64/16/20，609 行实际得到 389/98/122 行。该函数没有读取 cluster 标识或执行序列分组，也没有产生五个互补测试折。

源表 class 0/1 分别为 433/176；每次测试集为 87/35。源表 609 个 SMILES 字符串均不同，这只是精确字符串检查，不等同于分子规范化、序列同源性或上游 `main90` 构建规则的审计。

我们按 scikit-learn 1.7.2 的公开分层随机划分算法，独立用 NumPy 重建样本分配与排列。10 个输入 CSV 均先校验固定提交的 Git blob。三个 seeds 下，三种模型的全部 9 份公开测试导出均逐行匹配重建结果。源表在历史与当前提交的 blob 相同。

这直接支持这些公开测试导出与历史随机留出路径相符；训练/验证的 389/98 是按脚本重建的数量，尚无完整训练日志证明当时每一步训练都采用了相同配置。不能仅根据当前 manifest 中的 `cluster_aware_single_table` 名称认定按簇隔离，也不能由本次核查断言已经发现某一对具体泄漏样本。

## 3. 阈值计算与 Table S8 对上

作者当前 [eval.ipynb](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/figure_generation/results/runs_LoRA_highrank/eval.ipynb) 同时存在两条路径：按 notebook JSON 从 0 起计数，cell 2 遍历测试预测的唯一 logit 值，用测试标签选择 MCC 最大的阈值，再计算同一测试集的指标；cell 4 使用固定 logit 阈值 0，旧优化循环被注释。不能只凭存在其中一个单元就认定实际运行顺序。

因此本次独立重算两种路径：`score >= threshold`，候选按唯一 logit 升序，排除预测仅有一类的候选，MCC 并列时取第一个。固定阈值 0 等价于 sigmoid 概率阈值 0.5。分数汇总采用三个 seeds 的均值与样本标准差（ddof=1）。

| 模型 | 正式 S8 MCC；测试择优阈值重算相同 | 固定 logit 0 重算 MCC | 正式 S8 F1；择优重算相同 | 正式 S8 AUROC；两路径均相同 |
|---|---:|---:|---:|---:|
| MLM | 0.756 ± 0.019 | 0.693 ± 0.062 | 0.826 ± 0.012 | 0.949 ± 0.006 |
| Hybrid | 0.747 ± 0.036 | 0.667 ± 0.066 | 0.818 ± 0.022 | 0.940 ± 0.019 |
| MTR | 0.698 ± 0.036 | 0.623 ± 0.047 | 0.784 ± 0.029 | 0.924 ± 0.016 |

三种模型×三个指标×均值/标准差共 18 个值均匹配正式表的三位小数。每次运行的阈值、混淆矩阵、完整精度分数及两种 SD 计算保存在 [重算结果](thpep_audit_results.json)。MCC/F1 匹配测试择优路径、固定阈值路径不匹配，结合 notebook 中相同逻辑，形成对表 S8 计算口径的具体证据；这仍不是完整运行日志或端到端训练复现。

AUROC 基于连续分数排序，不受这里的单个分类阈值改变影响；这并不自动证明其余训练/选择步骤完全独立。固定阈值分数仅用于诊断计算口径，不作为论文的“修正成绩”，也不能据此替作者比较所有基线。本次未重算 RDKit、Morgan、ChemBERTa 或 CheMeleon，未审计其他任务的全部结果。

## 4. 对本研究的影响

P15 仍可作为肽 SMILES 预训练、LoRA 与性质预测的方法先例。引用 THPep 表 S8 时必须附带阈值选择和具体划分限制，不能据此直接证明优于本项目或传统基线。本项目应在训练/验证内锁定阈值，并在统一数据、划分与预算下比较；测试标签仅用于最终计分。

## 5. 可复核材料与执行方法

[证据索引](thpep_evidence.json) 保存历史脚本、删除提交、当前 notebook、源表及 9 份预测的固定链接和 Git blob。独立核查脚本为 [verify_thpep_exports.py](audit_scripts/verify_thpep_exports.py)，仅依赖 NumPy/pandas；本次环境版本为 2.3.5/3.0.1。未推定作者实际安装的 scikit-learn 版本；采用 1.7.2 算法的依据及实现位置另列于证据索引。

在本研究目录运行以下命令可重新取得固定提交的 10 个公开 CSV 并核查，结果写到指定目录；已经备好字节相同的输入文件时可去掉 `--download`：

```text
python audit_scripts/verify_thpep_exports.py --input-dir work/thpep_inputs --output work/thpep_audit_results.json --download
```

校验包括输入 blob、9 份测试集行序、18 个正式表数值，以及完全正确、完全反向、分数相等和部分正确等手算指标案例。文献记录仍为 28 条，补充材料不另算一篇论文。
