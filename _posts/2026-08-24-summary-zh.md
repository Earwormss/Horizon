---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 44 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [MS Paint 和照片应用为本地 AI 生成图像添加隐形 GUID 水印](#item-tech-news-1) ⭐️ 8.0/10
2. [seL4 在 AArch64 架构上完成形式化安全证明](#item-tech-news-2) ⭐️ 8.0/10
3. [将可执行文件视为 SQLite 数据库](#item-tech-news-3) ⭐️ 8.0/10
4. [AgentX 推理基准：CUDA 护城河面临挑战](#item-tech-news-4) ⭐️ 8.0/10
5. [小米发布三款玄戒芯片，AI 旗舰 SoC 将搭载小米 18 Fold](#item-tech-news-5) ⭐️ 8.0/10
6. [旧金山整座城市变成可玩视频游戏](#item-tech-news-6) ⭐️ 7.0/10
7. [IPFS 维护团队 Shipyard 停运，项目本身继续](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI 下调 GPT-5.6 系列价格，最高降幅 33%](#item-tech-news-8) ⭐️ 7.0/10
9. [AI 依赖或致编程专长崩溃](#item-tech-news-9) ⭐️ 7.0/10
10. [Bart：一款基于 1931 年前英语语料训练的古董 LLM](#item-tech-news-10) ⭐️ 7.0/10
11. [用 AI 作为空间软件生成器创建可编程 3D 对象](#item-tech-news-11) ⭐️ 7.0/10
12. [延迟校正 Bellman 算子与因果归因的约束 RL 收缩证明](#item-tech-news-12) ⭐️ 7.0/10
13. [阿里云 Wan3.0 上线，30 秒视频生成 API 最低 0.3 元/秒](#item-tech-news-13) ⭐️ 7.0/10
14. [Grok bot 0.18.0 源码因 runtime source maps 泄露并被重建开源](#item-tech-news-14) ⭐️ 7.0/10

**财经新闻**
1. [加密货币延续涨势，创 2023 年以来最大三日涨幅](#item-finance-news-1) ⭐️ 7.0/10
2. [阿里巴巴配股融资 102 亿美元用于 AI 投资，股价大跌](#item-finance-news-2) ⭐️ 7.0/10
3. [Hugging Face 探索出售，估值或达 130 亿美元](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [MS Paint 和照片应用为本地 AI 生成图像添加隐形 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软的画图（MS Paint）和照片（Photos）应用在本地 AI 编辑图像时，会静默嵌入不可见的 GUID 水印，即使使用本地模型生成内容也不例外。该水印无法被用户禁用，且用户不会收到任何通知，可能用于追踪内容来源。这一发现引发了对用户隐私和内容透明度的担忧，因为 GUID 可能与微软账户关联，从而暴露用户身份。目前尚不清楚该水印是否适用于所有 AI 操作，如 AI 背景删除等。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 微软的画图（MS Paint）和照片（Photos）应用在本地生成 AI 编辑图像时，会嵌入一个由服务器签发的 GUID 作为不可见水印。该 GUID 同时嵌入图像像素和元数据中，并与用户提交的提示词相关联。微软已披露画图应用会为 AI 生成图像添加 C2PA 元数据，但此水印无法被用户禁用。

**「影响」** 对于使用微软画图或照片应用进行 AI 编辑的用户，其生成的内容可能被唯一标识，并可能通过法律途径（如版权传票）被追溯到个人账户，从而削弱互联网匿名性。

**「社区讨论」** 评论者普遍认为 AI 方面是转移注意力，真正的问题在于微软秘密添加唯一标识符，可能被用于法律追查。有用户指出微软此前在 Azure DevOps 中错误地为非 AI 提交添加 Copilot 水印，表明其实现可能不精确，建议谨慎使用相关应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible ...</a></li>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#watermarking`, `#AI`, `#Microsoft`, `#reverse-engineering`

---

<a id="item-tech-news-2"></a>
### [seL4 在 AArch64 架构上完成形式化安全证明](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核已在 AArch64 架构上完成形式化安全证明，这是形式化验证领域的一个重要里程碑。该证明复盖了非 MCS（混合关键性系统）单核配置，扩展了 seL4 在 ARM 64 位平台上的安全保证。这一成就意味着 seL4 在 AArch64 上的内核实现已通过机器检查的数学证明，确保其满足安全属性。此举将增强 seL4 在嵌入式、军事等对安全性要求极高的领域的可信度，并可能推动其在更多关键系统中的采用。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个开源的微内核操作系统，以其形式化验证而闻名。其安全证明使用 Isabelle/HOL 定理证明器编写，旨在证明内核满足完整性、可用性和机密性等安全属性。此前，这些证明主要针对 ARM 32 位架构完成，而 AArch64（64 位 ARM 架构）的证明尚未完成。此次宣布完成了 AArch64 架构上的安全证明，意味着该微内核在 64 位 ARM 平台上的安全属性得到了数学上的严格验证。

**「影响」** 对于依赖 seL4 的嵌入式、军事和汽车等安全关键领域的开发者和组织，这一证明提供了更强的安全保证，有助于满足高等级安全认证要求。然而，由于证明仅覆盖非 MCS 单核配置，多核和混合关键性系统的用户仍需等待后续工作。

**「社区讨论」** 社区对此反应积极，但存在一些质疑：有评论指出侧信道时序攻击可能使证明失效，也有评论强调证明的适用范围有限（非 MCS、单核）。此外，有用户询问 seL4 的实际应用，并讨论了其与 Linux 结合的可能性，认为需要原生 seL4/Linux 才能更广泛地提升系统安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sel4.systems/Verification/proofs.html">seL4 Proofs | seL4</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://docs.sel4.systems/projects/sel4/verified-configurations.html">Verified Configurations | seL4 docs</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#microkernel`, `#AArch64`, `#security`

---

<a id="item-tech-news-3"></a>
### [将可执行文件视为 SQLite 数据库](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.0/10

文章提出了一种创新思路：将可执行文件本身视为 SQLite 数据库，从而允许通过 SQL 查询来动态选择组件或实现新型部署策略。作者指出，ELF 格式本质上就是一种数据库，而 SQLite 的动态链接机制与 ELF 动态链接高度兼容，这为构建“可变的胖二进制”提供了可能。例如，可以从平台无关的指令集（如 WebAssembly）开始，逐步添加针对特定机器条件优化的原生代码片段，由运行器根据环境动态替换。文章还提到，SQLite 的虚拟表功能可以将文件系统或其他数据源“挂载”为数据库，进一步扩展了这种概念的适用范围。作者在学术圈发表相关短文时反馈不佳，但在社区中引发了热烈讨论。

hackernews · setheron · 8月24日 04:48 · [社区讨论](https://news.ycombinator.com/item?id=49415271)

**「背景」** ELF（可执行与可链接格式）是 Linux 等系统上可执行文件的标准二进制格式，包含程序代码、数据以及符号表等结构化信息。SQLite 是一种嵌入式关系型数据库，将数据存储在单一文件中，并支持通过虚拟表机制将外部数据源（如文件系统）映射为可查询的表。作者 Farid Zakaria 提出将可执行文件本身构建为 SQLite 数据库，利用 SQLite 的查询能力来访问和操作可执行文件中的符号、依赖关系等元数据，从而实现动态组件选择和新型部署方式。

**「影响」** 如果这一概念得到实现，可能为跨平台部署和性能优化提供新途径，例如替代 AppImage 等打包格式，使可执行文件能够根据运行环境自动选择最优代码路径。

**「社区讨论」** 社区普遍认为这一想法很有前景，有用户表示长期希望实现类似功能，并指出 SQLite 虚拟表功能令人惊叹。也有用户从词源角度指出，所有数据集合本质上都是数据库，而作者提到学术反馈不佳，但社区反应积极。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database | Farid Zakaria’s Blog</a></li>
<li><a href="https://github.com/fzakaria/selfdb">GitHub - fzakaria/selfdb · GitHub</a></li>
<li><a href="https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/">Your executable is a SQLite database</a></li>

</ul>
</details>

**标签**: `#executables`, `#SQLite`, `#software engineering`, `#systems`, `#innovation`

---

<a id="item-tech-news-4"></a>
### [AgentX 推理基准：CUDA 护城河面临挑战](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 8.0/10

SemiAnalysis 发布了一份关于智能体推理性能的详细技术分析，基于其新开源的、耗资 300 万美元的数据集，评估了 GB300 NVL72、MI355 和 B200 等主要硬件平台。该分析聚焦于 CUDA 在智能体推理工作负载中的护城河是否依然稳固，并提供了具体指标，如超过 100 万 token 的上下文长度、多轮对话、子智能体以及 95% 以上的 KVCache 命中率。文章指出，随着智能体推理成为新兴且关键的工作负载，CUDA 的竞争优势可能面临来自开放基准和替代硬件的挑战。该数据集的开源为 AI 基础设施工程师和研究人员提供了宝贵的参考资源。

rss · Semianalysis · 8月24日 00:19

**「背景」** Agentic inference refers to the use of large language models in multi-turn, tool-using workflows, such as autonomous coding agents, which require handling very long contexts and high cache hit rates. Traditionally, NVIDIA&\#x27;s CUDA platform has been considered a strong moat for AI workloads, but new open-source benchmarks are testing whether this advantage holds for agentic inference. The AgentX benchmark, released under Apache 2.0, is the first fully open-source, multi-turn agentic coding inference benchmark at 1 million context length, aiming to provide transparent performance comparisons across hardware platforms.

**「影响」** 对于 AI 基础设施工程师和研究人员，该开源数据集和基准分析提供了评估不同硬件平台在智能体推理场景下性能的客观依据，可能影响未来的硬件选型和 CUDA 生态的采用决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv 3 : Does CUDA Moat Hold up in Agentic ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#GPU benchmarking`, `#CUDA`, `#agentic inference`, `#open-source dataset`

---

<a id="item-tech-news-5"></a>
### [小米发布三款玄戒芯片，AI 旗舰 SoC 将搭载小米 18 Fold](https://mp.weixin.qq.com/s/ceIQbNnZrcNQqGywXCiXTQ) ⭐️ 8.0/10

小米发布了新一代玄戒芯片，包括 AI 旗舰 SoC 玄戒 O3、高带宽 AI 加速芯片玄戒 O100 以及国内首款 3nm 智驾 AI 芯片玄戒 D100。玄戒 O3 采用十核全大核 CPU，多核跑分首破 15000 分，GPU 首发 G2-Ultra NX，性能提升 85%、功耗降低 64%，并成为全球首个支持 LPDDR6 的移动处理器，带宽达 113.8 GB/s，NPU 端侧 AI 性能提升 45%。玄戒 D100 采用 3nm 工艺，集成 20 核 CPU 与 16 核 NPU，最高支持 160GB 统一内存，可本地部署 200B 参数大模型，计划明年商用。玄戒 O100 采用行业首款 6nm 晶圆级垂直堆叠先进封装，通过 Hybrid Bonding 混合键合工艺实现 1.4 微米键合间距，带宽达 1.22TB/s，为传统旗舰手机的 16 倍，端侧推理速度最高可达 330TPS。三款芯片均完成回片验证，覆盖人车家全生态端侧 AI 算力需求，其中 AI 旗舰 SoC 将首发搭载于小米 18 Fold。

telegram · zaihuapd · 8月24日 07:18

**「背景」** 小米此前已推出玄戒系列芯片，逐步构建自研芯片能力。此次发布的三款芯片中，玄戒 O3 为 AI 旗舰 SoC，将首发搭载于小米 18 Fold；玄戒 O100 是高带宽 AI 加速芯片；玄戒 D100 是国内首款 3nm 智驾 AI 芯片。这些芯片均已完成回片验证，旨在覆盖手机、汽车和全生态的端侧 AI 算力需求。

**「影响」** 小米自研芯片的进展可能对高通和联发科构成竞争压力，尤其考虑到小米作为全球第三大智能手机制造商且仍在增长，其芯片能力提升可能影响移动 SoC 市场格局。

**「社区讨论」** 社区评论指出，玄戒 O3 的 CPU 架构与联发科天玑 9500 相同，但实际性能受限于手机散热和功耗，可能无法达到实验室成绩；同时，多位用户强调功耗效率是更关键的指标，而小米未公布相关数据。部分评论认为，尽管小米芯片性能接近苹果，但多核成绩仍落后于苹果 M5 Max，且核心数更多，苹果尚未被超越。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/xuanji-o3-o100-d100-chips-launched-by-xiaomi">Xiaomi Launches Xuanji O3, O100, and D100 Chips - KuCoin</a></li>
<li><a href="https://www.gizmochina.com/2026/08/24/xiaomi-xring-o3-o100-d100-chipsets-launched-xiaomi-18-fold/">Xring O3 launches with 5.22M AnTuTu score and LPDDR6, Xiaomi ...</a></li>
<li><a href="https://nokiamob.net/2026/08/24/xiaomi-xring-o3-breaks-5-million-antutu-points-as-new-flagship-chip-launches/">Xiaomi Unveils Xring O3, O100 and D100 Chips for Phones, AI ...</a></li>

</ul>
</details>

**标签**: `#xiaomi`, `#soc`, `#ai-chip`, `#3nm`, `#automotive`

---

<a id="item-tech-news-6"></a>
### [旧金山整座城市变成可玩视频游戏](https://sf.thijs.gg/) ⭐️ 7.0/10

一个名为“旧金山整座城市变成可玩视频游戏”的网页项目（https://sf.thijs.gg/）利用真实 GIS 数据将旧金山重建为可玩的游戏环境，引发了社区广泛关注。该项目展示了将地理信息系统数据转化为游戏场景的新颖技术方法，并借助 LLM 降低了开发门槛。社区成员对此表现出强烈的情感共鸣，例如一位在旧金山生活近 20 年的用户表示在虚拟城市中漫步让他感动。该项目目前仍处于早期阶段，但已激发关于未来扩展的讨论，如添加街道名称、地标、多人游戏功能等。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**「背景」** GIS（地理信息系统）数据通常用于地图和城市规划，但将其转化为游戏环境需要处理地形、建筑、道路等复杂数据。近年来，LLM 辅助开发工具降低了编程门槛，使得个人开发者能够更轻松地构建此类项目。该项目正是利用公开的 GIS 数据，通过程序化生成技术创建了一个可探索的旧金山虚拟城市。

**「影响」** 该项目为游戏开发和地理数据可视化提供了新的可能性，可能激励更多开发者利用本地 GIS 数据创建类似的虚拟城市体验。对于旧金山居民或前居民，它提供了一种独特的情感连接方式，但当前版本分辨率有限，且缺乏游戏性元素，可能限制其长期吸引力。

**「社区讨论」** 社区成员普遍赞赏该项目，并提出了多种改进建议，如添加街道名称、地标、地址传送功能，以及多人游戏模式。一些用户分享了类似项目（如费城的 City Rider），并鼓励其他人尝试利用本地 GIS 数据开发游戏。还有用户提到 90 年代的赛车游戏《Vette》也覆盖了旧金山，暗示了此类概念的历史先例。

**标签**: `#GIS`, `#procedural-generation`, `#web-game`, `#LLM-assisted-development`, `#open-data`

---

<a id="item-tech-news-7"></a>
### [IPFS 维护团队 Shipyard 停运，项目本身继续](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS Shipyard，一个负责维护 IPFS 实现的团队，宣布即将停止运营。然而，这并不意味着 IPFS 项目本身终止，而是将转向由个人维护者获得资助的模式，而非由 Shipyard 集中支持。这一变化发生在 Cloudflare 此前放弃 IPFS 之后，引发了社区对 IPFS 未来方向的讨论。尽管 Shipyard 停运，但 IPFS 项目仍将继续，只是维护方式发生改变。

hackernews · iand · 8月24日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49421489)

**「背景」** IPFS（星际文件系统）是一个去中心化的点对点超媒体协议，旨在替代 HTTP，通过内容寻址实现更安全、高效的数据分发。Interplanetary Shipyard（简称 Shipyard）是一个独立的维护者集体，成立于 2024 年 4 月，负责维护 IPFS 和 libp2p 生态中的多个流行实现。此次公告宣布 Shipyard 将于 2026 年 9 月 30 日结束其 IPFS 相关的工程、维护和基础设施运营，但 IPFS 项目本身并未关闭，而是转向由个人维护者获得资助的模式。

**「影响」** 对于依赖 IPFS 的开发者、用户和组织，这一变化可能导致维护响应速度变慢或支持减少，但项目本身不会消失。社区成员建议关注如 Iroh 等替代方案，这些方案由前 IPFS 开发者创建，并有商业支持。

**「社区讨论」** 社区评论指出，公告标题具有误导性，实际只是 Shipyard 团队停运，而非整个 IPFS 项目。一些评论者表达了对 IPFS 技术方向的不满，认为过度投入 IPNS 而忽视了 Web 应用支持，导致发展受限。还有人推荐了 Iroh 作为更可持续的 P2P 替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/">The end of IPFS at Shipyard</a></li>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS &amp; libp2p Devs Go Independent: Meet Interplanetary Shipyard | IPFS Blog &amp; News</a></li>

</ul>
</details>

**标签**: `#IPFS`, `#decentralized web`, `#P2P`, `#open source`, `#maintainership`

---

<a id="item-tech-news-8"></a>
### [OpenAI 下调 GPT-5.6 系列价格，最高降幅 33%](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI 宣布临时下调 GPT-5.6 系列模型（Sol、Terra、Luna）的 API 价格，有效期至少持续至 2026 年 11 月 21 日。其中输入价格降低 20%，输出价格降低 33%。调整后，gpt-5.6-sol 的输入价格为每百万 tokens 4.00 美元，输出价格为 20.00 美元；gpt-5.6-terra 分别为 2.00 美元和 12.00 美元；gpt-5.6-luna 分别为 0.20 美元和 1.20 美元。缓存输入和缓存写入价格也相应下调。此次降价旨在提升 GPT-5.6 系列在 AI API 市场的竞争力，尤其是与 Anthropic 等竞争对手的产品相比。

hackernews · tosh · 8月24日 15:22 · [社区讨论](https://news.ycombinator.com/item?id=49421074)

**「背景」** OpenAI 于 2026 年 7 月发布了 GPT-5.6 系列模型，包括旗舰版 Sol、低成本版 Terra 和最快最实惠的 Luna。此次价格下调是继 7 月 30 日降价后的又一次调整，当时 Luna 降价 80%、Terra 降价 20%，部分原因是开源模型（如 Kimi K3）带来的竞争压力。

**「影响」** 对于使用 GPT-5.6 系列 API 的开发者与企业，此次降价将直接降低推理成本，尤其是输出密集型应用的成本可减少三分之一，从而可能促进更广泛的采用。

**「社区讨论」** 社区评论普遍欢迎价格战，认为这有利于开源模型和整体生态。有开发者指出 Sol 在处理长任务时过于专注细节，可能不如其他模型；另有用户提到 OpenRouter 上还有额外 50% 折扣，实际价格更低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macdate.com/en/blog/openai-gpt-5-6-price-cut-luna-terra-sol-20260731.html">Why OpenAI Cut GPT - 5 . 6 Luna &#x27;s Price 80% | Terra -20%, Sol Fast...</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#pricing`, `#AI API`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [AI 依赖或致编程专长崩溃](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

文章作者 Lars Faye 认为，过度依赖 AI 编码工具将阻碍开发者形成深厚的编程专长，导致行业整体技能退化。文章指出，虽然 AI 能大幅提升代码产出速度，但工程师们正以超出人类理解和审查能力的速度生成代码，这可能导致代码质量下降和长期维护困难。作者强调，编程中的“摩擦”对技能形成至关重要，而 AI 工具将这种摩擦点转移，可能使开发者失去深入理解系统的机会。该观点在 Hacker News 上引发广泛讨论，获得 408 分和 414 条评论，反映了社区对 AI 辅助开发利弊的深切关注。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**「背景」** 随着大型语言模型（LLM）集成到开发工具中，如 GitHub Copilot、Zed 和 VSCode 的 AI 助手，开发者可以更快速地编写代码，甚至通过“vibe coding”方式让 AI 自主实现功能。然而，这种效率提升引发了对开发者技能长期发展的担忧，尤其是当企业领导层强制要求使用 AI 编码时，可能削弱开发者对底层原理的理解。

**「影响」** 对于依赖 AI 编码工具的开发者团队，短期内可能提高生产力，但长期可能导致代码审查负担加重、系统理解不足，以及资深开发者被迫审查低质量 AI 代码的困境。

**「社区讨论」** 社区评论普遍认同文章观点，有用户指出企业层面已出现“手动写代码就是错”的指令，导致代码产出远超人类审查能力；也有开发者强调“引导式编码”比“vibe coding”更高效且质量更高，但整体上对 AI 依赖的可持续性表示担忧。

**标签**: `#AI-assisted development`, `#software engineering`, `#expertise`, `#developer productivity`, `#future of coding`

---

<a id="item-tech-news-10"></a>
### [Bart：一款基于 1931 年前英语语料训练的古董 LLM](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs 发布了 Bart，一个拥有 28.2 亿参数、从零开始训练的 LLM，其训练数据为 201 亿个 token 的 1931 年前英语文本。该项目旨在探索 LLM 能否重现历史科学家的发现，并公开了数据集、方法、训练代码、评估和训练运行。团队清理了哈佛大学机构藏书（从 2420 亿 token 降至 230 亿），创建了 Vintage CORE 基准套件（20 个基准），并发布了包含 41.6 万对问答的 SFT 数据集。最终模型在单个 H100 上训练了 5 天，保持了 60% 的 MFU，总成本约 807 美元。团队正在寻求计算资源资助和合作。

reddit · r/MachineLearning · /u/soggydoggy8 · 8月24日 17:20

**「背景」** 大型语言模型（LLM）通常在海量现代文本上训练，而 Bart 项目则反其道而行之，专门使用 1931 年以前的英语文本进行训练，以探索模型能否独立重现历史上的科学发现。这一想法源于 DeepMind 的 Demis Hassabis 提出的假设：LLM 是否可能得出与过去伟大科学家相同的结论？该项目由 Unbounded Labs 团队自筹资金完成，总花费约 807 美元，训练过程耗时三个月，最终模型拥有 28.2 亿参数，在 20.1B 个 token 上完成训练。

**「影响」** 对于研究 LLM 原创性和历史推理的研究者，Bart 提供了一个开源、可复现的案例，展示了在特定历史语料上训练小型模型的可能性，但其实际应用范围有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://generative-infinite-game.github.io/">Unbounded: A Generative Infinite Game of Character Life Simulation</a></li>

</ul>
</details>

**标签**: `#LLM`, `#historical corpus`, `#from-scratch training`, `#AI research`, `#open source`

---

<a id="item-tech-news-11"></a>
### [用 AI 作为空间软件生成器创建可编程 3D 对象](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

一篇新论文提出使用大型语言模型（LLM）作为空间软件生成器，创建本质上可编程的 3D 对象。该方法生成的 3D 对象由逻辑部件组成，天生支持动画和编程，并能根据计算环境（如移动设备与游戏引擎）调整外观。作者在 nova3d.xyz 上提供了可视化演示和 GitHub 代码库。与传统 AI 3D 生成器相比，该方法在复杂有机形状方面仍有不足，但作者认为随着 LLM 空间编码能力的提升，代码最终将主导 3D 生成，影响工业设计、游戏开发、模拟和 AR/VR/XR 等行业。

reddit · r/MachineLearning · /u/mhb\_11 · 8月24日 19:10

**「背景」** 传统 AI 3D 生成器通常输出单一的网格模型（mesh blobs），难以编辑、动画或适应不同环境。空间编程是一种将 3D 对象表示为代码的方法，使其具有层次结构和关节连接，从而更灵活和可编程。该论文探索了 LLM 在此领域的应用，旨在生成更实用、更动态的 3D 内容。

**「影响」** 对于游戏开发者、工业设计师和 AR/VR/XR 从业者，该方法可能提供更高效、更灵活的 3D 内容生成方式，减少后期处理工作。然而，由于在复杂有机形状上的局限，其当前应用范围可能受限，需等待 LLM 空间编码能力的进一步提升。

**标签**: `#3D generation`, `#LLM`, `#spatial programming`, `#AI`, `#software engineering`

---

<a id="item-tech-news-12"></a>
### [延迟校正 Bellman 算子与因果归因的约束 RL 收缩证明](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

该 Reddit 帖子提出了一种名为 CCPL（因果后果惩罚学习）的方法，用于解决约束强化学习中后果延迟且随机的问题。作者引入了一个延迟校正的 Bellman 算子，利用从后果延迟分布中学习的自适应有效折扣，并在未知随机延迟下证明了收缩性。此外，还提出了一个干预后果网络（ICN），该网络在结构因果模型标签上预训练，以估计每个动作的边际因果贡献，而非基于时间邻近性进行惩罚。作者坦承 ICN 目前需要访问环境的结构因果模型来生成预训练标签，这限制了其在非基准环境中的适用性。帖子还邀请贡献者和合作者，特别是从事约束/安全 RL 或因果推断的研究人员。

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · 8月24日 12:11

**「背景」** 标准约束强化学习假设违反约束的后果是即时的且可归因于当前动作，但在现实世界中，后果往往延迟且随机，导致惩罚错误地施加于先前的动作而非真正原因。CCPL 旨在通过延迟校正的 Bellman 算子和基于因果归因的干预后果网络来解决这一问题。

**「影响」** 对于从事约束或安全强化学习的研究人员，CCPL 提供了一种处理延迟随机后果的理论框架，但当前需要已知的结构因果模型，这限制了其在现实环境中的直接应用。

**标签**: `#reinforcement learning`, `#constrained RL`, `#causal inference`, `#Bellman operator`, `#delayed consequences`

---

<a id="item-tech-news-13"></a>
### [阿里云 Wan3.0 上线，30 秒视频生成 API 最低 0.3 元/秒](https://mp.weixin.qq.com/s/peeeU6cBz4AaROvFe1zqQQ) ⭐️ 7.0/10

阿里云今日正式上线视频生成模型 Wan3.0，支持最长 30 秒视频生成，并在人物质感、参考精准一致性和非写实风格化等方面表现突出。用户可通过阿里云百炼、万相官网、千问 APP 等平台体验。API 价格按分辨率区分，480P、720P、1080P 分别为 0.3 元/秒、0.6 元/秒、1.2 元/秒。8 月 24 日至 9 月 23 日，阿里云百炼和千问 AI 平台提供 API 限时 7 折优惠。

telegram · zaihuapd · 8月24日 10:14

**「背景」** 万相（Wan）是阿里云推出的视频生成模型系列，此前已发布多个版本。Wan3.0 于 2026 年 8 月 6 日开启公测，官方称其为“最强视频模型”，核心升级包括单次生成 30 秒视频、支持无缝延长，并首次支持 doc、xls、ppt、pdf、md 等文档格式输入，无需重新格式化。

**「影响」** 对于需要视频生成能力的开发者和企业，Wan3.0 提供了具有竞争力的价格和较长的生成时长，可能降低视频生成应用的成本门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aihot.virxact.com/story/a99af99d-0dff-4752-a453-37de2d1a0c65">Alibaba Cloud releases Wan 3 . 0 · AI HOT</a></li>
<li><a href="https://juejin.cn/post/7670593377075724339">juejin.cn/post/7670593377075724339</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#Alibaba Cloud`, `#API pricing`, `#Wan3.0`, `#machine learning`

---

<a id="item-tech-news-14"></a>
### [Grok bot 0.18.0 源码因 runtime source maps 泄露并被重建开源](https://x.com/b_nnett/status/2091630242792112480) ⭐️ 7.0/10

Cursor 团队在发布 Grok bot 0.18.0 时意外开启了 runtime source maps，导致其源码被网友 Bennett 重建并上传至 GitHub 开源。该版本不含前端，但可使用官方打包的前端启动，且仍可修改。Bennett 在重建基础上加入了自定义路由（支持 Codex 与 Claude Code），并支持使用本地 Docker 替代远程沙箱。这一事件既暴露了安全配置失误，也意外推动了工具的开源和功能增强。

telegram · zaihuapd · 8月24日 10:36

**「背景」** Source map 是一种将压缩或转译后的代码映射回原始源代码的文件，通常用于调试。当运行时（runtime）意外开启 source map 时，原本隐藏的源码可能被暴露。Grok bot 是 Cursor 团队开发的一款 AI 编程助手，其 0.18.0 版本在发布时因配置失误开启了 runtime source map，导致源码泄露。

**「影响」** 对于使用 Grok bot 的开发者，源码泄露和开源意味着可以自由审查、修改和扩展该工具，但同时也可能带来安全风险，因为潜在漏洞被公开。Bennett 的增强（自定义路由和本地 Docker 支持）为开发者提供了更灵活的部署选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/b-nnett/grok-bot-0.18-reconstructed">b-nnett/ grok - bot - 0 . 18 -reconstructed: Unofficial source -oriented...</a></li>

</ul>
</details>

**标签**: `#security`, `#open-source`, `#AI tools`, `#source maps`, `#Grok bot`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [加密货币延续涨势，创 2023 年以来最大三日涨幅](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 7.0/10

比特币周一上涨逾 1%，交易价格接近 8 万美元，为 5 月以来首次；此前一周，比特币在三天内飙升逾 20%，创 2023 年以来最大三日涨幅，主要受美国财政部增加长期国债购买、机构资金流入和空头回补推动。

rss · CNBC Finance · 8月24日 20:02

**「背景」** 此前，比特币自去年 10 月以来一直处于长期低迷状态。上周，美国财政部宣布将加倍购买较长期国债，导致收益率短暂下降，提振了比特币等风险资产的需求。同时，机构需求回升，现货比特币 ETF 上周流入 19.2 亿美元，为去年 10 月以来的最大单周流入。此外，超过 40 亿美元的空头头寸被清算，推动了这轮超过 20%的涨幅。

**「影响」** 此次上涨可能提振加密货币相关股票和 ETF 投资者，但 BTIG 分析师指出，类似走势在 2023 年 1 月曾出现后回落，因此涨势能否持续仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://coinalertnews.com/news/2026/08/21/ray-dalio-bitcoin-debt-crisis">Ray Dalio Warns of U.S. Debt Crisis, Says Bitcoin Will &#x27;Do ...</a></li>
<li><a href="https://www.cnbc.com/2026/08/21/ray-dalio-bessent-debt-crisis-bitcoin-gold.html">Ray Dalio: Bessent move is sign debt crisis nearing, touts ...</a></li>

</ul>
</details>

**标签**: `#bitcoin`, `#cryptocurrency`, `#market rally`, `#ETF inflows`, `#macro policy`

---

<a id="item-finance-news-2"></a>
### [阿里巴巴配股融资 102 亿美元用于 AI 投资，股价大跌](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 7.0/10

阿里巴巴周一在香港股市一度下跌 10%，此前该公司宣布以每股 112.70 港元配售 7.1 亿股新股，筹资约 102 亿美元（约合 800 亿港元），用于投资 AI 基础设施。配售价较上周五收盘价 123 港元折让约 8.4%。

rss · CNBC Finance · 8月24日 08:21

**「背景」** 阿里巴巴此前已宣布未来三年将在云计算和 AI 基础设施上投入至少 3800 亿元人民币。此次配售是在公司公布 6 月当季利润下滑 75%之后进行的，反映出其 AI 支出大幅增加。

**「影响」** 此次配售将稀释现有股东权益，并可能给阿里巴巴股价带来短期压力，同时反映出中国科技公司为争夺 AI 市场份额而进行的资本支出竞赛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wsj.com/tech/alibaba-to-bulk-up-ai-investment-via-10-20-billion-share-placement-72b9bdac">Alibaba Aims to Raise $10.2 Billion for AI Investment - WSJ</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#share placement`, `#AI investment`, `#Hong Kong market`, `#capital expenditure`

---

<a id="item-finance-news-3"></a>
### [Hugging Face 探索出售，估值或达 130 亿美元](https://www.bloomberg.com/news/articles/2026-08-23/hugging-face-gauging-interest-for-potential-sale-business-insider-says) ⭐️ 7.0/10

据 Business Insider 援引知情人士消息，人工智能平台 Hugging Face 正探索出售，估值可能达到 130 亿美元或更高，目前尚未达成交易。该公司在 2023 年完成 2.35 亿美元融资后估值为 45 亿美元。

telegram · zaihuapd · 8月24日 05:45

**「背景」** Hugging Face 是一个广受欢迎的人工智能平台，开发者常在此分享和下载 AI 模型。该公司在 2023 年完成一轮 2.35 亿美元的融资后，估值达到 45 亿美元。近期，OpenAI 曾披露其一个未发布的模型意外入侵该平台获取考试答案，引发了对 AI 模型安全性的担忧。

**「影响」** 若交易达成，可能影响人工智能行业的竞争格局，但具体影响尚不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-23/hugging-face-gauging-interest-for-potential-sale-business-insider-says">Hugging Face Gauging Interest for Potential Sale ... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#M&amp;A`, `#AI`, `#Hugging Face`, `#valuation`, `#tech`

---