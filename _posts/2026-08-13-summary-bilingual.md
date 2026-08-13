---
layout: default
title: "Horizon Summary: 2026-08-13 (EN / ZH)"
date: 2026-08-13
lang: en
---

> Selected 18 important items from 41 fetched items. Each English entry is followed by its Chinese version.

---

## Technology News / 科技新闻

**English**

<a id="bilingual-item-1-en"></a>
### [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

OpenAI and Cerebras announced GPT-5.6 Sol Ultrafast, a collaboration that claims to deliver 7x faster inference on HLE benchmarks compared to standard models. In evaluations, GPT-5.6 Sol on Ultrafast mode answered all 2,500 HLE questions in 11 hours and 11 minutes, while Claude Fable 5 took 78 hours and 27 minutes, achieving comparable accuracy nearly 7x faster. The announcement highlights the potential of speed to enhance iterative reasoning and real-time AI applications, though it does not explicitly confirm that Ultrafast mode produces identical accuracy to the standard GPT-5.6 Sol. Pricing details have not been released, and the collaboration is seen as a significant milestone in AI inference performance.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**「Background」** OpenAI and Cerebras have partnered to introduce Ultrafast mode, a new service tier in the OpenAI API that runs GPT-5.6 Sol up to 14 times faster than standard processing, generating up to 750 output tokens per second. This collaboration leverages Cerebras&\#x27; specialized hardware to accelerate inference, which is the process of generating responses from a trained AI model. The speed increase is significant because faster inference enables more iterative reasoning, where the model can refine its outputs multiple times, potentially improving the quality of its answers.

**「Impact」** This development could significantly reduce inference time for complex reasoning tasks, enabling more practical real-time AI applications and potentially lowering compute costs for users, though the lack of explicit accuracy equivalence and pricing information introduces uncertainty.

**「Community Discussion」** Community members expressed excitement about the collaboration&\#x27;s potential, with some emphasizing that speed enhances thought quality through iteration. However, others noted the absence of explicit confirmation that Ultrafast mode matches standard accuracy, and the lack of pricing details, suggesting the performance claims may be incomplete.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT - 5 . 6 Sol at up to 14X the... | OpenAI</a></li>
<li><a href="https://scalevise.com/resources/openai-cerebras-gpt-5-6-sol-ultrafast/">OpenAI Cerebras Partnership Powers GPT - 5 . 6 Sol Ultrafast</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#inference`, `#Cerebras`, `#OpenAI`

**中文**

<a id="bilingual-item-1-zh"></a>
### [OpenAI 与 Cerebras 推出 GPT-5.6 Sol Ultrafast，推理速度提升 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

OpenAI 与 Cerebras 合作发布了 GPT-5.6 Sol Ultrafast，声称在 HLE 基准测试上推理速度提升约 7 倍。据称，Ultrafast 模式在 11 小时 11 分钟内回答了全部 2500 个 HLE 问题，而 Claude Fable 5 需要 78 小时 27 分钟，实现了相当的准确率。此外，与 Artificial Analysis 报告的 Fable 5 相比，Ultrafast 模式输出速度快 11 倍，比 Opus 4.8 Fast 模式快 5 倍。该模型旨在通过更快的迭代推理提升 AI 的思考质量，但官方尚未明确确认其准确性与标准版完全一致。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**「背景」** GPT-5.6 Sol 是 OpenAI 开发的大型语言模型，通常通过标准 API 提供推理服务。Cerebras 是一家以高性能 AI 芯片（如 WSE 系列）著称的公司，其硬件专为加速深度学习推理而设计。此次合作将 Cerebras 的硬件与 OpenAI 的模型结合，推出了名为“Ultrafast”的新服务层级，旨在显著提升推理速度。

**「影响」** 对于依赖快速迭代推理的 AI 应用（如实时决策、复杂问题求解）的开发者，Ultrafast 模式可能显著缩短推理时间，提升交互体验。然而，由于缺乏与标准版准确性的明确对比，其实际性能优势仍需进一步验证。

**「社区讨论」** 社区对速度与思考质量的关系展开讨论，认为快速迭代可能提升推理质量，但也有评论指出官方未明确确认 Ultrafast 模式与标准版性能完全一致，且未公布定价信息，引发对实际可用性的猜测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT - 5 . 6 Sol at up to 14X the... | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#inference`, `#Cerebras`, `#OpenAI`

---

**English**

<a id="bilingual-item-2-en"></a>
### [DeepSeek Harness Developer Preview Released](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek has released an open-source developer preview of DeepSeek Harness, an agent harness that records every model input in an append-only session log, including system prompts, reasoning, tool calls, results, subagent scheduling, and context injections. The Trajectory view allows inspection by source, and resume, fork, search, and replay operate on the same event stream. The project is available on GitHub under the MIT license, with an early preview expected to have rough edges and compatibility-breaking changes. The harness uses Cordis v4, a plugin system that supports hot-reload and dynamic enable/disable with state and side-effect cleanup. This traceability feature is highlighted as a key differentiator, especially compared to US models that encrypt or obfuscate traces.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**「Background」** DeepSeek Harness is an open-source agent harness released by DeepSeek as a developer preview under the MIT license. It is built on the Cordis meta-framework, which enables hot-loading and unloading of plugins without restarting a running process, and can revert state and side effects when plugins are unloaded. The harness implements every agent capability as a plugin, allowing components such as models, tools, skills, sessions, sandboxes, storage, orchestration, and the web interface to be swapped or recomposed.

**「Impact」** Developers building AI agents will gain full traceability and replay capabilities, enabling easier debugging and auditing of agent behavior, which is particularly valuable for open-source and transparency-focused projects.

**「Community Discussion」** Community members praised the traceability feature as a killer capability, contrasting it with US models&\#x27; encrypted traces. One author acknowledged it&\#x27;s an early preview with rough edges, while others discussed the underlying Cordis v4 plugin system and its hot-reload capabilities, though some expressed plugin fatigue.

<details><summary>References</summary>
<ul>
<li><a href="https://deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://deepseek-code.com/">DeepSeek Harness: Open-Source AI Agent Framework</a></li>
<li><a href="https://x.com/deepseek_ai/status/2087887408440164663">DeepSeek on X: &quot;🧩 DeepSeek Harness v0.1 is now available in Developer Preview! 🔹 We’re opening it up to developers building agent harnesses worldwide and open-sourcing the codebase in MIT license. 🔹 Powered by the Cordis meta-framework, DeepSeek Harness is an agent harness built around one&quot; / X</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#open source`, `#developer tools`, `#DeepSeek`, `#traceability`

**中文**

<a id="bilingual-item-2-zh"></a>
### [DeepSeek Harness 开发者预览版发布](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 发布了开源开发者预览版 DeepSeek Harness，这是一个 AI 代理工具，提供完整的可追溯性和重放功能。该工具以 MIT 许可证发布，目前处于早期阶段，可能存在粗糙之处和破坏性变更。其核心特性是记录模型所见的一切，包括系统提示、推理、工具调用和结果，并支持通过轨迹视图检查、恢复、分叉、搜索和重放。社区讨论强调，这一功能与美国模型的加密或混淆轨迹形成鲜明对比，被视为杀手级能力。此外，该工具基于 Cordis v4 构建，支持插件热加载和动态启用/禁用。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**「背景」** DeepSeek Harness 是 DeepSeek 于 2025 年 10 月发布的开发者预览版开源智能体框架，采用 MIT 许可证。其核心特性是“一切皆插件”的架构，所有智能体能力（如模型、工具、技能、会话、沙箱、存储、编排和 Web 界面）均可作为插件替换或重组。该框架基于 Cordis 元框架构建，Cordis 已在 Koishi 项目中使用四年（v3），支持插件热加载和卸载，并能回滚插件产生的状态和副作用。

**「影响」** 对于 AI 代理开发者和调试者，DeepSeek Harness 提供了前所未有的透明度和可重放性，可能显著简化代理行为的调试和复现，尤其是在复杂多步骤任务中。

**「社区讨论」** 社区反应积极，作者确认这是早期预览版，欢迎反馈。有评论者认为完整轨迹记录是杀手级功能，而美国模型不允许这样做。也有评论者指出其基于 Cordis v4，支持插件热加载和状态回滚，但有人对“一切皆插件”的架构表示疲劳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://deepseek-code.com/">DeepSeek Harness: Open-Source AI Agent Framework</a></li>
<li><a href="https://x.com/deepseek_ai/status/2087887408440164663">DeepSeek on X: &quot;🧩 DeepSeek Harness v0.1 is now available in Developer Preview! 🔹 We’re opening it up to developers building agent harnesses worldwide and open-sourcing the codebase in MIT license. 🔹 Powered by the Cordis meta-framework, DeepSeek Harness is an agent harness built around one&quot; / X</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#open source`, `#developer tools`, `#DeepSeek`, `#traceability`

---

**English**

<a id="bilingual-item-3-en"></a>
### [DRAM Attack Achieves Arbitrary Code Execution](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

A security researcher has disclosed a novel DRAM attack technique that exploits the memory controller to achieve arbitrary code execution, potentially bypassing hardware protections on affected systems. The technique, detailed in a GitHub repository, targets the AMD Jaguar architecture \(from 2013\) and involves manipulating memory controller registers to gain access to privileged &\#x27;negative ring&\#x27; territory. The attack has significant implications for gaming consoles like Xbox and PlayStation, which use similar hardware, and underscores the growing attack surface of modern DRAM interfaces. The researcher notes that newer architectures like Zen 3 have different base addresses for memory controller registers, but the full scope of affected processors remains unclear.

hackernews · matt\_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**「Background」** DRAM controllers translate physical addresses into row, column, bank, and rank coordinates, and modern CPUs add an address-scrambling layer to spread accesses evenly and mitigate row-hammer attacks. AMD&\#x27;s memory controller exposes configuration registers that control this scrambling, and on certain families \(e.g., AMD16h, used in the Jaguar architecture\) these registers are writable from ring 0. Christopher Domas&\#x27;s skitter-creek-bath-salts project exploits this by reprogramming the DRAM address translation to remap physical memory, allowing an attacker with kernel privileges to access regions normally hidden from the OS, such as the Platform Security Processor \(PSP\), System Management Mode \(SMM\), C6 state, and microcode.

**「Impact」** On affected systems, an attacker with ring-0 \(kernel\) access can escalate to the most privileged hardware level, gaining unfettered control over the system, which is particularly concerning for gaming consoles where such access is normally locked down.

**「Community Discussion」** Commenters expressed excitement for the accompanying Black Hat talk by Christopher Domas, praising his ability to explain complex reverse engineering topics. Others noted the increasing complexity of DRAM and the corresponding growth of attack surface, while some questioned the applicability to newer CPUs beyond the AMD Jaguar architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>
<li><a href="https://aicrier.com/post/8hov5f155djs35wmjopv">Skitter Creek Bath Salts Rewrites DRAM Security — AICrier</a></li>

</ul>
</details>

**Tags**: `#security`, `#DRAM`, `#hardware`, `#exploit`, `#reverse engineering`

**中文**

<a id="bilingual-item-3-zh"></a>
### [DRAM 攻击技术实现任意代码执行](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

安全研究员 Christopher Domas 发布了一项名为“Spaghettifying DRAM”的新型攻击技术，该技术利用内存控制器漏洞，在 AMD Jaguar 架构（2013 年发布）上实现了任意代码执行。该攻击通过操纵 DRAM 刷新机制，使攻击者能够绕过硬件保护，获得对系统底层资源的完全控制。该技术对游戏主机（如 Xbox 和 PlayStation）的安全构成潜在威胁，因为这些设备使用类似架构。目前，该攻击已在 AMD 16h 系列上验证，但其他处理器家族（如 Zen 3）的适用性尚不明确。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**「背景」** DRAM（动态随机存取存储器）通过行地址选通（RAS）和列地址选通（CAS）等信号进行寻址，而现代处理器中的内存控制器负责将物理地址映射到实际的 DRAM 单元。AMD 处理器使用一种称为 DRAM 地址加扰（DRAM address scrambling）的机制，通过内存控制器中的寄存器对物理地址进行重新映射，以增强安全性。安全研究员 Christopher Domas 发布了一个名为“skitter-creek-bath-salts”的开源项目，该项目通过操纵 AMD 内存控制器的寄存器，重新映射 DRAM 物理地址，从而访问通常被操作系统隐藏的内存区域，包括 PSP（平台安全处理器）、SMM（系统管理模式）、C6 状态和微码等。该技术利用了内存控制器设计中的漏洞，实现了对受保护内存的任意读写，可能影响游戏主机和系统安全。

**「影响」** 该攻击技术可能影响使用 AMD Jaguar 架构的设备，尤其是游戏主机，一旦获得 ring-0 权限，攻击者可以完全控制系统。对于其他处理器，如 Zen 3，攻击的可行性尚待验证，但内存控制器的复杂性可能使更多平台面临风险。

**「社区讨论」** 社区对该技术表示高度关注，认为这是对系统安全的重大突破，但也指出其适用范围可能有限。有评论者提到，现代 DRAM 的复杂性增加了攻击面，而另一些人则质疑该攻击在较新 CPU 上的有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>
<li><a href="https://aicrier.com/post/8hov5f155djs35wmjopv">Skitter Creek Bath Salts Rewrites DRAM Security — AICrier</a></li>
<li><a href="https://news.linxi.com.au/news/amd-hardware-vulnerability-exposed-by-dram-address-scrambling-research">AMD DRAM Scrambling Exploit Bypasses Security Fences | Linxi News</a></li>

</ul>
</details>

**标签**: `#security`, `#DRAM`, `#hardware`, `#exploit`, `#reverse engineering`

---

**English**

<a id="bilingual-item-4-en"></a>
### [Choose Boring Technology](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley&\#x27;s 2015 essay &\#x27;Choose Boring Technology&\#x27; argues that companies should limit the number of novel technologies they adopt, framing this as a fixed budget of &\#x27;innovation tokens&\#x27;—typically about three per company. The core idea is that every new or unconventional technology choice consumes a token, and once spent, tokens are unavailable for a long time, so teams should reserve them for areas that directly differentiate the product. McKinley illustrates this with examples from his experience at Etsy and other companies, where choosing mature, well-understood technologies for non-core components reduced risk and operational burden. The essay has become a classic in software engineering, widely cited for its practical framework for managing technical risk and focusing innovation where it matters most. It remains relevant today, with recent discussions applying the concept to AI agents and modern development practices.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**「Background」** Dan McKinley, a software engineer who worked at Etsy and Stripe, published the essay &\#x27;Choose Boring Technology&\#x27; in March 2015. The core idea is that every company has a limited number of &\#x27;innovation tokens&\#x27; to spend on adopting new or novel technologies; once spent, these tokens are unavailable for other innovations for a long time. McKinley argues that most technology choices should be &\#x27;boring&\#x27;—mature, well-understood, and reliable—so that the scarce innovation tokens are reserved for areas that truly differentiate the product. He cites examples like Postgres, Python, Memcached, and Cron as boring but effective choices, and warns that non-tech companies especially risk failure by spending tokens on shiny new technologies.

**「Impact」** The &\#x27;innovation tokens&\#x27; framework provides engineering leaders and product managers with a concrete, communicable method for justifying conservative technology choices, helping teams avoid unnecessary complexity and technical debt. It has influenced how many organizations evaluate new tools, encouraging a bias toward proven solutions unless a clear, differentiating need exists.

**「Community Discussion」** Commenters largely praise the essay, with one calling it &\#x27;one of the most useful concepts&\#x27; for making tradeoffs and explaining them to colleagues. However, some push back, arguing that &\#x27;innovation tokens&\#x27; are arbitrary and that engineers should evaluate technologies based on requirements and risks rather than novelty alone. Others note the difficulty of finding companies that genuinely practice such pragmatism, and one commenter suggests that in the age of AI agents, teams should &\#x27;push all innovation tokens into agents&\#x27; and use boring technology for everything else.

<details><summary>References</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Dan McKinley :: Choose Boring Technology</a></li>
<li><a href="https://www.annageller.com/p/summary-choose-boring-technology">Summary: Choose Boring Technology by Dan McKinley - Anna Geller</a></li>

</ul>
</details>

**Tags**: `#software-engineering`, `#technology-strategy`, `#engineering-culture`, `#innovation-tokens`, `#tech-debt`

**中文**

<a id="bilingual-item-4-zh"></a>
### [选择无聊技术：创新代币框架](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley 的经典文章《选择无聊技术》（2015）提出，公司应将新技术采用限制在少数“创新代币”内，以管理风险并集中创新于产品差异化。该框架建议，大多数技术栈应使用成熟、可预测的“无聊”技术，而将有限的创新预算用于真正需要突破的领域。文章通过具体案例说明，过度采用新颖技术会增加复杂性和维护成本，而创新代币的稀缺性迫使团队做出更审慎的权衡。这一观点在近期 Hacker News 讨论中再次引发共鸣，并被重新解读为在 AI 代理时代应优先选择代理擅长的技术。该文对工程领导者和实践者具有持久价值，提供了实用的决策框架。

hackernews · tosh · 8月13日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49289512)

**「背景」** Dan McKinley 在 2015 年发表的《Choose Boring Technology》一文中提出了“创新代币”（innovation tokens）的概念，认为每家公司在一段时间内只能承受有限数量的新技术引入，超出这个额度会带来不必要的风险。他建议将创新精力集中在产品差异化上，而基础设施和工具则应优先选择成熟、可预测的“无聊”技术，例如 Postgres、Python、Memcached 和 Cron。这一观点在工程管理领域产生了广泛影响，成为技术选型讨论中的经典框架。

**「影响」** 该框架为工程团队提供了一种可操作的决策方法，帮助他们在技术选型时平衡创新与风险，尤其适用于需要向各级同事解释技术权衡的领导者。在 AI 代理时代，它被引申为建议将创新代币集中于代理技术，而让代理使用的底层技术保持“无聊”和主流，以最大化效率。

**「社区讨论」** 评论者普遍认同“创新代币”概念，认为它有助于做出正确权衡并清晰传达决策，但也有反对声音指出该概念过于武断，认为工程师应基于具体需求、风险和收益而非“新颖”或“无聊”的标签来做决策。此外，有评论者希望存在一个经过验证的工程文化公司招聘平台，以避开那些声称务实但实际过度工程化的团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Dan McKinley :: Choose Boring Technology</a></li>
<li><a href="https://jadon.us/posts/notes-on-choose-boring-technology/">Notes on - Choose Boring Technology by Dan McKinley</a></li>
<li><a href="https://www.annageller.com/p/summary-choose-boring-technology">Summary: Choose Boring Technology by Dan McKinley - Anna Geller</a></li>

</ul>
</details>

**标签**: `#software-engineering`, `#technology-strategy`, `#engineering-culture`, `#innovation-tokens`, `#tech-debt`

---

**English**

<a id="bilingual-item-5-en"></a>
### [DeepSeek V4 Pro 0813 Released with Open Weights](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek has released DeepSeek V4 Pro 0813, the latest version of its Pro model, available via API on OpenRouter and through DeepSeek&\#x27;s own API, app, and web interface under the model name deepseek-v4-pro. The open weights are now available on Hugging Face, totaling 1.7 trillion parameters and 893 GB, following the pattern of previous releases like DeepSeek-V4-Pro and DeepSeek-V4-Flash-0731. The model enhances agent capabilities and natively supports the Responses API format, making it compatible with Codex. Additionally, both V4-Pro and V4-Flash introduce new reasoning levels: low, high, and max, with API pricing shifting to peak/off-peak rates effective August 17, 2026, where off-peak prices are half of peak prices. Simon Willison observed notably different outputs across reasoning levels, as illustrated by his pelican test images, and noted that benchmark results were shared via unofficial channels after a Reddit post was removed.

rss · Simon Willison · Aug 12, 23:59

**「Background」** DeepSeek V4 Pro 0813 is the production release of DeepSeek&\#x27;s flagship model, ending a preview period of nearly four months. It is available via API, app, and web, with open weights on Hugging Face \(1.7T parameters, 893 GB\). The model introduces enhanced agent capabilities, native support for the Responses API format \(compatible with Codex\), and three reasoning levels \(low, medium, high\). Pricing will shift to peak/off-peak rates starting August 17, 2026, with off-peak prices at half the peak rate.

**「Impact」** Developers and organizations using open-source LLMs can now access a state-of-the-art 1.7T-parameter model with open weights, enabling local deployment and fine-tuning, while the new peak/off-peak pricing may reduce API costs for off-peak workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves ...</a></li>
<li><a href="https://aireleasetracker.com/model/deepseek/deepseek-v4-pro-0813">DeepSeek-V4-Pro-0813 — Benchmarks, Specs &amp; Release Date</a></li>
<li><a href="https://byteiota.com/deepseek-v4-pro-0813-is-live-and-prices-are-about-to-jump/">DeepSeek V4 Pro 0813 Is Live — And Prices Are About to Jump</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#open-source`, `#model release`, `#LLM`

**中文**

<a id="bilingual-item-5-zh"></a>
### [DeepSeek V4 Pro 0813 发布：开放权重与 API 峰谷定价](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 已通过 API 发布，并同步上线 APP 和网页端，模型名为 deepseek-v4-pro。该模型增强了 Agent 能力，原生支持 Responses API 格式，适配 Codex。其开放权重已在 Hugging Face 上提供，参数量为 1.7T，文件大小 893 GB。API 将实行峰谷定价，新价格于 2026 年 8 月 17 日 0 时生效，闲时价格为高峰时段的一半。此外，V4-Pro 和 V4-Flash 的思考模式新增了 low、high、max 三档。DeepSeek 还发布了全新的 Harness 应用，采用 MIT 协议开源，以“一切皆插件”的架构设计，提供标准、PTC、极简和创造四种运行模式。

rss · Simon Willison · 8月12日 23:59

**「背景」** DeepSeek V4 Pro 是 DeepSeek 的旗舰模型，此前经历了近四个月的预览期。2026 年 8 月 12 日，DeepSeek 发布了其正式版 V4 Pro 0813，通过 API 提供，并随后在 Hugging Face 上开放了权重（1.7T 参数，893 GB）。该模型支持 Agent 能力增强，并原生支持 Responses API 格式，适配 Codex。此外，DeepSeek 还发布了 Harness 应用，以 MIT 协议开源，采用“一切皆插件”的架构。

**「影响」** 对于依赖开源大模型的开发者而言，DeepSeek V4 Pro 0813 的开放权重（1.7T 参数）提供了强大的本地部署选项，可能推动社区微调和应用创新。API 峰谷定价降低了闲时使用成本，但高峰时段价格可能上涨，影响成本敏感型用户的调用策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves ...</a></li>
<li><a href="https://aireleasetracker.com/model/deepseek/deepseek-v4-pro-0813">DeepSeek-V4-Pro-0813 — Benchmarks, Specs &amp; Release Date</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#open-source`, `#model release`, `#LLM`

---

**English**

<a id="bilingual-item-6-en"></a>
### [DeepMind SL2T Brings Sign Language AI to Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

Google DeepMind has released SL2T, a large-scale multilingual sign language-to-text model, marking the first consumer integration of sign language AI. The model initially supports American Sign Language \(ASL\) to English and is now available on Pixel 11 devices through Gboard and Live Transcribe, with plans to expand to more devices and languages. SL2T was trained on over 100,000 hours of sign language data across more than 50 languages, achieving a zero-shot score of 70 BLEURT on the FLEURS-ASL benchmark, significantly surpassing previous records. To protect privacy, the model processes only hand and body pose keypoints rather than raw video. This deployment represents a major step forward in accessibility AI, bringing sign language translation to everyday consumer products.

telegram · zaihuapd · Aug 13, 08:55

**「Background」** Sign language translation has traditionally been a research challenge due to the complexity of continuous, multi-modal signing and the lack of large-scale datasets. Prior systems were often limited to isolated word recognition or required specialized hardware, and none had been integrated into mainstream consumer devices. DeepMind&\#x27;s SL2T model changes this by using over 100,000 hours of data from more than 50 sign languages, and it processes only hand and body keypoints rather than raw video to preserve privacy. This marks the first time a sign language-to-text model has been deployed in consumer products, starting with American Sign Language to English on Pixel 11&\#x27;s Gboard and Live Transcribe.

**「Impact」** Deaf and hard-of-hearing users who sign can now use Pixel 11&\#x27;s Gboard and Live Transcribe to convert ASL into English text in real time, a first for consumer devices. The privacy-preserving keypoint approach may set a precedent for future on-device sign language AI, though broader language and device support remains pending.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://techmymoney.com/2026/08/12/deepmind-sl2t-brings-asl-input-to-pixel-11-phones/">DeepMind SL2T: ASL Input on Pixel 11 Phones - techmymoney.com</a></li>

</ul>
</details>

**Tags**: `#DeepMind`, `#sign language AI`, `#accessibility`, `#Pixel 11`, `#SL2T`

**中文**

<a id="bilingual-item-6-zh"></a>
### [DeepMind 发布手语转文字模型 SL2T，首次落地 Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 发布大规模多语言手语转文字模型 SL2T，首次将手语 AI 引入消费产品。该模型率先支持美国手语转英语，已在 Pixel 11 的 Gboard 键盘和 Live Transcribe 实时字幕功能中上线，后续将扩展至更多设备和语言。SL2T 使用超过 10 万小时、涵盖 50 多种手语的数据训练，在 FLEURS-ASL 基准上零样本得分为 70 BLEURT，显著高于此前纪录。为保护隐私，模型仅处理手部和身体姿态关键点，不读取原始视频。

telegram · zaihuapd · 8月13日 08:55

**「背景」** 手语翻译技术此前多停留在实验室或专用设备阶段，尚未大规模集成到主流消费产品中。DeepMind 的 SL2T 模型是首个将手语转文字能力直接嵌入智能手机系统的方案，利用超过 10 万小时、50 多种手语数据训练，并在 FLEURS-ASL 基准上取得零样本 70 BLEURT 的成绩。该模型仅处理手部和身体姿态关键点，不读取原始视频，以保护用户隐私。

**「影响」** 对于使用 Pixel 11 的听障用户和手语使用者，SL2T 首次在消费级设备上提供实时手语转文字功能，显著提升了无障碍交互的可用性；其隐私保护设计（仅处理关键点）可能为后续 AI 无障碍应用树立技术规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://techmymoney.com/2026/08/12/deepmind-sl2t-brings-asl-input-to-pixel-11-phones/">DeepMind SL2T: ASL Input on Pixel 11 Phones - techmymoney.com</a></li>
<li><a href="https://www.notebookcheck.net/Google-Pixel-11-turns-American-Sign-Language-into-typed-text.1367397.0.html">Google Pixel 11 turns American Sign Language into typed text</a></li>

</ul>
</details>

**标签**: `#DeepMind`, `#sign language AI`, `#accessibility`, `#Pixel 11`, `#SL2T`

---

**English**

<a id="bilingual-item-7-en"></a>
### [Google Unveils Gemini 3.7 Flash with Competitive Pricing](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

Google has introduced Gemini 3.7 Flash, a new AI model with competitive performance and introductory pricing. The model shows strong results in vision tasks, as noted by community members, though it is an incremental improvement over recent releases. Pricing is set to double on December 31, 2026, from an initial rate of $1.50 per 1 million input tokens and $7.50 per 1 million output tokens starting January 1, 2027. The release follows closely after Gemini 3.6 Flash, which came out just three weeks prior, and has sparked discussion about its value compared to other models like GPT-5.6 Luna.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**「Background」** Gemini Flash is Google&\#x27;s line of lightweight, cost-efficient AI models designed for high-volume, latency-sensitive tasks such as summarization, parsing, and formatting. The Flash series has historically prioritized low cost and speed over top-tier reasoning, with the latest release, Gemini 3.7 Flash, arriving just three weeks after Gemini 3.6 Flash. This rapid cadence reflects Google&\#x27;s iterative development approach, where each version incorporates developer feedback and algorithmic improvements.

**「Impact」** Developers and organizations using Google&\#x27;s Gemini API for vision-heavy or high-volume text tasks may find Gemini 3.7 Flash a cost-effective option, but the rapid release cadence and upcoming price increase could reduce its long-term appeal.

**「Community Discussion」** Community members are divided: some praise Gemini 3.7 Flash&\#x27;s vision performance relative to its price, while others question the value given the scheduled price hike and the availability of cheaper alternatives like GPT-5.6 Luna. There is also skepticism about the need for such frequent model updates.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Gemini`, `#model release`, `#benchmarks`

**中文**

<a id="bilingual-item-7-zh"></a>
### [谷歌发布 Gemini 3.7 Flash，性能提升但定价引争议](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

谷歌发布了 Gemini 3.7 Flash，这是一款新的 AI 模型，在视觉任务上表现出色，并提供了入门定价。该模型在 DeepSWE 1.1 基准测试中表现良好，但社区评测认为其相比 Opus 5 等竞品仍有差距。值得注意的是，其入门定价计划于 2026 年 12 月 31 日翻倍，而 3.6 Flash 仅在三周前发布，这种快速迭代和定价策略引发了讨论。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**「背景」** Gemini 3.7 Flash 是 Google DeepMind 于 2026 年 8 月 13 日发布的最新“工作马”级 AI 模型，紧随三周前发布的 Gemini 3.6 Flash 之后。该模型专注于编码和智能体任务，支持 100 万 token 的上下文窗口，输入定价为每百万 token 0.75 美元，并计划于 2026 年 12 月 31 日之后价格翻倍。此次发布是 Google 快速迭代策略的一部分，旨在通过开发者反馈和算法创新持续改进模型。

**「影响」** 对于依赖低成本、高容量文本处理（如摘要、解析、格式化）的开发者，Gemini 3.7 Flash 提供了新的选择，但其定价翻倍计划可能影响长期采用。

**「社区讨论」** 社区成员对 Gemini 3.7 Flash 的视觉能力表示认可，但认为 Opus 5 在图像转 HTML 任务上仍是最佳。同时，有用户指出 GPT-5.6 Luna 的折扣和性能使其更具吸引力，而 Gemini 3.7 Flash 的定价和快速迭代降低了其紧迫性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://www.marktechpost.com/2026/08/13/google-ai-just-released-gemini-3-7-flash/">Google AI Just Released Gemini 3.7 Flash: A Coding and Agent Model at $0.75/1M Input Tokens - MarkTechPost</a></li>
<li><a href="https://www.axios.com/2026/08/13/google-gemini-37-flash">Google&#x27;s Gemini 3.7 Flash arrives before Gemini 3.5 Pro</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Gemini`, `#model release`, `#benchmarks`

---

**English**

<a id="bilingual-item-8-en"></a>
### [Gloomberb: Open-Source TUI for Financial Data](https://gloom.sh/) ⭐️ 7.0/10

Gloomberb is an open-source terminal user interface \(TUI\) for financial data, featuring a tiling interface that allows users to view multiple market data panes simultaneously. It has gained significant attention on Hacker News with 373 points and 189 comments, indicating strong interest from the tech community. The tool aims to provide a lightweight, keyboard-driven alternative to professional terminals like Bloomberg, but it lacks the proprietary data connections and depth of such services. Users can customize panes, though some features, like linking ticker symbols across panes, are not fully intuitive. The project is available at gloom.sh and is positioned as a novel approach to accessing market data for developers and tech-savvy users.

hackernews · rbanffy · Aug 13, 13:52 · [Discussion](https://news.ycombinator.com/item?id=49285982)

**「Background」** Gloomberb is an open-source terminal user interface \(TUI\) for financial data, featuring a tiling layout that allows users to view multiple panes of market information simultaneously. It is often compared to the Bloomberg Terminal, a professional financial software platform that provides real-time data, news, and analytics, but at a significantly higher cost \(around $31,980 per year\). Unlike Bloomberg, Gloomberb is free and open-source, though it lacks the proprietary data connections and depth of professional services.

**「Impact」** Gloomberb offers a free, open-source option for developers and hobbyist traders who want a terminal-based financial dashboard, potentially reducing reliance on expensive professional terminals for basic market monitoring. However, its utility is limited by the lack of premium data sources, so it is unlikely to replace Bloomberg for professional use.

**「Community Discussion」** Commenters appreciate Gloomberb&\#x27;s tiling UI and find it useful for casual trading, but they note that Bloomberg&\#x27;s value lies in its data connections, not just its interface. Some users express concerns about the installation script&\#x27;s dependency management, preferring package managers, and others point out alternative terminals like Godel Terminal, though that is not open source.

<details><summary>References</summary>
<ul>
<li><a href="https://numfer.com/feremabraz/bloomberg-terminal">bloomberg - terminal : Real-time Financial Data UI</a></li>

</ul>
</details>

**Tags**: `#terminal`, `#finance`, `#open-source`, `#tui`, `#market-data`

**中文**

<a id="bilingual-item-8-zh"></a>
### [Gloomberb：开源终端金融数据界面引发热议](https://gloom.sh/) ⭐️ 7.0/10

Gloomberb 是一个开源的终端用户界面（TUI），专为金融数据设计，提供平铺式界面，允许用户在终端中同时查看多个市场数据面板。该项目在 Hacker News 上引发了广泛讨论，获得 373 分和 189 条评论，社区对其实用性与专业终端（如 Bloomberg）的对比展开了辩论。Gloomberb 提供了对市场数据的全新访问方式，但缺乏 Bloomberg 等专业终端的深度数据源和连接能力。其安装脚本采用 curl 方式，引发了对依赖管理和安全性的担忧。

hackernews · rbanffy · 8月13日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49285982)

**「背景」** Gloomberb 是一个开源的终端用户界面（TUI），用于展示金融数据，采用平铺式界面设计。它旨在为技术用户提供一种轻量级、可定制的市场数据访问方式，与 Bloomberg Terminal 等专业金融终端形成对比。Bloomberg Terminal 是金融行业广泛使用的专业服务，提供实时数据、新闻和分析工具，但价格昂贵（每年约 31,980 美元），且主要面向机构投资者。Gloomberb 则免费开源，适合个人开发者或爱好者使用，但可能缺乏 Bloomberg 的深度数据源和连接能力。

**「影响」** 对于熟悉终端的技术用户，Gloomberb 提供了一种轻量、免费的市场数据监控方式，但无法替代 Bloomberg 等专业终端的数据深度和可靠性。

**「社区讨论」** 社区讨论集中在安装方式的透明度（用户希望了解技术栈和依赖管理）、与 Bloomberg 的对比（强调数据源的价值而非界面），以及实际使用体验（如平铺界面的易用性和自定义面板的困惑）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://numfer.com/feremabraz/bloomberg-terminal">bloomberg - terminal : Real-time Financial Data UI</a></li>

</ul>
</details>

**标签**: `#terminal`, `#finance`, `#open-source`, `#tui`, `#market-data`

---

**English**

<a id="bilingual-item-9-en"></a>
### [City2Graph: Python Library for Urban Heterogeneous Graphs](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph is a new Python library that converts geospatial urban data into heterogeneous graphs for spatial analysis, network analysis, and Graph Neural Networks \(GNNs\). It supports building morphological graphs from OpenStreetMap and Overture Maps data, transit graphs from GTFS and GBFS feeds via DuckDB, mobility graphs from origin-destination matrices, and proximity/contiguity graphs using KNN, Delaunay, Gilbert, Waxman, and queen/rook methods. The library integrates with PyTorch Geometric, NetworkX, rustworkx, and GeoDataFrames, preserving geometry and attributes across conversions. The accompanying paper by Sato, Pietrostefani, Mahabir, and Arribas-Bel was published in Computers, Environment and Urban Systems \(2026\), volume 130, article 102492. The library is available on GitHub at https://github.com/c2g-dev/city2graph.

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · Aug 13, 11:59

**「Background」** Urban data is often stored as flat feature tables, which lose the relational structure inherent in cities, such as how buildings connect to streets or how people move between areas. Heterogeneous graphs represent multiple types of nodes and edges, enabling more expressive models for tasks like urban planning and mobility prediction. City2Graph addresses the gap by providing a unified tool to construct such graphs from diverse geospatial data sources.

**「Impact」** Researchers and practitioners in urban computing and GeoAI can now use City2Graph to streamline the conversion of raw geospatial data into graph formats compatible with popular GNN frameworks, potentially accelerating work in urban analytics and machine learning. However, as a new tool, its adoption and long-term maintenance remain to be seen.

**Tags**: `#graph-neural-networks`, `#geospatial`, `#urban-computing`, `#python-library`, `#spatial-analysis`

**中文**

<a id="bilingual-item-9-zh"></a>
### [City2Graph：面向城市系统的异构图神经网络与空间分析 Python 库](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph 是一个新发布的 Python 库，用于将地理空间城市数据转换为异构图，以支持图神经网络（GNN）和空间分析。该库支持形态学、交通、流动性和邻近性图，并集成了 PyTorch Geometric 和 DuckDB。其论文已发表于《Computers, Environment and Urban Systems》第 130 卷，文章编号 102492，作者为 Sato、Pietrostefani、Mahabir 和 Arribas-Bel（2026 年）。该库支持从 OpenStreetMap 和 Overture Maps 构建建筑、街道和细分城市肌理的形态图，通过 DuckDB 处理 GTFS 和 GBFS 数据，并支持 OD 矩阵和流动数据。此外，它提供 KNN、Delaunay、Gilbert、Waxman 以及 queen/rook 邻接图，支持异构图和元路径，并能在 GeoDataFrames、NetworkX、rustworkx 和 PyTorch Geometric 之间进行转换。

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · 8月13日 11:59

**「背景」** 城市数据通常以平面特征表形式存储，但城市系统本质上是相互关联的实体网络，如建筑、街道和交通站点。异构图能够同时表示多种节点和边类型，更适合捕捉这些复杂关系。City2Graph 旨在填补将地理空间数据转换为图结构的工具空白，为 GNN 和空间分析提供标准化流程。

**「影响」** 对于从事城市计算、GeoAI 和空间分析的研究人员和开发者，City2Graph 提供了一种便捷的方式，将地理空间数据转换为可直接用于 GNN 的图结构，减少了数据预处理的工作量。该库的发布可能促进异构图神经网络在城市研究中的应用，但作为新工具，其广泛采用仍需时间。

**标签**: `#graph-neural-networks`, `#geospatial`, `#urban-computing`, `#python-library`, `#spatial-analysis`

---

**English**

<a id="bilingual-item-10-en"></a>
### [WorldProof: Diagnosing World-Model Failures and Pixel Metric Limits](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

The author introduces WorldProof, an open-source tool \(Apache-2.0, pip install worldproof\) for diagnosing world models that predict future frames from context and actions. It compares rollouts against ground truth and physical invariants, measuring metrics like PSNR, SSIM, LPIPS, latent prediction error, calibration, and object permanence, without scoring task success. Validation on real robot video revealed that pixel metrics often cannot rank models: a last-frame baseline \(predicting no change\) achieved 0.983 SSIM and 53.9 dB PSNR on a 30fps SO-101 arm recording \(64 rollouts, 6-step horizon, dynamic-region masked\), with error not growing over the horizon. On DROID footage \(15fps, 48 steps\), the baseline showed three regimes: near-perfect ties at steps 1-3, steep monotonic decline from steps 4-24 \(the only separable window\), and a floor around 0.20 SSIM and 10.3 dB from step 28 onward. The author argues that evaluation setups, not metrics, often lack discriminative power, and recommends reporting horizon curves rather than summary scalars, as including step 0 inflates averages \(e.g., 119.8 dB at step 0 dragged the scalar from ~32 to 53.9\).

reddit · r/MachineLearning · /u/georgia\_bucea · Aug 13, 19:58

**「Background」** World models are machine learning systems that predict future video frames given an initial context and a sequence of actions, often used in robotics and simulation. Evaluating these models typically relies on pixel-level metrics such as SSIM and PSNR, which compare predicted frames against ground truth. However, recent benchmarks like WorldBench have highlighted challenges in assessing physical fidelity, and the effectiveness of pixel metrics on real-world data remains an open question. The tool described in the post, worldproof, is an open-source diagnostic that aims to identify where and why world-model predictions fail, using both pixel metrics and physical invariants.

**「Impact」** Researchers and engineers evaluating world models on real robot video should measure horizon curves and identify the separable window \(e.g., 8-24 steps for DROID-like footage\) rather than relying on summary scalars, as trivial baselines can tie or beat models outside that window, making rankings meaningless.

<details><summary>References</summary>
<ul>
<li><a href="https://world-bench.github.io/">WorldBench: How Close are World Models to the Physical World?</a></li>

</ul>
</details>

**Tags**: `#world models`, `#evaluation metrics`, `#robotics`, `#open source`, `#machine learning`

**中文**

<a id="bilingual-item-10-zh"></a>
### [worldproof：诊断世界模型预测失效并测量像素指标何时无法对模型排序](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

开源工具 worldproof（Apache-2.0，可通过 pip install worldproof 安装）用于诊断世界模型（根据起始上下文和动作序列预测未来帧的模型）的预测失败，通过将 rollout 与真实情况以及物理不变量进行比较，指出预测在何处以及为何失效。在验证过程中，作者发现像素指标（如 SSIM 和 PSNR）在真实机器人视频上往往无法对模型进行排序：在 SO-101 手臂记录（30fps，三摄像头，64 次 rollout，6 步 horizon，仅对动态区域评分）上，复制最后帧的基线（预测“无变化”）获得了 0.983 的 SSIM 和 53.9 dB 的 PSNR，且误差不随 horizon 增长（步骤 1 到 6 的 SSIM 在 0.893 到 0.972 之间波动），导致所有模型得分相近，评估无法区分优劣。在 DROID 数据（15fps，64 次 rollout，48 步）上，基线在步骤 1-3 表现接近完美（SSIM 约 0.87），步骤 4-24 呈单调下降（SSIM 从 0.797 降至 0.260），步骤 28 之后触底（SSIM 约 0.20，PSNR 约 10.3 dB），预测完全去相关，因此可用的评估窗口约为 8 到 24 步，且该窗口取决于帧率与任务速度的比值，而非通用常数。工具还报告了 n=8 与 n=64 的差异（动态 PSNR 从 48.2 dB 变为 53.9 dB），并指出包含步骤 0 会因高帧率而虚增汇总标量（例如 30fps 下步骤 0 的 PSNR 为 119.8 dB，将平均值从约 32 拉高到 53.9），因此建议报告曲线而非标量。

reddit · r/MachineLearning · /u/georgia\_bucea · 8月13日 19:58

**「背景」** 世界模型（world model）是一类根据初始帧和动作序列预测未来帧的机器学习模型，常用于机器人操作和视频预测。评估这类模型通常使用像素级指标（如 SSIM、PSNR）来比较预测与真实帧的相似度，但这些指标在真实数据上的有效性可能受限。已有的基准如 WorldBench 通过视频预测和物理模拟来评估世界模型的物理理解能力，但尚未系统研究像素指标在真实机器人视频上的判别力。

**「影响」** 对于使用像素指标评估世界模型的研究者和工程师，该发现表明在真实机器人视频上，简单的“最后帧复制”基线可能获得高分且误差不随 horizon 增长，导致现有评估设置无法区分模型优劣；因此，评估时应测量自身数据上的有效 horizon 窗口（如 DROID 上约 8-24 步），并优先报告曲线而非汇总标量，以避免帧率带来的虚高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://world-bench.github.io/">WorldBench: How Close are World Models to the Physical World?</a></li>

</ul>
</details>

**标签**: `#world models`, `#evaluation metrics`, `#robotics`, `#open source`, `#machine learning`

---

**English**

<a id="bilingual-item-11-en"></a>
### [Ablating One Attention Head Breaks Chess Transformer&\#x27;s Sacrifice Finding](https://www.reddit.com/r/MachineLearning/comments/1vmvl4w/chessformer_lens_demo_ablating_1_of_a_chess/) ⭐️ 7.0/10

A Reddit post on r/MachineLearning demonstrates that ablating a single attention head in a chess transformer, named chessformer\_lens, causes the model to stop finding Morphy&\#x27;s queen sacrifice. The demo includes GIFs and links to GitHub notebooks for replication. This finding highlights the critical role of specific attention heads in learned behaviors, offering a concrete example of mechanistic interpretability in transformers. The post is brief and lacks detailed analysis, but the reproducible nature of the result makes it valuable for understanding transformer internals.

reddit · r/MachineLearning · /u/Weird-Asparagus4136 · Aug 13, 00:29

**「Background」** Mechanistic interpretability aims to reverse-engineer the internal computations of neural networks, often by studying attention heads in transformers. Ablation studies, where parts of a model are removed or disabled, help identify which components are responsible for specific behaviors. Morphy&\#x27;s queen sacrifice is a famous chess tactic from a historic game, used here as a test case for the model&\#x27;s ability to recognize complex patterns.

**「Impact」** This demonstration provides evidence that individual attention heads can be responsible for specific high-level behaviors in transformers, which could inform future interpretability research and model debugging. However, the result is from a single demo and may not generalize across all models or tasks.

**Tags**: `#mechanistic interpretability`, `#transformers`, `#chess AI`, `#attention heads`, `#ablation study`

**中文**

<a id="bilingual-item-11-zh"></a>
### [消融单个注意力头使国际象棋 Transformer 无法找到 Morphy 后翼弃兵](https://www.reddit.com/r/MachineLearning/comments/1vmvl4w/chessformer_lens_demo_ablating_1_of_a_chess/) ⭐️ 7.0/10

一个名为 chessformer\_lens 的演示表明，在国际象棋 Transformer 的 128 个注意力头中消融一个头，会导致模型无法找到 Morphy 的后翼弃兵。该演示由 Reddit 用户 Weird-Asparagus4136 发布在 r/MachineLearning 上，并提供了 GitHub 上的可复现笔记本。这一结果凸显了特定注意力头在模型学习行为中的关键作用，对机械可解释性研究具有实际意义。演示内容简短，但提供了具体的复现路径。

reddit · r/MachineLearning · /u/Weird-Asparagus4136 · 8月13日 00:29

**「背景」** 机械可解释性旨在理解神经网络内部机制，注意力头是 Transformer 模型中的关键组件，负责处理输入序列的不同部分。国际象棋 Transformer 通过自监督学习掌握棋局模式，Morphy 的后翼弃兵是一个著名的战术组合，模型需要识别并执行这一系列走法。消融研究通过移除或禁用特定组件来观察其对模型行为的影响，从而推断该组件的功能。

**「影响」** 对于研究 Transformer 内部机制的开发者，这一演示提供了具体证据，表明单个注意力头可能对特定高级行为至关重要，挑战了分布式表示的传统观点。然而，该结果基于单一模型和单一行为，其普遍性尚待验证。

**标签**: `#mechanistic interpretability`, `#transformers`, `#chess AI`, `#attention heads`, `#ablation study`

---

**English**

<a id="bilingual-item-12-en"></a>
### [Claude Chrome Extension Syncs Sessions Across Devices](https://techmymoney.com/2026/08/12/claude-in-chrome-now-carries-your-session-to-the-desktop/) ⭐️ 7.0/10

Anthropic has rebuilt its Claude Chrome extension to run as full Cowork sessions, allowing tasks started in the browser to continue on desktop, web, and mobile apps, with conversations, skills, and connectors synced to the account. The update is available today for Max and Team users, with Pro users gaining access in the coming weeks, while enterprise deployments have it disabled by default and require admin enablement. A new &\#x27;auto-approve&\#x27; permission mode compares actions like form submissions, messages, and file downloads against original instructions, but purchases and personal data still require manual confirmation. Anthropic acknowledges that these measures reduce but do not eliminate risks, as malicious instructions on web pages remain a challenge. Local files, other Chromium browsers, and mobile devices are not yet supported.

telegram · zaihuapd · Aug 13, 04:10

**「Background」** Anthropic&\#x27;s Claude is an AI assistant that can be used through a Chrome extension, which previously kept sessions confined to the browser tab where they started. The extension is part of Anthropic&\#x27;s broader &\#x27;Cowork&\#x27; initiative, which aims to integrate Claude more deeply into users&\#x27; workflows across different platforms. This update transforms the Chrome extension into a full Cowork client, allowing sessions, skills, and connectors to sync across devices via the user&\#x27;s account.

**「Impact」** Max and Team subscribers can now seamlessly move Claude-assisted work between browser and desktop without losing context, improving workflow continuity, while Pro users will gain the same capability within weeks; however, enterprise users must wait for admin approval, and the lack of support for local files and non-Chrome browsers limits the feature&\#x27;s reach.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-in-chrome-cross-device-sync-desktop-mobile-web-august-2026">Claude in Chrome Cross-Device Sync: Pro, Max, Team (2026) | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://www.macobserver.com/news/claude-in-chrome-is-now-a-full-cowork-session-across-all-claude-apps/">Claude in Chrome Is Now a Full Cowork Session Across All Claude Apps</a></li>
<li><a href="https://thenewstack.io/claude-chrome-cowork-sessions/">Anthropic&#x27;s Chrome extension is now a Cowork session - The New Stack</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#Chrome extension`, `#AI tools`, `#cross-device`

**中文**

<a id="bilingual-item-12-zh"></a>
### [Claude 浏览器会话可续传桌面端，技能与连接器跨设备同步](https://techmymoney.com/2026/08/12/claude-in-chrome-now-carries-your-session-to-the-desktop/) ⭐️ 7.0/10

Anthropic 重构了 Claude 的 Chrome 扩展，使其以完整 Cowork 会话运行，用户可以在浏览器中开始任务，并延续到桌面、网页和移动 App，对话、技能与连接器随账户同步。Max 和 Team 用户今日可用，Pro 用户将在未来几周内获得访问权限，企业版默认关闭，需由管理员启用。新增的“自动批准”模式允许某些操作自动执行，但表单提交、消息和文件下载等操作会与原指令比对，购买和个人数据仍需人工确认。Anthropic 承认这些措施能降低风险但无法完全消除，网页内恶意指令仍是难题。目前本地文件、其他 Chromium 浏览器和移动端暂不支持该功能。

telegram · zaihuapd · 8月13日 04:10

**「背景」** Anthropic 的 Claude 此前作为 Chrome 扩展运行时，会话通常局限于发起它的标签页，用户无法在桌面、网页或移动端无缝继续任务。此次更新将扩展重构为完整的 Cowork 会话客户端，使对话、技能和连接器随账户跨设备同步，用户无需在 Chrome 内重新配置已关联的技能和连接器。

**「影响」** 对于使用 Claude Chrome 扩展的 Max 和 Team 用户，这一更新将显著提升跨设备工作流的连续性，减少重复操作，但企业用户需等待管理员启用，且安全限制可能影响自动化程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-in-chrome-cross-device-sync-desktop-mobile-web-august-2026">Claude in Chrome Cross-Device Sync: Pro, Max, Team (2026) | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://www.macobserver.com/news/claude-in-chrome-is-now-a-full-cowork-session-across-all-claude-apps/">Claude in Chrome Is Now a Full Cowork Session Across All Claude Apps</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#Chrome extension`, `#AI tools`, `#cross-device`

---

## Financial News / 财经新闻

**English**

<a id="bilingual-item-13-en"></a>
### [S&amp;P 500 Profit Margins Hit Record High, Boosting Stocks](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 8.0/10

S&amp;P 500 companies&\#x27; net profit margin reached a record 16.9% in the second quarter, up from 14.8% in the first quarter and 12.9% a year ago, according to FactSet data. This is the highest since FactSet began tracking in 2009, driven by strong demand and contributions from mega-caps like Alphabet and Amazon.

rss · CNBC Finance · Aug 13, 20:21

**「Background」** Net profit margin is the percentage of revenue a company keeps after paying all expenses. The five-year average for the S&amp;P 500 is 12.4%, so the current figure is well above the norm. Eight of 11 sectors reported higher margins than a year ago, led by technology and communication services.

**「Impact」** Higher profit margins mean companies are more efficient at converting sales into profit, which supports stock valuations and can benefit investors. However, competitive pressure in tech could pose a future risk to margins, according to Vanguard economist Adam Schickling.

**Tags**: `#S&amp;P 500`, `#profit margins`, `#earnings`, `#stock market`, `#FactSet`

**中文**

<a id="bilingual-item-13-zh"></a>
### [标普 500 利润率创历史新高，推动股市持续上涨](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 8.0/10

标普 500 指数公司第二季度的净利润率（即扣除所有费用后保留的销售收入比例）达到创纪录的 16.9%，高于第一季度的 14.8%和去年同期的 12.9%，也远高于五年平均水平的 12.4%。这一数据来自 FactSet 的估算，若最终确认，将是自 2009 年该机构开始追踪该指标以来的最高水平。

rss · CNBC Finance · 8月13日 20:21

**「背景」** 净利润率衡量的是公司从每 1 美元销售额中最终保留的利润比例。FactSet 的数据显示，Alphabet 和亚马逊是这一创纪录利润率的最大贡献者，但即使剔除这两家公司，标普 500 的利润率仍达到 15%的创纪录水平。

**「影响」** 利润率上升意味着企业盈利增长强劲，这为股市的持续上涨提供了基本面支撑。不过，科技行业面临竞争压力，未来利润率可能受到挑战。

**标签**: `#S&amp;P 500`, `#profit margins`, `#earnings`, `#stock market`, `#FactSet`

---

**English**

<a id="bilingual-item-14-en"></a>
### [CXMT Overtakes Tencent as Most Valuable Chinese Company](https://www.bloomberg.com/news/articles/2026-08-13/cxmt-overtakes-tencent-to-become-most-valuable-chinese-company) ⭐️ 8.0/10

CXMT, a Chinese memory chip maker, has overtaken Tencent to become the most valuable Chinese company by market capitalization, with a market cap of $524 billion versus Tencent&\#x27;s $510 billion. This follows CXMT&\#x27;s Shanghai IPO last month, where shares surged 467% on the first day and have since risen another 8%.

telegram · zaihuapd · Aug 13, 10:10

**「Background」** CXMT, a Chinese memory chip maker, listed on Shanghai&\#x27;s STAR Market last month, with its shares surging nearly 470% on the first day of trading, making it one of the year&\#x27;s most notable IPOs.

**「Impact」** This shift reflects investor enthusiasm for semiconductor companies amid China&\#x27;s push for chip self-sufficiency, while Tencent has faced pressure due to increased AI investments and a year-to-date decline of over 26%.

<details><summary>References</summary>
<ul>
<li><a href="https://cn.investing.com/analysis/article-200500820">Aurra Markets： 长 鑫 存 储 （ CXMT ） 上 海 IPO ... | Investing.com</a></li>

</ul>
</details>

**Tags**: `#CXMT`, `#Tencent`, `#market cap`, `#IPO`, `#China tech`

**中文**

<a id="bilingual-item-14-zh"></a>
### [长鑫存储市值超越腾讯，成为中国市值最高公司](https://www.bloomberg.com/news/articles/2026-08-13/cxmt-overtakes-tencent-to-become-most-valuable-chinese-company) ⭐️ 8.0/10

长鑫存储（CXMT）市值达到 5240 亿美元，超越腾讯的 5100 亿美元，成为中国市值最高的公司。该公司上月在上海上市首日暴涨 467%，而腾讯因加大 AI 投入股价下跌。

telegram · zaihuapd · 8月13日 10:10

**「背景」** 长鑫存储（CXMT）是一家中国存储芯片制造商，上月在上海科创板上市，首日股价飙升近 470%。此次市值超越腾讯，主要受其 IPO 后股价持续上涨推动，而腾讯因加大 AI 投入股价下跌。

**「影响」** 这一变化反映了市场对中国半导体行业的看好，可能吸引更多投资者关注芯片领域，同时腾讯的股价下跌可能影响其投资者信心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cn.investing.com/analysis/article-200500820">Aurra Markets： 长 鑫 存 储 （ CXMT ） 上 海 IPO ... | Investing.com</a></li>

</ul>
</details>

**标签**: `#CXMT`, `#Tencent`, `#market cap`, `#IPO`, `#China tech`

---

**English**

<a id="bilingual-item-15-en"></a>
### [Bill Ackman&\#x27;s Pershing Square Re-enters Netflix, Citing Streaming Victory](https://www.cnbc.com/2026/08/13/ackman-buys-netflix-again-four-years-later-says-it-won-streaming-wars.html) ⭐️ 7.0/10

Bill Ackman&\#x27;s Pershing Square Capital Management has disclosed a new stake in Netflix, saying the company has &quot;effectively won the streaming wars&quot; with over 325 million subscribers and an attractive valuation after a sharp sell-off. Netflix shares rose nearly 4% on the news.

rss · CNBC Finance · Aug 13, 18:04

**「Background」** Ackman previously bought Netflix in early 2022 but sold the entire stake about three months later after the company reported its first subscriber decline in over a decade, citing uncertainty about its business model. Since then, Netflix shares have fallen roughly 50% from their June 2025 high, cutting its valuation to about 21 times forward earnings from over 40 times.

**「Impact」** The disclosure signals confidence in Netflix&\#x27;s competitive position and could influence investor sentiment, potentially affecting the company&\#x27;s stock price and the broader streaming sector.

**Tags**: `#Netflix`, `#Bill Ackman`, `#Pershing Square`, `#Streaming`, `#Investments`

**中文**

<a id="bilingual-item-15-zh"></a>
### [比尔·阿克曼再次买入奈飞，称其已赢得流媒体战争](https://www.cnbc.com/2026/08/13/ackman-buys-netflix-again-four-years-later-says-it-won-streaming-wars.html) ⭐️ 7.0/10

比尔·阿克曼的潘兴广场资本管理公司在半年报中披露，已重新买入奈飞股票，称其拥有超过 3.25 亿订阅用户，已“有效赢得流媒体战争”，且估值在股价从 2025 年 6 月高点下跌约 50%后变得有吸引力。奈飞股价在消息公布后上涨近 4%。

rss · CNBC Finance · 8月13日 18:04

**「背景」** 阿克曼曾在 2022 年初大举买入奈飞，但在约三个月后因公司首次出现订阅用户下滑而清仓。当时他表示，公司商业模式的变化使其未来前景难以预测。

**「影响」** 这一投资可能提振投资者对奈飞及流媒体行业的信心，但具体影响尚不明确。

**标签**: `#Netflix`, `#Bill Ackman`, `#Pershing Square`, `#Streaming`, `#Investments`

---

**English**

<a id="bilingual-item-16-en"></a>
### [Chinese chipmaker YMTC overtakes Micron and Kioxia in NAND memory shipments](https://www.cnbc.com/2026/08/13/chinese-firm-tops-micron-kioxia-shipments-nand-memory-chips.html) ⭐️ 7.0/10

Yangtze Memory Technologies \(YMTC\) rose to third place in global NAND memory chip shipments in the second quarter, with a 14% share, surpassing Micron and Kioxia, according to Counterpoint Research. The company still trails Samsung and SK hynix, and its revenue from NAND chips remains below Micron and Kioxia.

rss · CNBC Finance · Aug 13, 02:59

**「Background」** NAND memory chips store data even when a device is off, and demand has been rising with AI servers. YMTC, a Chinese chipmaker, has been expanding its share in this market, reaching 13% in the first quarter of 2026, according to Counterpoint Research.

**「Impact」** YMTC&\#x27;s rise could pressure Micron and Kioxia in the NAND market, especially as data centers are expected to account for half of NAND demand by end of 2026, an area where YMTC currently lags.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/ymtc-nand-market-share-13-percent/">YMTC&#x27;s NAND flash market share surges to 13%, tying SanDisk and Micron</a></li>

</ul>
</details>

**Tags**: `#NAND memory`, `#YMTC`, `#market share`, `#semiconductors`, `#China`

**中文**

<a id="bilingual-item-16-zh"></a>
### [中国 YMTC 在 NAND 闪存芯片出货量上超越美光与铠侠，跃居全球第三](https://www.cnbc.com/2026/08/13/chinese-firm-tops-micron-kioxia-shipments-nand-memory-chips.html) ⭐️ 7.0/10

据 Counterpoint Research 数据，中国长江存储（YMTC）在 2026 年第二季度全球 NAND 闪存芯片出货量中占据 14%份额，超越美光和铠侠，升至第三位，仅次于三星和 SK 海力士。

rss · CNBC Finance · 8月13日 02:59

**「背景」** NAND 闪存是一种在断电后仍能保留数据的存储芯片，广泛应用于智能手机、电脑和数据中心。长期以来，该市场由三星、SK 海力士、铠侠、美光等少数几家厂商主导。

**「影响」** YMTC 的崛起可能加剧全球存储芯片市场的竞争，对美光、铠侠等现有厂商构成压力，并可能影响未来 NAND 芯片的定价和供应格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/13/chinese-firm-tops-micron-kioxia-shipments-nand-memory-chips.html">This Chinese firm has topped Micron and Kioxia in shipments of crucial NAND memory chips</a></li>

</ul>
</details>

**标签**: `#NAND memory`, `#YMTC`, `#market share`, `#semiconductors`, `#China`

---

**English**

<a id="bilingual-item-17-en"></a>
### [EVs Dominate China&\#x27;s Car Market: 5 Takeaways from Latest Auto Sales Data](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

New energy vehicles \(battery and hybrid cars\) captured 65.1% of new passenger car sales in China in July, up from 54% a year earlier, according to the China Passenger Car Association. However, overall passenger car sales for the year through July fell 20.3%, and new energy vehicle sales dropped 12.5% in the same period.

rss · CNBC Finance · Aug 13, 01:31

**「Background」** China&\#x27;s auto market has been shifting toward electric vehicles \(EVs\) for years, supported by government subsidies and consumer demand. However, recent data shows a slowdown: EV sales fell 13% in the first half of 2026, partly due to upcoming subsidy cuts, and overall passenger car sales have declined sharply.

**「Impact」** The shift toward electric vehicles affects automakers and consumers, as domestic brands like Geely and BYD gain market share, while foreign and gasoline-powered car makers face declining sales.

<details><summary>References</summary>
<ul>
<li><a href="https://www.carscoops.com/2026/07/china-ev-tax-break-cuts/">China’s Electrified Car Sales Sank 13%, And The World Is About To Feel It | Carscoops</a></li>

</ul>
</details>

**Tags**: `#China auto market`, `#EV sales`, `#Geely`, `#Tesla`, `#BYD`

**中文**

<a id="bilingual-item-17-zh"></a>
### [中国汽车市场 7 月数据：新能源车占比升至 65.1%，吉利销量领先](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

中国汽车市场 7 月新车销售中，新能源车（包括纯电和混动）占比达 65.1%，高于去年同期的 54%；但今年前 7 个月乘用车总销量同比下降 20.3%，新能源车销量也下降 12.5%。吉利旗下星愿电动 hatchback 以近 19.75 万辆成为最畅销车型，特斯拉 Model Y 以超 18 万辆紧随其后。

rss · CNBC Finance · 8月13日 01:31

**「背景」** 中国汽车市场正经历向新能源车的快速转型，但 2026 年整体销量下滑，部分原因是政府补贴减少。据行业数据，7 月新能源车占新车销量的 65.1%，高于一年前的 54%。

**「影响」** 这一趋势对传统燃油车制造商构成压力，尤其是外国品牌，如大众是唯一进入前十的传统外资车企，其燃油车型朗逸排名第九。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.carscoops.com/2026/07/china-ev-tax-break-cuts/">China’s Electrified Car Sales Sank 13%, And The World Is About To Feel It | Carscoops</a></li>

</ul>
</details>

**标签**: `#China auto market`, `#EV sales`, `#Geely`, `#Tesla`, `#BYD`

---

**English**

<a id="bilingual-item-18-en"></a>
### [China&\#x27;s Economic Slowdown Pushes Gig Work to 53 Million, Yet Oversupply Persists](https://www.ft.com/content/a3803e70-cb4d-444f-a31e-05be2f2c44f6?accessToken=zwAAAZ_5xcXzkdOjgD5wy01ET9OjHgW-LyxE9g.MEUCIQCWTIny3JTJV8e-PGyK0XL2tg5g_7Ay-rpKkwGZCpp1-AIgbMgJQPlqWgqAsX4s1k4gYaC4b8k0JveZOs35OJQvbZ4&amp;amp;sharetype=gift&amp;amp;token=7e8483bb-395d-429e-afca-2f4ab5ad150b) ⭐️ 7.0/10

China&\#x27;s economic slowdown has increased gig work to over 53 million food delivery and ride-hailing drivers as of 2025, up 10 million in two years, but oversupply is lowering incomes and lengthening wait times, with taxi drivers at some airports waiting up to 10 hours for passengers.

telegram · zaihuapd · Aug 13, 06:40

**「Background」** China&\#x27;s economic slowdown has reduced formal job opportunities, pushing many workers into the gig economy, which includes platform-based jobs like food delivery and ride-hailing. The number of gig workers has grown rapidly, but oversupply is leading to lower incomes and longer waiting times for work.

**「Impact」** Gig workers, particularly ride-hailing and delivery drivers, face reduced earnings and longer working hours due to oversupply, affecting their livelihoods.

<details><summary>References</summary>
<ul>
<li><a href="https://slguardian.org/chinas-gig-economy-expands-as-weak-job-market-pushes-millions-into-insecure-work/">China’s Gig Economy Expands as Weak Job Market Pushes Millions into Insecure Work</a></li>

</ul>
</details>

**Tags**: `#China economy`, `#gig economy`, `#labor market`, `#employment`, `#oversupply`

**中文**

<a id="bilingual-item-18-zh"></a>
### [中国经济放缓挤压就业，零工岗位增至 5300 万仍供过于求](https://www.ft.com/content/a3803e70-cb4d-444f-a31e-05be2f2c44f6?accessToken=zwAAAZ_5xcXzkdOjgD5wy01ET9OjHgW-LyxE9g.MEUCIQCWTIny3JTJV8e-PGyK0XL2tg5g_7Ay-rpKkwGZCpp1-AIgbMgJQPlqWgqAsX4s1k4gYaC4b8k0JveZOs35OJQvbZ4&amp;amp;sharetype=gift&amp;amp;token=7e8483bb-395d-429e-afca-2f4ab5ad150b) ⭐️ 7.0/10

中国经济放缓加剧就业压力，截至 2025 年，外卖和网约车司机等零工岗位人数超过 5300 万，两年内增加 1000 万，但供过于求导致收入下降、等待时间延长。

telegram · zaihuapd · 8月13日 06:40

**「背景」** 零工经济通常指通过平台接单的灵活就业，如外卖配送和网约车。近年来，中国房地产低迷、消费疲弱及制造业收缩导致传统就业岗位减少，零工经济成为吸纳过剩劳动力的重要渠道。

**「影响」** 零工从业者面临收入减少和工时延长，例如上海浦东、北京大兴和成都天府机场出租车司机排队等客最长分别达 7 小时、8 小时和 10 小时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://slguardian.org/chinas-gig-economy-expands-as-weak-job-market-pushes-millions-into-insecure-work/">China’s Gig Economy Expands as Weak Job Market Pushes Millions into Insecure Work</a></li>

</ul>
</details>

**标签**: `#China economy`, `#gig economy`, `#labor market`, `#employment`, `#oversupply`

---