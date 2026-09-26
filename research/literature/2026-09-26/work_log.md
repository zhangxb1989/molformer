# 检索与工作日志

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
