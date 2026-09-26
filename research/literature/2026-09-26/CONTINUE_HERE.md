# 续接记录：作者代码核查与官方原件补档

更新：2026-09-26。仓库 zhangxb1989/molformer，**只操作 gpt，不修改 main**。沿用 28 条文献，用户已取消的无关字段不重新添加；未启动模型训练。

## 先读

README.md、code_audit.md、quality_check.md、comparison_and_novelty.md、sources.json、pdf_manifest.json、access_audit.json。不要从零重查。

## 本次已完成

1. P12 作者代码固定提交 1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de：确认完整 BCE、初始/对抗两次等系数反传、30 模型等权概率平均；发现用 test 标签选阈值并在同批 test 计分。Accuracy 是样本平均 Jaccard。只能对可见代码路径作判断，未证明论文表格由此提交生成；FGM 源实现仍缺。
2. P15 固定代码提交 6b9708d4cb05717307d310daaf1c0f88c71ff084：确认启动示例 25% span 掩码、0.6/0.4 目标、分类 BCE/专用回归 MSE；token CE 包含非 padding 原始 token。现成划分文件与 5 折 fallback 是不同路径，不能将所有结果写成统一 3×5 折。
3. code_audit.md/code_evidence.json 已提交于 ae7654274e664c64d7c7ab77075e290f9d5c6fc2。全部为静态阅读，未执行作者代码、未改作者仓库。
4. NCBI 旧 OA Web Service 已停止；新版官方入口 https://pmc.ncbi.nlm.nih.gov/tools/pmcaws/。本轮核查现有 10 条的版本元数据，新增 8 份原 PDF：P02、P04、P09、P11、P15、P16、P21、P24。PDF 提交 f4bbf7471ec32a629f7b231902288b34de73fce5，全部新增文件已从 GitHub 读回核验。累计 16 份原件，其余 12 条链接保留。
5. 先前 8 份原 PDF 的校验仍有效；P19 当前文件与旧缓存不同，previous_download 保留旧值，不恢复旧哈希。
6. P14/P09 的历史 AUC/F1 表头不一致、不同划分限制继续保留；P21 沿用正式版，不恢复旧预印本计数矛盾。

## 仍未解决的证据限制

- P15 正式版元数据确定（2026-07-13 在线，10.1021/acs.jcim.6c00652），正式全文方法仍受访问限制；归档 PDF 是 June 23, 2026 bioRxiv v5。正式版与预印本一致性未验证。
- P15 THPep 的 prepared_data 划分文件/生成脚本未见，manifest 的 cluster-aware 声明和随机划分文字仍不能闭合。P12 FGM 的扰动实现及论文表格对应快照未核实。
- 未归档原文逐条见 manifest/access_audit。P08/P25 是 TDM 作者稿且云服务无 PDF；P17 转载许可未核实。本轮八份原件的传输问题均已解决，其余文献仍按各自访问与许可状态处理。
- 原项目 128/109 化合物口径、标签证据、六个全阳性外测和实际 MolFormer checkpoint 需要原始数据核查；不能冒充已解决，也不能凭文献分析产生训练成绩。

## 当前研究结论

MolFormer 肽任务已有 P10/P16/P25 等先例，不能声称 first。P24 的 83 种植物化学物 TEER/Papp/ER 是最邻近端点证据。原多酚任务更适合用可追溯数据、严格分组评估和相对指纹/描述符的实际增量支持贡献。测试数据不能用于选阈值。不同端点、指标和划分不可直接横比。

## 保存与后续操作

main 基线为 3b9ac434db387fadf2cf99b99def654cbf193841。提交前读取当前 gpt HEAD，不写死旧 SHA；只通过 GitHub 连接器 update_ref(gpt, force=false)。本地 work/review/ 是工作缓存，work/source_code/ 是所读作者代码缓存，work/pmc_access/ 含完整与未完整下载；只按 manifest 的已核实路径提交。

后续优先解决需要新证据的正式版/划分问题或用户原始数据审计；不要反复把访问限制当成已完成。继续用简短中文报告实际进度。
