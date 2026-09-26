# MolFormer、多酚与多肽活性预测：近三年文献研究

截止：2026-09-26。窗口：2023-09-26—2026-09-26；2022 年 MolFormer 单列基础文献。原课题为多酚/代谢物肠屏障相关活性预测，多肽文献用于补充方法、数据和评估先例。

提取字段：任务、数据与标签、输入表示、模型与预训练、loss、inference、metrics、划分与泄漏控制。未核实字段标记 NR。

最重要的结论：

- 不能声称首次把 MolFormer 用于多肽：LANTERN、TIDE 和标准到修饰多肽泛化研究已有先例。
- 2026 年已有植物化学物 TEER、Papp、ER 的机器学习预测，宽泛的“首次预测肠屏障相关性质”也不成立。
- 本课题的贡献应由可追溯数据、明确标签、严格分组评估，以及相对指纹/描述符的实际增量支持。
- 多酚与多肽可共同提供方法参考；不同活性端点的标签和成绩不能直接合并比较。

文件导航：

- [阶段 1：候选与筛选](screening.md)
- [阶段 2：逐篇分析](structured_review.md)
- [阶段 3：直接比较与创新判断](comparison_and_novelty.md)
- [文献库 JSON](sources.json) · [BibTeX](references.bib)
- [作者代码核查](code_audit.md) · [固定代码证据](code_evidence.json)
- [工作日志](work_log.md) · [PDF 清单](pdf_manifest.json) · [PDF 原文](pdfs/)

本报告不宣称穷尽全部数据库。预印本和正式版按同一工作去重，实际阅读版本另记。PDF 仅归档已经获取、许可允许转载的原件，其余保留入口和原因。

## 本轮续接状态

沿用 **28 条文献**。归档 **16 份论文主文/预印本 + 1 份正式补充材料，共 17 个 PDF、263 页**，每份均已从 GitHub 读回核验；其余 12 条文献尚无主文 PDF。版本与许可见 [主文清单](pdf_manifest.json)、[补充材料清单](supplement_manifest.json) 和 [归档校验](archive_verification.json)。P15 主文文件是预印本 v5，新取得的文件是正式 SI，不能混写成已取得正式主文。

新增 [THPep 专项核查](thpep_protocol_audit.md)：找回历史划分脚本，全部 9 份公开测试集逐行匹配分层随机留出；正式 SI 表 S8 的三种模型分数与测试标签择优阈值的计算结果相符。已保存 [证据索引](thpep_evidence.json)、[逐次重算结果](thpep_audit_results.json) 和 [独立复核脚本](audit_scripts/verify_thpep_exports.py)。该结果限制阈值相关指标的可比性，不是新的模型训练成绩。

[作者代码核查](code_audit.md) 继续保留 P12 的测试阈值问题及 FGM 缺口。P15 正式主文和完整训练日志仍未取得。后续见 [质量检查](quality_check.md) 与 [续接记录](CONTINUE_HERE.md)。
