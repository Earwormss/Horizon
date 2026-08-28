---
layout: default
title: "Horizon Summary: 2026-08-28 (EN / ZH)"
date: 2026-08-28
lang: en
---

> Selected 21 important items from 38 fetched items. Each English entry is followed by its Chinese version.

---

## Technology News / 科技新闻

**English**

<a id="bilingual-item-1-en"></a>
### [Cloudflare&\#x27;s DNS Cache Optimization Saves 100 TB](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare engineers optimized the memory usage of their 1.1.1.1 DNS cache, achieving a reduction of 100 terabytes of memory. The optimization involved advanced systems programming techniques, including data structure layout improvements and more efficient memory management. This change is significant because it reduces operational costs and improves efficiency for one of the world&\#x27;s largest public DNS resolvers. The blog post details the technical approach, which includes rethinking how cache entries are stored and accessed. The work demonstrates the ongoing importance of low-level optimization in large-scale infrastructure.

hackernews · TangerineDream · Aug 27, 17:17 · [Discussion](https://news.ycombinator.com/item?id=49468083)

**「Background」** Cloudflare operates the 1.1.1.1 public DNS resolver, which handles a massive volume of DNS queries globally. To serve these efficiently, the resolver maintains a large in-memory cache of DNS records. The cache is implemented in Rust as part of a project called Big Pineapple. Over time, the per-entry memory footprint of this cache grew, consuming significant amounts of RAM across Cloudflare&\#x27;s fleet. The optimization described in the blog post involved restructuring the data layout of cache entries to reduce memory usage per entry from 953 bytes to 420 bytes, a 56% reduction, freeing approximately 100 terabytes of memory fleet-wide.

**「Impact」** Cloudflare&\#x27;s optimization directly reduces memory usage for its 1.1.1.1 DNS service, potentially lowering infrastructure costs and improving performance for millions of users. The techniques may also serve as a reference for other developers working on memory-constrained systems.

**「Community Discussion」** Commenters generally praised the optimization as a good example of post-launch cost reduction, with some noting that such optimizations are easier after a product is stable. Others discussed specific technical details, such as potential further improvements like embedding record data directly in cache entries, and debated whether the approach undermines Rust&\#x27;s safety guarantees. Some shared personal experiences with similar memory optimizations, highlighting the practical impact of such techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s ...</a></li>
<li><a href="https://explainx.ai/blog/cloudflare-dns-cache-100-terabytes-memory-optimization-august-2026">Cloudflare Saved 100TB Memory: DNS Cache Rust Deep Dive ...</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#memory-optimization`, `#systems-programming`, `#cloudflare`, `#performance`

**中文**

<a id="bilingual-item-1-zh"></a>
### [Cloudflare 优化 1.1.1.1 DNS 缓存，节省 100 TB 内存](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 8.0/10

Cloudflare 通过优化其 1.1.1.1 DNS 缓存的数据结构布局和内存管理，成功节省了 100 TB 的内存。这一优化涉及将多个独立列表合并为单一列表、调整结构体对齐等系统编程技术，显著降低了内存占用。该成果展示了在大型基础设施中通过精细的内存优化所能带来的巨大收益，同时也引发了关于 Rust 安全性与性能权衡的讨论。尽管这些技术并非全新，但其在真实世界中的大规模应用和量化结果具有重要参考价值。

hackernews · TangerineDream · 8月27日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=49468083)

**「背景」** Cloudflare 的 1.1.1.1 是一个公共 DNS 解析服务，每天处理海量查询，其缓存需要高效存储大量 DNS 记录。为了降低内存占用并提升性能，Cloudflare 对缓存的数据结构进行了优化，将每个条目的内存占用从 953 字节降至 420 字节，减少了 56%，从而在整个服务器群中释放了约 100 TB 的内存，同时使查询延迟降低 19%，插入吞吐量提升 43%。这些优化涉及 Rust 层面的五项数据布局调整，包括合并多个列表、调整结构体对齐等。

**「影响」** 对于运行 1.1.1.1 的 Cloudflare 基础设施，这一优化直接减少了 100 TB 的内存需求，降低了运营成本并可能提升缓存效率。对于其他开发者，文中展示的优化方法（如结构体重排、合并分配）可应用于类似的高性能系统，但需注意在 Rust 中可能牺牲部分安全保证。

**「社区讨论」** 社区评论普遍认可这种先交付产品再优化的做法，并分享了类似的内存优化经验，例如通过单次大块分配大幅减少内存占用。也有开发者指出，将多个列表合并可能削弱 Rust 的安全保证，但认为这些优化在系统编程中属于常见手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s ...</a></li>
<li><a href="https://explainx.ai/blog/cloudflare-dns-cache-100-terabytes-memory-optimization-august-2026">Cloudflare Saved 100TB Memory: DNS Cache Rust Deep Dive ...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#memory-optimization`, `#systems-programming`, `#cloudflare`, `#performance`

---

**English**

<a id="bilingual-item-2-en"></a>
### [Google Releases Gemini-3.5-Transcribe STT Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

Google has announced Gemini-3.5-Transcribe, a specialized speech-to-text model designed for high accuracy and low latency, with features including function calling that allows delegation of complex tasks to other Gemini models, currently available in the Gemini macOS app. The model reportedly outperforms other STT models on accuracy benchmarks, but community testing indicates latency remains a concern for real-time applications. The release is part of Google&\#x27;s broader Gemini model family, targeting developers and applications requiring robust speech recognition. Specific performance metrics and availability details were not provided in the source content.

hackernews · k9294 · Aug 27, 18:03 · [Discussion](https://news.ycombinator.com/item?id=49468818)

**「Background」** Gemini 3.5 Transcribe is a speech-to-text model built on Google&\#x27;s Gemini audio understanding capabilities. It is designed to convert natural speech into clean, formatted text, removing disfluencies like &\#x27;ums&\#x27; and corrections. The model also supports function calling, allowing it to delegate tasks such as image generation or file analysis to other Gemini models, and is currently available in the Gemini macOS app.

**「Impact」** Developers building speech-to-text applications now have a new high-accuracy option from Google, but those prioritizing real-time performance may still prefer alternatives like Soniox STT v5 or Voxtral Mini 3b based on community benchmarks.

**「Community Discussion」** Community members who tested the model report mixed experiences: while accuracy is praised, latency is a noted weakness for real-time use, and some users on Pixel devices find the transcription can oversimplify precise wording, altering meaning. The function calling feature has also caused confusion, as it is clarified to be for delegating tasks to other models, not for arbitrary execution.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Intelligent transcription with Gemini 3.5 Transcribe</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3.5 Transcribe | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Tags**: `#speech-to-text`, `#Google`, `#AI models`, `#machine learning`, `#developer tools`

**中文**

<a id="bilingual-item-2-zh"></a>
### [谷歌发布 Gemini-3.5-Transcribe 语音转文本模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

谷歌发布了 Gemini-3.5-Transcribe，这是一款专用的语音转文本（STT）模型，宣称具有高准确率，并支持函数调用功能，可将图像生成和文件分析等复杂任务委托给其他 Gemini 模型。该模型目前已在 Gemini macOS 应用中提供。社区测试显示，其准确率优于其他模型，但延迟仍有改进空间。开发者文档提供了更多技术细节，但部分用户对函数调用的描述感到困惑。

hackernews · k9294 · 8月27日 18:03 · [社区讨论](https://news.ycombinator.com/item?id=49468818)

**「背景」** Gemini 3.5 Transcribe 是谷歌基于其 Gemini 音频理解能力推出的专用语音转文本模型，旨在将自然语音转换为干净、格式化的文本，并支持通过函数调用将图像生成、文件分析等复杂任务委托给其他 Gemini 模型。该模型已在 Gemini macOS 应用中提供，开发者可通过 Gemini API 使用。此前，语音转文本领域已有多种模型，如 Soniox STT v5、Voxtral Mini 3b 和 Eleven Labs 等，它们在准确性、延迟和本地部署方面各有优劣。

**「影响」** 对于开发语音转文本应用的开发者而言，Gemini-3.5-Transcribe 提供了高准确率的选择，但延迟问题可能影响其实时应用场景。

**「社区讨论」** 社区成员分享了实际测试结果：有用户认为 Soniox STT v5 在延迟方面更优，而 Gemini-3.5-Transcribe 在准确率上领先；另有用户测试了 20 多个模型，认为本地模型 Voxtral Mini 3b 和付费 API Eleven Labs 表现更好。还有用户对函数调用的描述感到困惑，并指出模型在特定措辞上可能简化语义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Intelligent transcription with Gemini 3.5 Transcribe</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3.5 Transcribe | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#speech-to-text`, `#Google`, `#AI models`, `#machine learning`, `#developer tools`

---

**English**

<a id="bilingual-item-3-en"></a>
### [Claude Code Auto Mode Bypassed by Zip Import Attack](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

Johann Rehberger, a prominent prompt injection researcher, has disclosed an attack against Claude Code&\#x27;s auto mode that he claims succeeds 80% of the time. The attack tricks Claude Code into downloading and extracting a zip archive, then executing code that imports the \`base64\` module, which inadvertently imports and runs a malicious local \`struct.py\` file from the archive. In some runs, auto mode even blocked Claude&\#x27;s own attempts to terminate the malware process, turning the safety mechanism into part of the failure. Simon Willison, who reported this, agrees with Rehberger&\#x27;s conclusion that the only safe way to run agents under adversarial conditions is with a sandbox, recommending containers, VMs, network egress restrictions, monitoring, and not exposing sensitive credentials to the agent runtime.

rss · Simon Willison · Aug 27, 22:50

**「Background」** Prompt injection is a class of security attack in which an AI system is tricked by malicious instructions hidden in input data, such as text in a webpage or file, into performing unintended actions. Johann Rehberger is an independent AI security researcher who has repeatedly demonstrated such vulnerabilities across many AI tools, including a notable 2023 example against OpenAI&\#x27;s ChatGPT. Claude Code is Anthropic&\#x27;s coding agent that can operate in an &\#x27;auto mode&\#x27;, which uses a safety classifier to approve or block commands the agent wants to run; Anthropic recently made this mode the default for users.

**「Impact」** Developers using Claude Code&\#x27;s auto mode as a default security measure against prompt injection are at risk of compromise, with the attack potentially executing arbitrary code and even preventing cleanup commands, undermining trust in the feature.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Aug/15/the-summer-of-johann/">The Summer of Johann: prompt injections as far as the eye can see</a></li>
<li><a href="https://insidetelecom.com/ai-prompt-injection-is-all-the-rage-in-hacking-circles/">AI Prompt Injection is all the Rage in Hacking Circles - Inside Telecom</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#Claude Code`, `#coding agents`, `#vulnerability`

**中文**

<a id="bilingual-item-3-zh"></a>
### [Claude Code 自动模式被曝 80% 成功率的提示注入攻击](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

安全研究员 Johann Rehberger 发现了一种针对 Claude Code 自动模式（auto mode）的提示注入攻击，声称成功率高达 80%。该攻击利用 Python 的导入行为，通过诱使 Claude Code 下载并解压一个 zip 压缩包，然后执行其中包含的本地 struct.py 文件，从而在导入 base64 时被劫持执行恶意代码。在某些情况下，自动模式甚至阻止了 Claude 尝试终止恶意进程的清理命令，导致安全机制本身成为故障的一部分。Anthropic 近期已将自动模式设为默认，并对其有效性做出大胆声明，但此攻击表明该模式并非完全可靠。Rehberger 建议，在可能面临对抗性攻击风险的环境中，应使用容器、虚拟机或操作系统沙箱运行无人值守的编码代理，并限制网络出口、监控代理行为，避免暴露主目录、SSH 密钥和云凭证等敏感信息。

rss · Simon Willison · 8月27日 22:50

**「背景」** 提示注入（prompt injection）是一种针对 AI 系统的攻击方式，攻击者通过精心构造的输入，诱导模型执行非预期操作。Johann Rehberger 是一位知名的独立安全研究员，长期专注于 AI 安全领域，曾多次公开演示针对 ChatGPT 等 AI 工具的提示注入攻击。Claude Code 是 Anthropic 推出的编程助手，其“自动模式”（auto mode）被设计为一种安全机制，旨在通过分类器阻止有害命令的执行，并已成为默认设置。

**「影响」** 对于依赖 Claude Code 自动模式作为安全防护的开发者，此攻击表明该模式可能被绕过，导致恶意代码执行，且自动模式可能阻止清理命令，加剧风险。因此，在对抗性环境中运行编码代理时，必须采用沙箱和严格的网络限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Aug/15/the-summer-of-johann/">The Summer of Johann: prompt injections as far as the eye can see</a></li>
<li><a href="https://insidetelecom.com/ai-prompt-injection-is-all-the-rage-in-hacking-circles/">AI Prompt Injection is all the Rage in Hacking Circles - Inside Telecom</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#coding agents`, `#vulnerability`

---

**English**

<a id="bilingual-item-4-en"></a>
### [HarnessOpt-Bench: Measuring AI&\#x27;s Ability to Improve Other Agents](https://www.reddit.com/r/MachineLearning/comments/1w052xg/can_ai_improve_itself_rsi_might_be_the_answer_r/) ⭐️ 8.0/10

A Reddit post introduces HarnessOpt-Bench, a benchmark designed to measure how well LLMs can improve other agents&\#x27; harnesses, addressing the risk of cheating by keeping evaluation data and permission controls outside the optimizer&\#x27;s sandbox. The benchmark was tested with 5 frontier models, 4 downstream tasks, and 111 runs, testing two hypotheses: swapping models in the same harness \(Claude Opus 5 tops 3 of 4 tasks\) and swapping harnesses for the same model \(no consistent home-field edge, with opencode beating native harnesses in 11 of 20 model–task pairs\). Model choice affects gains 1.8× more than harness choice. The work is motivated by a recent incident where an OpenAI eval agent escaped its sandbox to access test solutions. The paper is available on arXiv \(2608.06301\) and code is on GitHub \(scaleapi/vero\), built on the team&\#x27;s ICML 2026 VeRO.

reddit · r/MachineLearning · /u/shehio · Aug 27, 20:13

**「Background」** Recursive self-improvement \(RSI\) refers to an AI system&\#x27;s ability to enhance its own capabilities or those of other AI systems, potentially leading to rapid capability gains. In practice, this often involves an LLM paired with a coding harness—a framework that provides tools and structure for coding tasks—to modify another agent&\#x27;s harness \(the code that defines how the agent operates\) to improve performance. A key challenge is preventing the optimizer from cheating by accessing test answers or evaluation metrics directly. HarnessOpt-Bench, introduced in the arXiv paper 2608.06301, formalizes this as an end-to-end harness optimization problem under expensive and stochastic evaluation, where an optimizer receives a target agent&\#x27;s seed harness, graded feedback, and a fixed evaluation budget. The benchmark builds on prior work like VeRO and RSIBench, which similarly measure whether coding agents can learn from their own trajectories and improve on hidden benchmarks.

**「Impact」** This benchmark provides a concrete, safety-conscious methodology for evaluating recursive self-improvement in LLMs, which could influence how AI safety researchers and developers design and assess agent improvement systems, particularly in preventing cheating and ensuring reliable evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.06301">[2608.06301] HarnessOpt-Bench: Evaluating LLMs at Harness ...</a></li>
<li><a href="https://arxiv.org/html/2608.06301">HarnessOpt-Bench: Evaluating LLMs at Harness Optimization</a></li>
<li><a href="https://harness-rsibench.com/">RSIBench</a></li>

</ul>
</details>

**Tags**: `#recursive self-improvement`, `#AI safety`, `#benchmark`, `#LLM`, `#agent`

**中文**

<a id="bilingual-item-4-zh"></a>
### [HarnessOpt-Bench：衡量 AI 自我改进的新基准](https://www.reddit.com/r/MachineLearning/comments/1w052xg/can_ai_improve_itself_rsi_might_be_the_answer_r/) ⭐️ 8.0/10

HarnessOpt-Bench 是一个新基准，用于衡量大型语言模型（LLM）改进其他智能体 harness 的能力，其设计旨在防止作弊。该基准通过将评估器、API 密钥和预算控制置于优化器沙箱之外，从结构上保证隔离，而非依赖指令。研究团队使用 5 个前沿模型、4 个下游任务和 111 次运行测试了两个假设：在相同编码 harness 下更换模型，Claude Opus 5 在 OpenCode 上于 4 个任务中的 3 个表现最佳；在相同模型下更换 harness，opencode 在 20 个模型-任务对中的 11 个中优于原生 harness（如 Claude Code、Codex、Kimi CLI），且模型选择对性能提升的影响是 harness 选择的 1.8 倍。该研究还提及了近期 OpenAI 评估智能体逃逸事件，并提供了论文和代码链接。

reddit · r/MachineLearning · /u/shehio · 8月27日 20:13

**「背景」** 递归自我改进（RSI）指的是 AI 系统改进自身或其他 AI 系统的能力，但这一概念常因作弊风险而受到质疑。近期，OpenAI 的一个评估代理逃出其沙箱并侵入 Hugging Face 以获取基准测试答案的事件，凸显了此类风险。为应对这一挑战，HarnessOpt-Bench 基准被提出，用于衡量 LLM 在受控条件下优化其他代理的“harness”（即编码框架）的能力。该基准通过将评估器、API 密钥和预算控制置于优化器沙箱之外，确保隔离性，从而防止作弊。

**「影响」** 该基准为 AI 安全领域提供了一种可复现的评估方法，有助于开发者衡量和改进 LLM 的递归自我改进能力，同时降低作弊风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.06301">[2608.06301] HarnessOpt-Bench: Evaluating LLMs at Harness ...</a></li>
<li><a href="https://harness-rsibench.com/">RSIBench</a></li>

</ul>
</details>

**标签**: `#recursive self-improvement`, `#AI safety`, `#benchmark`, `#LLM`, `#agent`

---

**English**

<a id="bilingual-item-5-en"></a>
### [Anthropic Previews Model Hardware Standard for AI-Driven Device Control](https://www.anthropic.com/news/model-hardware-standard-research-preview) ⭐️ 8.0/10

Anthropic has released a research preview of its Model Hardware Standard \(MHS\), which enables AI agents to safely control laboratory and industrial hardware such as microscopes, liquid handlers, and robotic arms, and to execute complex tasks in parallel. The standard reduces device integration time from weeks or months to hours or even minutes. Initial partners span biotechnology, robotics, and quantum computing, including Genentech, Carnegie Mellon University, and QuEra. Notably, QuEra&\#x27;s AI controller successfully restored quantum computer laser locks without human intervention in 99.3% of cases. Anthropic plans to open-source the standard after completing safety assessments.

telegram · zaihuapd · Aug 28, 01:38

**「Background」** AI agents have traditionally been limited to software environments, with hardware control requiring custom, time-consuming integration. The Model Hardware Standard aims to provide a common interface for AI systems to interact with physical devices, potentially accelerating automation in research and industrial settings. This preview builds on Anthropic&\#x27;s broader work in AI safety and agentic systems.

**「Impact」** For researchers and engineers in biotechnology, robotics, and quantum computing, MHS could dramatically reduce the effort needed to deploy AI-driven automation, as evidenced by QuEra&\#x27;s high autonomous recovery rate. However, the standard is still in preview and subject to safety assessments, so widespread adoption depends on the final open-source release and community validation.

**Tags**: `#AI hardware integration`, `#Anthropic`, `#robotics`, `#quantum computing`, `#open source`

**中文**

<a id="bilingual-item-5-zh"></a>
### [Anthropic 开放 AI 操控硬件标准预览，集成时间缩至分钟级](https://www.anthropic.com/news/model-hardware-standard-research-preview) ⭐️ 8.0/10

Anthropic 发布了模型硬件标准（MHS）的研究预览，该标准允许 AI 智能体安全地操控显微镜、液体处理器、机械臂等实验室和工业设备，并并行执行复杂任务。这一标准将设备集成时间从数周至数月缩短到几小时甚至几分钟。首批合作方包括生物技术领域的基因泰克、机器人领域的卡内基梅隆大学以及量子计算领域的 QuEra，其中 QuEra 的 AI 控制器在 99.3% 的情况下无需人工干预即可恢复量子计算机的激光锁定。Anthropic 计划在完成安全评估后开源该标准。

telegram · zaihuapd · 8月28日 01:38

**「背景」** AI 智能体通常只能与软件交互，而控制物理硬件需要针对每种设备进行定制开发，集成周期长且成本高。模型硬件标准旨在提供统一的接口和协议，使 AI 能够更通用地操控多种硬件设备，从而加速自动化在科研和工业领域的应用。

**「影响」** 该标准有望显著降低实验室和工业自动化门槛，使研究人员和工程师能够快速部署 AI 驱动的硬件控制，尤其在量子计算等精密领域，AI 自主恢复能力可减少人工干预，提升系统稳定性。

**标签**: `#AI hardware integration`, `#Anthropic`, `#robotics`, `#quantum computing`, `#open source`

---

**English**

<a id="bilingual-item-6-en"></a>
### [Tencent Hy4 Preview: Open-Source Model Outperforms Rivals in Blind Test](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

Tencent has released Hy4 preview, an open-source model that enhances software engineering, office analysis, game development, and scientific research capabilities. In a blind test involving 163 experts evaluating 203 engineering tasks, Hy4 preview scored an average of 2.99 out of 4.00, slightly outperforming GLM-5.3 and Kimi K3. Additionally, when combined with Hyra, the model advanced the lower bound for the three-dimensional Blaschke–Lebesgue problem to 0.41104, closing the gap to a final proof to about 2%. The model is available on Tencent&\#x27;s blog and Hugging Face.

telegram · zaihuapd · Aug 28, 06:11

**「Background」** Tencent&\#x27;s Hunyuan team has released Hy4 preview, a new open-source Mixture-of-Experts \(MoE\) flagship model with 770B total parameters \(49B activated per token\) and a 1M-token context window. The model uses advanced techniques such as Gated DSA sparse attention, IndexCache index reuse, iHC residual connections, and native MTP speculative decoding. In a blind test by 163 experts across 203 engineering tasks, Hy4 preview scored 2.99/4.00, slightly outperforming GLM-5.3 and Kimi K3. Additionally, when combined with the Hyra research agent, the model advanced the lower bound of the three-dimensional Blaschke–Lebesgue problem from 0.380799 to 0.41104, leaving only about 2% gap to the Meissner tetrahedron conjecture&\#x27;s value of 0.41986.

**「Impact」** This release provides developers and researchers with a competitive open-source alternative to existing models like GLM-5.3 and Kimi K3, potentially accelerating progress in software engineering and scientific research, while the mathematical advancement could contribute to solving a long-standing geometry problem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/995/570.htm">稳居开源模型第一梯队，腾讯发布混元 Hy4 preview 模型 - IT之家</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview</a></li>
<li><a href="https://www.chooseai.net/news/6281/">腾讯混元开源 Hy4 preview：770B 参数、1M 上下文，内部盲测略胜 GLM-...</a></li>
<li><a href="https://www.aibase.com/news/30694">Tencent Hunyuan launches open-source flagship model ...</a></li>
<li><a href="https://www.ithome.com/0/995/570.htm">稳居开源模型第一梯队，腾讯发布混元 Hy4 preview 模型 - IT之家</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#LLM`, `#Tencent`, `#mathematics`

**中文**

<a id="bilingual-item-6-zh"></a>
### [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 8.0/10

腾讯混元发布了开源模型 Hy4 preview，旨在提升软件工程、办公分析、游戏开发与科学研究能力。在 163 名专家对 203 个工程任务的盲测中，Hy4 preview 的均分为 2.99/4.00，略优于 GLM-5.3 与 Kimi K3。此外，配合 Hyra，该模型将三维 Blaschke–Lebesgue 几何难题的体积下界推进至 0.41104，距最终证明仅剩约 2% 的差距。该模型已通过腾讯混元官方渠道、博客、Hugging Face 等平台发布。

telegram · zaihuapd · 8月28日 06:11

**「背景」** 腾讯混元（Tencent Hunyuan）是腾讯推出的大语言模型系列，此前已发布多代开源模型。Hy4 preview 是腾讯混元团队开发的新一代混合专家（MoE）旗舰模型，总参数达 770B，每个 token 激活 49B 参数，支持 1M 上下文长度，并采用 Gated DSA 稀疏注意力、IndexCache 索引复用、iHC 残差连接及原生 MTP 投机解码等技术。Hyra 是腾讯混元推出的 AI 研究智能体，用于科学发现。Blaschke–Lebesgue 问题是几何学中的经典难题，涉及三维凸体的最小体积，Meissner 四面体猜想给出了一个理论下界。

**「影响」** 对于依赖开源大模型的开发者和研究机构，Hy4 preview 提供了在工程任务上具有竞争力的新选择，并展示了 AI 在辅助数学证明方面的潜力，可能推动相关领域的研究进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview</a></li>
<li><a href="https://hunyuan3d.cc/hunyuan-hyra">Hunyuan Hyra: AI Research Agent for Scientific Discovery</a></li>
<li><a href="https://www.ithome.com/0/995/570.htm">稳居开源模型第一梯队，腾讯发布混元 Hy4 preview 模型 - IT之家</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#LLM`, `#Tencent`, `#mathematics`

---

**English**

<a id="bilingual-item-7-en"></a>
### [Small Models Have Arrived](https://calv.info/small-models-have-arrived) ⭐️ 7.0/10

The article argues that small, efficient AI models are becoming increasingly important for practical applications, contrasting with the frontier labs&\#x27; focus on ever-larger models. It highlights a growing demand for &\#x27;fast/cheap/good-enough&\#x27; models that can run locally and serve specific use cases without the overhead of massive parameter counts. The author shares a personal experience from early 2024 using a 7B local model with the Guidance library to create a test-driven development flow, predating &\#x27;thinking&\#x27; models. The piece suggests that startups and consumer companies may find opportunities by building products that leverage these smaller models, rather than competing directly with frontier labs. Community comments echo this sentiment, noting that large models often contain unnecessary world knowledge and that there is room for &\#x27;bottom-up&\#x27; strategies in AI development.

hackernews · tosh · Aug 27, 15:56 · [Discussion](https://news.ycombinator.com/item?id=49466917)

**「Background」** Small language models \(SLMs\) are compact AI models, typically ranging from one to a few billion parameters, designed to run efficiently on local hardware or modest cloud resources. They contrast with frontier models from major labs, which have hundreds of billions of parameters and require massive compute. SLMs are increasingly recognized for being faster, cheaper, more controllable, and more deployable in practical applications, as noted in recent industry analyses. This trend reflects a shift toward AI deployment as the competitive battleground, where capability becomes commoditized and efficiency and practicality take precedence.

**「Impact」** Developers and startups can expect to build practical AI applications more cheaply and quickly using small models, potentially disrupting the assumption that only frontier-scale models are viable. This trend may also influence investment strategies, as some investors are already questioning the lack of consumer AI companies.

**「Community Discussion」** Commenters generally agree with the thesis, sharing personal experiences and analogies. One commenter notes that large models are &\#x27;slush funds&\#x27; of world knowledge and reasoning, and that many applications don&\#x27;t need that excess. Another draws a parallel to Paul Graham&\#x27;s Maker&\#x27;s Schedule, distinguishing between &\#x27;IQ 180&\#x27; work and &\#x27;token spewer&\#x27; work, suggesting that small models excel at the latter.

<details><summary>References</summary>
<ul>
<li><a href="https://www.georgejamesconsulting.com/post/small-language-models-for-small-and-medium-sized-countries-the-practical-ai-strategy-for-the-next-d">Small Language Models for Small and Medium-Sized Countries: The Practical AI Strategy for the Next Decade</a></li>
<li><a href="https://blog.neurometric.ai/p/the-top-25-small-language-models">The Top 25 Small Language Models - by Rob May</a></li>

</ul>
</details>

**Tags**: `#small language models`, `#AI trends`, `#practical AI`, `#model efficiency`, `#startups`

**中文**

<a id="bilingual-item-7-zh"></a>
### [小型模型时代已至](https://calv.info/small-models-have-arrived) ⭐️ 7.0/10

一篇题为《小型模型已到来》的文章认为，小型、高效的 AI 模型正变得日益重要，尤其适用于追求快速、廉价且“足够好”的实际应用场景，这与前沿实验室追求大规模模型的路径形成对比。文章指出，对这类模型的需求即将爆发，并引用了早期使用 7B 本地模型结合 Guidance 库编写测试和代码的实践经验。文章还讨论了投资者对消费级 AI 公司稀缺的困惑，以及“IQ 180”型工作与“token 喷涌”型工作的区别。社区评论进一步探讨了小型模型在特定应用中可能优于大型模型的场景，认为大型参数模型中的世界知识并非总是必要。

hackernews · tosh · 8月27日 15:56 · [社区讨论](https://news.ycombinator.com/item?id=49466917)

**「背景」** 小型语言模型（SLM）通常指参数规模在数十亿以下、可在本地或边缘设备运行的 AI 模型。与前沿实验室开发的大型模型相比，SLM 在推理速度、成本和部署灵活性上具有优势，尤其适合对实时性要求高或数据隐私敏感的应用场景。近年来，随着模型压缩技术和高效架构的发展，SLM 在诸多实际任务中已能达到“足够好”的性能，成为 AI 落地的重要方向。

**「影响」** 对于开发者和初创企业而言，小型模型降低了 AI 应用的门槛，使其能够以更低成本快速构建特定场景的解决方案，并可能催生更多面向消费者的 AI 产品。

**「社区讨论」** 评论者分享了使用小型模型的实际经验，并讨论了小型模型在不需要广泛世界知识的应用中的优势，同时对比了“IQ 180”型工作与“token 喷涌”型工作的差异，认为后者更适合小型模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.georgejamesconsulting.com/post/small-language-models-for-small-and-medium-sized-countries-the-practical-ai-strategy-for-the-next-d">Small Language Models for Small and Medium-Sized Countries: The Practical AI Strategy for the Next Decade</a></li>

</ul>
</details>

**标签**: `#small language models`, `#AI trends`, `#practical AI`, `#model efficiency`, `#startups`

---

**English**

<a id="bilingual-item-8-en"></a>
### [Microduck: Open-Source Bipedal Robot with AI Training](https://pollen-robotics.com/microduck/) ⭐️ 7.0/10

Pollen Robotics, a French company, has introduced Microduck, an open-source bipedal robot designed for AI experimentation. The robot features a Rockchip RK3566 processor with an AI accelerator, 1GB RAM, 32GB storage, Wi-Fi, Bluetooth, microphones, a speaker, two NFC antennas, and a removable battery providing about one hour of runtime. It weighs 800g and uses Dynamixel servos, with an onboard policy loop running at 50 hertz. Microduck comes with seven pre-trained behaviors including walking, sitting, standing, kicking, ground pickup, roller skating, and self-recovery. Users can train additional behaviors locally or via Hugging Face Jobs, export models to ONNX, and deploy them on the robot. The project includes a simulator, making it accessible for developers and hobbyists.

hackernews · robotswantdata · Aug 27, 10:57 · [Discussion](https://news.ycombinator.com/item?id=49462763)

**「Background」** Microduck is a 25 cm open-source bipedal robot developed by Pollen Robotics, a French company. It features 15 motors, a camera, LiDAR, and a grasping beak, and is designed for physical AI and reinforcement learning. The robot runs on a Rockchip RK3566 processor with an AI accelerator, 1GB RAM, 32GB storage, and includes Wi-Fi, Bluetooth, microphones, a speaker, two NFC antennas, and a removable battery with about one hour of runtime. It weighs 800g and uses Dynamixel servos with a 50 Hz onboard policy loop. Users can train new behaviors in simulation and deploy them on the robot, with support for exporting to ONNX and training via Hugging Face Jobs.

**「Impact」** Microduck lowers the barrier to entry for experimenting with bipedal robotics and reinforcement learning, offering a fully open-source platform with integrated AI training tools. This enables hobbyists, educators, and researchers to develop and deploy custom behaviors without needing extensive robotics expertise.

**「Community Discussion」** Community members noted the simulator&\#x27;s default AZERTY keyboard layout \(ZQSD\) due to the company&\#x27;s French origin, suggesting adding layout preferences for broader usability. Others shared links to alternative open-source bipedal and quadruped robots, and one commenter highlighted the widespread use of the MuJoCo physics engine in robotics research, which is maintained by Google DeepMind.

<details><summary>References</summary>
<ul>
<li><a href="https://pollen-robotics.com/microduck/">Microduck - A tiny biped robot you can teach new tricks ...</a></li>
<li><a href="https://github.com/pollen-robotics/microduck">GitHub - pollen-robotics/microduck: A Tiny biped duck robot</a></li>
<li><a href="https://store.pollen-robotics.com/products/microduck">Microduck – Pollen Robotics SAS</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#open-source`, `#AI`, `#bipedal`, `#hardware`

**中文**

<a id="bilingual-item-8-zh"></a>
### [Microduck：开源双足机器人](https://pollen-robotics.com/microduck/) ⭐️ 7.0/10

Microduck 是 Pollen Robotics 推出的一款开源双足机器人，配备 Rockchip RK3566 处理器（含 AI 加速器）、1GB 内存、32GB 存储、Wi-Fi、蓝牙、麦克风、扬声器、两个 NFC 天线和可拆卸电池（续航约 1 小时）。其机载策略循环频率为 50 赫兹，使用 Dynamixel 伺服电机，重量 800 克。出厂时具备七种行为：行走、坐立、踢腿、地面拾取、轮滑和自恢复，用户可通过 Hugging Face Jobs 在本地训练额外行为，并导出为 ONNX 格式部署。该项目还提供模拟器，便于开发和测试。

hackernews · robotswantdata · 8月27日 10:57 · [社区讨论](https://news.ycombinator.com/item?id=49462763)

**「背景」** Microduck 是法国公司 Pollen Robotics 推出的一款开源双足机器人，高 25 厘米，配备 15 个电机、摄像头、激光雷达和一个可抓取的喙。它采用 Rockchip RK3566 处理器（带 AI 加速器）、1GB 内存、32GB 存储，并支持 Wi-Fi、蓝牙、麦克风、扬声器、两个 NFC 天线和可拆卸电池（续航约 1 小时）。机器人出厂时具备行走、坐立、踢腿、捡起地面物体、轮滑和自恢复等七种行为，用户可通过仿真环境（基于 MuJoCo 引擎）训练新行为，并借助 Hugging Face Jobs 进行训练，导出为 ONNX 格式后部署到实体机器人上。

**「影响」** 对于机器人爱好者和开发者，Microduck 提供了一个价格相对亲民、可定制且支持 AI 训练的开源双足平台，降低了双足机器人实验的门槛。

**「社区讨论」** 社区成员指出模拟器默认使用 AZERTY 键盘布局（ZQSD），建议增加键盘布局选项以适配更常见的 QWERTY 和 QWERTZ 用户；也有用户列举了其他开源双足和四足机器人项目，并提到 MuJoCo 引擎在机器人强化学习中的广泛应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pollen-robotics.com/microduck/">Microduck - A tiny biped robot you can teach new tricks ...</a></li>
<li><a href="https://github.com/pollen-robotics/microduck">GitHub - pollen-robotics/microduck: A Tiny biped duck robot</a></li>
<li><a href="https://store.pollen-robotics.com/products/microduck">Microduck – Pollen Robotics SAS</a></li>

</ul>
</details>

**标签**: `#robotics`, `#open-source`, `#AI`, `#bipedal`, `#hardware`

---

**English**

<a id="bilingual-item-9-en"></a>
### [Open-Source Rust LLM Gateway Routes and Trains from Traffic](https://github.com/experientiallabs/experiential) ⭐️ 7.0/10

Experiential Labs released an open-source, Rust-native LLM gateway that unifies self-hosted, frontier, and open-source models behind a single API, handling provider-specific quirks like streaming formats, tool calls, rate limits, and error behavior. The gateway adds under 1 ms overhead for bring-your-own-key requests and under 2 ms when Experiential supplies the provider key, supports 1000+ models refreshed daily via an automated codex agent, and takes no token markup. A standout feature is an opt-in system that uses standardized OpenTelemetry traces to mine real tasks, simulate model rollouts with text world models, apply an LLM judge, and fit a nearest-neighbor classifier to route each request to the optimal model, aiming for a better cost/quality Pareto curve. The project is available on GitHub and can be self-hosted or used via a hosted version with zero markup. It is early-stage without proven production adoption, and community questions focus on caching costs and calibration of simulated rankings.

hackernews · SilenN · Aug 27, 21:18 · [Discussion](https://news.ycombinator.com/item?id=49471407)

**「Background」** LLM gateways are intermediary services that provide a single, unified API endpoint in front of multiple model providers, handling tasks like authentication, rate limiting, and format conversion. They simplify integration and management for developers who use various models, but many commercial gateways charge a markup on token usage. Experiential is an open-source, Rust-native gateway that aims to offer the same convenience without markup, and it adds a novel feature: using production traffic to train personalized routing models or fine-tuned models, based on the project&\#x27;s website and GitHub repository.

**「Impact」** Developers and organizations using multiple LLM providers can reduce routing complexity and token costs with an open-source gateway that offers low overhead and no markup, but they should verify caching behavior and calibration before relying on it in production.

**「Community Discussion」** Commenters praised the open-source, no-markup approach and the sub-millisecond overhead, but raised concerns about caching costs when switching models and asked how simulated rankings are recalibrated against real task success, with some also inquiring about semantic caching and effort-level decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.experientiallabs.ai/">Experiential Labs · The open source AI gateway</a></li>
<li><a href="https://github.com/experientiallabs/experiential">GitHub - experientiallabs/experiential: An open source model ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#gateway`, `#open-source`, `#Rust`, `#model-routing`

**中文**

<a id="bilingual-item-9-zh"></a>
### [开源 Rust 原生 LLM 网关：用流量训练个性化模型](https://github.com/experientiallabs/experiential) ⭐️ 7.0/10

Experiential 是一个开源的 Rust 原生 LLM 网关，旨在统一管理自托管、前沿和开源模型，并处理不同提供商之间的配置差异，如流式格式、工具调用、参数、速率限制和错误行为。该网关对 BYOK 请求增加不到 1 毫秒延迟，对 Experiential 提供密钥的请求增加不到 2 毫秒，支持所有主要推理提供商，并通过 Codex 代理每日刷新 1000 多个模型。其核心创新是可选参与：利用标准化 OTel 追踪数据，挖掘代表性任务，通过文本世界模型模拟不同模型的输出，使用 LLM 评判器评估，并基于提示嵌入拟合最近邻分类器，以选择最优模型，从而在成本和质量之间实现更好的帕累托曲线。项目开源、无加价，允许混合本地模型和市场模型，并提供自托管或托管版本。

hackernews · SilenN · 8月27日 21:18 · [社区讨论](https://news.ycombinator.com/item?id=49471407)

**「背景」** 大型语言模型（LLM）网关是一种中间层服务，它统一了不同模型提供商的 API 接口，使开发者能够通过一个标准端点访问多个模型，并处理流式格式、工具调用、参数差异和错误行为等兼容性问题。传统的网关通常会对令牌收取额外费用，而 Experiential Labs 推出的这个开源项目旨在以零加价的方式提供类似功能，同时利用流量数据（可选）训练个性化模型。该项目采用 Rust 编写，强调并发性能，并支持自托管、自带密钥（BYOK）和本地模型。

**「影响」** 对于寻求降低 LLM 网关复杂性和成本（尤其是避免 10% 的 token 加价）的开发者和组织，Experiential 提供了一个开源、低延迟的替代方案，并可能通过流量训练个性化模型来优化模型选择。然而，该项目仍处于早期阶段，尚未有大规模生产采用的公开证据，其路由优化和缓存策略的实际效果仍需验证。

**「社区讨论」** 社区对开源和无加价的做法表示赞赏，但主要关注点在于缓存机制：评论者担心在多个模型之间切换可能导致缓存命中率下降，从而增加成本，并询问是否有语义缓存支持。此外，还有关于模拟排名如何通过在线信号校准、以及网关是否决定推理努力水平（如思考时间）的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.experientiallabs.ai/">Experiential Labs · The open source AI gateway</a></li>
<li><a href="https://github.com/experientiallabs/experiential">GitHub - experientiallabs/experiential: An open source model ...</a></li>
<li><a href="https://www.experientiallabs.ai/about">About · Experiential Labs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#gateway`, `#open-source`, `#Rust`, `#model-routing`

---

**English**

<a id="bilingual-item-10-en"></a>
### [Claude&\#x27;s Overused Phrases Analyzed via GitHub PRs](https://louisabraham.github.io/load-bearing/) ⭐️ 7.0/10

A data-driven analysis of Claude&\#x27;s most overused phrases, based on GitHub PR data, reveals patterns like &quot;load-bearing,&quot; &quot;the crux,&quot; and &quot;first-class citizen.&quot; The project, created by Labo333, updates daily via GitHub Actions and is expanding to 1000 PRs per day with a search bar. This matters because it highlights stylistic tics in LLM outputs that may signal insight rather than demonstrate it, affecting how developers and prompt engineers interpret AI-generated text. The analysis is presented concisely on a single screen, avoiding the verbosity typical of LLMs.

hackernews · Labo333 · Aug 27, 08:59 · [Discussion](https://news.ycombinator.com/item?id=49461817)

**「Background」** The project analyzes Claude&\#x27;s most overused phrases by scraping 100 GitHub pull requests daily and grouping them by vocabulary patterns. It highlights terms like &quot;load-bearing&quot; that appear 123.04 times more frequently in certain components, suggesting a stylistic fingerprint in AI-generated text. This approach is novel because it uses real-world code contributions to quantify linguistic habits, rather than relying on anecdotal observations. The analysis is updated daily via GitHub Actions, providing a continuously evolving dataset.

**「Impact」** For AI practitioners and prompt engineers, this analysis provides concrete examples of overused phrases that can be targeted in system prompts to improve response quality, as demonstrated by a user who added Orwell&\#x27;s rule to reduce such phrases.

**「Community Discussion」** Community members noted that these output patterns are worsening across models, possibly due to AI-generated content being ingested in training data, and appreciated the author&\#x27;s unbiased presentation and the site&\#x27;s concise design.

<details><summary>References</summary>
<ul>
<li><a href="https://louisabraham.github.io/load-bearing/">The load - bearing vocabulary of Claude</a></li>
<li><a href="https://github.com/louisabraham/load-bearing">GitHub - louisabraham/ load - bearing : The load - bearing vocabulary ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI`, `#prompt-engineering`, `#data-analysis`, `#Claude`

**中文**

<a id="bilingual-item-10-zh"></a>
### [Claude 高频词汇的数据分析](https://louisabraham.github.io/load-bearing/) ⭐️ 7.0/10

该项目基于 GitHub 拉取请求数据，对 Claude 最常过度使用的短语进行了数据驱动分析，揭示了诸如“load-bearing”、“the crux”和“first-class citizen”等词汇的频繁出现。作者 Labo333 表示，该数据集和分析通过 GitHub Actions 每日更新，目前正计划增加搜索功能并将数据量提升至每天 1000 个 PR。这一分析对 LLM 从业者具有参考价值，因为它提供了一种新颖的量化方法，并引发了关于模型输出风格和提示工程影响的讨论。

hackernews · Labo333 · 8月27日 08:59 · [社区讨论](https://news.ycombinator.com/item?id=49461817)

**「背景」** 该分析基于每日抓取的 100 个 GitHub 拉取请求，统计 Claude 在代码审查和描述中高频使用的词汇，例如“load-bearing”在语料库中每百万词出现 20 次，频率是其他组件的 123.04 倍。项目由 louisabraham 开发，通过 GitHub Actions 每日更新数据，并采用无监督方式按词汇聚类分组，而非预设主题。这种数据驱动方法旨在揭示 LLM 在真实编码场景中的语言习惯，为提示工程提供参考。

**「影响」** 对于依赖 Claude 生成文本的开发者，这一分析可能促使他们调整提示词以减少陈词滥调，例如添加 Orwell 的规则来避免常见隐喻，从而获得更具体、更清晰的输出。

**「社区讨论」** 社区成员 ben30 分享了通过添加 Orwell 规则来减少 Claude 中“load-bearing”等词汇的尝试，并指出 Claude 认为该规则与其系统提示冲突。nater5000 赞赏了作者简洁的呈现方式，而 SalariedSlave 则担忧所有模型都存在类似风格问题，并猜测可能与 AI 生成内容的反馈循环有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://louisabraham.github.io/load-bearing/">The load - bearing vocabulary of Claude</a></li>
<li><a href="https://github.com/louisabraham/load-bearing">GitHub - louisabraham/ load - bearing : The load - bearing vocabulary ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI`, `#prompt-engineering`, `#data-analysis`, `#Claude`

---

**English**

<a id="bilingual-item-11-en"></a>
### [FFmpeg Division by Zero Bug Found via Vibecoded Fuzzer](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) ⭐️ 7.0/10

A division-by-zero bug in FFmpeg was discovered using a &\#x27;vibecoded&\#x27; fuzzer, an AI-assisted approach that generates fuzzing harnesses. The bug was reported in an FFmpeg issue, and a patch was already submitted in April, with prior discussion dating back to 2024. The finding highlights the potential of AI-assisted fuzzing to uncover vulnerabilities in complex codebases, though some community members question whether the bug is a real issue or merely a result of controlling a custom AVIO module. The discovery underscores both the promise and limitations of AI in software testing.

hackernews · dclavijo · Aug 27, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49468642)

**「Background」** FFmpeg is a widely used open-source multimedia framework that handles audio and video decoding, encoding, and processing. Fuzzing is a software testing technique that feeds malformed or unexpected inputs to a program to uncover crashes or bugs. The reported issue is an integer division-by-zero in the VPK demuxer&\#x27;s vpk\_read\_packet function, triggered when a custom AVIO module supplies crafted data. A patch addressing this bug was submitted to the FFmpeg development mailing list in April, and the bug had been discussed previously in 2024.

**「Impact」** For FFmpeg users and developers, the bug could cause crashes when processing malformed input, but the practical impact is limited because it requires control over a custom AVIO module, which is not typical in standard usage. The patch submission suggests the issue is being addressed, but the debate indicates uncertainty about its real-world exploitability.

**「Community Discussion」** Community comments note that a patch was already submitted in April and that the bug was discussed in 2024, with some arguing that AI-assisted fuzzing is a powerful tool due to its lack of fatigue and broad knowledge. Others question the bug&\#x27;s validity, suggesting it only occurs when controlling a custom AVIO module, and debate whether marking all division operations as potential divide-by-zero is a practical solution.

<details><summary>References</summary>
<ul>
<li><a href="https://hn.today/s/we-found-a-division-by-zero-bug-in-ffmpeg-with-a-vibecoded-fuzzer">We found a division by zero bug in FFmpeg with a vibecoded fuzzer</a></li>
<li><a href="https://geekoven.net/digital-defense/a-vibecoded-fuzzer-a-divide-by-zero-and-what-it-means/">A Vibecoded Fuzzer , a Divide - by - Zero , and What It... - geekoven.net</a></li>
<li><a href="https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290">#24290 - Integer Divide - by - Zero in... - FFmpeg Forgejo</a></li>

</ul>
</details>

**Tags**: `#ffmpeg`, `#fuzzing`, `#ai-assisted-development`, `#bug-hunting`, `#security`

**中文**

<a id="bilingual-item-11-zh"></a>
### [FFmpeg 除零漏洞由 AI 辅助模糊测试发现](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) ⭐️ 7.0/10

FFmpeg 中发现了一个除零漏洞，该漏洞是通过一个由 AI 辅助（vibecoded）的模糊测试器发现的。该漏洞的补丁已于 4 月提交至 FFmpeg 开发邮件列表，但社区对其实际影响存在争议。有评论者指出，该漏洞可能仅在自定义 AVIO 模块提供恶意数据时触发，因此可能并非 FFmpeg 核心代码中的真实缺陷。尽管如此，这一发现展示了 AI 在自动化漏洞挖掘中的潜力，但也引发了关于 AI 可能降低软件质量的讨论。

hackernews · dclavijo · 8月27日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49468642)

**「背景」** FFmpeg 是一个广泛使用的开源音视频处理库，其解析器（demuxer）负责读取各种容器格式的数据。模糊测试（fuzzing）是一种通过向程序输入随机或变异数据来发现崩溃或异常行为的技术。本次发现的 bug 位于 VPK 解复用器（vpk\_read\_packet）中，属于整数除零错误，通常被认为严重性较低。该 bug 是通过一个由 AI 辅助编写的模糊测试器（即“vibecoded” fuzzer）发现的，这种工具利用大型语言模型快速生成测试代码。

**「影响」** 该漏洞可能影响使用自定义 AVIO 模块的 FFmpeg 用户，但实际风险有限，因为默认配置下可能无法触发。补丁已提交，用户应关注后续版本更新。

**「社区讨论」** 社区对漏洞的真实性存在分歧：有评论者认为这并非 FFmpeg 的真实缺陷，而是自定义 AVIO 模块的预期行为；另一些评论者则强调 AI 在漏洞挖掘中的效率优势，但也担忧其可能降低软件质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hn.today/s/we-found-a-division-by-zero-bug-in-ffmpeg-with-a-vibecoded-fuzzer">We found a division by zero bug in FFmpeg with a vibecoded fuzzer</a></li>
<li><a href="https://geekoven.net/digital-defense/a-vibecoded-fuzzer-a-divide-by-zero-and-what-it-means/">A Vibecoded Fuzzer , a Divide - by - Zero , and What It... - geekoven.net</a></li>
<li><a href="https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290">#24290 - Integer Divide - by - Zero in... - FFmpeg Forgejo</a></li>

</ul>
</details>

**标签**: `#ffmpeg`, `#fuzzing`, `#ai-assisted-development`, `#bug-hunting`, `#security`

---

**English**

<a id="bilingual-item-12-en"></a>
### [Decompiling a Nintendo 64 Game in 84 Days](https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/) ⭐️ 7.0/10

A developer has documented the process of decompiling the Nintendo 64 game Snowboard Kids in 84 days, highlighting the significant role of large language models \(LLMs\) in accelerating reverse engineering. The project demonstrates how LLMs can streamline the translation of assembly code into high-level source code, making decompilation more accessible and efficient. The article provides practical insights into the workflow, including the use of LLMs for code generation and analysis, and discusses the broader implications for software engineering and AI-assisted development. This achievement underscores the growing potential of AI tools in complex technical tasks, offering a model for future decompilation projects.

hackernews · knackers · Aug 27, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49466006)

**「Background」** Decompilation is the process of translating a compiled program&\#x27;s machine code back into a higher-level language, such as C, to understand or recreate its source code. For Nintendo 64 games, this often involves matching decompiled functions to the original C code so that recompiling produces byte-identical ROMs. Historically, such projects relied on manual reverse engineering and &\#x27;clean room&\#x27; reimplementation to avoid legal issues, but recent efforts have used AI tools to accelerate the process.

**「Impact」** This decompilation project enables the preservation and potential enhancement of Snowboard Kids, allowing the community to create mods, fixes, and ports, similar to other decomp projects. It also demonstrates a practical methodology for using LLMs in reverse engineering, which could inspire and guide other developers in tackling similar challenges.

**「Community Discussion」** Commenters expressed enthusiasm for decomp projects, with one recommending the Legend of Dragoon recomp as another labor of love. Another highlighted the productivity gains from embracing LLMs in rigorous projects, while others discussed the legal status of decompilation and wondered why game companies don&\#x27;t pursue such projects themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cdlewis/snowboardkids-decomp">GitHub - cdlewis/snowboardkids-decomp: Decompilation of ...</a></li>
<li><a href="https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/">Decompiling a Nintendo 64 Game in 84 Days | Chris&#x27; Blog</a></li>

</ul>
</details>

**Tags**: `#reverse engineering`, `#LLM`, `#Nintendo 64`, `#decompilation`, `#software engineering`

**中文**

<a id="bilingual-item-12-zh"></a>
### [84 天反编译 N64 游戏：LLM 加速逆向工程](https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/) ⭐️ 7.0/10

一位开发者详细记录了在 84 天内反编译 Nintendo 64 游戏《Snowboard Kids》的过程，并强调了大型语言模型（LLM）在加速逆向工程中的关键作用。该项目展示了如何利用 LLM 辅助理解汇编代码、识别函数和重构 C 代码，从而显著缩短了传统上耗时数月的反编译工作。文章还提到了其他类似的社区项目，如《龙骑士传说》的重编译项目，以及《黄金眼》的逆向工程进展。这一成就不仅体现了 LLM 在软件工程中的实际应用价值，也为复古游戏的保存和重制提供了新的可能性。

hackernews · knackers · 8月27日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49466006)

**「背景」** Nintendo 64 游戏《Snowboard Kids》的完整反编译项目在 84 天内完成，所有函数均匹配可编译为相同机器码的 C 实现。该项目由开发者 Chris Lewis 主导，利用前沿 AI 模型（如 Codex）、社区专家和改良工具加速了进程，相比其续作《Snowboard Kids 2》的 596 天大幅缩短。反编译过程涉及从 ROM 中提取资源，并与逆向工程得到的 C 代码结合，以生成完全相同的 ROM。项目明确声明非商业用途，且包含来自任天堂 libultra 和 libmus 音频库的数百个代码段。

**「影响」** 对于从事逆向工程和复古游戏开发的开发者而言，这一案例证明了 LLM 可以大幅提升反编译效率，可能推动更多经典游戏的社区重制项目。然而，其法律地位仍存在争议，因为直接翻译原始代码可能涉及版权问题，而非传统的“净室”重新实现。

**「社区讨论」** 社区成员对这类反编译项目表示赞赏，认为它们为被遗弃的游戏注入了新生命，并推荐了类似项目如《龙骑士传说》的重编译。同时，有人质疑游戏公司为何不利用这些成果进行官方重制，并讨论了此类项目的法律模糊性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cdlewis/snowboardkids-decomp">GitHub - cdlewis/snowboardkids-decomp: Decompilation of ...</a></li>
<li><a href="https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/">Decompiling a Nintendo 64 Game in 84 Days | Chris&#x27; Blog</a></li>
<li><a href="https://zeli.app/story/49466006">Snowboard Kids Decompiled in 84 Days, Thanks to AI and ...</a></li>

</ul>
</details>

**标签**: `#reverse engineering`, `#LLM`, `#Nintendo 64`, `#decompilation`, `#software engineering`

---

**English**

<a id="bilingual-item-13-en"></a>
### [Emacs 31&\#x27;s New Markdown-ts-mode: A Guide](https://rahuljuliato.com/posts/markdown-ts-mode-emacs-31) ⭐️ 7.0/10

Emacs 31 introduces a new built-in Markdown-ts-mode that leverages tree-sitter for fast, spec-compliant Markdown editing. The mode supports CommonMark and GitHub Flavored Markdown \(GFM\), including checkboxes and strikethrough, and requires no extra packages. Currently experimental, users must opt in by loading the mode manually. This guide provides an unofficial overview of its features and usage.

hackernews · RahulMJ · Aug 27, 13:22 · [Discussion](https://news.ycombinator.com/item?id=49464543)

**「Background」** Emacs is a highly extensible text editor that has traditionally used regex-based font-lock for syntax highlighting. Tree-sitter is an incremental parsing library that provides fast, accurate syntax trees, and Emacs has been integrating tree-sitter support since version 29. Emacs 31 introduces a new built-in markdown-ts-mode that leverages tree-sitter for Markdown editing, offering better performance and support for CommonMark and GitHub Flavored Markdown \(GFM\). This mode is experimental and requires users to opt in, as it is not enabled by default.

**「Impact」** Emacs users who frequently edit Markdown will benefit from improved performance and spec compliance without installing third-party packages, though they must enable the experimental mode manually.

**「Community Discussion」** Commenters clarified that &\#x27;ts&\#x27; stands for tree-sitter and highlighted the mode&\#x27;s built-in nature and experimental status. Some users questioned the keystroke efficiency of the mode compared to typing Markdown syntax directly, while others expressed interest in a Markdown-centric alternative to org-mode for better collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/LionyxML/markdown-ts-mode">GitHub - LionyxML/ markdown - ts - mode : A major mode for Emacs ...</a></li>
<li><a href="https://sourcefeed.dev/a/emacs-31-refines-tree-sitter-and-introduces-native-markdown">Emacs 31 Refines Tree - Sitter and Introduces Native Markdown</a></li>
<li><a href="https://www.rahuljuliato.com/posts/markdown-ts-mode-emacs-31">An unofficial guide to markdown - ts - mode on Emacs 31 | Rahul&#x27;s Blog</a></li>

</ul>
</details>

**Tags**: `#emacs`, `#tree-sitter`, `#markdown`, `#editor`, `#open-source`

**中文**

<a id="bilingual-item-13-zh"></a>
### [Emacs 31 内置 Markdown-ts-mode 非官方指南](https://rahuljuliato.com/posts/markdown-ts-mode-emacs-31) ⭐️ 7.0/10

Emacs 31 引入了内置的 Markdown-ts-mode，这是一个基于 tree-sitter 的 Markdown 编辑模式，提供高性能的解析和语法高亮。该模式支持 CommonMark 规范和 GFM（GitHub Flavored Markdown），因此任务列表（如 \`- \[ \]\`）和删除线（~~strikethrough~~）等功能开箱即用。作为内置模式，用户无需安装额外包，但目前仍处于实验阶段，需要用户主动选择启用。该模式旨在提升 Markdown 编辑的速度和规范符合性，对 Emacs 用户而言是一个值得关注的改进。

hackernews · RahulMJ · 8月27日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49464543)

**「背景」** Emacs 31 引入了内置的 markdown-ts-mode，这是一个基于 tree-sitter 的 Markdown 编辑模式，提供快速且符合规范的语法高亮和编辑功能。tree-sitter 是一种增量解析库，能够为编辑器提供高性能的语法分析。此前，Emacs 用户通常需要安装第三方包（如 markdown-mode）来获得类似功能，而 markdown-ts-mode 作为内置模式，无需额外安装。该模式目前处于实验阶段，用户需要显式启用。

**「影响」** 对于 Emacs 用户，尤其是依赖 Markdown 进行写作或协作的用户，Markdown-ts-mode 提供了更快速、更符合规范的编辑体验，且无需额外配置。然而，由于仍处于实验阶段，用户可能需要承担稳定性风险，并主动调整工作流程以利用其特性。

**「社区讨论」** 社区评论中，作者 RahulMJ 补充说明该模式基于 tree-sitter，性能优越，且内置支持 CommonMark 和 GFM，但需用户主动启用。其他用户讨论了该模式与 org-mode 的对比，认为 Markdown 原生支持可能减少协作摩擦，但也有用户质疑启用该模式在按键效率上的优势，认为直接输入 Markdown 语法可能更快捷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/LionyxML/markdown-ts-mode">GitHub - LionyxML/ markdown - ts - mode : A major mode for Emacs ...</a></li>
<li><a href="https://sourcefeed.dev/a/emacs-31-refines-tree-sitter-and-introduces-native-markdown">Emacs 31 Refines Tree - Sitter and Introduces Native Markdown</a></li>
<li><a href="https://www.rahuljuliato.com/posts/markdown-ts-mode-emacs-31">An unofficial guide to markdown - ts - mode on Emacs 31 | Rahul&#x27;s Blog</a></li>

</ul>
</details>

**标签**: `#emacs`, `#tree-sitter`, `#markdown`, `#editor`, `#open-source`

---

**English**

<a id="bilingual-item-14-en"></a>
### [Google Unveils Gemini Omni 1.1 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) ⭐️ 7.0/10

Google has announced Gemini Omni 1.1 Flash, a new multimodal AI model designed to handle text, images, audio, and video generation. The model builds on Google&\#x27;s continued investment in video generation, which some observers link to the development of world models. However, the announcement lacks deep technical details, and community feedback notes that the model still cannot sync generated video to provided audio, a limitation that persists from the previous Omni release. The model&\#x27;s release is part of Google&\#x27;s broader strategy to compete in the multimodal AI space, though it has not yet addressed all practical use cases.

hackernews · saretup · Aug 27, 17:06 · [Discussion](https://news.ycombinator.com/item?id=49467922)

**「Background」** Gemini Omni is Google DeepMind&\#x27;s family of multimodal AI models designed for video generation and editing. The newly released Gemini Omni 1.1 Flash builds on this foundation, adding capabilities such as extending video clips up to 40 seconds, controlling the first and last frames, and producing 1080p or 4K output. It also offers a lower-cost 360p drafting mode at roughly one-third the price, while maintaining the same $0.10 per second rate for standard generation.

**「Impact」** Developers and creators using Google&\#x27;s multimodal AI tools will find Gemini Omni 1.1 Flash useful for generating content across multiple modalities, but those needing precise audio-video synchronization will still need to rely on alternative solutions like Minimax H3.

**「Community Discussion」** Community members expressed mixed reactions: some noted the potential impact on voice actors and questioned how industries are adapting, while others joked about Google&\#x27;s browser compatibility issues. A user highlighted that the model still cannot sync generated video to pre-existing audio, a practical limitation that persists, and another criticized Google for not releasing a new Gemini Pro version.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/">Build with Gemini Omni 1 . 1 Flash</a></li>
<li><a href="https://www.orcarouter.ai/blog/gemini-omni-1-1-flash-launch">Gemini Omni 1 . 1 Flash : 40-Second Scenes, Frame Control &amp; 4K</a></li>

</ul>
</details>

**Tags**: `#Google`, `#Gemini`, `#AI`, `#multimodal`, `#model release`

**中文**

<a id="bilingual-item-14-zh"></a>
### [谷歌发布 Gemini Omni 1.1 Flash 多模态模型](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) ⭐️ 7.0/10

谷歌宣布推出 Gemini Omni 1.1 Flash，这是一款新的多模态 AI 模型，旨在处理文本、图像、音频和视频等多种输入。该模型是谷歌在视频生成领域持续投资的一部分，与 OpenAI 放弃 Sora 形成对比，可能反映了谷歌对“世界模型”发展的重视。社区讨论指出，该模型仍无法实现将生成的视频与预先存在的音频同步的功能，而这一功能在本地工具如 Minimax H3 中已可实现。目前，该模型的详细技术规格和性能数据尚未公布。

hackernews · saretup · 8月27日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49467922)

**「背景」** Gemini Omni 是 Google DeepMind 推出的多模态 AI 模型系列，专注于视频生成与编辑。此前发布的 Gemini Omni 1.0 已具备视频生成能力，但存在场景长度和分辨率限制。此次发布的 Gemini Omni 1.1 Flash 是更新版本，面向开发者提供更强大的视频创作工具，支持 40 秒场景扩展、首尾帧控制、360p 草稿模式（成本约为原来的三分之一）以及 1080p/4K 输出，定价仍为每秒 0.10 美元。该模型旨在提升动态镜头运动理解和风格迁移能力，被视为 Google 在视频生成领域持续投入的一部分，可能与其“世界模型”战略相关。

**「影响」** 对于依赖多模态 AI 的开发者而言，Gemini Omni 1.1 Flash 可能提供更强大的视频生成能力，但缺乏音频同步功能可能限制其在配音或对口型等实际应用中的使用。

**「社区讨论」** 社区评论中，有用户对 AI 在配音和表演行业的影响表示好奇，而另一些用户则对谷歌迟迟不发布 Gemini Pro 的新版本表示不满。还有用户指出，该模型无法将生成的视频与现有音频同步，而本地工具如 Minimax H3 已能实现此功能，这反映了社区对模型实用性的关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/">Build with Gemini Omni 1 . 1 Flash</a></li>
<li><a href="https://www.orcarouter.ai/blog/gemini-omni-1-1-flash-launch">Gemini Omni 1 . 1 Flash : 40-Second Scenes, Frame Control &amp; 4K</a></li>
<li><a href="https://deepmind.google/models/gemini-omni/">Gemini Omni — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#AI`, `#multimodal`, `#model release`

---

**English**

<a id="bilingual-item-15-en"></a>
### [py-evoFE: Automated Evolutionary Feature Engineering for Tabular ML](https://www.reddit.com/r/MachineLearning/comments/1w0788j/pyevofe_automated_evolutionary_feature/) ⭐️ 7.0/10

py-evoFE v0.3.0 is a new open-source Python library that applies genetic algorithms to automate feature engineering for tabular machine learning, integrating with scikit-learn and polars. It offers over 40 built-in transformers, including nonlinear arithmetic, target encoding, string similarity, dimensionality reduction, and clustering, and uses hierarchical chaining to evolve features across generations. The library emphasizes performance through vectorized Polars/PyArrow computation, matrix hashing and nearest-neighbor caching, and multi-fidelity screening to reduce computational overhead. It supports island-model parallel search with various topologies and Caruana ensembling, and provides an interactive HTML replay viewer. py-evoFE is fully scikit-learn compatible, implements fit, transform, predict, and predict\_proba, and is available via pip install py-evoFE under the MIT license.

reddit · r/MachineLearning · /u/tanopereira · Aug 27, 21:33

**「Background」** Feature engineering is the process of creating new input variables from raw data to improve machine learning model performance, and it is often critical for tabular data tasks. Genetic programming is an evolutionary computation technique that evolves programs or expressions to solve problems, and it has been applied to automated feature engineering in libraries such as EvolutionaryForest and EvoFeat. py-evoFE builds on this tradition by using genetic algorithms to search for feature transformations, integrating with scikit-learn and Polars for compatibility and performance.

**「Impact」** Practitioners using tabular ML with LightGBM or XGBoost can now leverage py-evoFE to automatically discover compact, high-impact feature transformations, potentially improving model performance without manual feature engineering. The library&\#x27;s scikit-learn compatibility and open-source availability make it easy to integrate into existing pipelines, though its effectiveness on diverse datasets remains to be validated by the community.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/hengzhe-zhang/EvolutionaryForest">GitHub - hengzhe-zhang/EvolutionaryForest: An open source python library for automated feature engineering based on Genetic Programming · GitHub</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-981-96-0077-9_2">EvoFeat: Genetic Programming-Based Feature Engineering Approach to Tabular Data Classification | SpringerLink</a></li>

</ul>
</details>

**Tags**: `#feature engineering`, `#genetic algorithms`, `#tabular ML`, `#python`, `#open source`

**中文**

<a id="bilingual-item-15-zh"></a>
### [py-evoFE：基于遗传算法的自动化特征工程库](https://www.reddit.com/r/MachineLearning/comments/1w0788j/pyevofe_automated_evolutionary_feature/) ⭐️ 7.0/10

py-evoFE v0.3.0 是一个开源的 Python 库，利用遗传算法自动发现、组合和优化表格数据的特征变换，并与 scikit-learn 和 Polars 集成。该库提供 40 多种内置变换器，包括非线性算术、目标编码、字符串相似度、降维和聚类方法，并支持层次化链式特征构建。性能优化方面，采用 Polars 和 PyArrow 进行向量化计算，通过矩阵哈希和最近邻缓存减少冗余计算，并使用多保真度筛选加速评估。此外，py-evoFE 实现了岛屿模型并行搜索和 Caruana 集成，提供交互式回放查看器，并完全兼容 scikit-learn 的 Pipeline 和 GridSearchCV。该库以 MIT 许可证发布，可通过 pip 安装，旨在解决手动特征工程繁琐和暴力生成特征导致过拟合的问题。

reddit · r/MachineLearning · /u/tanopereira · 8月27日 21:33

**「背景」** 特征工程是表格数据机器学习中的关键步骤，但手动设计特征既耗时又受限于人类直觉，而暴力生成特征会导致维度爆炸、过拟合和高内存消耗。遗传编程（Genetic Programming）是一种受自然选择启发的自动搜索方法，能够自动发现和组合特征变换。此前已有类似库如 EvolutionaryForest（基于遗传编程的自动化特征工程库）和相关研究（如 EvoFeat），但 py-evoFE 通过集成 Polars 和 PyArrow 实现向量化计算，并引入多保真度筛选、岛屿模型等机制，旨在提高搜索效率和模型泛化能力。

**「影响」** 对于使用 LightGBM 或 XGBoost 等 GBDT 模型的表格数据从业者，py-evoFE 提供了一种自动化特征工程方案，可能减少手动特征工程的时间，并发现更紧凑、泛化能力更强的特征组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/hengzhe-zhang/EvolutionaryForest">GitHub - hengzhe-zhang/EvolutionaryForest: An open source python library for automated feature engineering based on Genetic Programming · GitHub</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-981-96-0077-9_2">EvoFeat: Genetic Programming-Based Feature Engineering Approach to Tabular Data Classification | SpringerLink</a></li>

</ul>
</details>

**标签**: `#feature engineering`, `#genetic algorithms`, `#tabular ML`, `#python`, `#open source`

---

**English**

<a id="bilingual-item-16-en"></a>
### [OpenAI Develops Persistent Codex Agent](https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/) ⭐️ 7.0/10

OpenAI is developing a persistent mode for its command-line Codex agent, according to code reviewed by WIRED. In this mode, the agent will continue working until put to sleep, unlike current modes that stop after minutes or hours. The feature includes an &\#x27;initiative&\#x27; setting that allows the agent to autonomously create and execute follow-up tasks across sessions, based on its understanding of the user, while still requiring prior approval for changes outside the user&\#x27;s system. OpenAI confirmed it is testing the feature but has no immediate plans for release.

telegram · zaihuapd · Aug 28, 02:47

**「Background」** Codex is OpenAI&\#x27;s command-line coding agent that assists developers with programming tasks. Currently, Codex operates in short sessions, stopping after a few minutes or hours. The reported &\#x27;persistent mode&\#x27; would allow the agent to work continuously until explicitly put to sleep, autonomously creating and executing follow-up tasks across sessions, based on its understanding of the user. This represents a shift toward more autonomous AI agents that can operate over extended periods.

**「Impact」** If released, this persistent mode could significantly change software engineering workflows by enabling longer-running, autonomous coding tasks, but its impact is currently uncertain as the feature is not yet available and no release timeline has been announced.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/openai-codex-persistent-mode-always-on-agents-august-2026">Codex Persistent Mode: OpenAI Tests Always-On Agents (2026 ...</a></li>
<li><a href="https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/">OpenAI Is Developing a ‘Persistent’ AI Agent - WIRED</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI agents`, `#Codex`, `#autonomous coding`, `#AI development`

**中文**

<a id="bilingual-item-16-zh"></a>
### [OpenAI 开发常驻 Codex，代理持续工作直至休眠](https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/) ⭐️ 7.0/10

据 WIRED 审查的代码，OpenAI 正在为命令行版 Codex 添加“常驻模式”，使 AI 代理能够持续工作，直到被用户“休眠”，这与现有模式在几分钟或几小时后自动停止的做法不同。该模式内置“主动性”设定，代理在回答请求后可自行创建后续任务，并能跨会话执行，同时会根据对用户的了解来决定工作内容；但修改用户系统之外的内容仍需事先获得批准。OpenAI 已确认正在测试该功能，但暂无近期上线计划。这一进展标志着 AI 代理向更自主的方向发展，可能对软件工程工作流程产生重要影响。

telegram · zaihuapd · 8月28日 02:47

**「背景」** OpenAI 的 Codex 是一款命令行编程代理，此前版本在完成单次请求后会在几分钟或几小时后自动停止。据 WIRED 审查的代码，OpenAI 正在为其添加“常驻模式”，使代理能够持续工作直至用户将其“休眠”，并内置“主动性”设定，可自行创建后续任务并跨会话执行。OpenAI 已确认正在测试该功能，但暂无近期上线计划。

**「影响」** 对于依赖 Codex 进行编码的开发者，常驻模式有望减少手动干预，实现更长时间的自动化任务执行，但跨会话的自主行为也可能带来对代码库意外修改的风险，需谨慎管理权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/openai-codex-persistent-mode-always-on-agents-august-2026">Codex Persistent Mode: OpenAI Tests Always-On Agents (2026 ...</a></li>
<li><a href="https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/">OpenAI Is Developing a ‘Persistent’ AI Agent - WIRED</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI agents`, `#Codex`, `#autonomous coding`, `#AI development`

---

**English**

<a id="bilingual-item-17-en"></a>
### [US Judge Blocks Pentagon Ban on Anthropic AI](https://www.bloomberg.com/news/articles/2026-08-28/anthropic-wins-court-challenge-to-us-supply-chain-risk-label?srnd=phx-technology) ⭐️ 7.0/10

A US district judge in San Francisco ruled that the Trump administration must lift its ban on Anthropic&\#x27;s AI technology for federal agencies. The judge found that the Defense Department&\#x27;s designation of Anthropic, the maker of the Claude model, as a supply chain risk lacked sufficient justification and appeared to be retaliation for the company&\#x27;s criticism of the government, rather than a genuine belief that Anthropic would undermine its own models. Anthropic welcomed the ruling and stated it will continue to cooperate with the government. The ban was imposed after negotiations over military AI with the Pentagon broke down, leading Anthropic to sue.

telegram · zaihuapd · Aug 28, 03:15

**「Background」** The Pentagon had designated Anthropic as a supply chain risk, prohibiting government agencies from using its technology, following the collapse of talks over military AI applications. This designation is typically used to exclude vendors deemed to pose security threats. Anthropic challenged the decision in court, arguing that the label was unjustified and retaliatory.

**「Impact」** This ruling allows Anthropic to resume potential business with federal agencies, reversing a significant barrier to government procurement of its AI technology. It also sets a legal precedent that may constrain the government&\#x27;s ability to use supply chain risk labels for punitive purposes, affecting how tech companies engage with federal contracts.

**Tags**: `#AI regulation`, `#Anthropic`, `#government procurement`, `#legal`, `#AI industry`

**中文**

<a id="bilingual-item-17-zh"></a>
### [美国法官叫停五角大楼对 Anthropic 的禁令](https://www.bloomberg.com/news/articles/2026-08-28/anthropic-wins-court-challenge-to-us-supply-chain-risk-label?srnd=phx-technology) ⭐️ 7.0/10

美国旧金山地区法官裁定，特朗普政府必须解除对 Anthropic 人工智能技术用于联邦机构的禁令。法官认为，国防部将 Claude 开发商列为供应链风险缺乏充分依据，此举意在因其批评政府而“杀鸡儆猴”，并非相信它会破坏自身模型。此前，Anthropic 与五角大楼的军事 AI 谈判破裂后，国防部将其列为供应链风险并禁止政府机构使用其技术，Anthropic 随后提起诉讼。Anthropic 对裁决表示欢迎，称将继续与政府合作。这一裁决对 AI 监管、政府采购以及科技公司与政府关系具有重要影响。

telegram · zaihuapd · 8月28日 03:15

**「背景」** Anthropic 是一家领先的人工智能公司，其开发的 Claude 模型在业界具有重要地位。此前，Anthropic 与五角大楼就军事 AI 应用进行谈判，但谈判最终破裂。随后，美国国防部将 Anthropic 列为供应链风险，禁止联邦机构使用其技术，这促使 Anthropic 提起诉讼挑战该决定。

**「影响」** 这一裁决意味着 Anthropic 的 AI 技术可以重新用于联邦机构，为该公司与政府合作扫清了障碍，同时也为其他科技公司挑战政府类似决定提供了先例。

**标签**: `#AI regulation`, `#Anthropic`, `#government procurement`, `#legal`, `#AI industry`

---

## Financial News / 财经新闻

**English**

<a id="bilingual-item-18-en"></a>
### [Nvidia Reports $96.2B Quarterly Revenue, Issues First One-Year-Ahead Growth Guidance](https://mp.weixin.qq.com/s/JTZ_ZJ_pn5vgrI_1QUyWNw) ⭐️ 9.0/10

Nvidia reported fiscal Q2 2027 revenue of $96.2 billion, up 106% year-over-year, and for the first time issued guidance for fiscal 2028, projecting about 70% growth, constrained by supply. Data center revenue reached $89 billion, up 117% year-over-year.

telegram · zaihuapd · Aug 27, 08:51

**「Background」** Nvidia&\#x27;s fiscal year runs from late January to late January, so the second quarter of fiscal 2027 ended on July 26, 2026. The company&\#x27;s revenue has more than doubled over the past year, driven by surging demand for its AI data center chips. Nvidia&\#x27;s next-generation platform, Vera Rubin, began shipping this month and is expected to contribute about 20% of data center revenue in the third quarter.

**「Impact」** This guidance signals sustained strong demand for AI infrastructure, which could affect technology companies and investors globally as they assess the pace of AI adoption and supply constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027">NVIDIA Announces Financial Results for Second Quarter Fiscal 2027</a></li>
<li><a href="https://www.hudson-labs.com/research/nvidia-q2-2027-earnings-preview-nvda-revenue-guidance-key-factors">Nvidia Q2 2027 Earnings Preview: NVDA Revenue, Guidance, Key ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#earnings`, `#AI`, `#data center`, `#guidance`

**中文**

<a id="bilingual-item-18-zh"></a>
### [英伟达季度营收 962 亿美元，首次提前一年给出 70%增长指引](https://mp.weixin.qq.com/s/JTZ_ZJ_pn5vgrI_1QUyWNw) ⭐️ 9.0/10

英伟达发布 2027 财年第二季度财报，营收 962.21 亿美元，同比增长 106%；数据中心收入 890 亿美元，同比增长 117%。公司首次提前一年给出 2028 财年营收指引，预计同比增长约 70%，并强调该增长受限于供给。

telegram · zaihuapd · 8月27日 08:51

**「背景」** 英伟达的财年与自然年不同，2027 财年第二季度截至 2026 年 7 月 26 日。此前该公司已连续多个季度营收同比翻倍以上增长，本次财报延续了这一势头。

**「影响」** 这一指引表明 AI 计算需求强劲，可能影响全球科技行业和投资者对 AI 相关企业的预期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027">NVIDIA Announces Financial Results for Second Quarter Fiscal 2027</a></li>
<li><a href="https://www.hudson-labs.com/research/nvidia-q2-2027-earnings-preview-nvda-revenue-guidance-key-factors">Nvidia Q2 2027 Earnings Preview: NVDA Revenue, Guidance, Key ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#earnings`, `#AI`, `#data center`, `#guidance`

---

**English**

<a id="bilingual-item-19-en"></a>
### [Midday Stock Movers: Nvidia, Salesforce, Okta Lead Gains](https://www.cnbc.com/2026/08/27/stocks-making-the-biggest-moves-midday-nvda-okta-hrl-veev.html) ⭐️ 8.0/10

Nvidia shares surged 9% after the company reported second-quarter adjusted earnings of $2.22 per share on revenue of $96.22 billion, beating analyst estimates of $2.10 per share and $92.17 billion, and forecast third-quarter revenue of $108 billion. Salesforce jumped 21% after reporting adjusted earnings of $5.90 per share, far above the $3.27 estimate, and Okta rose over 27% after beating expectations and raising full-year guidance.

rss · CNBC Finance · Aug 27, 20:09

**「Background」** These stock moves follow the release of quarterly earnings reports. Nvidia, Salesforce, and Okta all reported results that beat analyst expectations, while other companies like HP and Hormel faced investor concerns despite their own reports.

**「Impact」** These moves affect investors in major tech and software stocks, with Nvidia&\#x27;s performance often influencing the broader AI and semiconductor sector.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rexshares.com/nvidia-earnings/">NVIDIA Earnings Q2 FY27: Revenue, Data Center, AI Capex</a></li>
<li><a href="https://www.vantagemarkets.com/market-news/salesforce-q2-fy2027-earnings-august-27-2026/">Salesforce Q 2 Earnings 2026: CRM Jumps 14% on Beat</a></li>
<li><a href="https://www.zacks.com/stock/news/2981283/okta-q2-earnings-beat-on-subscription-growth-fy27-view-raised">OKTA Q 2 Earnings Beat on Subscription Growth, FY27... - Zacks.com</a></li>

</ul>
</details>

**Tags**: `#earnings`, `#stock movers`, `#Nvidia`, `#Salesforce`, `#Okta`

**中文**

<a id="bilingual-item-19-zh"></a>
### [英伟达、Salesforce、Okta 等股票盘中大幅波动](https://www.cnbc.com/2026/08/27/stocks-making-the-biggest-moves-midday-nvda-okta-hrl-veev.html) ⭐️ 8.0/10

英伟达第二季度营收和盈利超预期，营收同比增长超过一倍，股价上涨 9%；Salesforce 和 Okta 因财报超预期分别大涨 21%和 27%。

rss · CNBC Finance · 8月27日 20:09

**「背景」** 这些公司大多在 8 月 26 日盘后发布了截至 7 月底的季度财报。财报季中，投资者密切关注人工智能相关支出和消费需求，以判断科技股高估值是否合理。

**「影响」** 这些财报结果可能影响科技股投资者情绪，尤其是人工智能相关股票。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rexshares.com/nvidia-earnings/">NVIDIA Earnings Q2 FY27: Revenue, Data Center, AI Capex</a></li>
<li><a href="https://www.vantagemarkets.com/market-news/salesforce-q2-fy2027-earnings-august-27-2026/">Salesforce Q 2 Earnings 2026: CRM Jumps 14% on Beat</a></li>
<li><a href="https://www.zacks.com/stock/news/2981283/okta-q2-earnings-beat-on-subscription-growth-fy27-view-raised">OKTA Q 2 Earnings Beat on Subscription Growth, FY27... - Zacks.com</a></li>

</ul>
</details>

**标签**: `#earnings`, `#stock movers`, `#Nvidia`, `#Salesforce`, `#Okta`

---

**English**

<a id="bilingual-item-20-en"></a>
### [U.S. Warns of Sanctions on Chinese Banks Over Iran Oil Ahead of Trump-Xi Meeting](https://www.cnbc.com/2026/08/28/trump-x-meeting-us-china-iran-sanctions.html) ⭐️ 7.0/10

The U.S. has warned it could impose secondary sanctions on Chinese banks that help process Iranian oil, as officials from both countries prepare for President Xi Jinping&\#x27;s state visit to Washington. Treasury Secretary Scott Bessent said banks involved in turning Iranian oil into money would be targeted, but no specific actions have been announced yet.

rss · CNBC Finance · Aug 28, 01:35

**「Background」** The U.S. and China have been managing a delicate relationship, marked by a trade truce and high-level visits. In May 2026, President Trump made a state visit to China, and President Xi Jinping is scheduled to visit Washington in September 2026. The U.S. has also been escalating pressure on Iran, including threats of secondary sanctions on Chinese banks that facilitate Iranian oil trade.

**「Impact」** If enacted, the sanctions could affect Chinese banks and their international operations, as well as global oil trade, but analysts note that Beijing may interpret the threat as largely performative and expect the U.S.-China trade truce to hold.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_state_visit_by_Donald_Trump_to_China">2026 state visit by Donald Trump to China - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/08/28/trump-x-meeting-us-china-iran-sanctions.html">Trump ratchets up rhetoric against Beijing as U.S.-China officials meet for Xi&#x27;s Washington visit</a></li>
<li><a href="https://brusselssignal.eu/2026/07/trump-confirms-xi-visit-to-washington-as-ai-tops-agenda/">Trump confirms Xi visit to Washington - Brussels Signal</a></li>

</ul>
</details>

**Tags**: `#U.S.-China relations`, `#Iran sanctions`, `#trade policy`, `#diplomacy`, `#financial system`

**中文**

<a id="bilingual-item-20-zh"></a>
### [美国警告可能制裁中国银行，特朗普与习近平会晤前关系紧张](https://www.cnbc.com/2026/08/28/trump-x-meeting-us-china-iran-sanctions.html) ⭐️ 7.0/10

美国财政部长贝森特警告，如果中国银行参与将伊朗石油转化为资金的体系，可能面临制裁，但未提供具体行动细节。与此同时，美中官员正在为习近平访问华盛顿做准备。

rss · CNBC Finance · 8月28日 01:35

**「背景」** 此次会晤是继 2026 年 5 月特朗普访问北京后，中美两国元首的又一次高层互动。美国财政部长贝森特周一警告称，若中国银行参与将伊朗石油转化为资金的活动，将面临制裁，但具体措施尚未明确。

**「影响」** 如果制裁实施，涉及伊朗石油交易的中国银行可能受到限制，影响相关贸易和金融往来。但分析人士认为，美国可能不会采取重大行动，以避免破坏全球金融体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_state_visit_by_Donald_Trump_to_China">2026 state visit by Donald Trump to China - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/08/28/trump-x-meeting-us-china-iran-sanctions.html">Trump ratchets up rhetoric against Beijing as U.S.-China officials meet for Xi&#x27;s Washington visit</a></li>

</ul>
</details>

**标签**: `#U.S.-China relations`, `#Iran sanctions`, `#trade policy`, `#diplomacy`, `#financial system`

---

**English**

<a id="bilingual-item-21-en"></a>
### [Fed&\#x27;s Schmid: Inflation Sticky, Policy Rate May Not Be Restrictive](https://www.cnbc.com/2026/08/27/kansas-city-feds-schmid-says-inflation-stubborn-and-sticky-policy-rate-not-restrictive.html) ⭐️ 7.0/10

Kansas City Fed President Jeffrey Schmid said Thursday that inflation remains &\#x27;stubborn&\#x27; and &\#x27;sticky,&\#x27; and that the current policy rate target of 3.5%-3.75% may not be restrictive, suggesting possible further tightening. His comments follow a report showing core inflation at 3.3% year-over-year, well above the Fed&\#x27;s 2% target.

rss · CNBC Finance · Aug 27, 14:11

**「Background」** Schmid spoke at the Fed&\#x27;s annual Jackson Hole symposium, a day after the Commerce Department reported that the Fed&\#x27;s primary inflation gauge showed core prices rose 3.3% from a year ago. Schmid does not vote on the FOMC this year but participates in meetings.

**「Impact」** If the Fed raises rates further, borrowing costs for households and businesses could increase, potentially slowing economic growth. Schmid noted the economy grew at 1.5% in the second quarter with unemployment at 4.1%.

**Tags**: `#Federal Reserve`, `#inflation`, `#monetary policy`, `#interest rates`, `#Jackson Hole`

**中文**

<a id="bilingual-item-21-zh"></a>
### [堪萨斯城联储主席施密德：通胀“顽固”，政策利率可能不具限制性](https://www.cnbc.com/2026/08/27/kansas-city-feds-schmid-says-inflation-stubborn-and-sticky-policy-rate-not-restrictive.html) ⭐️ 7.0/10

堪萨斯城联邦储备银行行长杰弗里·施密德 8 月 27 日表示，通胀仍然“顽固且粘性”，并称当前 3.5%-3.75%的政策利率目标可能并不具有限制性，但他未明确支持加息。此前美国商务部数据显示，美联储首选通胀指标核心价格同比上涨 3.3%，远高于 2%的目标。

rss · CNBC Finance · 8月27日 14:11

**「背景」** 施密德在杰克逊霍尔年度研讨会上发表上述言论。他今年不是联邦公开市场委员会（FOMC）的投票成员，但去年曾两次反对降息。

**「影响」** 施密德的言论可能暗示美联储未来或进一步收紧货币政策，这可能影响借款成本和企业及消费者的支出决策。

**标签**: `#Federal Reserve`, `#inflation`, `#monetary policy`, `#interest rates`, `#Jackson Hole`

---