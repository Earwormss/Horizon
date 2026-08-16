---
layout: default
title: "Horizon Summary: 2026-08-16 (EN / ZH)"
date: 2026-08-16
lang: en
---

> Selected 11 important items from 33 fetched items. Each English entry is followed by its Chinese version.

---

## Technology News / 科技新闻

**English**

<a id="bilingual-item-1-en"></a>
### [Anthropic Publishes Claude System Prompts for Transparency](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic has published the system prompts for its Claude models on the platform documentation site, allowing public scrutiny of the instructions that shape model behavior. The release includes prompts for models such as Opus 4.8 and Opus 5, with notable additions like a directive that Claude should verify whether an image is actually present rather than assuming from prompt wording. Community members, including Simon Willison, have created git history repositories to track changes between versions, highlighting the value for developers and researchers. This transparency move offers deep insight into the operational guardrails and behavioral priorities of a leading AI model, though it is not a technical breakthrough itself.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**「Background」** System prompts are the initial instructions given to an AI model at the start of a conversation, shaping its behavior and providing context such as the current date. Since August 2024, Anthropic has published the system prompts for its Claude models as part of its official documentation, updating them with each model release and logging changes at docs.claude.com/en/release-notes/system-prompts. This transparency allows developers and researchers to examine how the model is guided, as seen in community analyses like Simon Willison&\#x27;s git history of prompt changes.

**「Impact」** Developers and researchers using Claude can now better understand and anticipate model behavior, enabling more effective prompt engineering and safety analysis. The public availability of system prompts also sets a precedent for transparency in the AI industry, potentially influencing other providers to follow suit.

**「Community Discussion」** Community members appreciate the transparency, with Simon Willison providing a git history of prompt changes for easier diffing. Some express skepticism about the effectiveness of system prompts for powerful models, noting that basic common sense instructions may not fully address underlying issues. Others see the prompts as a window into Anthropic&\#x27;s roadmap and behavioral priorities, such as prioritizing user wellbeing in crisis situations.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://tactiq.io/learn/claude-system-prompt">Claude System Prompt Explained: What&#x27;s Inside and Why It Matters</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#system prompts`, `#AI transparency`, `#LLM`

**中文**

<a id="bilingual-item-1-zh"></a>
### [Anthropic 公开 Claude 系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 在 Claude 平台文档中发布了 Claude 模型的系统提示词，使公众能够审查和分析模型行为。这一透明度举措受到开发者社区欢迎，Simon Willison 甚至将这些提示词整理成 Git 提交历史，便于追踪版本间变化。例如，Opus 4.8 与 Opus 5 之间的差异显示，新提示词加入了关于 Claude Fable 5 和 Claude Mythos 5 的说明。系统提示词还包含一些行为准则，如当用户处于危机或表达痛苦时，Claude 优先考虑其福祉而非完成任务。这些提示词是塑造模型行为的分层系统的一部分，反映了 Anthropic 对模型未来行为的规划。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**「背景」** Anthropic 自 2024 年 8 月起，在其官方文档中随每次模型发布公开 Claude 的系统提示词，并记录在发布说明中。系统提示词是对话开始时提供给模型的一段指令，包含当前日期、行为规范（如代码用 Markdown 格式）等信息，用于引导模型行为。

**「影响」** 对于开发者、研究人员和 AI 伦理关注者而言，公开系统提示词提供了前所未有的视角，有助于理解 Claude 的行为机制和 Anthropic 的设计意图，可能促进更广泛的 AI 透明度和责任性讨论。

**「社区讨论」** 社区成员 Simon Willison 创建了 Git 仓库来追踪提示词变更，并指出 Opus 4.8 到 Opus 5 的差异中新增了关于 Claude Fable 5 和 Claude Mythos 5 的说明。有用户质疑通过系统提示词强制模型检查图像是否真的存在，认为这反映了 Anthropic 对模型智能的局限看法。另有用户担忧论坛可能移除对 AI 有负面影响的帖子，但此观点与主题无关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://tactiq.io/learn/claude-system-prompt">Claude System Prompt Explained: What&#x27;s Inside and Why It Matters</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#system prompts`, `#AI transparency`, `#LLM`

---

**English**

<a id="bilingual-item-2-en"></a>
### [AI Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

The article argues that AI models are intentionally becoming less knowledgeable in favor of tool use and external knowledge, a shift with major implications for AI system design. It highlights that models like Gemini 2.5 Pro score only 53% on SimpleQA, a benchmark of factual recall with no tools allowed, indicating that even the best recall misses half the questions. The trend suggests that model weights will store less factual knowledge, relying instead on external tools and knowledge bases, which could reduce hallucinations but also change how models are evaluated. The article notes that this shift may lead to model cards no longer listing knowledge cutoffs, as the knowledge in weights becomes stale on a scale of years instead of weeks. This represents a significant change in model architecture, moving from storing facts in weights to leveraging external resources.

hackernews · hruvhwe · Aug 16, 19:04 · [Discussion](https://news.ycombinator.com/item?id=49322695)

**「Background」** Large language models traditionally store factual knowledge in their weights, which leads to issues like knowledge cutoffs and hallucinations. The article discusses a shift toward models that rely on external tools and knowledge bases instead of memorizing facts. Recent developments, such as Cactus&\#x27;s Needle 2, a 14MB model focused on tool calling, illustrate this trend toward smaller, tool-oriented models.

**「Impact」** This shift will affect developers and organizations that rely on LLMs for factual recall, as they will need to integrate external knowledge bases and tool-calling capabilities to maintain accuracy, potentially reducing hallucinations but also introducing new dependencies on external systems.

**「Community Discussion」** Commenters discuss the potential for pluggable knowledge bases, where models can be customized with specific knowledge domains, and note recent examples like Cactus&\#x27;s Needle, a 14 MB tool-calling model. Some question whether reasoning and facts are truly separable, arguing that reasoning about human behavior requires factual context. Others point out that the article&\#x27;s data is outdated, as Gemini 2.5 Pro is sixteen months old and SimpleQA hasn&\#x27;t been updated in a long time.

<details><summary>References</summary>
<ul>
<li><a href="https://cactuscompute.com/needle">Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus</a></li>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for ...</a></li>
<li><a href="https://www.marktechpost.com/2026/08/13/cactus-compute-needle-2-45m-parameter-tool-calling-model/">Meet Needle 2: An Open 45M-Parameter Tool-Calling Model That ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLMs`, `#model architecture`, `#knowledge bases`, `#hallucination`

**中文**

<a id="bilingual-item-2-zh"></a>
### [模型正有意变得更笨：转向工具与外部知识](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

文章指出，AI 模型正有意减少参数中存储的事实知识，转而依赖外部工具和知识库，这一趋势对模型架构、幻觉问题和知识截止日期产生深远影响。作者认为，将事实从权重中移出可降低幻觉率，但也会使模型在无工具环境下表现更差。社区评论指出，SimpleQA 基准已过时，Gemini 2.5 Pro 并非当前最佳模型，并提及 Cactus 公司推出的 14MB 工具调用模型 Needle，以及可插拔知识库的设想。这一转变意味着模型卡可能不再列出知识截止日期，因为权重中的知识会以年为单位过时。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**「背景」** 大型语言模型（LLM）传统上通过将事实知识编码进模型权重来存储信息，这导致模型存在知识截止日期和幻觉问题。近期，业界出现一种趋势，即模型不再依赖内部存储的事实，而是转向通过工具调用和外部知识库来获取信息。例如，Cactus 公司发布了 Needle 2，一个仅 45M 参数、14MB 大小的开源模型，专门用于工具调用和设备使用，这体现了模型小型化与外部工具结合的设计方向。

**「影响」** 对于依赖模型内置知识的开发者，这一趋势意味着需要重新设计系统，集成外部工具和知识检索，否则模型在无工具环境下的事实回答能力将下降。

**「社区讨论」** 社区对可插拔知识库表示期待，认为模型无需内置所有知识，可按需组合。同时，有评论指出文章引用的基准数据过时，并质疑推理与事实是否真正分离，认为推理需要基于事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cactuscompute.com/needle">Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus</a></li>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for ...</a></li>
<li><a href="https://www.marktechpost.com/2026/08/13/cactus-compute-needle-2-45m-parameter-tool-calling-model/">Meet Needle 2: An Open 45M-Parameter Tool-Calling Model That ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#model architecture`, `#knowledge bases`, `#hallucination`

---

**English**

<a id="bilingual-item-3-en"></a>
### [Qwen 3.8 27B: Strong but Overthinks by Default](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Simon Willison reviews Qwen 3.8 27B, an Apache 2 licensed 27B parameter vision-capable LLM from Alibaba&\#x27;s Qwen lab, noting its strong performance and self-reported benchmark improvements over both Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus. However, the model defaults to an &\#x27;xhigh&\#x27; reasoning effort, causing it to overthink even simple tasks, consuming excessive tokens and time. For example, generating an SVG of a pelican on a bicycle took 21 minutes and 22,276 reasoning tokens, while turning off reasoning reduced it to 137 seconds. Willison recommends running the model with low or no reasoning settings initially, and notes that it performs well on tasks like bounding boxes. He tested it on a 128GB M5 Max MacBook Pro and an NVIDIA DGX Spark using LM Studio&\#x27;s 17GB Q4\_K\_M quantized build.

rss · Simon Willison · Aug 16, 22:00

**「Background」** Qwen 3.8 27B is an Apache 2.0-licensed, 27-billion-parameter vision-capable large language model released by Alibaba&\#x27;s Qwen research lab. It is the successor to Qwen 3.6 27B and is designed to run on consumer hardware, such as a laptop with sufficient RAM. The model supports a configurable &\#x27;reasoning\_effort&\#x27; parameter with levels including &\#x27;xhigh&\#x27; \(default\), &\#x27;medium&\#x27;, and &\#x27;low&\#x27;, which controls the depth of reasoning and associated computational cost. This parameter is part of Qwen&\#x27;s approach to balancing accuracy and speed, and it significantly affects the model&\#x27;s behavior and output quality.

**「Impact」** Users running Qwen 3.8 27B on consumer hardware should disable or lower the default &\#x27;xhigh&\#x27; reasoning effort to avoid excessive latency and token usage, as the default can make even simple prompts take minutes. The model&\#x27;s strong performance at lower reasoning levels makes it a practical choice for local deployment, but the default setting undermines usability.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#open-source`, `#AI`, `#benchmarks`

**中文**

<a id="bilingual-item-3-zh"></a>
### [Qwen 3.8 27B 评测：性能出色但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

Simon Willison 评测了阿里巴巴 Qwen 实验室新发布的 Apache 2.0 许可的 27B 参数视觉语言模型 Qwen 3.8 27B。该模型自称在基准测试中优于其前代 Qwen 3.6 27B 以及闭源的 Qwen 3.7-Plus，但 Willison 发现其默认的推理强度设置为 xhigh，导致模型在简单任务上过度思考，例如生成一个 SVG 圆形的请求会触发数分钟的推理并产生一个动画圆。在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上，使用 LM Studio 的 17GB Q4\_K\_M 量化版本，xhigh 设置下生成一个鹈鹕骑自行车的 SVG 耗时 21 分钟，使用 22,276 个推理 token 和 3,223 个输出 token；关闭推理后仅需 137 秒。Willison 建议用户忽略默认设置，从 low 或关闭推理开始使用，并指出该模型在边界框任务上表现出色。

rss · Simon Willison · 8月16日 22:00

**「背景」** Qwen 3.8 27B 是阿里巴巴 Qwen 研究实验室于 2026 年 8 月发布的开源（Apache 2.0）视觉语言模型，拥有 270 亿参数，其前代 Qwen 3.6 27B 已表现出色。该模型支持通过 reasoning\_effort 参数调节推理深度，默认设置为 xhigh，旨在处理复杂任务，但会导致过度思考。模型在 Hugging Face 上提供 55.6GB 的完整检查点，LM Studio 提供 17GB 的 Q4\_K\_M 量化版本。

**「影响」** 对于在消费级硬件上运行 Qwen 3.8 27B 的用户，默认的 xhigh 推理设置会导致极长的生成时间和上下文窗口耗尽，因此必须手动调整推理强度或增加上下文长度才能获得实用性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/">Qwen3.8-27B: Specs, Benchmarks &amp; Verdict</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Qwen`, `#open-source`, `#AI`, `#benchmarks`

---

**English**

<a id="bilingual-item-4-en"></a>
### [US Grid&\#x27;s $12B Modeling Mistake Risks Repeating](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

An in-depth analysis by SemiAnalysis reveals that flawed modeling in the US power grid has led to a $12 billion waste of ratepayer funds, and the PJM Interconnection is at risk of repeating the same mistake. The article, authored by Robert Boswall, details how incorrect assumptions in grid planning models caused significant financial losses and highlights systemic risks if these modeling errors are not corrected. The analysis underscores the urgent need for improved modeling practices to prevent further waste and protect ratepayers. The piece combines technical depth on modeling flaws with substantial financial and societal impact, making it a critical read for those involved in energy systems and infrastructure.

rss · Semianalysis · Aug 16, 22:27

**「Background」** PJM Interconnection is the regional transmission organization that operates the electricity grid for 13 states in the Mid-Atlantic and Midwest, serving about 65 million people. In 2024, PJM&\#x27;s capacity market auction used flawed modeling assumptions about electricity supply, which led to a $12 billion increase in costs for ratepayers. The Union of Concerned Scientists filed a complaint with the Federal Energy Regulatory Commission \(FERC\) to prevent a repeat of this costly error, and PJM has proposed a reliability backstop procurement that some state advocates warn could again raise ratepayer costs.

**「Impact」** US ratepayers have already borne a $12 billion cost due to modeling errors, and if PJM proceeds with similar flawed models, they face additional financial losses and potential grid reliability issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.rtoinsider.com/138882-maryland-fears-pjm-backstop-effort-could-raise-ratepayer-costs/">Maryland Ratepayers at Risk from PJM Backstop, Advocate Says</a></li>

</ul>
</details>

**Tags**: `#power grid`, `#modeling`, `#infrastructure`, `#energy systems`, `#systems engineering`

**中文**

<a id="bilingual-item-4-zh"></a>
### [美国电网建模失误浪费 120 亿美元，PJM 拟重蹈覆辙](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 8.0/10

据 SemiAnalysis 分析，美国电网因建模错误导致纳税人资金浪费高达 120 亿美元，而负责运营的 PJM 公司正计划再次采用类似的有缺陷模型，可能引发新的财务风险。文章指出，这些模型未能准确反映电网实际运行条件，导致投资决策失误和资源错配。分析强调，若不改进建模方法，类似的高昂代价将不可避免。该问题涉及电力系统建模、基础设施投资和公共资金管理，对能源行业和监管机构具有重要警示意义。

rss · Semianalysis · 8月16日 22:27

**「背景」** PJM 是美国最大的区域输电组织之一，负责协调美国东部多个州的电力批发市场。2024 年，PJM 因在容量市场建模中采用了不恰当的电力供应假设，导致容量价格飙升，使消费者多支付了约 120 亿美元。美国忧思科学家联盟（UCS）等机构对此提出投诉，要求 PJM 纠正规则，避免类似成本再次发生。此外，PJM 还提议引入可靠性后备采购机制，但马里兰等州的费率倡导者担心这可能进一步推高消费者成本。

**「影响」** 对于美国电力用户和纳税人，这一建模失误已造成 120 亿美元的直接经济损失，且 PJM 若继续使用类似模型，未来可能再次导致巨额浪费，影响电价和电网可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.rtoinsider.com/138882-maryland-fears-pjm-backstop-effort-could-raise-ratepayer-costs/">Maryland Ratepayers at Risk from PJM Backstop, Advocate Says</a></li>

</ul>
</details>

**标签**: `#power grid`, `#modeling`, `#infrastructure`, `#energy systems`, `#systems engineering`

---

**English**

<a id="bilingual-item-5-en"></a>
### [SSOG-Attention: Sub-quadratic Attention via Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention introduces a novel attention mechanism that replaces the quadratic complexity of standard scaled dot-product attention \(SDPA\) with a sub-quadratic approach using a sum of separable Gaussians. By learning a few Gaussian atoms per head and steering them based on the query token, the method reduces complexity from O\(N²·d\) to O\(N·√N·d\). Experiments reported by the author show that SSOG outperforms SDPA on CIFAR-100 and achieves equivalent performance with faster convergence on ImageNet \(IN1k\), while being more memory-efficient at larger scales. The project includes a blog post and a public repository, with the author noting that AI was used for some code and writing but that they stand behind the work.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**「Background」** Standard vision transformers use scaled dot-product attention \(SDPA\), which computes similarity scores between every pair of tokens, leading to O\(N²·d\) complexity. SSOG \(Sum of Separable Gaussians\) replaces this content-scored attention with a learned geometric field: each attention head uses a few Gaussian atoms over relative position, with small bounded nudges that let content steer the field without scoring every token. This factorization reduces complexity to O\(N·√N·d\).

**「Impact」** For researchers and practitioners working on efficient transformers, especially in computer vision, SSOG offers a concrete alternative to SDPA that could enable scaling to longer sequences with lower computational and memory costs, though these results are from the author&\#x27;s own experiments and not yet peer-reviewed.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>

</ul>
</details>

**Tags**: `#attention mechanism`, `#efficient transformers`, `#computer vision`, `#machine learning`, `#scalability`

**中文**

<a id="bilingual-item-5-zh"></a>
### [SSOG-Attention：可分离高斯和实现亚二次复杂度注意力机制](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

SSOG-Attention 提出了一种新的注意力机制，通过可分离高斯和（Sum Of Separable Gaussians）替代标准缩放点积注意力（SDPA），将计算复杂度从 O\(N²·d\) 降低到 O\(N·√N·d\)。该方法为每个注意力头学习少量高斯原子，并根据查询令牌几何调整它们，从而在保持性能的同时提升效率。实验表明，在 CIFAR-100 上 SSOG 明显优于 SDPA，在 ImageNet（IN1k）上性能相当且收敛更快，同时随着规模增大，速度和内存效率优势更加显著。该研究由作者发布在 Reddit 上，并提供了博客文章和代码仓库，但尚未经过同行评审。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**「背景」** 标准视觉 Transformer 中的缩放点积注意力（SDPA）会为每个查询令牌计算与所有图像令牌的相似度得分，导致计算复杂度为 O\(N²·d\)。SSOG（可分离高斯和）则用一组可学习的几何高斯原子替代内容评分，每个注意力头仅包含少量高斯原子，并通过查询令牌进行几何引导，从而将复杂度降至 O\(N·√N·d\)。

**「影响」** 对于需要处理长序列或高分辨率图像的 Transformer 模型开发者，SSOG-Attention 提供了一种可扩展的注意力替代方案，能在保持与 SDPA 相当性能的同时显著降低计算和内存开销，尤其适用于资源受限或大规模部署场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/4rtemi5/ssog/blob/main/README.md">ssog/README.md at main · 4rtemi5/ssog · GitHub</a></li>

</ul>
</details>

**标签**: `#attention mechanism`, `#efficient transformers`, `#computer vision`, `#machine learning`, `#scalability`

---

**English**

<a id="bilingual-item-6-en"></a>
### [Cloudflare silently injects analytics when switching nameservers](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

A Hacker News user reported that after switching nameservers to Cloudflare to enable R2 bucket serving on a custom subdomain, Cloudflare silently injected a JavaScript analytics snippet into their HTML-only, JS-free site textlog.cc. The user had to manually navigate to the Analytics dashboard, add the site, and then disable the snippet, criticizing the lack of opt-in consent. Community members confirmed the behavior, noting the injected script from static.cloudflareinsights.com and suggesting a Content-Security-Policy meta tag as a workaround. The issue appears to affect sites using Cloudflare&\#x27;s proxy, as users with DNS-only setups did not see the injection.

hackernews · stagas · Aug 16, 17:49

**「Background」** Cloudflare is a content delivery network \(CDN\) and DNS provider that also offers a suite of web services, including Web Analytics. When a site owner switches their domain&\#x27;s nameservers to Cloudflare, the domain is managed through Cloudflare&\#x27;s DNS, and if the site is proxied through Cloudflare \(orange-clouded\), Cloudflare can modify the HTML responses to inject scripts. Web Analytics is a privacy-focused analytics service that Cloudflare offers, and it appears that for some users, it is enabled by default when they start using Cloudflare&\#x27;s proxy, requiring manual opt-out. This behavior has been noted in Cloudflare&\#x27;s own blog post about Web Analytics, which discusses how the feature works and how to control it.

**「Impact」** Web developers and site owners who switch to Cloudflare&\#x27;s proxy may unknowingly have analytics scripts injected into their sites, affecting privacy and site performance, and requiring manual opt-out. Users can mitigate this by using a Content-Security-Policy to block external scripts or by ensuring they use DNS-only mode if they do not need Cloudflare&\#x27;s proxy.

**「Community Discussion」** Commenters confirmed the injection and provided technical workarounds, such as using a Content-Security-Policy meta tag to restrict script sources. Some noted that the injection only occurs when Cloudflare is used as a proxy, not for DNS-only setups, and referenced Cloudflare&\#x27;s blog post about enabling web analytics.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49322107">Tell HN: Cloudflare silently injects its analytics when you switch ...</a></li>
<li><a href="https://zeli.app/en/story/49322107">Cloudflare silently injects analytics into your site when you switch ...</a></li>
<li><a href="https://upstract.com/x/ad8b6c184f3818b7">Tell HN: Cloudflare silently injects its analytics when you switch ...</a></li>

</ul>
</details>

**Tags**: `#cloudflare`, `#privacy`, `#web-analytics`, `#dns`, `#security`

**中文**

<a id="bilingual-item-6-zh"></a>
### [Cloudflare 在切换域名服务器时静默注入分析脚本](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

一位用户报告称，在将域名服务器切换到 Cloudflare 以启用 R2 存储桶服务后，Cloudflare 静默地向其纯 HTML 网站注入了 JavaScript 分析脚本。该用户必须手动进入分析仪表板，添加网站，然后禁用脚本，这引发了关于默认选择加入而非选择退出的隐私担忧。社区成员提供了技术解决方案，如使用内容安全策略（CSP）来阻止外部脚本，并指出 Cloudflare 的博客文章讨论了此行为。其他用户确认在代理模式下看到了类似脚本，而 DNS-only 设置的用户则未观察到注入。

hackernews · stagas · 8月16日 17:49

**「背景」** Cloudflare 是一家提供 CDN、DNS 和安全服务的公司，其 Web Analytics 功能默认会向网站注入一段 JavaScript 脚本，用于收集访问数据。当用户将域名服务器切换到 Cloudflare 时，该功能可能被自动启用，而无需用户明确同意。

**「影响」** 使用 Cloudflare 代理的网站所有者可能会在不知情的情况下向其站点注入分析脚本，这可能导致隐私问题并影响页面性能。用户可以通过配置 CSP 或手动禁用 Cloudflare 分析来缓解此问题。

**「社区讨论」** 社区成员提供了技术解决方案，如使用 CSP 限制脚本来源，并分享了 Cloudflare 博客文章的链接，该文章解释了 Web Analytics 的启用过程。一些用户确认在代理模式下看到了注入的脚本，而 DNS-only 设置的用户则未观察到，这表明该行为与 Cloudflare 的代理服务相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49322107">Tell HN: Cloudflare silently injects its analytics when you switch ...</a></li>
<li><a href="https://zeli.app/en/story/49322107">Cloudflare silently injects analytics into your site when you switch ...</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#privacy`, `#web-analytics`, `#dns`, `#security`

---

**English**

<a id="bilingual-item-7-en"></a>
### [Solving Long-Range Recall in Linear Attention for DNA](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

A researcher working on DNA sequence modeling reports that linear attention models, which are necessary for handling sequences up to 1M tokens due to the prohibitive cost of softmax attention, perform poorly on long-range recall tasks. On a Needle in a Haystack-style benchmark with a four-token DNA vocabulary \(A/C/G/T\), their model achieved around 25% accuracy, essentially random chance, and a small 16K-context variant only reached 50–60%. The same benchmark gave HyenaDNA only 25–27%, indicating the issue is not specific to one implementation. Architectural modifications improved recall only to about 27%, still near chance. The researcher asks whether this is a fundamental limitation of the compressed-state representation in linear attention or if there are architectural approaches that can scale to million-token DNA sequences without resorting to expensive softmax attention or large external memory.

reddit · r/MachineLearning · /u/No-Coffee-8227 · Aug 16, 07:47

**「Background」** Linear attention mechanisms replace the softmax attention&\#x27;s quadratic complexity with a linear-time computation, often by compressing past context into a fixed-size state. This compression can hinder the model&\#x27;s ability to retrieve specific information from long sequences, a problem known as long-range recall. The Needle in a Haystack benchmark tests this by requiring the model to find a specific piece of information embedded in a long context. For DNA sequences, which can be millions of tokens long, this limitation is particularly pronounced, as the user&\#x27;s experiments show recall dropping to near chance levels \(25% for a four-token vocabulary\) at long contexts, even with models like HyenaDNA.

**「Impact」** This highlights a critical bottleneck for applying linear attention to long-context DNA modeling, where reliable long-range recall is essential; current approaches may require hybrid architectures or external memory, increasing complexity and cost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spheron.network/blog/log-linear-attention-gpu-cloud-inference-2026/">Log- Linear Attention on GPU Cloud: The O(N log...) | Spheron Blog</a></li>

</ul>
</details>

**Tags**: `#linear attention`, `#long-range recall`, `#DNA sequence modeling`, `#benchmarking`, `#machine learning`

**中文**

<a id="bilingual-item-7-zh"></a>
### [线性注意力在长距离召回中的挑战与解决思路](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

一位研究人员在 DNA 序列建模中尝试使用线性注意力机制，因为 DNA 序列可长达 100 万 token，标准 softmax 注意力在内存和计算上代价过高。然而，在类似“大海捞针”的基准测试中，该模型的长距离召回率仅为 25%左右，接近随机水平（DNA 词汇表为 A/C/G/T 四种）。他们发现 HyenaDNA 在相同基准下表现也差（约 25-27%），表明问题并非特定实现所致。当上下文缩短至 16K 时，小型线性注意力模型召回率可达 50-60%，但随着上下文增长，召回问题加剧。尽管尝试了架构修改，改进仅约 27%，仍接近随机。作者质疑这是否是线性注意力压缩状态表示的固有局限，并寻求无需 softmax 注意力或大型外部记忆、可扩展至百万 token DNA 序列的解决方案。

reddit · r/MachineLearning · /u/No-Coffee-8227 · 8月16日 07:47

**「背景」** 线性注意力机制通过将注意力计算近似为线性复杂度，使得处理超长序列（如 DNA 序列可达百万级 token）成为可能，但代价是状态压缩导致的长距离信息检索能力下降。传统 softmax 注意力虽能精确检索，但计算和内存开销随序列长度呈二次增长，难以直接用于超长序列。

**「影响」** 该问题直接影响依赖线性注意力进行长序列建模的研究人员和开发者，尤其是在基因组学等需要处理百万级 token 的应用中，因为当前线性注意力模型在长距离信息检索上表现不佳，可能限制其实际部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/73">Log- Linear Attention Mechanism</a></li>
<li><a href="https://www.spheron.network/blog/log-linear-attention-gpu-cloud-inference-2026/">Log- Linear Attention on GPU Cloud: The O(N log...) | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#linear attention`, `#long-range recall`, `#DNA sequence modeling`, `#benchmarking`, `#machine learning`

---

**English**

<a id="bilingual-item-8-en"></a>
### [Revisiting ECA-Net: Cross-Channel Interaction Hypothesis Questioned](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

A Reddit post by /u/arkuto critically re-examines the Efficient Channel Attention \(ECA\) paper \(2019, ~12k citations\), arguing that its central hypothesis—that cross-channel interaction is key—is conceptually flawed. The author contends that applying a 1D convolution over channel means is inappropriate because channels lack the spatial topology that convolutions assume. Using chess endgame tablebases as a complete dataset, they benchmarked several attention variants: IdentityGate \(96.04% accuracy\), SqueezeExcitation \(SE8\) \(96.17%\), ECA with k=3 \(96.68%\), ECA with k=1 \(96.61%\), CenterMasked ECA \(96.63%\), and PerChannelGate \(96.65%\). Notably, ECA with k=1, which has no cross-channel interaction, still outperforms SE, undermining the paper&\#x27;s hypothesis. The author also notes that no public repository, including the official one, has tested a pure k=1 ablation, and suggests that synthetic datasets like chess tablebases should be used to separate regularization effects from architectural efficiency.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**「Background」** The Efficient Channel Attention \(ECA\) module was introduced in the 2019 paper &\#x27;ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks&\#x27; by Qilong Wang and colleagues. It was proposed as an improvement over the Squeeze-and-Excitation \(SE\) block, which uses a fully connected layer to model channel dependencies. ECA instead applies a 1D convolution directly on the channel-wise global average pooled features, avoiding dimensionality reduction and using only a few parameters. The paper claims that local cross-channel interaction is key to its effectiveness, and it adaptively selects the kernel size of the 1D convolution. The module has been widely adopted, with the paper accumulating over 12,000 citations.

**「Impact」** This analysis challenges the widely accepted explanation for ECA&\#x27;s success, potentially prompting researchers to reconsider the role of cross-channel interaction in attention mechanisms and to test degenerate cases like k=1 in future work.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA - Net : Efficient Channel Attention for Deep...</a></li>
<li><a href="https://paperswithcode.co/paper/1910.03151">ECA - Net : Efficient Channel Attention for Deep... | Papers with Code</a></li>
<li><a href="https://scispace.com/papers/eca-net-efficient-channel-attention-for-deep-convolutional-35il3j6w2b">(Open Access) ECA - Net : Efficient Channel Attention for Deep...</a></li>

</ul>
</details>

**Tags**: `#attention mechanisms`, `#deep learning`, `#CNN`, `#research critique`, `#machine learning`

**中文**

<a id="bilingual-item-8-zh"></a>
### [重新审视高效通道注意力论文：核心假设存疑](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

一篇 Reddit 帖子对 2019 年发表的 Efficient Channel Attention（ECA）论文提出批评，认为其核心假设——跨通道交互是关键——在概念上存在缺陷。作者指出，ECA 在通道维度上使用一维卷积，类似于对表格数据应用卷积，缺乏拓扑结构支撑。作者使用国际象棋残局表库数据进行了实验，结果显示 k=1（无跨通道交互）的 ECA 性能与 k=3 相当，甚至优于 SE，这削弱了原论文的假设。作者还发现，官方仓库和其他复现项目均未对 k=1 进行独立消融测试，并建议在合成数据集上测试架构以区分正则化效应和核心架构效率。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**「背景」** ECA-Net（Efficient Channel Attention Network）是 2019 年提出的一种轻量级注意力模块，旨在改进 SENet（Squeeze-and-Excitation Network）的性能。SENet 通过将通道均值压缩到较小的隐藏层来建模通道间依赖，而 ECA-Net 则直接对通道均值应用一维卷积，避免了降维操作，从而在减少参数的同时提升了性能。ECA-Net 的核心假设是跨通道交互（cross-channel interaction）是提升性能的关键，其卷积核大小 k 通常设置为 3。该论文在 ImageNet 等数据集上取得了显著效果，并获得了大量引用。

**「影响」** 该分析对 ECA-Net 的机制解释提出质疑，可能促使研究人员重新审视注意力机制的设计，并推动在完整数据集上进行更严谨的消融测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA - Net : Efficient Channel Attention for Deep...</a></li>
<li><a href="https://paperswithcode.co/paper/1910.03151">ECA - Net : Efficient Channel Attention for Deep... | Papers with Code</a></li>
<li><a href="https://scispace.com/papers/eca-net-efficient-channel-attention-for-deep-convolutional-35il3j6w2b">(Open Access) ECA - Net : Efficient Channel Attention for Deep...</a></li>

</ul>
</details>

**标签**: `#attention mechanisms`, `#deep learning`, `#CNN`, `#research critique`, `#machine learning`

---

**English**

<a id="bilingual-item-9-en"></a>
### [US asks allies to pick sides in AI cooperation](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 7.0/10

The United States is reportedly asking allies and countries seeking AI cooperation with Washington to choose sides, warning that failure to do so could result in exclusion from US-led AI alliances. A draft letter prepared by the US State Department is said to state that signing the Pax Silica declaration not only means joining the alliance but also prohibits joining other overlapping initiatives that conflict with it. This move appears to be part of a broader effort to counter China&\#x27;s influence in AI development. The report, sourced from Neowin, indicates that the US is leveraging its position to consolidate allied support in the AI race. However, details remain limited, and the source is a secondary report, so the exact contents and status of the letter are unconfirmed.

telegram · zaihuapd · Aug 16, 02:30

**「Background」** Pax Silica is a United States-led international initiative focused on securing supply chains for advanced technologies such as semiconductors, artificial intelligence, and rare earth elements. The U.S. Department of State describes it as its flagship effort on AI and supply chain security, advancing a new economic security consensus among allies and trusted partners. The initiative was formalized with the signing of the Pax Silica Declaration, for example, by the United States and India on February 20, 2026.

**「Impact」** Allied nations and companies seeking US AI partnerships may face pressure to align exclusively with US-led initiatives, potentially limiting their ability to collaborate with China or participate in competing AI frameworks. This could reshape international AI cooperation and accelerate a geopolitical split in AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica/">Pax Silica - United States Department of State</a></li>
<li><a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/02/united-states-and-india-sign-pax-silica-declaration/">United States and India Sign Pax Silica Declaration</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#geopolitics`, `#US-China`, `#international relations`, `#technology industry`

**中文**

<a id="bilingual-item-9-zh"></a>
### [美国据报要求盟友在 AI 合作中选边](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 7.0/10

据报道，美国要求盟友及希望与华盛顿开展 AI 合作的国家选边，否则可能被排除在美国主导的 AI 联盟之外。美国国务院准备的信函草案称，签署 Pax Silica 宣言不仅是加入联盟，还意味着不能同时加入预期相冲突的重复倡议。这一动向可能重塑国际 AI 合作格局，加剧中美科技竞争。目前细节有限，且来源为二手报道，需进一步核实。

telegram · zaihuapd · 8月16日 02:30

**「背景」** Pax Silica 是美国主导的一项国际倡议，旨在保障半导体、人工智能和稀土等先进技术的供应链安全。美国国务院将其定位为在盟友和可信伙伴间推进经济安全共识的旗舰努力。2026 年 2 月 20 日，美国和印度签署了 Pax Silica 宣言，标志着该倡议的实质性推进。

**「影响」** 此举可能迫使各国在 AI 合作中明确站队，影响全球 AI 研发与标准制定，尤其对依赖美国技术或市场的国家构成压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica/">Pax Silica - United States Department of State</a></li>
<li><a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/02/united-states-and-india-sign-pax-silica-declaration/">United States and India Sign Pax Silica Declaration</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#geopolitics`, `#US-China`, `#international relations`, `#technology industry`

---

**English**

<a id="bilingual-item-10-en"></a>
### [AI Tool Helps Shut Down 524 Pirated Telegram Channels in 61 Days](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 7.0/10

Researchers developed an AI tool called Anti-RIP to detect pirated content on Telegram. After analyzing 1057 channels with about 209,000 posts, they found 983 channels involved in piracy, with posts totaling 4.85 billion views and covering 19,033 films and TV shows. The tool scanned approximately 249,000 new channels and flagged 802 suspected pirate channels with a test accuracy of 98%. After reporting the results to Telegram and rights holders, 524 previously unknown pirate channels were shut down within 61 days, though the tool still has false positives.

telegram · zaihuapd · Aug 16, 09:13

**「Background」** Telegram has become a significant platform for video piracy, with researchers estimating that such activity costs the industry around $18 billion. To address this, researchers developed Anti-RIP, an open-source AI tool that scans Telegram channels for pirated content. The tool uses machine learning to identify channels sharing copyrighted material, and its findings can be submitted to Telegram and rightsholders for takedown actions.

**「Impact」** This demonstrates a practical AI application for content moderation on messaging platforms, enabling rights holders and Telegram to take down hundreds of pirate channels quickly, though false positives remain a limitation.

<details><summary>References</summary>
<ul>
<li><a href="https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/">Researchers Hunt Telegram Pirates with AI Tool , Flag... * TorrentFreak</a></li>
<li><a href="https://piracymonitor.org/18b-lost-to-piracy-via-telegram-motivated-researchers-to-develop-an-effective-app-to-detect-it/">$18B lost to piracy via Telegram motivated researchers to develop an...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#piracy`, `#Telegram`, `#content moderation`, `#machine learning`

**中文**

<a id="bilingual-item-10-zh"></a>
### [AI 工具追踪 Telegram 盗版，61 天关闭 524 个频道](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 7.0/10

研究人员开发了一款名为 Anti-RIP 的 AI 工具，用于识别 Telegram 上的盗版频道。他们分析了 1057 个频道中的约 20.9 万条帖子，发现其中 983 个涉及盗版内容，相关帖子累计获得 48.5 亿次浏览，涉及 19033 部影视作品。随后，该工具扫描了约 24.9 万个新频道，标记出 802 个疑似盗版频道，测试准确率达到 98%。研究人员将结果提交给 Telegram 及版权方后，61 天内有 524 个此前未知的盗版频道被关闭，但该工具仍存在误报。

telegram · zaihuapd · 8月16日 09:13

**「背景」** Telegram 是一个以隐私和加密为特色的即时通讯平台，其频道功能允许用户向大量订阅者广播内容，但也常被用于传播盗版影视作品。此前的研究估计，Telegram 上的盗版行为每年造成约 180 亿美元的损失。为应对这一问题，研究人员开发了名为 Anti-RIP 的 AI 工具，用于实时检测 Telegram 上新兴的视频盗版社区。该工具已开源，相关数据集也已公开，可供 Telegram 和版权方使用。

**「影响」** 该工具为版权方和平台提供了一种可量化的盗版检测手段，在 61 天内关闭了 524 个频道，显著减少了盗版内容的传播渠道，但误报问题仍需改进，可能影响无辜频道的正常运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/">Researchers Hunt Telegram Pirates with AI Tool , Flag... * TorrentFreak</a></li>
<li><a href="https://piracymonitor.org/18b-lost-to-piracy-via-telegram-motivated-researchers-to-develop-an-effective-app-to-detect-it/">$18B lost to piracy via Telegram motivated researchers to develop an...</a></li>

</ul>
</details>

**标签**: `#AI`, `#piracy`, `#Telegram`, `#content moderation`, `#machine learning`

---

## Financial News / 财经新闻

**English**

<a id="bilingual-item-11-en"></a>
### [Anthropic Q2 Preliminary Revenue Surpasses $11.5 Billion](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic&\#x27;s preliminary Q2 revenue exceeded $11.5 billion, up over 14 times year-over-year from $787 million in Q2 2025, and the company reported positive adjusted operating income for the quarter.

telegram · zaihuapd · Aug 16, 07:26

**「Background」** The figures are preliminary and may be adjusted, according to a Bloomberg report citing documents. The company is preparing for a potential IPO that could launch this fall.

**「Impact」** The revenue surge and positive operating income could strengthen Anthropic&\#x27;s position ahead of a potential IPO, affecting investors and the AI industry.

**Tags**: `#Anthropic`, `#revenue`, `#AI`, `#IPO`, `#earnings`

**中文**

<a id="bilingual-item-11-zh"></a>
### [Anthropic 第二季初步营收超 115 亿美元，同比增长逾 14 倍](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

据彭博社援引的文件，Anthropic 第二季初步营收超过 115 亿美元，较去年同期的 7.87 亿美元增长逾 14 倍，且当季调整后营业利润转正。这些数字为初步数据，仍可能调整。

telegram · zaihuapd · 8月16日 07:26

**「背景」** Anthropic 是一家 AI 公司，正筹备可能在今秋启动的大型 IPO。

**「影响」** 这一强劲增长可能增强投资者对 AI 行业的信心，并影响 Anthropic 的 IPO 估值。

**标签**: `#Anthropic`, `#revenue`, `#AI`, `#IPO`, `#earnings`

---