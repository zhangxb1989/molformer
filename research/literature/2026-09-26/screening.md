# 阶段 1：候选文献库与筛选

窗口：2023-09-26—2026-09-26，按正式在线发表或预印本公开日期判断。共 28 条去重记录：27 条窗口内，1 条窗口外基础文献。该数字是保留条目数，不是数据库检索命中数。

纳入结构到性质/活性、多肽表征、相关阴性/泛化评估与邻近端点；纯生物机制、专利、二次转载与无关关键词命中不进入主分析。评论和生成模型明确作为背景。

| ID | 年份 | 文献 | 阅读状态 | 角色 |
|---|---|---|---|---|
| F01 | 2022 | [MoLFormer](https://www.nature.com/articles/s42256-022-00580-7) | abstract_or_partial | background |
| P01 | 2023 | [Representation_limits_comment](https://pmc.ncbi.nlm.nih.gov/articles/PMC10575963/) | full_text_key_sections | background |
| P02 | 2023 | [PeptideBERT](https://pmc.ncbi.nlm.nih.gov/articles/PMC10683064/) | full_text_key_sections | include |
| P03 | 2024 | [ActFound](https://www.nature.com/articles/s42256-024-00876-w) | abstract_or_partial | include |
| P04 | 2024 | [AutoPeptideML](https://pmc.ncbi.nlm.nih.gov/articles/PMC11438549/) | full_text_key_sections | include |
| P05 | 2024 | [PepNet](https://www.nature.com/articles/s42003-024-06911-1) | full_text_key_sections | include |
| P06 | 2024 | [DeepAIP](https://pubmed.ncbi.nlm.nih.gov/39357724/) | abstract_or_partial | include |
| P07 | 2024 | [Deep2Pep](https://www.sciencedirect.com/science/article/pii/S1476927124000094) | abstract_or_partial | include |
| P08 | 2025 | [PeptideCLM](https://pmc.ncbi.nlm.nih.gov/articles/PMC11971985/) | full_text_key_sections | include |
| P09 | 2025 | [PepLand](https://pmc.ncbi.nlm.nih.gov/articles/PMC12315545/) | full_text_key_sections | include |
| P10 | 2025 | [Peptide_generalization](https://pmc.ncbi.nlm.nih.gov/articles/PMC12751563/) | full_text_key_sections | include |
| P11 | 2025 | [AOP_DRL](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800373/) | full_text_key_sections | include |
| P12 | 2025 | [MFP_MFL](https://pmc.ncbi.nlm.nih.gov/articles/PMC11818429/) | full_text_key_sections | include |
| P13 | 2025 | [BPFun](https://link.springer.com/article/10.1186/s12859-025-06190-5) | full_text_key_sections | include |
| P14 | 2026 | [PeptiVerse](https://pmc.ncbi.nlm.nih.gov/articles/PMC13388690/) | full_text_key_sections | include |
| P15 | 2026 | [PeptideCLM2](https://pubs.acs.org/doi/10.1021/acs.jcim.6c00652) | preprint_full_text | include |
| P16 | 2026 | [LANTERN](https://pmc.ncbi.nlm.nih.gov/articles/PMC13045841/) | full_text_key_sections | include |
| P17 | 2026 | [PepBenchmark](https://proceedings.iclr.cc/paper_files/paper/2026/hash/56a225639da77e8f7c0409f6d5ba996b-Abstract-Conference.html) | full_text_key_sections | include |
| P18 | 2024 | [Phenols_CDFT](https://www.sciencedirect.com/science/article/abs/pii/S2210271X24003219) | abstract_or_partial | include |
| P19 | 2025 | [Antioxidant_QSAR](https://pmc.ncbi.nlm.nih.gov/articles/PMC12194667/) | full_text_key_sections | include |
| P20 | 2026 | [Barrier_metabolomics](https://pubmed.ncbi.nlm.nih.gov/41854110/) | abstract_or_partial | include |
| P21 | 2026 | [HELM_BERT](https://pmc.ncbi.nlm.nih.gov/articles/PMC13417886/) | full_text_key_sections | include |
| P22 | 2025 | [GP_MoLFormer](https://pubs.rsc.org/en/content/articlehtml/2025/dd/d5dd00122f) | abstract_or_partial | background |
| P23 | 2023 | [Systematic_molecular_benchmark](https://www.nature.com/articles/s41467-023-41948-6) | full_text_key_sections | include |
| P24 | 2026 | [Phytochemical_QSPR](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/jsfa.70701) | publisher_methods_and_partial_results | include |
| P25 | 2026 | [TIDE](https://pmc.ncbi.nlm.nih.gov/articles/PMC13159490/) | full_text_key_sections | include |
| P26 | 2026 | [NPCLM](https://arxiv.org/html/2602.13958v1) | full_text_key_sections | include |
| P27 | 2025 | [Food_foundation_models](https://www.sciencedirect.com/science/article/pii/S1466856425003315) | abstract_or_partial | include |

## 去重与版本规则

按 DOI、题名、作者和模型/数据关系归并；预印本、PMC 镜像、出版社版本不重复计数。

- P08 PeptideCLM：2024 预印本与 2025 正式版归并。
- P09 PepLand：2023 预印本与 2025 正式版归并。
- P14 PeptiVerse：早期预印本与 2026-07 正式版归并。
- P15 PeptideCLM-2：2026 正式版元数据已确认，实际详细阅读预印本 v5。
- P16 LANTERN：2025 预印本与 2026 PeerJ 版归并。
- P17 PepBenchmark：arXiv 与 ICLR 2026 proceedings 归并，会议状态已核验。
- P21 HELM-BERT：2025 预印本与 2026 正式版归并，分析更新到正式正文。
- P22 GP-MoLFormer：2024 预印本与 2025 正式发表归并。
- P25 TIDE：BIBM 2025 卷/会议，在线日期 2026-01-29，单列日期说明。与 LANTERN 有作者/任务重合，保留不同出版条目但不视作两组独立数据证据。
- P26 NPCLM：仅确认 arXiv v1；未确认正式接收。

## 阅读与遗漏边界

全文关键部分已读不等于代码复现。abstract_or_partial 项对数据量、loss、阈值或划分明确用 NR，后续获取全文再补。P24 已读方法与部分结果；P15 所读版本必须继续与正式版对照。

后续若要保留 first，须扩展全时段、多数据库与引用链；三年窗口只能支持近期定位。模型名检索也可能漏掉未在标题/摘要使用 MolFormer 的工作。

## 续接复核说明

2026-09-26 完成记录一致性检查及关键证据抽查，未重新扩大候选库。P15 正式版元数据由 PubMed 42443143 再次核验，方法仍限预印本 v5；P21 继续使用正式版。详细纠正及未解决项见 [quality_check.md](quality_check.md)。
