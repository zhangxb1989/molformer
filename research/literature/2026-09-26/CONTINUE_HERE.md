# 续接记录：归档已补齐，方法访问限制保留

更新：2026-09-26。仓库 `zhangxb1989/molformer`，**只写 gpt，不修改 main**。本轮沿用 28 条文献记录，没有扩大候选库或启动训练。用户已取消此前误带入的无关分析字段，不要重新添加。

## 先读

README.md、quality_check.md、comparison_and_novelty.md、structured_review.md、sources.json、screening.md、pdf_manifest.json、archive_verification.json。不要从零重查。

## 已完成

1. 对 28 条记录做结构、版本/阅读状态、NR 与引用一致性检查；关键方法和数值的原始来源抽查范围写在 quality_check.md，不能说成全部全文重读或代码复现。
2. 原 pending_upload 的 7 份 PDF 已补齐，加 P01 共 8 份。PDF 归档提交为 `ac3d399aadf06ce7a74e2810204ee47ee9f528c4`，全部从 GitHub 读回并核验 SHA-256/字节数/Git blob SHA。
3. P19 当前官方原件与旧记录字节不同，manifest 保留 previous_download，当前字段对应实际归档原件。其余 7 份与旧哈希相同。不要把旧 P19 哈希覆盖回当前文件。
4. 清理题名/期刊中的 HTML 标签、实体及换行，同步 JSON、Markdown、BibTeX、PDF 清单和本地历史命名的 inventory。
5. P14 的 7,475 条通透数据补记 PAMPA 6,869/Caco-2 606。P14 Table 1 的历史分类指标与 P09 原表 AUC/F1 名称不一致，且划分不同；该表不可用于直接排名。
6. P12/P13 公式页人工核对：前者仍需代码核实完整 BCE 实现，后者主文确为 MSE。P21 继续采用 2026 正式版，不能恢复旧预印本的负采样计数矛盾。

## 仍有证据或访问限制

- P15 PeptideCLM-2 正式版元数据已再次确认（2026-07-13 在线，DOI 10.1021/acs.jcim.6c00652），所读方法仍为 bioRxiv v5（2026-06-23）。正式全文返回 403，方法差异核对**未完成**。预印本 THPep 划分措辞也需结合代码；不要宣称已与正式版一致。
- 其余 20 条 PDF 未归档，保留入口和原因；P17 转载许可未核实。未取得或许可不明的原件不补造、不用网页打印件替代。
- 未核实字段继续保留 NR；first 须全时段查新才可能进一步讨论。
- 原项目 128 与 109 的化合物口径、标签证据、六个全阳性外测、实际 checkpoint 仍需用户原始数据核查，不在本轮冒充已完成。

## 当前结论

MolFormer 肽任务已有 P10/P16/P25 等先例，不能声称 first；P24 的 83 种植物化学物 TEER/Papp/ER 是端点邻近研究。原多酚任务更适合用可追溯数据、严格分组评估和相对描述符/指纹的实际增量支持贡献。不同端点、数据划分和指标不可直接横比。

## 保存与分支

本轮开始 main 为 `3b9ac434db387fadf2cf99b99def654cbf193841`，PDF 归档后再次读取仍相同。后续提交须读取 gpt 当前 HEAD 作为父节点，不写死旧 SHA；使用 GitHub 连接器提交并 `update_ref(gpt, force=false)`。

本机工作缓存位于当前聊天的 `work/review/`，源文提取与渲染在 `work/`；这些只是本地工作缓存，不要把全文缓存整体上传。最终公开报告与 8 份许可允许的原 PDF 位于 GitHub 的 `research/literature/2026-09-26/`。

用户此前多次担心中断，继续工作时每分钟内用简短中文报告实际进度。不要把保留的访问限制说成全部解决。
