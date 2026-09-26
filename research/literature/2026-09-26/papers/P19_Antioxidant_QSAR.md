# P19｜抗氧化QSAR：预测小分子DPPH强度

QSAR Models for Predicting the Antioxidant Potential of Chemical Substances

Sofia Ghironi、Edoardo Luca Viganò、Gianluca Selvestrel 等；2025；Journal of Xenobiotics。

[论文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC12194667/) · [已归档PDF](../pdfs/P19_2025_Antioxidant_QSAR.pdf)

**阅读范围：正文关键部分。** 更新：2026-09-26。

## 1. 做了什么研究

预测小分子抗氧化强度的连续数值，而不只是活性/无活性标签；围绕DPPH实验整理数据并比较回归模型。

## 2. 用了什么模型

从规范SMILES计算Mordred描述符，使用F-test、互信息筛选特征，比较11种回归器；以ExtraTrees、Gradient Boosting、XGBoost等构成集成。

## 3. 用了什么数据集

AODB清理后1,911种独立化合物，采用30分钟DPPH测量并转为pIC50；按InChI去重和过滤冲突。随机80%/20%训练测试，训练内10折。

## 4. 最后结果怎么样

测试集集成R²约0.78；最佳单模型ExtraTrees的R²约0.77、RMSE约0.45。集成改善幅度有限，说明经过整理的数据和传统描述符已有较强预测能力。 [依据：论文原文](../pdfs/P19_2025_Antioxidant_QSAR.pdf)

## 5. 贡献是什么（阅读归纳）

构建测量条件相对统一的小分子抗氧化回归资料，并给出传统机器学习基线与连续活性预测流程。

## 6. 缺陷与局限是什么（阅读判断）

所谓external测试来自同一数据池的随机留出，不是前瞻性新来源验证。结构相近化合物及特征选择步骤可能影响结果；DPPH终点也不能直接代表肠屏障功能。

证据位置：既有逐篇提取中的相应方法、数据与结果；仅部分阅读者以摘要为限。数值为论文报告；贡献与局限为阅读归纳。

[← 上一篇 P18](P18_Phenols_CDFT.md) · [返回逐篇索引](README.md) · [下一篇 P20 →](P20_Barrier_metabolomics.md)
