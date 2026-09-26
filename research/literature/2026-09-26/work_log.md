# 检索与工作日志

## 当前进度（2026-09-26，按用户最新要求）

| 工作 | 当前状态 |
|---|---|
| 每篇独立六项速读分析 | 28/28份已建立，含总索引及前后篇跳转 |
| 原文阅读深度 | 8条摘要/部分内容；其余见各篇标注，P15/P26保留版本限制 |
| 作者代码核查 | 本轮不开展；已有历史文件保留 |
| 第三阶段详细比较与创新分析 | 用户要求留待以后；已有草稿保留 |
| PDF归档 | 维持17个文件、263页，本轮未新增 |

主阅读入口：[每篇文献独立分析](papers/README.md)。以下为按时间保留的历史记录，旧阶段安排已由本栏及最新续接记录更新。


日期：2026-09-26（Asia/Kuala_Lumpur）。按工作批次记录；未记录精确分钟，不伪造数据库命中总数。

1. 恢复项目背景、稿件版本和 GitHub 约定：仓库 zhangxb1989/molformer，仅写 gpt。
2. 采用 2023-09-26—2026-09-26 窗口；2022 MolFormer 作为基础。范围覆盖多酚、肽、小分子抗氧化和评估方法。
3. 按用户更正移除误带入的无关分析字段；提取任务、数据、表示、模型、loss、inference、metrics、划分。
4. 检索后用出版社、PubMed/PMC、arXiv、ICLR proceedings 和作者仓库核验；正式版与预印本归并，阅读版本单列。
5. 阅读方法、数据与结果；未核实字段标 NR；记录源文矛盾，避免自动补齐。
6. 补检增加 P24 植物化学物 QSPR、P25 TIDE、P26 天然产物 CLM、P27 食品基础模型；HELM-BERT 更新为 2026 正式版，不能沿用旧预印本的缺漏判断。
7. 获取 PDF，检查文件头、页数和 SHA-256；403、验证码 HTML、许可未核实分别记录；没有把网页打印件冒充原 PDF。
8. 命令行 Git 推送认证失败，转已连接 GitHub API。PDF 大块读取被截断，改为分块。调用被中断后先提交文本，再补 PDF。

## 查询记录

下表同时含实际精确检索和按已执行检索主题整理的关键词，不声称在 WoS/Scopus 完成系统检索。

| 类型 | 查询 | 目的 |
|---|---|---|
| 主题 | MolFormer peptide activity prediction；polyphenol machine learning intestinal barrier | 原任务与模型 |
| 模型名 | PeptideBERT、PeptideCLM、PepLand、PeptiVerse、PeptideCLM-2、HELM-BERT | 表示学习 |
| 活性模型名 | PepNet、DeepAIP、Deep2Pep、AOP-DRL、BPFun、MFP-MFL | 标签和推断 |
| 评估主题 | AutoPeptideML、peptide generalization、PepBenchmark、systematic molecular property prediction | 阴性、去重与外推 |
| 邻近主题 | phenols antioxidant QSAR；ActFound；intestinal barrier metabolomics | 任务边界 |
| 精确补检 | `"MolFormer" "polyphenol" "intestinal"` | 狭义先例 |
| 精确补检 | `"tight junction" "polyphenols" "machine learning"` | 发现 P24 |
| 精确补检 | `"MolFormer" "peptide" activity prediction` | 发现 P25–P27 |
| 精确核验 | `"HELM-BERT" "2026" "6c00451"`；`"Deep2Pep" "10.1016"` | 版本与 DOI |
| 精确复核 | `"MolFormer" "intestinal barrier" polyphenols` | 未获得精确匹配的新证据 |

使用两种网页检索渠道；无关返回不作为不存在先例的证明。没有付费数据库全量结果，没有全历史查新认证。本环境未提供每周额度百分比，不能声称已经核实余额大于 5%；按用户授权持续完成本轮。

## 本地桌面续接批次

9. 从上一聊天恢复被转写损坏的仓库名与日期路径，读取 gpt 检查点 b60a75c；开始时 main 为 3b9ac434db387fadf2cf99b99def654cbf193841。
10. 重新获取 8 份官方原 PDF，检查文件头、完整页数、SHA-256、Git blob SHA 与题名首页；人工检查 P12/P13 公式页和 P14 Table 1。7 份与旧缓存字节相同，P19 使用当前官方原件并保留旧哈希。
11. 先以 1bb8a56 保存 PeptiVerse，再以 ac3d399 补齐归档，总数 8。通过原始文件 URL 读回全部 8 份，SHA-256 与本地原件一致；记录于 archive_verification.json。
12. 对 28 条记录检查 ID、提取字段、DOI、版本/阅读状态、NR 和引用格式一致性；对关键数字、公式和主张回查原始论文，范围列在 quality_check.md。清理题名/期刊中的 HTML 标签、换行与重复转义。
13. P15 正式版元数据再次核验（2026-07-13 在线），ACS 全文返回 403，方法版本差异仍未解决；保留预印本 v5 限定及许可范围。P21 再次确认最终版 1:4 阴性采样与 BCE 权重 4。
14. 新发现 P14 Table 1 的历史分类指标名称与 P09 原表不一致，并补注两文划分不同；不据此进行模型排名。P14 通透性总数拆记 PAMPA/Caco-2，P10 HPO 标为最多 200 steps，P12 损失公式保留代码待核查状态。

本批次核验查询示例：`"10.1002/jsfa.70701" "249"`、`"PepLand" "0.628" "0.768"`、`"PeptideCLM-2" "THPep" "5-fold"`、`"HELM-BERT" "positive" "4" "20,057"`；来源限定原始出版社、PMC/PubMed 和官方文件。未下载或提交受限全文缓存，没有开展训练实验。

## 后续代码核查与公开云服务归档

15. 在 gpt 提交 ae7654274e664c64d7c7ab77075e290f9d5c6fc2 保存 P12/P15 固定作者代码证据，补齐 loss、阈值和推理细节；P12 测试阈值问题与 P15 协议未闭合均已记入比较限制。
16. 核对 NCBI 新公开云服务的 10 条既有记录，新增 8 份许可原 PDF（提交 f4bbf7471ec32a629f7b231902288b34de73fce5），累计 16 份；新增文件 MD5 与官方元数据一致，GitHub 读回 SHA-256/大小/Git blob SHA 一致。P15 明确为预印本 v5；P08/P25 保留 TDM/无 PDF 限制。其余未完成传输不算归档，访问结果保存于 access_audit.json。
17. 同步清单、署名、数量、版本和续接记录；没有运行模型或创建新的性能结果。

## THPep 历史协议与正式补充表核查

18. 续接起点 gpt=f7a36a56cfd9dcb7dfe76ee57f71766f0ab46f82。查作者仓库提交历史，找到被 ea5cbc5 删除的 prepare_benchmark_data.py，最后版本4740c70；核对历史与当前源表blob相同。
19. ACS 主文仍受限；通过官方 Figshare 搜索取得正式 SI v1，DOI 10.1021/acs.jcim.6c00652.s001，核对CC BY-NC许可、MD5、9页以及S5/S6/S8。原样归档于e2a586368935b8a944f0c822d67b471e0743a8b9，GitHub读回SHA-256/字节数/Git blob均相符。
20. 独立重建609行源表的分层随机留出；3 seeds×3变体的9份测试导出逐行匹配。重算固定logit0和测试MCC择优阈值，后者18个均值/样本SD与正式S8的三位小数全部一致。未执行作者notebook，未训练模型；实际训练日志、上游main90处理及其他任务/基线仍未核实。
21. 新增专项报告、证据索引、完整重算结果和独立复核脚本；同步逐篇分析、比较判断、引用、许可和续接记录。计数为28条文献、16份论文主文/预印本+1份正式SI=17个PDF、263页。其余12条缺主文PDF的状态不变。

## 每篇独立速读文档（用户调整工作重点）

22. 用户要求优先为每篇文献单独成文，集中记录研究、模型、数据、结果、贡献、缺陷；不用继续核查代码，第三阶段以后再处理。已据此调整首页及CONTINUE_HERE.md，历史记录不删除。
23. 新建papers/下28份文档和README索引，每篇包括论文来源、阅读范围与前后篇跳转。把作者报告的结果和阅读归纳的贡献/局限分开；摘要阅读与全文关键部分不混标。文档齐全不等于全部原文精读完成。
24. 依据现有PDF及官方/作者机构摘要补充结果：P03、P04、P06、P07、P10、P11、P13、P18、P21、P22、P24、P25、P26。P13为Table 7；P24为原PDF第8页Table 2，并渲染确认R²与NRMSE列。P07数据来源来自出版社可见段落，仍不猜独立样本数。
25. sources.json为每条新增paper_note_path和quick_read六项摘要，并同步structured_review.md的新事实；P24从方法/部分结果更新为正文关键部分。8条仍是摘要/部分阅读，P15正式主文和P26发表状态继续限定。
26. 检查28条ID与独立文档一一对应、六项齐备、所有本地链接和前后篇导航有效；核对关键结果数字及元数据同步。仅将本轮文档与导航/日志更新保存到gpt，main保持原状。未新增代码核查、模型训练或第三阶段分析。

下一步：继续按六项结构补充原论文阅读证据，优先补摘要/部分阅读项；暂不恢复技术核查或第三阶段。
