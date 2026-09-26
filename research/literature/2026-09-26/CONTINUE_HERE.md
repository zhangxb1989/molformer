# 续接记录：THPep 历史划分与正式补充表核查

更新：2026-09-26。仓库 zhangxb1989/molformer，**只操作 gpt，不修改 main**。沿用28条文献，不恢复用户已取消的无关字段；未启动模型训练。

## 先读

README.md、thpep_protocol_audit.md、thpep_evidence.json、thpep_audit_results.json、code_audit.md、quality_check.md、comparison_and_novelty.md。提取见sources.json；主文与补充文件分别见pdf_manifest.json、supplement_manifest.json。不要从零重查。

## 本次已完成

1. 当前作者快照6b9708d4cb05717307d310daaf1c0f88c71ff084。找回历史prepare_benchmark_data.py：最后版本4740c70c3f5246c4be66cc54de11d7cb3a1c8b2a；删除提交ea5cbc59c27c739c8eeab305c074f128b29e6683。THPep两次按标签分层的20%随机留出，分别使用seed×45671、seed×52984。
2. 源表609行（class 0/1为433/176），重建训练389/验证98/测试122；三个seeds101/202/303×三种large模型MLM/Hybrid/MTR的9份测试导出，样本、标签和行序全部匹配。10个CSV输入blob均与固定提交一致。THPep函数没有实施cluster分组，不能凭manifest名称认定簇隔离；没有审计main90上游构建，也没有真实训练日志。
3. 正式SI来自ACS Figshare article32979761/file66601469，DOI10.1021/acs.jcim.6c00652.s001，v1，2026-07-14，9页，CC BY-NC4.0。直接核查S5/S6方法、S8指标；正式主文完整方法仍未取得。
4. 作者eval.ipynb同时存在测试标签择优阈值（0起算cell2）和固定logit0（cell4）路径。独立重算后，测试MCC择优阈值的18个均值/样本SD与正式S8三位小数全部一致；固定阈值MCC/F1不匹配。具体范围见专项报告。不要推断作者意图、所有其他实验、所有基线或完整训练流程；固定阈值结果是计算诊断，不是替代论文排名。
5. SI PDF提交e2a586368935b8a944f0c822d67b471e0743a8b9，已远端读回核验。累计16份论文主文/预印本+1份正式SI，共17个PDF、263页；文献记录仍28条，其余12条无主文PDF。
6. 新增专项报告、证据索引、重算结果和audit_scripts/verify_thpep_exports.py。仅执行自写核查，未执行作者代码、未训练模型、未修改作者仓库。结论已同步逐篇稿、比较稿、质量记录与sources.json。

## 保留的既有成果

- P12固定提交1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de：完整BCE、初始/对抗两次等系数反传、30模型等权概率平均；公开路径用test标签择阈值再计分。Accuracy是样本平均Jaccard。FGM源实现及论文表格对应快照仍缺。
- P15现有代码：25% span启动示例、0.6/0.4目标、分类BCE与专用回归MSE；token CE涵盖非padding原始token。固定文件和5折fallback必须区分。
- 先前16份论文PDF均已验证；P19当前官方字节不同于旧缓存，previous_download保留旧值，不恢复旧哈希。
- P14/P09历史指标表头及不同划分限制保留；P21使用正式版。P15预印本与正式SI不能混写成正式主文已读。

## 剩余工作与下一步

1. 优先处理12条未归档主文中可合法取得的官方原件/作者稿。先读manifest与access_audit；P08/P25此前只有TDM作者稿且云无PDF，P17转载许可未核实。不要重复同一已确认受限入口，不把网页打印件当论文原PDF。
2. P15正式主文与预印本完整对照、真实训练日志、main90上游处理仍缺。已找回历史脚本并核对测试导出，不再写“生成脚本未见”。扩展到其他任务/基线时，须另查相应预测和协议，不能外推THPep结论。
3. P12 FGM扰动实现、论文表格对应快照仍未核实。
4. 原项目128/109化合物口径、标签证据、六个全阳性外测和实际MolFormer checkpoint需要用户当前原始数据；当前仓库树未见这些数据，不能凭文献补造或宣称已解决。

## 当前研究结论

MolFormer肽任务已有P10/P16/P25等先例，不能声称first。P24植物化学物TEER/Papp/ER是邻近端点证据。原多酚任务更适合用可追溯数据、严格分组评估和相对指纹/描述符的实际增量支持贡献。阈值须在训练/验证内确定；不同端点、指标、划分和调参方式不可直接横比。

## 保存与后续操作

main基线3b9ac434db387fadf2cf99b99def654cbf193841。本轮起点gpt=f7a36a56cfd9dcb7dfe76ee57f71766f0ab46f82；提交前重新读取当前gpt HEAD，只通过GitHub连接器update_ref(gpt,force=false)。续接记录不预写未来提交号，以分支实际HEAD为准。

本地work/review/是研究缓存，work/round3/是本轮证据与输入；仅按主文/补充manifest和文本白名单提交。文本使用UTF-8/LF，避免换行转换导致blob不一致。独立复核脚本可下载固定提交的10个公开CSV并校验输入blob，命令见专项报告。不要提交完整作者源码、临时缓存或半截下载文件。
