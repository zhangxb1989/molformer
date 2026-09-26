# 新窗口续接记录（2026-09-26）

用户要求：继续 MolFormer 与多酚/多肽活性预测的近三年文献研究，按候选库→逐篇分析→direct comparison/novelty gap/first 三阶段。用户已明确取消误带的分析字段；不要添加该维度。用户授权持续工作，周额度大于 5% 不用等指令，但本环境未提供额度查询。

## 先读

README.md、comparison_and_novelty.md、structured_review.md、sources.json、screening.md、work_log.md、pdf_manifest.json。文字分析已有完整草稿，28 条记录（27 近三年 + 1 基础），不要从零重查。

仓库：zhangxb1989/molformer。**只写 gpt，未经特别确认不能修改 main。** 本次开始时 main 为 3b9ac434db387fadf2cf99b99def654cbf193841；此前文字检查点为 3f5de612aefc942b10a064472d81eb9abf78dd0a。读取 gpt 当前 HEAD 作为新提交父节点，不写死旧 SHA。

## 尚需完成

1. 对完整文字草稿做一次质量检查，重点核对个别数值/方法出处、NR 标记和当前版本；源文 HTML 的数学式有时不完整，不猜 loss。
2. 将 pdf_manifest.json 中 pending_upload 的 7 个 PDF 归档；本检查点已加入 P01 评论原 PDF。其他 7 个已下载验证，详见 SHA-256/页数；本地存在时复用，失效时由 manifest 的官方下载链接重取。不要把文本检查点说成 PDF 全部完成。
3. 其他文章未取得可转载 PDF，已记录来源/403/非 PDF/许可情况，不绕过访问限制，不将网页打印件冒充原 PDF。P17 官方原 PDF 已下载用于阅读，但转载许可尚未确认，先保留链接。
4. P15 PeptideCLM-2 阅读的是预印本 v5；正式 DOI 已核实，最后方法差异仍需核对。P21 HELM-BERT 已更新到 2026 正式版，不要重新套用旧预印本的负采样计数矛盾。
5. 完成后验证 gpt 远端文件及 PDF 哈希，确认 main 未改变，再向用户汇报实际保存数量与剩余限制。不是要开展新的训练实验。

## 当前主要结论

已有 MolFormer 肽建模先例 P10/P16/P25，不能声称 first。P24（10.1002/jsfa.70701）用 83 种植物化学物预测 TEER/Papp/ER，属于最接近的端点邻近研究。原多酚课题更适合以数据与严格评估为贡献。不同活性端点不能横比数字或混合标签。

原稿件 128 与 109 化合物口径待统一；旧稿 122/6 类别计数不能套用新稿。六个外部候选均实验阳性，5/6 一致不能证明特异度。公开 MolFormer checkpoint 的约 1 亿与原论文 11 亿规模需对应真实权重。这些是稿件审计事项，并非本轮已核实的最终数据事实。

## 执行环境及保存注意

本地若仍在：/workspace/scratch/219f1d3ee01c/molformer/research/literature/2026-09-26/。
临时源文缓存：/workspace/scratch/219f1d3ee01c/source_cache/；包含官方 HTML/提取文本和已下载 PDF。不可把全文缓存一并复制到公开仓库。

命令行 git push 无认证，连接器 Git data API 可创建 blob/tree/commit 并 update_ref(gpt, force=false)。文本提交已经成功。不要反复要求用户重新授权写 gpt。

大 PDF 经工具读取时单次输出会在约 1 MiB 截断，必须按 393216 字节的原始文件块（3 的整数倍）逐块 base64 编码，检查输出长度后拼接，再 create_blob(encoding=base64)。不要把 base64 打印给用户。P01 blob 已存在：e28a113263054fc9c90527ef7454c1b7979cf74c。P14 的 2356968 字符 base64 曾准备完成，但提交调用被中断，不能视作已上传。

用户多次担心卡住：每分钟以内用简短中文同步实际进度；先形成可访问提交，再继续大文件。最终答复简短，附 GitHub 链接。
