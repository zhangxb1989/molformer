# 续接质量检查与剩余限制

日期：2026-09-26。沿用 28 条记录（27 条近三年、1 条基础），未扩充候选库；本次完成全库结构、版本/阅读状态、NR 与引用一致性检查，并对影响结论的数字和方法进行原始来源抽查。**不把这次检查描述成 28 篇全文重读或代码复现。**

## 已处理

| 对象 | 核查结果及处理 | 可追溯来源 |
|---|---|---|
| 全部 28 条 | 清理题名/期刊的 HTML 标签、实体与换行；同步 JSON、分析稿、BibTeX；部分阅读项不再使用含糊的 full text 版本标签 | sources.json、structured_review.md、references.bib |
| P02 | 86.051%、70.018%、88.365% 及随机 81/9/10 均按对应任务理解；原文明确同序列可有重复测量/冲突标签，保留泄漏限制 | [原文 Methods/Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC10683064/) |
| P05 | PDF p.3–4 的 AMP F1/MCC 与报告相符；p.10/11 的数据名对调问题仍保留；不根据 softmax 猜 loss | [官方原 PDF](pdfs/P05_2024_PepNet.pdf) |
| P08 | Full 23M 一行的 AUROC/AUPRC/RMSE 对应无误；23M 是预训练分子数，44M 是参数数 | [原文 Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC11971985/) |
| P09 | nc-CPP/nc-Binding 的 0.628/0.768 属 Spearman；c-CPP/c-Sol 属 AUC | [原论文 Table 1](https://academic.oup.com/view-large/527864395) |
| P10 | p.3 数据规模与 p.4 HPO 核对；200 steps 有提前停止，应记为最多 200；保留 5 折与 5 seeds | [官方原 PDF](pdfs/P10_2025_Peptide_generalization.pdf) |
| P12 | p.14–15 单功能/双功能计数是独立序列口径；p.5 主表指标与 p.19 结论有对调；人工看 p.19 式 (10)–(11) 后确认不是 HTML 提取丢项 | [官方原 PDF](pdfs/P12_2025_MFP_MFL.pdf) |
| P13 | p.11 sigmoid 与 >0.5 阈值、p.12 式 (17) MSE 已核查；另有 L2 正则 | [官方原 PDF](pdfs/P13_2025_BPFun.pdf) |
| P14 | 7,475 条非典型肽通透数据拆记为 PAMPA 6,869、Caco-2 606；半衰期 130/245。另发现历史分数指标表头不一致，详见下段 | [官方原 PDF](pdfs/P14_2026_PeptiVerse.pdf) p.5、7–8 |
| P15 | 正式在线日期 2026-07-13/卷期日期 2026-07-27 已核验；方法仍限 2026-06-23 bioRxiv v5，不能宣称已完成正式版对照 | [正式元数据](https://pubmed.ncbi.nlm.nih.gov/42443143/)、[所读预印本](https://pmc.ncbi.nlm.nih.gov/articles/PMC12803269/) |
| P19 | 官方原件的题名、DOI、作者、许可、13 页及关键结果已核查；测试 R² 约 0.78/单模型约 0.77，与报告相符。当前 PDF 字节不同于旧记录，保留两份哈希信息 | [本次官方原件](pdfs/P19_2025_Antioxidant_QSAR.pdf)、pdf_manifest.json |
| P21 | 正式版预训练 39,079、通透性 7,715；PPI 随机配对分组 20,057、蛋白簇分组 20,055；1:4 阴性采样与 BCE 阳性权重 4 再次核验 | [正式版 ACS Methods](https://pubs.acs.org/doi/10.1021/acs.jcim.6c00451)、[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417886/) |
| P23 | PDF 中的 62,820 是模型实例数量，不是分子数 | [官方原 PDF](pdfs/P23_2023_Systematic_molecular_benchmark.pdf) p.1、4 |
| P24 | 83 个独立植物化学物、三重复共 249 测量样本、5,003 描述符再次核验；不把重复测量当独立化合物 | [Wiley 方法与结果](https://scijournals.onlinelibrary.wiley.com/doi/full/10.1002/jsfa.70701) |

F01、P01、P03、P04、P06、P07、P11、P16、P17、P18、P20、P22、P25、P26、P27 的详细方法主要沿用前一检查点；本批次检查其字段、NR、版本与比较角色，没有宣称逐一重新获取全文。P01 原件另已校验；F01 权重规模仍须依据用户实际使用的 checkpoint，而非替用户认定。

### P14 与 P09 的比较限制

PeptiVerse 正式 PDF p.5 Table 1 将 PepLand c-CPP/c-Sol 的 0.838/0.662 放在 “Classification (Best F1)” 表头下。[PepLand 原 Table 1](https://academic.oup.com/view-large/527864395) 将这两项标为 AUC，且 PeptiVerse 自己的表注明确历史研究与本研究划分不同。这里记录的是**原表之间可观察到的指标名称和协议不一致**；没有替作者重算，也不据此判断任何模型实际更差。已同步到逐篇分析和直接比较报告。

### P15 版本核查结果

正式 DOI/作者/日期可由 ACS 和 PubMed 确认；本次 ACS 正式全文抓取返回 403，尚未取得可核对完整 Methods 的正式版本。预印本 v5 的微调节写 THPep 随机 5 折与三种 seeds，基线节又写 triplicate random splits；本轮代码核查已补齐 loss 与条件划分入口，但 prepared_data 的生成及与预印本/正式版结果对应仍未证实，详见 code_audit.md。预印本许可只对应该预印本，不能据此转载正式排版 PDF。**正式版方法差异核对仍未完成，不能标成已解决。**

## PDF 实际交付与校验

上一归档批次补齐原定 7 份待上传文件，加上已有 P01，共归档 **8 份 PDF**。其中 P01/P05/P10/P12/P13/P14/P23 与旧记录 SHA-256 相同；P19 重新从 MDPI 官方文件服务器取得不同字节原件，已单列旧值、当前值与来源。未修改论文 PDF。

全部 8 份已从提交 `ac3d399aadf06ce7a74e2810204ee47ee9f528c4` 的原始文件 URL 重新读回，校验 SHA-256、Git blob SHA 与文件大小，全部相符。详见 [archive_verification.json](archive_verification.json)。本地首页已渲染核对，涉及公式/比较表的关键页另行视觉检查。

## 保留限制

- 当前其余 12 条没有归档 PDF，来源与访问/许可限制见 [pdf_manifest.json](pdf_manifest.json)。P17 保留官方链接，转载许可仍未核实。
- NR 指本轮证据不足，不等于论文没有报告。尤其摘要/部分阅读项、P12 FGM 的具体实现、P15 正式版方法及 THPep 划分生成，仍不能补猜。
- 三年窗口不支持全历史 first 认证；原稿 128/109、阳阴计数、六个全阳性外测和实际 checkpoint 均属于另需原始数据的稿件审计，不是本轮已核实的训练事实。
- 本轮没有启动模型训练，也没有产生新的性能结果。所有外部性能数值保留作者、任务、版本和比较限制。

## 作者代码续查

P12 已确认完整 BCE、两次等系数反传、30 模型概率等权平均，并识别测试标签参与阈值选择。P15 已核实启动示例的 25% 掩码及 0.6/0.4 权重、分类 BCE 与专用回归 MSE；THPep 的现成文件入口和 5 折 fallback 必须区分。代码版本不能自动代替正式论文方法，详细证据及未闭合项见 [code_audit.md](code_audit.md) 和 [code_evidence.json](code_evidence.json)。

## 官方云服务补充归档

本轮新增 8 份原 PDF（P02、P04、P09、P11、P15、P16、P21、P24），累计 16 份、254 页。使用 NCBI 新版官方 Cloud Service，按每个版本的元数据核实 DOI、许可与 PDF MD5；检查 PDF 文件头、页数、题名首页和许可文本，并从提交 f4bbf7471ec32a629f7b231902288b34de73fce5 重新下载新增文件核验 SHA-256/字节数/Git blob SHA。P15 首页确认 June 23, 2026 和 CC BY 4.0，归档的是预印本 v5，正式版方法限制未解除。

P08/P25 云服务仅列 TDM 作者稿、无 PDF，未把文本挖掘权限扩展成原件转载许可。其他未取得完整文件者继续保留具体访问原因；不上传部分下载文件。完整访问结果见 [access_audit.json](access_audit.json)。这批新增 PDF 主要是为已有研究补充原件留存，不宣称本轮重新逐页精读全部新增论文。
