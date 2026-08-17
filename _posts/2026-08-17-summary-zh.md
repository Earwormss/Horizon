---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 42 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [Qwen3.8 27B 在 Artificial Analysis 上得分 52，超越更大模型](#item-tech-news-1) ⭐️ 9.0/10
2. [DuckDB v2.0 预览发布](#item-tech-news-2) ⭐️ 8.0/10
3. [追踪稀有书籍运输：终点是亚马逊 AI 训练设施](#item-tech-news-3) ⭐️ 8.0/10
4. [如何让稀疏注意力与 KV 压缩看起来效果更好？](#item-tech-news-4) ⭐️ 8.0/10
5. [AI 生成的 GitHub Copilot“自动修复”导致 Snowflake 的 Jira 被入侵](#item-tech-news-5) ⭐️ 7.0/10
6. [AI;DR：AI 生成内容引发阅读疲劳与信任危机](#item-tech-news-6) ⭐️ 7.0/10
7. [GPT 5.6 Sol 视觉模型评测：多数基准落后于 Gemini 3.5 Flash](#item-tech-news-7) ⭐️ 7.0/10
8. [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](#item-tech-news-8) ⭐️ 7.0/10
9. [美团高管反思全员 AI 运动：日耗千万 Token，干扰真实经营](#item-tech-news-9) ⭐️ 7.0/10
10. [宇树预告人形机器人“超人”：原地跳高 2 米破人类纪录](#item-tech-news-10) ⭐️ 7.0/10
11. [苹果调整 ATT 授权规则以回应德国监管裁决](#item-tech-news-11) ⭐️ 7.0/10

**科技博客**
1. [vLLM-Omni 分布式分层卸载：高效扩展至 200B+ DiT 模型](#item-tech-blog-1) ⭐️ 9.0/10

**财经新闻**
1. [珍妮·巴斯反对出售湖人队家族股份](#item-finance-news-1) ⭐️ 7.0/10
2. [Synchrony 与 OpenAI 合作，允许在 ChatGPT 内使用商店卡购物](#item-finance-news-2) ⭐️ 7.0/10
3. [Stripe 据悉以超 70 亿美元收购 AI 模型平台 OpenRouter](#item-finance-news-3) ⭐️ 7.0/10
4. [宇树科技将于 8 月 19 日科创板上市，发行价 150.8 元](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen3.8 27B 在 Artificial Analysis 上得分 52，超越更大模型](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 9.0/10

Qwen3.8 27B 在 Artificial Analysis 上获得 52 分，超越了所有中型模型（40B–150B），并与大型模型（&gt;150B）中排名第五的 DeepSeek V4 Flash 0731 持平。相比之下，其前代 Qwen3.6 27B 得分为 38，曾是小型模型类别（4B–40B）中的最高分。这一成绩标志着高效 AI 的重大里程碑，表明 27B 参数模型能够达到前沿 SOTA 水平，同时可在游戏 PC 上流畅运行。该模型在更高推理层级上表现出强烈的智能体特性，用户反馈其具备目标追踪和工具调用能力，甚至表现出类似 GPT-5.6-Sol-max 的执着求解行为。

hackernews · anana\_ · 8月17日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=49334544)

**「背景」** Qwen 3.8 27B 是阿里巴巴开源的大型语言模型系列中的最新版本，其前代 Qwen 3.6 27B 在 4B–40B 参数的小型模型类别中得分最高（38 分）。Artificial Analysis Intelligence Index 是一个综合基准，评估模型在推理、知识、数学和编码方面的能力。该指数用于比较不同规模模型的性能，而 Qwen 3.8 27B 以 52 分的成绩超越了所有中型模型（40B–150B），并与大型模型类别（&gt;150B）中排名第五的 DeepSeek V4 Flash 0731 持平。

**「影响」** 对于本地部署和日常使用的开发者而言，Qwen3.8 27B 提供了接近前沿 SOTA 的能力，且硬件要求较低，可能改变模型选择策略，减少对超大规模数据中心和巨额债务投资的依赖。

**「社区讨论」** 社区用户对 Qwen3.8 27B 的性能表示惊讶和难以置信，认为其击败 Opus 4.6 既有趣又令人恐惧，并质疑构建大规模数据中心的必要性。多位用户计划进行广泛测试，其中一位用户提到其内部自动化基准测试大致遵循其工作流程，但评论被截断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen 3 . 8 27 B - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#AI benchmarks`, `#model efficiency`, `#open source`, `#artificial intelligence`

---

<a id="item-tech-news-2"></a>
### [DuckDB v2.0 预览发布](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

DuckDB 团队发布了 v2.0 的预览版，这是该开源分析数据库的一个重要里程碑。新版本引入了名为 Quack 的新功能，引发了社区的广泛关注和讨论。尽管是预览版，但社区对其开发速度和方向表现出高度热情。DuckDB 自 2023 年以来已被多家公司采用，用于降低资源需求并支持大规模数据处理。此次预览版的具体技术细节尚未完全披露，但社区期待其能带来性能提升和新特性。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**「背景」** DuckDB 是一个开源的分析型数据库，通常以嵌入式方式运行在应用程序进程中，无需单独部署服务器。其 v2.0 版本（代号 Cyanoptera）计划于 2026 年秋季发布，将引入 Quack 远程协议和新的 CONNECT 语句，使任何 DuckDB 进程都能通过网络作为客户端或服务器运行，支持完整的 DuckDB 功能集。此外，v2.0 还将加入 OAuth/OIDC 认证，并将 DuckLake 功能内联到核心中。

**「影响」** 对于依赖 DuckDB 进行数据分析和运行时处理的开发者和组织，v2.0 预览版可能带来性能改进和新功能，但需注意其仍处于预览阶段，可能存在不稳定因素。

**「社区讨论」** 社区对 Quack 功能表示兴奋，但也有用户质疑 10,000 次提交是否过多，可能涉及 AI 辅助开发。此外，有用户指出 DuckDB 仍缺少增量物化视图，认为这是与 ClickHouse 竞争的关键功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/duckdb-2-0-roadmap-duckcon-7/">DuckDB 2.0 Is Coming: What DuckCon #7 Revealed | byteiota</a></li>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>

</ul>
</details>

**标签**: `#duckdb`, `#database`, `#analytics`, `#release`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [追踪稀有书籍运输：终点是亚马逊 AI 训练设施](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media 的一项调查性报道使用苹果 AirTag 追踪了一批约 1000 本稀有书籍的运输，最终发现这批书被送往位于拉斯维加斯东北部的亚马逊 LAS8 设施中的 VGT3 区域，该区域入口处有恐龙与书籍的标志。在线论坛上亚马逊员工的讨论证实，VGT3 会对大量书籍进行破坏性扫描，这为书籍被用于 AI 训练提供了具体证据。此前已有书商报告收到大量匿名且对价格不敏感的订单，怀疑与 AI 训练数据采集有关，此次追踪证实了这些猜测。该报道由 Simon Willison 转发并评论，强调了这一发现对 AI 训练数据来源和版权讨论的重要性。

rss · Simon Willison · 8月17日 15:21

**「背景」** 近年来，书商经常收到大量书籍订单，买家匿名且对价格不敏感，外界普遍怀疑这些订单来自希望扫描书籍用于 AI 训练的公司。2025 年 6 月，Simon Willison 曾报道过 Anthropic 的书籍扫描活动，而此次 404 Media 的调查通过 AirTag 追踪提供了更直接的证据。

**「影响」** 这一发现证实了亚马逊参与大规模书籍扫描用于 AI 训练，可能加剧关于版权和 AI 训练数据合法性的争议，并促使书商和公众重新审视匿名大宗购书订单的来源。

**标签**: `#AI training data`, `#investigative journalism`, `#Amazon`, `#book scanning`, `#data sourcing`

---

<a id="item-tech-news-4"></a>
### [如何让稀疏注意力与 KV 压缩看起来效果更好？](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

一位机器学习从业者在 Reddit 上分享了一篇关于稀疏注意力和 KV 缓存压缩方法评估中常见陷阱的批判性文章。作者指出，通过选择对压缩有利的基准测试（如单跳检索、无干扰项、过时基准或无效的少样本学习），可以人为地让方法看起来效果很好。文章还建议避免隔离贡献、使用聚合指标掩盖弱点、利用饱和任务，并忽略统计显著性。作者呼吁社区采用更严格的评估实践，并承认自己也曾犯过这些错误。

reddit · r/MachineLearning · /u/korec1234 · 8月17日 12:18

**「背景」** 稀疏注意力和 KV 缓存压缩是提高大型语言模型推理效率的技术，通过减少注意力计算或缓存大小来降低内存和计算开销。评估这些方法通常使用基准测试，如 RULER，它包含多种任务，但某些任务可能对压缩方法过于友好，导致结果不能真实反映方法的实际性能。

**「影响」** 这篇帖子提醒研究者和工程师在评估稀疏注意力和 KV 压缩方法时，应警惕基准测试选择偏差和评估不严谨的问题，以避免被误导性的结果所迷惑。

**标签**: `#sparse attention`, `#KV cache compression`, `#evaluation methodology`, `#machine learning`, `#benchmarking`

---

<a id="item-tech-news-5"></a>
### [AI 生成的 GitHub Copilot“自动修复”导致 Snowflake 的 Jira 被入侵](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 7.0/10

安全研究人员演示了 AI 生成的 GitHub Copilot“自动修复”如何在 Snowflake 的 CI/CD 工作流中引入模板注入漏洞，最终导致其 Jira 系统被入侵。该漏洞源于对 GitHub Actions 工作流（如 jira\_issue.yml）的自动修复，其中未正确转义标题和正文中的特殊字符，使得攻击者能够通过模板扩展执行代码注入。这一事件凸显了 AI 生成代码在供应链安全中的风险，即使修复意图良好，也可能引入严重漏洞。研究人员强调，必须对 AI 生成的代码进行严格的安全审查，包括使用静态分析工具（如 zizmor）来检测此类问题。该案例为软件工程师和安全专业人员提供了重要警示，表明在采用 AI 辅助编码时，仍需保持传统代码审查和测试流程。

hackernews · galnagli · 8月17日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**「背景」** GitHub Copilot Autofix 是 GitHub 提供的 AI 辅助安全修复功能，能够自动生成代码修复建议。Wiz 研究团队开发了一个名为“Red Agent”的自主 AI 安全代理，用于模拟攻击者行为。在测试中，Red Agent 发现 Snowflake 的 GitHub Actions 工作流中存在一个模板注入漏洞，该漏洞由 Copilot Autofix 生成的修复代码引入，最终导致攻击者能够访问 Snowflake 的内部 Jira 环境。

**「影响」** 对于使用 GitHub Actions 和 AI 辅助编码的组织，此事件表明 AI 生成的代码修复可能引入安全漏洞，导致 CI/CD 管道和关联系统（如 Jira）被入侵。开发团队应强制对 AI 生成的代码进行静态分析和安全审查，以降低供应链攻击风险。

**「社区讨论」** 社区成员普遍认为，在 GitHub Actions 中使用静态分析工具（如 zizmor）是必要的，因为 AI 生成的代码同样需要质量检查。有评论指出，该漏洞的引入可能源于对现有工作流的简化重构，而 AI 生成的修复未能正确处理特殊字符。也有用户对 YAML 格式的复杂性表示不满，认为其容易导致安全陷阱。此外，有评论质疑漏洞是否真正由 Copilot 引入，因为相关 PR 中的提交并非全部由 AI 生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug">Red Agent Exploits Snowflake Vuln Missed by Github Copilot | Wiz Blog</a></li>
<li><a href="https://www.cyberkendra.com/2026/08/copilot-autofix-snowflake-jira-github-actions.html">Copilot Autofix Bug Exposed Snowflake&#x27;s Internal Jira - Cyber Kendra</a></li>
<li><a href="https://www.forbes.com/sites/timkeary/2026/08/17/github-copilot-missed-a-vulnerability-that-wizs-ai-agent-found/">Wiz’s AI Agent Finds A Vulnerability In Snowflake’s Internal Systems</a></li>

</ul>
</details>

**标签**: `#AI code generation`, `#security`, `#CI/CD`, `#GitHub Actions`, `#supply chain`

---

<a id="item-tech-news-6"></a>
### [AI;DR：AI 生成内容引发阅读疲劳与信任危机](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 7.0/10

一篇题为“AI;DR \(AI; Didn&\#x27;t Read\)”的文章探讨了 AI 生成内容泛滥的现象，以及人们日益不愿阅读此类内容的趋势。文章指出，在 2026 年，许多人认为在交流中直接发布 AI 生成的回复是不礼貌甚至令人反感的，因为读者希望听到的是作者本人的声音，而非模型的输出。社区评论中，有用户抱怨同事在代码审查中大量添加 AI 生成的文档和注释，导致代码库可读性下降；也有用户认为 AI 内容往往冗长、充满行话且过度自信，缺乏细微差别，从而削弱了阅读体验。文章引发了关于 AI 对沟通和软件工程文化影响的广泛讨论。

hackernews · mooreds · 8月17日 19:47 · [社区讨论](https://news.ycombinator.com/item?id=49336573)

**「背景」** 随着大型语言模型（LLM）的普及，AI 生成内容在互联网上迅速增加，从新闻文章到代码注释无所不包。这种趋势引发了关于内容真实性、作者身份和阅读价值的讨论。许多读者开始对 AI 生成的内容产生怀疑，认为其缺乏人类作者的独特见解和情感，同时可能包含不准确或空洞的表述。

**「影响」** 对于软件工程师和科技行业从业者，AI 生成内容的泛滥可能导致代码库可读性下降，增加维护成本，并削弱团队沟通的清晰度。此外，读者对 AI 内容的普遍不信任可能促使内容创作者更加注重原创性和个人声音，以避免被忽视。

**「社区讨论」** 社区评论普遍对 AI 生成内容持负面态度，认为其源于智力懒惰，且往往冗长、充满行话和过度自信。有用户建议，与其发送 AI 输出，不如分享生成它的提示词，因为提示词才包含真正的信息。也有用户抱怨同事在代码审查中大量使用 AI 生成的注释，导致代码库进入“后可读性”状态。

**标签**: `#AI-generated content`, `#communication`, `#software engineering`, `#community discussion`, `#technology culture`

---

<a id="item-tech-news-7"></a>
### [GPT 5.6 Sol 视觉模型评测：多数基准落后于 Gemini 3.5 Flash](https://blog.roboflow.com/openai-gpt-5-6/) ⭐️ 7.0/10

Roboflow 的基准评测显示，OpenAI 新发布的 GPT 5.6 Sol 视觉模型在多数任务上落后于 Gemini 3.5 Flash，仅在 OCR 任务中由 Fable 模型胜出。Gemini 3.5 Flash 不仅性能更优，而且成本仅为 GPT 5.6 Sol 的三分之一。尽管 GPT 5.6 Sol 在 UI 分析和 OCR 方面有一定优势，但整体上并非重大突破。社区评论指出，GPT 5.6 Sol 在视觉任务上表现不错，但高延迟和成本使其不适合高吞吐量场景。

hackernews · plurby · 8月17日 12:09 · [社区讨论](https://news.ycombinator.com/item?id=49329575)

**「背景」** GPT-5.6 Sol 是 OpenAI 于 2026 年 7 月发布的视觉模型，属于 GPT-5.6 系列中的一员，该系列还包括 Terra 和 Luna。Roboflow 的基准测试评估了这些模型在检测、计数、OCR 和提取等任务上的表现，并与 Gemini 3.5 Flash 等领先视觉语言模型进行了对比。

**「影响」** 对于需要高吞吐量视觉检测和计数的开发者，Gemini 3.5 Flash 仍是更经济高效的选择，而 GPT 5.6 Sol 可能更适合对延迟不敏感且需要精细 UI 分析的任务。

**「社区讨论」** 社区评论普遍认为 Roboflow 的总结过于保守，因为 GPT 5.6 Sol 在几乎所有基准上都被 Gemini 3.5 Flash 击败，且成本更高。有用户指出 GPT 5.6 Sol 在 UI 分析上表现出色，但也有用户质疑其延迟和成本不适合实际应用，并建议对比 Gemini 3 或 3.7 以更全面评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.roboflow.com/openai-gpt-5-6/">GPT 5.6 Sol is the best &quot;vision&quot; model OpenAI ever released</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#vision model`, `#benchmark`, `#GPT-5.6`, `#AI comparison`

---

<a id="item-tech-news-8"></a>
### [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 7.0/10

SineKAN 是一种 Kolmogorov-Arnold 网络（KAN）变体，使用正弦函数替代 B 样条作为激活函数。该研究已在 arXiv 上发表（arXiv:2407.04149），并提供了 GitHub 代码仓库（https://github.com/ereinha/SineKAN），同时还有一篇经过同行评审的正式论文发表于 MDPI 的《Mathematics》期刊（https://www.mdpi.com/2227-7390/13/19/3157）。这一工作表明，正弦激活函数在 KAN 架构中是可行的，为研究者提供了新的选择。尽管这属于对现有 KAN 的增量改进，而非重大突破，但它为探索不同激活函数在 KAN 中的表现提供了具体资源和参考。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**「背景」** Kolmogorov-Arnold 网络（KAN）是一种基于 Kolmogorov-Arnold 表示定理的神经网络架构，其核心思想是用可学习的激活函数替代传统的线性权重。原始 KAN 通常使用 B 样条作为激活函数，而 SineKAN 则尝试用正弦函数替代，以探索不同激活函数对网络性能的影响。

**「影响」** 对于研究 KAN 架构的机器学习研究者，SineKAN 提供了一种新的激活函数选择，并附有代码和同行评审论文，便于复现和进一步实验。

**标签**: `#Kolmogorov-Arnold Networks`, `#Activation Functions`, `#Machine Learning`, `#Neural Architecture`, `#Research`

---

<a id="item-tech-news-9"></a>
### [美团高管反思全员 AI 运动：日耗千万 Token，干扰真实经营](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 7.0/10

美团核心本地商业 CEO 王莆中在公开演讲中反思了公司内部的全员 AI 变革，称为期数月的“养虾运动”导致 AI 账单暴涨，每日消耗上千万元 Token，且产生的谬误干扰了真实经营。他指出 AI 落地难源于认知、效率、场景、考核四重错配，投入难以转化为可测量的生产力增长。王莆中透露，4 月起各事业部成立 AI 组织，6、7 月通过赛马机制明确 AI 转型是业务、组织、技术三位一体的系统工程，7 月 AI 初步在内部产品流程中跑通并产生价值。这一反思揭示了大型科技公司在 AI 应用中的实际挑战和调整过程。

telegram · zaihuapd · 8月17日 02:09

**「背景」** “养虾运动”是美团内部对全员使用 AI 工具的戏称，指公司鼓励所有员工在日常工作中大量使用 AI，以推动 AI 技术的普及和应用。然而，这种大规模使用导致了高昂的 Token 消耗成本，并可能因 AI 生成的不准确内容干扰正常业务运营。王莆中的反思反映了企业在 AI 转型中常见的“重投入、轻效果”问题。

**「影响」** 这一反思对美团内部 AI 战略具有直接影响，促使公司从全员盲目使用转向有组织的 AI 应用，并强调业务、组织、技术的协同。对其他企业而言，这是一个警示案例，表明 AI 投入需要与业务目标对齐，否则可能造成资源浪费和运营干扰。

**标签**: `#AI adoption`, `#Meituan`, `#LLM costs`, `#tech industry`, `#organizational change`

---

<a id="item-tech-news-10"></a>
### [宇树预告人形机器人“超人”：原地跳高 2 米破人类纪录](https://m.weibo.cn/detail/5332901463070926) ⭐️ 7.0/10

宇树科技发布人形机器人新机“超人”的预告，宣称其原地跳高达到 2 米，极限速度达到 12.66 米/秒（腿长 0.85 米），均超越全人类原地跳高与奔跑速度纪录。官方表示，这款全新整机仅用 3 个多月研发完成，未来几个月仍有较大完善空间。目前该消息仅为预告，尚未公布完整技术细节。

telegram · zaihuapd · 8月17日 07:12

**「背景」** 宇树科技是中国领先的人形机器人与四足机器人企业，其产品如售价 9.9 万元起的 G1 已实现量产，并推出了轻量化 R1 和全尺寸仿生人形机器人等型号。市场研究机构 Omdia 预计 2025 年全球人形机器人总出货量约 1.3 万台，但高盛报告指出当前机器人能力有限，放量速度可能慢于预期。此次预告的“超人”新机，是宇树在运动能力上的又一次突破性展示。

**「影响」** 若性能属实，该机器人将刷新人类与机器人运动能力的天花板，对仿生运动控制、高功率密度驱动等机器人技术领域具有标杆意义，并可能推动人形机器人在工业、物流等场景的应用。但作为预告，实际性能与量产能力仍需后续验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stock.10jqka.com.cn/20250302/c666402515.shtml">stock.10jqka.com.cn/20250302/c666402515.shtml</a></li>
<li><a href="https://m.gelonghui.com/p/3896766">宇 树 领跑、智元另辟蹊径：争一背后， 人 形 机 器 人 也需面临商业化大考</a></li>
<li><a href="https://www.tmtpost.com/7928956.html">人 形 机 器 人 这么“卷”， 宇 树 再不上市就晚了-钛媒体官方网站</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid-robot`, `#unitree`, `#AI`, `#hardware`

---

<a id="item-tech-news-11"></a>
### [苹果调整 ATT 授权规则以回应德国监管裁决](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

德国监管机构裁定苹果的 App 追踪透明度框架（ATT）对自家应用更有利，涉嫌违反竞争规则，要求苹果在裁决送达后四个月内调整 iPhone 和 iPad 上应用开发者使用个人数据投放定向广告的规则。苹果须确保第三方授权弹窗保持中立，去除劝阻性措辞和符号，且该承诺有效期为七年。此前，法国和意大利已分别对苹果处以 1.5 亿欧元和 9860 万欧元的罚款。这一裁决结束了多年调查，将影响所有 iOS 应用的广告追踪授权流程。

telegram · zaihuapd · 8月17日 12:50

**「背景」** 苹果的 App 追踪透明度（ATT）框架自 2021 年推出以来，要求应用在追踪用户或访问设备广告标识符（IDFA）前必须获得用户明确许可。该框架因默认弹窗提示可能劝阻用户同意，被批评为对苹果自身广告业务有利。此前，法国和意大利监管机构已分别对苹果处以 1.5 亿欧元和 9860 万欧元的罚款，而德国联邦卡特尔办公室（Bundeskartellamt）的此次裁决进一步要求苹果在四个月内调整弹窗设计，使其在内容、措辞和布局上保持中立，并去除可能劝阻用户的符号和警告。

**「影响」** 对于依赖 ATT 弹窗获取用户追踪授权的第三方应用开发者，其授权流程将被迫调整，可能影响广告收入；苹果自家广告业务在授权环节的优势将被削弱，但具体市场影响尚待观察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appleinsider.com/articles/26/08/17/how-german-regulators-are-cracking-down-on-app-tracking-transparency">How German regulators are cracking down on App Tracking Transparency</a></li>
<li><a href="https://www.macrumors.com/2026/08/17/apple-app-tracking-transparency-changes-germany/">Apple Agrees to Make &#x27;App Tracking Transparency&#x27; Changes in Germany - MacRumors</a></li>
<li><a href="https://www.theverge.com/tech/980977/apple-app-tracking-transparency-settlement-germany">Apple ordered to stop scaring iPhone and iPad users away from third-party apps | The Verge</a></li>

</ul>
</details>

**标签**: `#apple`, `#privacy`, `#regulation`, `#app-tracking-transparency`, `#ad-tech`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM-Omni 分布式分层卸载：高效扩展至 200B+ DiT 模型](https://vllm.ai/blog/2026-08-17-distributed-layerwise-offload) ⭐️ 9.0/10

rss · vLLM Blog · 8月17日 00:00

**「背景」** 大型扩散模型（如 Cosmos3-Super，64B 参数，124 GB）无法装入单设备 HBM，现有方案各有局限：HSDP 会填满 HBM，传统分层卸载则导致主机内存随设备数线性增长（4 设备需 4×124 GB），且加载时 RSS 峰值可达 O\(dp\_size × model\_size\)。

**「方案」** vLLM-Omni 的分布式分层卸载（DLO）通过四项协同技术解决内存瓶颈：首先，使用 meta 设备初始化和 mmap 权重加载，将权重映射到共享 OS 页缓存，消除私有副本，使冷启动 cgroup 可见峰值降低 73%（178 GB → 47 GB）。其次，权重分片（每 rank 仅存 1/dp\_size）并通过 AllGather 在运行时重建完整层，将总固定内存从 dp\_size × model\_size 降至 model\_size。第三，双缓冲预取机制确保每设备仅保留两层权重，HBM 占用与层数无关，实测 720p 10s 工作负载下峰值 HBM 仅从 23.1 GB 增至 28.1 GB（模型增大 3.8 倍）。最后，DP 多并发允许每个 rank 并行处理不同请求，实现 3.3× 吞吐量（约为理想 4× 的 83%）。在 Ascend NPU 上，pin\_memory 通过 /dev/davinci\_manager 分配 DMA 内存，cgroup 不可见，因此 cgroup 峰值按 O\(model\_size + dp\_size × constant\) 缩放，但物理 RAM 需计入该部分。验证显示 DLO+AG DP4 在 1024×1024 T2I 任务中吞吐量比 HSDP+USP4 高 1.39 倍，HBM 仅用 30%；在 720p 10s 任务中延迟接近 HSDP（差 2.13%），HBM 仅用 47%。MiniMax-H3 在 8× B300 上的拓扑研究表明，最佳 DLO 模式取决于 DP/SP 配置：DP1×SP8 用 AllGather，DP8×SP1 用 rank-local，吞吐量达 183.78 videos/h，能耗 43.97 Wh/video。作者强调这些结果是拓扑研究而非普适结论，且 400 GB 外推仅为估算，未经实际验证。

**「启示」** 作者认为，通过结合 mmap 加载、权重分片、双缓冲和 DP 并发，DLO 使 200B+ DiT 模型在有限主机内存下高效运行成为可能，同时揭示了内存计账（如 cgroup 与物理 RAM 差异）和集体通信同步约束等关键陷阱，这些经验对大规模分布式推理具有普遍参考价值。

**标签**: `#distributed inference`, `#memory optimization`, `#diffusion models`, `#vLLM`, `#NPU/GPU`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [珍妮·巴斯反对出售湖人队家族股份](https://www.cnbc.com/2026/08/17/jeanie-buss-opposes-sale-family-stake.html) ⭐️ 7.0/10

洛杉矶湖人队老板珍妮·巴斯通过律师致函其兄弟姐妹，反对出售家族持有的湖人队 17.8%股份，称任何未经她同意的出售投票均属无效。此前有报道称，鲍勃·艾格和约书亚·库什纳同意以 125 亿美元估值收购球队多数股权，但珍妮·巴斯希望保留股份以维持其控制人地位。

rss · CNBC Finance · 8月17日 22:31

**「背景」** 珍妮·巴斯是洛杉矶湖人队的老板和少数股权所有者。2017 年，法院裁定她为球队的控股所有者，这源于其父亲杰里·巴斯去世后家族内部的权力斗争。

**「影响」** 这一争议可能影响湖人队所有权的最终归属，若珍妮·巴斯成功阻止出售，艾格和库什纳的收购计划将受阻，球队控制权仍将留在巴斯家族手中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jeanie_Buss">Jeanie Buss - Wikipedia</a></li>
<li><a href="https://talbotlawpc.com/blog/2017/4/9/jeannie-buss-retains-control-over-the-la-lakers">Jeannie Buss Retains Control Over the L.A. Lakers - Talbot Law...</a></li>

</ul>
</details>

**标签**: `#Los Angeles Lakers`, `#Jeanie Buss`, `#sports business`, `#ownership dispute`, `#mergers and acquisitions`

---

<a id="item-finance-news-2"></a>
### [Synchrony 与 OpenAI 合作，允许在 ChatGPT 内使用商店卡购物](https://www.cnbc.com/2026/08/17/synchrony-openai-chatgpt-shopping.html) ⭐️ 7.0/10

Synchrony Financial，这家为亚马逊、沃尔玛和 Lowe&\#x27;s 等品牌发行信用卡的公司，正在与 OpenAI 合作，使购物者能够直接在 ChatGPT 内使用其商店卡购买产品。这是美国消费金融公司首次将融资、支付和奖励功能集成到 AI 聊天机器人中。

rss · CNBC Finance · 8月17日 18:32

**「背景」** Synchrony Financial 是美国最大的零售信用卡发行商之一，为亚马逊、沃尔玛等品牌提供商店卡。目前，消费者在 AI 聊天机器人中发现商品后，通常仍需跳转到品牌网站完成购买。OpenAI 已与 Visa、Stripe 等公司合作，推动在 ChatGPT 内直接完成交易。

**「影响」** 这一合作可能影响使用 Synchrony 商店卡的消费者，使他们能够在 AI 聊天机器人中直接完成购买，而无需跳转到品牌网站。同时，这也可能改变零售商、Synchrony 和 OpenAI 之间的费用分配方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/ai/articles/synchrony-financial-partners-openai-chatgpt-171341998.html">Synchrony Financial partners with OpenAI for ChatGPT shopping</a></li>
<li><a href="https://www.msn.com/en-us/technology/ecommerce/credit-card-issuer-synchrony-partners-with-openai-for-chatgpt-shopping/ar-AA2aj6v3">Credit card issuer Synchrony partners with OpenAI for ChatGPT ...</a></li>

</ul>
</details>

**标签**: `#fintech`, `#AI commerce`, `#credit cards`, `#OpenAI`, `#Synchrony`

---

<a id="item-finance-news-3"></a>
### [Stripe 据悉以超 70 亿美元收购 AI 模型平台 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 7.0/10

据知情人士透露，支付公司 Stripe 已与 AI 模型访问平台 OpenRouter 达成收购协议，交易金额超过 70 亿美元，但最终价格仍可能变动。OpenRouter 成立于 2023 年，为开发者提供超过 400 个 AI 模型的访问服务，并于今年 5 月称已服务 800 万名开发者。

telegram · zaihuapd · 8月17日 01:19

**「背景」** OpenRouter 是一个 AI 模型聚合平台，开发者可通过其统一接口访问多种 AI 模型。Stripe 是一家在线支付处理公司，此次收购旨在扩展其在 AI 基础设施领域的布局。

**「影响」** 若交易完成，OpenRouter 的开发者用户群可能受益于 Stripe 的支付基础设施，同时 Stripe 将增强在 AI 开发者生态中的竞争力。

**标签**: `#M&amp;A`, `#AI infrastructure`, `#Stripe`, `#OpenRouter`, `#fintech`

---

<a id="item-finance-news-4"></a>
### [宇树科技将于 8 月 19 日科创板上市，发行价 150.8 元](https://wap.eastmoney.com/a/202608173843415437.html) ⭐️ 7.0/10

宇树科技（688836.SH）公告，其股票将于 2026 年 8 月 19 日在上海证券交易所科创板上市，发行价为每股 150.80 元，对应 2025 年摊薄后静态市销率 35.89 倍，高于可比公司平均水平。

telegram · zaihuapd · 8月17日 13:20

**「背景」** 宇树科技是一家专注于人形机器人研发的公司，被称为“A 股人形机器人第一股”。此次发行价对应的市盈率（衡量股价与每股收益比值的指标）高达 219.23 倍，远高于所属行业平均的 38.56 倍，显示市场对其高增长预期。

**「影响」** 此次上市将为宇树科技筹集资金，并使其股票在公开市场交易，投资者可参与申购和交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1060472511_122502583">宇树科技发行价落定！150.80元/股，219倍PE，8月10日启动申购</a></li>
<li><a href="https://stock.jrj.com.cn/2026/08/06193258033858.shtml">中一签需缴款7.54万！宇树科技IPO定价150.8元，219倍PE，8月10日下周...</a></li>

</ul>
</details>

**标签**: `#IPO`, `#Unitree Robotics`, `#STAR Market`, `#valuation`, `#robotics`

---