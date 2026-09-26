# P24｜植物化学物：Papp、TEER与外排比预测

Molecular descriptor driven QSPR modeling of Papp, TEER and Efflux Ratio from Caco‐2 cells using machine learning for various phytochemicals

Jin‐Woo Kim、Rixing Cong、Jin‐Soo Park 等；2026；Journal of the Science of Food and Agriculture。

[论文入口](https://scijournals.onlinelibrary.wiley.com/doi/10.1002/jsfa.70701) · [已归档PDF](../pdfs/P24_2026_Phytochemical_Caco2_QSPR.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

从分子结构预测Caco-2实验中的表观通透系数Papp、跨上皮电阻TEER、外排比ER，探索植物化学物的结构与生物利用度相关指标的关系。

## 2. 用了什么模型

用PaDEL/alvaDesc计算描述符，经过特征筛选比较十类回归器；Stacking以CatBoost、LightGBM、Gradient Boosting为基础模型，线性回归为元模型，并用SHAP解释特征。

## 3. 用了什么数据集

83种独立植物化学物，三重复形成249行测量，初始5,003个描述符；采用重复5折×6。249行不能当作249种化合物，重复测量是否按化合物分组是重要限制。

## 4. 最后结果怎么样

原Table 2的Stacking测试R²：Papp 0.9550±0.0399；TEER 0.5435±0.4556；ER 0.9289±0.0602。对应NRMSE为0.0312、0.0781、0.0593（均值）。Papp和ER较好，TEER明显更不稳定。 [依据：论文原文](../pdfs/P24_2026_Phytochemical_Caco2_QSPR.pdf)

## 5. 贡献是什么（阅读归纳）

在同一批植物化学物上组织三个通透/屏障相关端点，并将结构描述符建模与特征解释结合，是与多酚肠屏障课题相邻的实验—建模研究。

## 6. 缺陷与局限是什么（阅读判断）

独立化合物仅83种，重复测量可能影响划分独立性；TEER标准差很大，不能用Papp的高分替代屏障表现。SHAP解释关联而非机制证明，三种端点也不等于紧密连接蛋白表达或屏障保护二分类。

证据位置：摘要、Methods、Table 2（PDF第8页）。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P23](P23_Systematic_molecular_benchmark.md) · [返回逐篇索引](README.md) · [下一篇 P25 →](P25_TIDE.md)
