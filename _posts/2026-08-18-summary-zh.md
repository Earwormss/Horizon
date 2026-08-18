---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 37 条内容中筛选出 15 条重要资讯。

---

**科技新闻**
1. [Mojo 编程语言正式开源](#item-tech-news-1) ⭐️ 9.0/10
2. [Linux 7.3 提升显存溢出性能](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B 在人工智能分析指数中得分 52](#item-tech-news-3) ⭐️ 8.0/10
4. [Turbovec：Rust 实现 Google TurboQuant 向量搜索](#item-tech-news-4) ⭐️ 7.0/10
5. [用铁路网络作为平板扫描仪](#item-tech-news-5) ⭐️ 7.0/10
6. [用 20 美元工具修复变砖的 Framework 笔记本](#item-tech-news-6) ⭐️ 7.0/10
7. [数据中心使下风向街区气温升高约 0.8°C](#item-tech-news-7) ⭐️ 7.0/10
8. [在 264KB SRAM 上运行扩散模型](#item-tech-news-8) ⭐️ 7.0/10
9. [企业微信 5.0.10 开放 CLI 与 MCP，支持 AI Agent 接入办公模块](#item-tech-news-9) ⭐️ 7.0/10
10. [中国要求部分政府机构提前卸载定制版 Windows 10](#item-tech-news-10) ⭐️ 7.0/10
11. [OpenAI 与 CodeAI 合作推进青少年 AI 教育](#item-tech-news-11) ⭐️ 7.0/10
12. [国产 AI 芯片 2026 年将占中国市场近 90%，寒武纪与华为成最大赢家](#item-tech-news-12) ⭐️ 7.0/10

**财经新闻**
1. [债券市场压力挤压普通家庭，华尔街静待沃什表态](#item-finance-news-1) ⭐️ 7.0/10
2. [Kalshi 申请推出股指永续合约，进军传统交易所领域](#item-finance-news-2) ⭐️ 7.0/10
3. [美国“先买后付”贷款 2025 年达 1600 亿美元，覆盖水电房租等日常支出](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Mojo 编程语言正式开源](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Mojo 编程语言现已正式开源，其编译器与工具链在 Apache 2.0 许可下发布。这一举措兑现了自 2023 年 5 月以来的承诺，并紧随上周发布的 1.0 版本。Mojo 最初旨在成为 Python 的超集，但自 2025 年 8 月起，其发展方向已调整为独立语言，专注于简化 GPU 编程，语法受 Python 启发，但并非完全兼容现有 Python 代码。此次开源对 AI 和高性能计算领域的开发者具有重要意义。

rss · Simon Willison · 8月18日 21:39

**「背景」** Mojo 是一种面向 AI 和高性能计算领域的编程语言，由 Modular 公司开发。它最初被定位为 Python 的超集，旨在让现有 Python 代码能够直接运行，但后来这一目标有所调整。Mojo 的语法设计借鉴了 Python，同时引入了 Rust 的静态类型和借用检查等系统编程特性，并针对 GPU 编程进行了优化。此前，Mojo 一直作为专有软件提供，其标准库虽已开源，但编译器本身并未开放。

**「影响」** 开发者现在可以自由使用、修改和分发 Mojo 的编译器与工具链，这将促进 Mojo 生态系统的成长，并可能加速其在 AI 和高性能计算领域的采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo ( programming language ) - Wikipedia</a></li>
<li><a href="https://amitxshukla.github.io/Mojo/standard.html">The Standard Library — The Mojo Programming Language</a></li>

</ul>
</details>

**标签**: `#mojo`, `#open-source`, `#programming-language`, `#ai`, `#compiler`

---

<a id="item-tech-news-2"></a>
### [Linux 7.3 提升显存溢出性能](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

Linux 7.3 引入了针对显存（VRAM）溢出场景的性能改进，旨在缓解 GPU 工作负载在显存不足时的性能下降问题。该改进通过优化内核在显存过载时的内存管理策略，提升了系统响应速度和整体性能。这一变化对依赖 GPU 计算和图形处理的开发者和用户具有重要意义，尤其是在显存容量受限的环境中。尽管该版本尚未正式发布，但社区已对其表现出浓厚兴趣，并期待其最终合并到主线内核。

hackernews · flaburgan · 8月18日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49342719)

**「背景」** Linux 内核的 VRAM 管理长期以来面临一个挑战：当 GPU 显存不足时，系统性能会急剧下降，甚至导致应用程序崩溃。Valve 的 Linux 图形团队工程师 Natalie Vock 今年早些时候提出了一系列补丁，旨在改善显存受限系统上的 Linux 游戏体验。这些补丁的初始部分计划在 Linux 7.3 内核中引入，后续更改仍在准备中。对于游戏引擎开发者来说，显存不足不再必然导致崩溃或帧率骤降。

**「影响」** 对于使用 Linux 7.3 且面临显存不足问题的 GPU 用户和开发者，该改进有望显著减少性能损失，提升工作负载的稳定性。然而，由于该版本尚未发布，实际效果仍需在正式版本中验证。

**「社区讨论」** 社区普遍对该改进表示赞赏，认为内核在内存分配策略上应更多依赖应用程序的提示，而非仅靠猜测。部分用户提到 Nvidia 显卡目前不支持分页，导致显存管理困难，并希望内核能进一步优化虚拟内存碎片化问题。此外，有评论者对比了 Linux 与 Windows 的更新体验，认为 Linux 的更新更受期待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7 . 3 To Land Initial Code Improving vRAM ... - Phoronix</a></li>
<li><a href="https://dzen.ru/b/aoQ5NBsdD1HIvsGi">Linux 7 . 3 защищает игры при дефиците VRAM Патчи... | Дзен</a></li>

</ul>
</details>

**标签**: `#Linux`, `#VRAM`, `#performance`, `#GPU`, `#kernel`

---

<a id="item-tech-news-3"></a>
### [Qwen 3.8 27B 在人工智能分析指数中得分 52](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B 在人工智能分析指数中取得了 52 分，与 GPT-5.6 Luna（最大）的得分持平，仅比 GLM-5.2（最大）和 DeepSeek V4 Pro 0813（最大）低一分。值得注意的是，GLM-5.2 拥有 7530 亿参数，DeepSeek V4 Pro 0813 拥有 1.7 万亿参数，而 Luna 的规模未知但可能远大于 27B。这一成绩展示了 Qwen 3.8 27B 在效率上的显著优势，以较小的模型规模达到了与更大模型相当的性能。该模型被描述为“真正令人惊叹的模型”，其性能表现引发了广泛关注。

rss · Simon Willison · 8月17日 23:58

**「背景」** Qwen 3.8 27B 是阿里巴巴开源的一个 270 亿参数稠密模型，原生支持 262,144 个 token 的上下文，并可通过 YaRN 扩展到 100 万个 token。Artificial Analysis Intelligence Index 是一个综合评估模型智能水平的基准测试，其分数用于横向比较不同规模和架构的模型。该模型在测试中生成 1.6 亿个 token，远超同类模型的中位数 4300 万，显示出较高的输出冗长度。

**「影响」** 对于 AI 开发者和研究人员而言，Qwen 3.8 27B 的高效表现意味着可以在资源受限的环境中部署接近顶级水平的模型，可能降低推理成本并扩大 AI 应用的可及性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen 3 . 8 27 B - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**标签**: `#qwen`, `#ai`, `#llms`, `#model-efficiency`, `#benchmark`

---

<a id="item-tech-news-4"></a>
### [Turbovec：Rust 实现 Google TurboQuant 向量搜索](https://github.com/RyanCodrai/turbovec) ⭐️ 7.0/10

Turbovec 是一个用 Rust 编写的库，实现了 Google 的 TurboQuant 技术，用于高效的向量搜索。它提供紧凑的索引，据称在性能上优于 FAISS，并支持本地、隐私优先的应用场景。该项目在 Hacker News 上引发讨论，社区成员指出 FAISS 已不再是当前最优，并提到 Qdrant 已集成 TurboQuant 数月。Turbovec 的潜在应用包括构建更快的反向索引和改善开发调试流程，但尚未提供 SQLite 绑定。

hackernews · fittingopposite · 8月18日 18:07 · [社区讨论](https://news.ycombinator.com/item?id=49349898)

**「背景」** TurboQuant 是 Google Research 于 2025 年提出的一种在线向量量化方法，旨在以接近最优的失真率压缩向量数据，从而加速向量搜索并缓解大语言模型推理中的键值缓存瓶颈。Turbovec 是这一方法的 Rust 实现，提供紧凑的索引结构，并声称在性能上优于 FAISS。

**「影响」** 对于需要高效向量搜索的 Rust 开发者，Turbovec 提供了一种可能超越 FAISS 的本地化解决方案，尤其适合隐私敏感的应用。然而，由于 Qdrant 等现有系统已集成 TurboQuant，其创新性有限，实际影响取决于后续的生态支持和采用情况。

**「社区讨论」** 社区普遍认可 Turbovec 的潜力，特别是其紧凑索引（如 1000 万文档仅需 4GB）和本地搜索优势，但有人建议改进 README 以更易采用，也有人质疑其相对于 Qdrant 的独特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>

</ul>
</details>

**标签**: `#vector-search`, `#rust`, `#quantization`, `#ann-benchmarks`, `#local-search`

---

<a id="item-tech-news-5"></a>
### [用铁路网络作为平板扫描仪](https://philo.gay/linecam/) ⭐️ 7.0/10

一项创意项目利用铁路网络作为平板扫描仪，通过狭缝扫描成像技术捕捉列车沿途的连续图像。该项目由作者 otherayden 发布在 philo.gay/linecam/ 上，展示了如何将铁路基础设施转化为一种独特的成像工具。狭缝扫描是一种通过逐行捕捉图像并拼接来创建全景或时间扭曲效果的技术。该项目在 Hacker News 上引发了社区讨论，用户分享了类似的实验和工具，如 slitscan.space 和手动拼接帧的动画创作。尽管这不是一项重大技术突破，但它提供了新颖的视角和实用的见解，展示了创意编码与计算机视觉的结合。

hackernews · otherayden · 8月18日 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49344825)

**「背景」** 狭缝扫描成像（slit-scan imaging）是一种通过连续捕捉一维像素线并随时间拼接成二维图像的技术，常用于创意摄影和艺术创作。该项目利用铁路网络作为“平板扫描仪”，通过固定相机拍摄经过的列车，将列车运动转化为扫描过程，从而生成高分辨率图像。类似的概念在早期已有实践，例如 2008 年有人使用 iSight 摄像头在办公室窗口进行过类似尝试。

**「影响」** 对于对创意编码、计算机视觉和成像技术感兴趣的开发者与艺术家，该项目提供了一个可复现的示例，展示了如何利用现有基础设施（如铁路）进行艺术创作，并可能激发更多类似的实验。

**「社区讨论」** 社区成员分享了类似的实验经历，如 2008 年 Ward Cunningham 和 msisk6 在波特兰的办公室用 iSight 相机进行狭缝扫描，以及 decae 用普通相机手动拼接帧的动画创作。用户 jonty 推荐了 slitscan.space 工具，而 awwaiid 称赞了项目的启发性和艺术与实用性的平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49344825">Using the railway network as a flatbed scanner | Hacker News</a></li>
<li><a href="https://elsolitario.org/en/2026/08/18/line-scan-camera-train-photo-scanner/">Line - Scan Camera: Photographing Trains at 56,894px</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#imaging`, `#creative coding`, `#hardware`, `#open source`

---

<a id="item-tech-news-6"></a>
### [用 20 美元工具修复变砖的 Framework 笔记本](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 7.0/10

一篇详细指南介绍了如何用约 20 美元的工具修复一台因 BIOS 更新失败而变砖的 AMD 7040 系列 Framework 13 笔记本电脑。文章指出，BIOS 更新失败导致设备变砖的问题仍然普遍存在，而制造商（包括 Framework）在支持此类故障方面存在不足。作者通过低成本工具成功恢复了设备，并强调了自行修复的可行性和重要性。该指南还讨论了制造商在保修和软件责任方面的争议，以及用户对 Framework 零件供应和售后支持的担忧。

hackernews · jp\_sc · 8月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49345220)

**「背景」** Framework Laptop 13 是一款模块化设计的笔记本电脑，用户可自行更换部件。AMD 7040 系列型号使用 Ryzen 7040 处理器，其 BIOS 更新通常通过官方工具进行。然而，BIOS 更新失败可能导致设备“变砖”，即无法启动。此类问题在 PC 制造商中并不罕见，但 Framework 的模块化设计本应使维修更容易，而实际维修可能仍需要专业工具或联系制造商。

**「影响」** 对于遇到类似 BIOS 更新变砖问题的 Framework 13 用户，该指南提供了一种无需昂贵专业设备即可自行恢复的可行方案，可能减少因变砖导致的电子垃圾。然而，由于作者未提供具体工具型号和操作细节，其普遍适用性尚不确定。

**「社区讨论」** 社区评论普遍对制造商在 BIOS 更新变砖问题上的责任表示不满，有用户建议通过小额索赔法庭维权，并指出此类问题在 PC 制造商中普遍存在。还有用户对 Framework 的零件供应和售后支持表示担忧，认为缺乏竞争性市场导致用户被锁定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/">Fixing a bricked AMD 7040 series Framework 13” laptop with $20...</a></li>
<li><a href="https://community.frame.work/t/framework-13-amd-ryzen-7040-bios-3-03b/46479/23">Framework 13 AMD Ryzen 7040 BIOS 3.03b</a></li>
<li><a href="https://www.youtube.com/watch?v=k6aDBetYP5c">Framework Laptop 13 - AMD Made it MUCH Better! - YouTube</a></li>

</ul>
</details>

**标签**: `#hardware`, `#BIOS`, `#repair`, `#Framework`, `#embedded`

---

<a id="item-tech-news-7"></a>
### [数据中心使下风向街区气温升高约 0.8°C](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban) ⭐️ 7.0/10

一项发表在 ASME 期刊《可持续建筑》上的实地测量研究首次量化了数据中心对邻近街区气温的影响。测量显示，在数据中心下风向约 500 米范围内，平均气温比上风向升高约 0.8°C（从约 42.7°C 升至 43.5°C）。该研究为数据中心局部热效应提供了实证数据，有助于工程师和政策制定者评估其环境影响。尽管升温幅度相对较小，但研究证实了数据中心废热确实会显著影响局部微气候。

hackernews · cwwc · 8月18日 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49349147)

**「背景」** 数据中心是城市环境中增长最快的人为热源之一，其热通量密度可超过峰值太阳辐射的 2 至 6 倍。然而，此前尚无同行评审文献直接测量或报告其对邻近社区的热影响。这项研究首次通过实地测量，量化了数据中心对下风向邻近区域空气温度的影响。

**「影响」** 该研究为数据中心选址和城市规划提供了量化依据，表明数据中心下风向 500 米内的居民可能感受到约 0.8°C 的额外升温，在高温地区可能加剧热应激。

**「社区讨论」** 评论中有人质疑数据中心恐慌的真实性，认为其规模相对地球而言微不足道，但也有人指出实测升温虽小但确实存在。部分评论者感叹讨论缺乏客观性，并提及凤凰城数据中心升温高达 4°C 的报道，以及对比石油炼油厂等污染源的关注度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban">Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field ...</a></li>

</ul>
</details>

**标签**: `#data centers`, `#environmental impact`, `#urban heat`, `#measurements`, `#infrastructure`

---

<a id="item-tech-news-8"></a>
### [在 264KB SRAM 上运行扩散模型](https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/) ⭐️ 7.0/10

一位开发者在一款名为 Shrike lite 的微控制器上训练并运行了一个生成 32x32 像素图像的扩散模型，该微控制器仅有 264KB 的 SRAM。开发者利用板载 FPGA 创建了两个并行的 INT8 MAC 引擎，并采用 16 位累加来加速计算，但由于 I/O 操作过多导致内存瓶颈，并行 MAC 引擎反而比仅用 MCU 运行更慢（约 220 秒/张 vs 约 70 秒/张）。由于重度量化和内存限制，生成的图像大多显得怪异且带有噪声，但部分效果不错。该项目展示了在极端资源受限的边缘设备上运行生成式 AI 的可行性与挑战。

reddit · r/MachineLearning · /u/PandaBean18 · 8月18日 09:26

**「背景」** 扩散模型是当前主流的图像生成模型，通常需要大量计算资源和内存，一般运行在云端 GPU 或高端边缘设备上。微控制器（MCU）通常只有几十到几百 KB 的 SRAM，且计算能力有限，因此很少被用于运行此类模型。FPGA（现场可编程门阵列）是一种可重构硬件，常用于加速特定计算任务，但 I/O 瓶颈可能抵消其并行计算的优势。

**「影响」** 该实验表明，在 264KB SRAM 的微控制器上运行扩散模型是可行的，但性能极低（每张图像约 70 秒），且图像质量因量化而严重下降。对于边缘 AI 开发者而言，这提供了在极端资源限制下部署生成模型的参考，但实际应用价值有限，除非未来能优化 I/O 和内存访问模式。

**标签**: `#edge-ai`, `#diffusion-models`, `#microcontrollers`, `#quantization`, `#fpga`

---

<a id="item-tech-news-9"></a>
### [企业微信 5.0.10 开放 CLI 与 MCP，支持 AI Agent 接入办公模块](https://mp.weixin.qq.com/s/uJf57P15-FQL_u6jLHiGYA) ⭐️ 7.0/10

企业微信 5.0.10 版本面向所有企业开放 CLI 与 MCP 能力，允许 WorkBuddy、DeepSeek Harness 和企业自建 Agent 直接调用 10 大核心办公模块。该版本支持人员与 AI 权限隔离、关键操作人工审批、限时授权和完整审计，确保安全可控。AI 还能读取文档和表格、分析数据并生成提案 PPT 或经营看板。这一更新为 AI 与办公流程的集成提供了标准化接口，有助于提升企业自动化效率。

telegram · zaihuapd · 8月18日 06:22

**「背景」** 企业微信是腾讯推出的企业通讯与办公协作平台，此前已提供 API 接口供企业集成，但主要面向开发者进行定制开发。MCP（Model Context Protocol）是一种开放协议，旨在标准化 AI 模型与外部工具、数据源的连接方式，使 AI 代理能够调用各类服务。CLI（命令行界面）则允许用户通过命令行直接操作软件。此次企业微信 5.0.10 版本开放 CLI 与 MCP 能力，意味着 AI 代理可以直接通过标准协议接入企业微信，调用其办公模块，而无需针对每个模块单独开发集成。

**「影响」** 对于使用企业微信的企业和开发者，此更新意味着可以更便捷地将 AI Agent 集成到日常办公中，实现文档处理、数据分析等任务的自动化，同时通过权限隔离和审批机制保障安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/991/088.htm">企业微信 5.0.10 开放 CLI 与 MCP，10 大办公模块可接入主流 Agent - IT之家</a></li>

</ul>
</details>

**标签**: `#WeCom`, `#MCP`, `#AI agents`, `#enterprise software`, `#CLI`

---

<a id="item-tech-news-10"></a>
### [中国要求部分政府机构提前卸载定制版 Windows 10](https://www.bloomberg.com/news/articles/2026-08-18/china-axing-microsoft-windows-from-state-agencies-ahead-of-plan) ⭐️ 7.0/10

中国国家安全部已要求部分政府相关机构卸载定制版 Windows 10，将原定于 2027 年 2 月的停用计划提前数月。知情人士称，该指令源于数据安全担忧，但未说明具体漏洞。微软回应称，未发现影响该产品的安全事件，且该产品仍在定期获得安全更新。此举可能影响微软在中国政府市场的布局，并引发对软件供应链安全的关注。

telegram · zaihuapd · 8月18日 06:22

**「背景」** 中国政府长期以来推动信息技术应用创新，以减少对外国软件的依赖。定制版 Windows 10 是微软为中国政府机构提供的特殊版本，旨在满足本地安全和合规要求。此次提前卸载指令是这一趋势的延续，反映了中国在数据安全方面的严格立场。

**「影响」** 受影响的政府机构将需要提前迁移至替代操作系统，可能增加短期内的 IT 转换成本，并影响微软在中国政府市场的收入。同时，此举可能促使其他机构加快国产操作系统的采用。

**标签**: `#China`, `#Windows 10`, `#government policy`, `#data security`, `#Microsoft`

---

<a id="item-tech-news-11"></a>
### [OpenAI 与 CodeAI 合作推进青少年 AI 教育](https://openai.com/index/chatgpt-for-teens/) ⭐️ 7.0/10

OpenAI 于 2026 年 8 月 18 日宣布与 CodeAI 合作，旨在帮助学生和教师负责任地使用 AI，该合作与 ChatGPT for Teens 的发布同步进行。ChatGPT for Teens 包含青少年保护功能和家长控制。未来一年，双方将通过联合咨询委员会、AI 素养课程、学生挑战赛和职业项目，帮助数百万学生了解 AI，并支持 CodeAI 开发免费的高中 AI Foundations 课程。这一举措标志着 AI 教育在 K-12 领域的扩展，对教育者和学生具有广泛影响。

telegram · zaihuapd · 8月18日 12:06

**「背景」** OpenAI 与 CodeAI 的合作旨在通过“Hour of AI”等项目，向数百万学生介绍负责任地使用 AI 的基础知识，并支持 CodeAI 开发免费的 AI Foundations 高中课程。这一举措与 ChatGPT for Teens 的发布同步进行，后者包含青少年保护功能和家长控制。此前，许多学生虽然使用 AI，但缺乏评估其输出的关键技能，此次合作旨在弥补这一理解差距。

**「影响」** 此次合作将直接惠及参与 CodeAI 项目的学校和教师，提供免费的 AI 课程和资源，同时 ChatGPT for Teens 的推出为青少年提供了更安全的 AI 使用环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/partnering-with-codeai/">Partnering with CodeAI to prepare the first AI generation | OpenAI</a></li>
<li><a href="https://beyondtmrw.org/article/openai-codeai-partnership-prepares-the-first-ai-generation-for-school">OpenAI CodeAI Partnership Prepares the First AI Generation f</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-partners-codeai-for-teen-ai-education">OpenAI Partners CodeAI for Teen AI Education | StartupHub. ai</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI education`, `#ChatGPT for Teens`, `#partnership`, `#K-12`

---

<a id="item-tech-news-12"></a>
### [国产 AI 芯片 2026 年将占中国市场近 90%，寒武纪与华为成最大赢家](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd) ⭐️ 7.0/10

TrendForce 预测，到 2026 年，中国本土 AI 加速器将占据国内市场的近 90%，相比去年的 45%大幅提升。寒武纪与华为被视为最大受益者。2025 年，英伟达以 220 万颗的出货量占据 55%的市场份额，而华为出货 81.2 万颗，占 20.3%。中国需要在一年内将高端 AI 芯片产量提升 2.2 倍至约 196 万颗，但产能能否跟上仍存疑。这一转变反映了中国在 AI 硬件领域减少对外依赖的战略趋势。

telegram · zaihuapd · 8月18日 13:03

**「背景」** TrendForce 是一家知名的市场研究机构，其预测基于对全球 AI 加速器市场的分析。2025 年，英伟达在中国市场占据主导地位，出货 220 万颗，市场份额达 55%；华为出货 81.2 万颗，占 20.3%。随着美国对高端 AI 芯片出口管制的加强，中国正加速推动本土芯片替代，以减少对外部供应商的依赖。

**「影响」** 这一趋势将显著影响英伟达和 AMD 在中国市场的份额，同时为寒武纪和华为带来巨大的市场机遇，但产能瓶颈可能限制其满足需求的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd">China &#x27;s homegrown AI accelerators to supply 90... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**标签**: `#AI accelerators`, `#China tech`, `#market analysis`, `#Huawei`, `#Cambricon`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [债券市场压力挤压普通家庭，华尔街静待沃什表态](https://www.cnbc.com/2026/08/18/bond-market-treasury-yields-warsh-main-street.html) ⭐️ 7.0/10

近期美国国债收益率上升，10 年期收益率突破 4.7%，推高抵押贷款利率至 6.75%，柴油价格同比上涨 48%，给普通家庭带来压力。分析师认为，财政赤字和供应冲击是主因，而华尔街因股市回报丰厚（标普 500 三年累计回报 77%）受影响较小。

rss · CNBC Finance · 8月18日 16:48

**「背景」** 近期美国长期国债遭抛售，收益率上升，部分原因是市场担忧财政赤字和供应冲击。新任美联储主席凯文·沃什（Kevin Warsh）对收益率上升持欢迎态度，这进一步推高了收益率。

**「影响」** 购房者和司机等普通消费者将直接承受更高融资和燃料成本，而科技公司因 AI 基础设施需求面临借贷成本上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fool.com/investing/2026/07/21/kevin-warsh-big-move-fed-bond-market-take-action/">Kevin Warsh Made His First Big Move as Fed Chair, and the Bond Market ...</a></li>
<li><a href="https://ecmsource.com/kevin-warsh-fed-chair-nomination-rates-bond-markets-2026/">Kevin Warsh Fed Nomination: What It Signals for Rates and Bonds</a></li>
<li><a href="https://www.cnn.com/2026/07/29/business/bond-yields-fed-warsh">The bond market to Kevin Warsh: What are you doing about inflation? - CNN</a></li>

</ul>
</details>

**标签**: `#Treasury yields`, `#Bond market`, `#Mortgage rates`, `#Inflation`, `#Fiscal policy`

---

<a id="item-finance-news-2"></a>
### [Kalshi 申请推出股指永续合约，进军传统交易所领域](https://www.cnbc.com/2026/08/18/kalshi-wants-to-launch-perps-tied-to-equity-indexes.html) ⭐️ 7.0/10

Kalshi 已向美国商品期货交易委员会（CFTC）提交申请，计划推出与股票指数挂钩的永续合约（perps），该合约将追踪追踪美国最大 500 家公司的 MerQube 美国大盘指数。这是 Kalshi 继加密货币和贵金属永续合约之后的最新扩张举措，旨在成为多资产金融交易所。

rss · CNBC Finance · 8月18日 16:49

**「背景」** Kalshi 是一家预测市场平台，于 2026 年 5 月底首次获得美国商品期货交易委员会（CFTC）批准，推出与加密货币挂钩的永续合约。永续合约是一种没有到期日的期货合约，交易者无需持有标的资产，合约价格通过资金费用与市场价格保持同步。此前，这类产品在美国境外交易，Kalshi 的获批使其成为美国首批受监管的此类产品之一。

**「影响」** 此举可能加剧与传统交易所（如 CME 集团和 CBOE）的竞争，这些交易所的股票在 Kalshi 首次获批时曾下跌，CME 甚至起诉了 CFTC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://coinunited.io/en/pulse/2026-08-18/kalshi-files-sp-500-perpetual-futures-what-a-new-247-leveraged-index-product-means-for-cme-vix-and-your-us500-positions">Kalshi Files S&amp;P 500 Perpetual Futures : What a New... | CoinUnited.io</a></li>
<li><a href="https://www.datawallet.com/crypto/what-are-kalshi-perpetuals">Kalshi Perpetuals: The First CFTC -Regulated Perps Explained</a></li>

</ul>
</details>

**标签**: `#Kalshi`, `#perpetual futures`, `#equity indexes`, `#CFTC`, `#derivatives market`

---

<a id="item-finance-news-3"></a>
### [美国“先买后付”贷款 2025 年达 1600 亿美元，覆盖水电房租等日常支出](https://www.nytimes.com/2026/08/17/business/buy-now-pay-later.html) ⭐️ 7.0/10

美国“先买后付”贷款机构已将服务扩展至水电、通信、保险、房租及医疗等日常支出，2025 年此类贷款总额达 1600 亿美元，较 2023 年近翻倍。LendingTree 调查显示，半数用户表示没有这类贷款难以维持收支，四分之一曾同时背负至少 3 笔贷款。

telegram · zaihuapd · 8月18日 01:41

**「背景」** “先买后付”贷款最初是让网购者无需传统信用卡即可分期付款。如今，随着美国生活成本上升，这类贷款正扩展到水电、房租等必需支出。

**「影响」** 依赖“先买后付”支付必需品的消费者可能面临透支费和债务累积风险，且多数此类贷款尚未纳入征信系统，可能影响未来信用评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/en-us/money/loan/from-sneakers-to-rent-buy-now-pay-later-expands-as-americans-struggle-to-make-ends-meet/ar-AA2amzM9">From sneakers to rent : ‘ Buy now , pay later ’ expands as Americans...</a></li>

</ul>
</details>

**标签**: `#buy-now-pay-later`, `#consumer debt`, `#US economy`, `#fintech`, `#household finance`

---