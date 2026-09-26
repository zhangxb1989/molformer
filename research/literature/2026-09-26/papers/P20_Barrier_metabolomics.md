# P20｜肠屏障功能障碍的代谢组预测

A Biologically Informed Machine Learning Pipeline Uncovers Metabolic Features of Intestinal Barrier Dysfunction

Ke-Xin Liu、Ze-Yuan Liang、Tong Li 等；2026；Analytical Chemistry。

[论文入口](https://pubmed.ncbi.nlm.nih.gov/41854110/) · [本次补读原文/材料](https://acs.figshare.com/articles/journal_contribution/A_Biologically_Informed_Machine_Learning_Pipeline_Uncovers_Metabolic_Features_of_Intestinal_Barrier_Dysfunction/31812620)

**阅读范围：正式摘要＋正式补充材料s001；主文仍未完整取得。** 更新：2026-09-26。

## 1. 做了什么研究

从代谢组特征预测连续肠屏障指数，并结合网络生物学与临床/体外验证筛选功能相关代谢物。

## 2. 用了什么模型

LASSO、XGBoost和随机森林用于集成特征筛选；最终五种回归器为线性回归、Bayesian Ridge、ElasticNet、PLS和SVR，辅以SHAP解释。

## 3. 用了什么数据集

小鼠实验S1报告七组、每组10只，最终清洗后建模数未确认；筛出10个功能相关代谢物。临床Table S7列健康/AP/IBD样本数：队列1为41/50/56，队列2为10/10/20；分别采血与采粪，用途不同，不当作同一回归测试集。 [来源](https://acs.figshare.com/articles/journal_contribution/A_Biologically_Informed_Machine_Learning_Pipeline_Uncovers_Metabolic_Features_of_Intestinal_Barrier_Dysfunction/31812620)

## 4. 最后结果怎么样

正式SI Table S6中，10特征方案测试R²/MAE分别为：ElasticNet 0.620/0.350、Bayesian Ridge 0.642/0.329、线性回归0.604/0.352、PLS 0.654/0.319、SVR 0.643/0.329。这是同一方案跨回归器的表现，不能写成临床诊断准确率。 [来源](https://acs.figshare.com/articles/journal_contribution/A_Biologically_Informed_Machine_Learning_Pipeline_Uncovers_Metabolic_Features_of_Intestinal_Barrier_Dysfunction/31812620)

## 5. 贡献是什么（阅读归纳）

把生物学知识用于筛选和解释代谢特征，并通过不同回归器、临床样本及体外转化实验检验候选线索。

## 6. 缺陷与局限是什么（阅读判断）

主文缺口仍影响对屏障指数定义、最终建模样本与训练/测试划分的判断；SI调参采用重复5折，但未据此确认所有预处理/筛选均在折内。临床组间存在BMI或年龄差异；代谢关联与体外转化不能单独证明体内保护因果。

证据位置：ACS正式SI（DOI 10.1021/acs.analchem.6c00178.s001）：S1/S4/S6；S24页Table S6、S25页Table S7。数值表已视觉确认。 数值为作者报告；贡献和局限为阅读归纳。

[← 上一篇 P19](P19_Antioxidant_QSAR.md) · [返回逐篇索引](README.md) · [下一篇 P21 →](P21_HELM_BERT.md)
