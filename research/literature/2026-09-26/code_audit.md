# 作者代码核查：MFP-MFL 与 PeptideCLM-2

核查日期：2026-09-26。范围为作者公开代码的静态阅读及与所读论文的对照，未运行训练、未复现分数。所有链接固定到代码提交，避免默认分支更新后证据漂移。代码可确认“该快照实现了什么”，不能单独证明论文表格由该快照生成。

## P12 MFP-MFL

原文 Data Availability 指向 Zhou-Jianren/Multifunctional-peptide-classification，GitHub 当前解析到 zhouworks/Multifunctional-peptide-classification。本次固定提交 `1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de`。

| 核查点 | 可确认的实现 | 证据 |
|---|---|---|
| 完整二元交叉熵 | GAT 输出 logits，训练调用无显式 weight/pos_weight 的 BCEWithLogitsLoss；包括正、负类项，默认求平均。不能继续写“代码 loss NR” | [GAT.py L168–172](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/GAT.py#L168) |
| 初始与对抗目标 | 清零优化器梯度后，先对 loss 反传，attack 后对 loss_adv 反传，restore 后执行一次 step；在该训练入口两次反传未乘额外系数，即梯度累加系数均为 1 | [GAT_train.py L131–143](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/GAT_train.py#L131) |
| 推理集成 | 30 个模型的 sigmoid 概率求算术平均；此快照不是可学习的非均匀加权集成 | [predict.py L62–105](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/predict.py#L62) |
| 阈值选择 | 枚举 0.30 至 0.69，步长 0.01，按 Accuracy 最大值选择；比较符号为严格 >。实现的初始回退值是 0，如果所有候选得分均为 0，会保留 0 | [threshold.py L8–23](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/utils/threshold.py#L8) |
| Accuracy 含义 | 逐样本标签集合交并比的平均，即样本平均 Jaccard；不是一般二分类正确率 | [evaluation.py L72–94](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/utils/evaluation.py#L72) |
| 测试标签参与选择 | 配置加载 test 特征/标签，TestModel 将预测与真实标签传给 threshold，随后在同批数据上算分；30 模型推理入口重复相同逻辑 | [配置 L24–40](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/GAT_train.py#L24)、[评估 L188–202](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/GAT_train.py#L188)、[推理 L36–38](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/predict.py#L36)、[L103–105](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/predict.py#L103) |

**可比性判断：**公开快照的阈值选择使用了被评分的测试标签，构成测试集参与调参。这些阈值相关指标不应当作完全独立的测试估计。该判断针对可见代码路径；论文最终表格与此提交的一一对应尚未证实，不能推断作者其他实验也全部采用此路径。

原 PDF p.19 式 (10)–(11) 仅印出正类项的观察仍保留；现在可补记作者公开模型实际使用完整 BCE。训练脚本引用 `model.FGM`，但本次完整仓库树未见该源文件，因此 FGM 的具体扰动对象、幅度和实现仍未核实。训练优化器只选择名字包含 `gat` 的参数（[L103–109](https://github.com/zhouworks/Multifunctional-peptide-classification/blob/1f7b35ffa8b3d51a32a92a9753ddf642d1b5c9de/model_GAT/GAT_train.py#L103)），进一步说明不能把这次静态核查写成端到端复现。

对本项目的直接启示：阈值、类别权重、校准都应在训练/验证内部选定，测试标签仅用于最终评价；多标签 Jaccard 不与本项目的二分类 accuracy 横比。

## P15 PeptideCLM-2

固定作者仓库提交 `6b9708d4cb05717307d310daaf1c0f88c71ff084`（2026-07-23）。正式论文在线发表于 2026-07-13；本次取得的方法文本仍是 2026-06-23 bioRxiv v5。代码快照晚于正式在线日期，不能把它直接视为正式论文提交时的运行版本。

| 核查点 | 可确认的实现 | 证据 |
|---|---|---|
| 混合预训练目标 | token 交叉熵与描述符 MSE 的加权和，类构造默认 alpha=0.6、beta=0.4 | [MTR_model.py L205–234](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/00_pretraining/model/MTR_model.py#L205) |
| 25% 掩码及权重 | 提供的 sbatch 启动示例明确传入 alpha=0.6、beta=0.4、masking_percentage=0.25，并启用 span；基础命令行默认是 1/0、15%，不能把默认值误判成论文实验值 | [启动示例 L25–39](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/00_pretraining/run_pretraining.sbatch#L25)、[基础默认 L400–415](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/00_pretraining/pretraining.py#L400) |
| token loss 覆盖范围 | collate 复制完整原始 token 为 labels；掩码只改变输入；labels 仅 padding 置 -100，未将未掩码 token 全部忽略。结合平铺 labels 的交叉熵，可见代码对非 padding token（含特殊 token）计算重建目标，不能未经说明就写成“只在被掩码位置计算 loss” | [labels 与掩码 L190–268](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/00_pretraining/pretraining.py#L190)、[交叉熵 L230–234](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/00_pretraining/model/MTR_model.py#L230) |
| 下游分类 loss | 分类入口为 BCEWithLogitsLoss；LoRA r=16、alpha=32、dropout=0.1，作用于 qkv_proj | [分类模型 L125–147](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/02_classification_benchmarks_training_code/scripts/classification_finetuning_v2.py#L125) |
| 下游回归 loss | CycPeptMPDB 专用回归入口为 MSELoss。通用分类脚本的非分类分支是 SmoothL1Loss，不能用后者代替专用通透性实验的目标 | [回归 L334–350](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/01_regression_benchmarks_training_code/finetune_ensemble.py#L334)、[通用分支 L144–147](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/02_classification_benchmarks_training_code/scripts/classification_finetuning_v2.py#L144) |
| 划分入口 | 若有 train/val/test 文件，直接使用固定文件；否则才 fallback 到 shuffle=True 的 5 折 KFold，非 StratifiedKFold | [分类入口 L348–396](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/02_classification_benchmarks_training_code/scripts/classification_finetuning_v2.py#L348) |
| THPep 声明与实际文件 | manifest 声明 cluster_aware_single_table；adapter 实际读取按 seed 准备好的 train/val/test。命名本身不能证明真正按簇隔离 | [manifest L53–65](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/02_classification_benchmarks_training_code/experiment/benchmark_manifest.json#L53)、[adapter L161–174](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/training/02_classification_benchmarks_training_code/adapters/common.py#L161) |
| THPep 运行记录 | 仓库有 101/202/303 三个 seed 的结果目录；检查的 hybrid-large seed 101 metadata 指向 prepared_data，fold 为 null。该记录证明存在此运行配置，不足以证明全套结果是 3×5 折 | [seed 101 metadata](https://github.com/AaronFeller/PeptideCLM-2/blob/6b9708d4cb05717307d310daaf1c0f88c71ff084/figure_generation/results/runs_LoRA_highrank/thpep/peptideclm-2-hybrid-large/seed_101/run_metadata.json) |

**剩余缺口：**该仓库树未发现对应 `tmp/prepared_data/thpep/` 的划分文件或生成脚本；manifest 的 cluster-aware 声明、所读预印本“随机 5 折/三次随机划分”与实际结果之间仍不能闭合。公开 runner/metadata 中的 `training/classification_finetuning_v2.py` 路径也与当前树中的嵌套位置不同，不能宣称仓库可原样复现。没有运行代码，也没有因这些路径问题修改作者仓库。

正式 ACS 全文方法尚未取得；上述代码核查补齐部分 loss 和推理配置，不代替正式版与预印本的逐项对照。准确表述是“预印本方法 + 固定提交代码补充证据，正式版方法一致性未验证”。

## 证据留存

[code_evidence.json](code_evidence.json) 记录已读文件的固定提交、Git blob SHA 和 URL。未把作者完整源代码或运行环境复制进本仓库。

