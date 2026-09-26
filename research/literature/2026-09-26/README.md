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

沿用 28 条记录。累计归档 **16 份原 PDF**，每份均已从 GitHub 读回核验 SHA-256；其余 12 条保留入口与具体原因。新增原件来自 NCBI 官方公开云服务，归档版本、许可和来源见 [PDF 清单](pdf_manifest.json) 与 [访问核查](access_audit.json)。P15 文件明确是 2026-06-23 预印本 v5，不能当作正式排版论文。

[作者代码核查](code_audit.md) 已补齐 P12/P15 的部分 loss、阈值及推理配置：P12 公开路径存在测试标签参与阈值选择；P15 THPep 的划分生成和正式版方法对应仍未验证。详见 [质量检查](quality_check.md)、[归档校验](archive_verification.json) 和 [续接记录](CONTINUE_HERE.md)。没有启动训练或产生新的模型成绩。
