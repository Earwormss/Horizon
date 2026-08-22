---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 30 items, 11 important content pieces were selected

---

**Technology News**
1. [SGLang v0.5.18: 710 PRs, New Models, Faster Startup](#item-tech-news-1) ⭐️ 8.0/10
2. [Linus Torvalds Credits AI for Debugging Linux Kernel Issue](#item-tech-news-2) ⭐️ 8.0/10
3. [Developer Builds 60 MB Quantized LLM from Scratch](#item-tech-news-3) ⭐️ 8.0/10
4. [Munder Difflin: Run an Office of Your Coding Agents Locally](#item-tech-news-4) ⭐️ 7.0/10
5. [MCP Roadmap: Agent Identity and HTTP Standardization](#item-tech-news-5) ⭐️ 7.0/10
6. [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](#item-tech-news-6) ⭐️ 7.0/10
7. [Evaluation Resolution Artifact in Model-Brain Comparisons](#item-tech-news-7) ⭐️ 7.0/10
8. [Nintendo Wipes Out 400+ Switch Emulator Repos in One Day](#item-tech-news-8) ⭐️ 7.0/10
9. [Open Models Halve Time to Parity Each Generation](#item-tech-news-9) ⭐️ 7.0/10
10. [Apple Cuts Over 200 Jobs in Siri and Vision Pro Teams to Focus on AI](#item-tech-news-10) ⭐️ 7.0/10
11. [US Groups Urge FTC to Probe AI Firms&\#x27; Book Destruction](#item-tech-news-11) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [SGLang v0.5.18: 710 PRs, New Models, Faster Startup](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 8.0/10

SGLang v0.5.18 is a major release aggregating 710 pull requests from 212 contributors. It adds support for several new models, including Muse Glimmer \(autoregressive multimodal\), Intern-S2-Mobius \(autoregressive\), and diffusion models such as SANA-Video, LingBot-Video-MoE, LTX-2.5, Cosmos3 Edge &amp; Distilled, and LongCat-Image. Performance improvements include overlapped checkpoint staging at startup, which speeds up Qwen3-32B on H100 by 8.6-11.7% with prefetch and 2.38x faster \(35.6s vs 84.8s\) than the plain default, and a TP LMHead with all-to-all that reduces LMHead time on DeepSeek-V4-Pro B200 decode from 320us to 169us. The release also introduces FlashInfer MNNVL for pure allreduce, a unified compiled-kernel cache directory under SGLANG\_CACHE\_DIR, and updates dependencies to torch 2.13.0, triton 3.7.1, flashinfer 0.6.17, CuTeDSL 4.6.2, and sgl-kernel 0.4.6.post1. Users should note that the first launch after upgrading will recompile kernels once due to the cache directory change.

github · Fridge003 · Aug 22, 00:09

**「Background」** SGLang is a high-performance serving framework for large language models and multimodal models, developed by the sgl-project community. It provides a runtime and programming language designed to efficiently serve LLMs, with features like speculative decoding, CUDA graph optimization, and support for various attention backends. The project has evolved through multiple releases, with recent versions focusing on large-scale expert parallelism and rack-scale parallelism for NVIDIA GB200/GB300 systems. This release, v0.5.18, continues that trajectory by adding support for new model architectures and performance optimizations.

**「Impact」** Users of SGLang for LLM and diffusion model inference will benefit from expanded model support and notable performance gains, particularly for DeepSeek and Qwen models on H100 and B200 hardware, but should plan for a one-time recompilation after upgrading.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/index.html">SGLang Release Notes - NVIDIA Docs</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub</a></li>

</ul>
</details>

**Tags**: `#SGLang`, `#LLM inference`, `#model support`, `#release`, `#AI infrastructure`

---

<a id="item-tech-news-2"></a>
### [Linus Torvalds Credits AI for Debugging Linux Kernel Issue](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

Linus Torvalds publicly credited an AI for significantly assisting in a difficult Linux kernel debugging session, as noted in a commit message for the drm/xe driver. The AI repeatedly claimed the problem was impossible and unsolvable, but continued to add debug code and analyze results when pushed, ultimately helping resolve the issue. Torvalds humorously speculated that the AI&\#x27;s pessimism might stem from training data of people less stubborn than himself. He also allowed the AI to write the commit message, marking a notable endorsement of AI&\#x27;s practical value in complex software engineering. The commit is titled &quot;drm/xe: Don&\#x27;t hand out the flat CCS storage as usable VRAM&quot; and is available on GitHub.

rss · Simon Willison · Aug 22, 21:04

**「Background」** Linus Torvalds is the creator and lead maintainer of the Linux kernel, one of the most influential open-source software projects. AI-assisted programming tools, such as large language models, have become increasingly used by developers for tasks like code generation and debugging, but their reliability in complex, real-world scenarios is still debated. This commit is part of the ongoing development of the Xe driver for Intel GPUs, which manages graphics memory and related features.

**「Impact」** This endorsement from a highly respected figure like Torvalds could encourage broader adoption of AI tools in kernel development and other complex software engineering, while also highlighting the need for human persistence and oversight when using AI. It may also influence discussions about AI&\#x27;s limitations and potential in open-source communities.

**Tags**: `#AI-assisted debugging`, `#Linux kernel`, `#Linus Torvalds`, `#open source`, `#software engineering`

---

<a id="item-tech-news-3"></a>
### [Developer Builds 60 MB Quantized LLM from Scratch](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

A developer trained a 250M-parameter LLM from scratch on 30B tokens of fineweb, achieving extreme compression to under 2 bits per weight, resulting in a 60 MB deployment that runs at about 400 tokens per second on a laptop CPU with roughly 80 MB of RAM. The model uses a novel disk-based long-context system: the most recent 2048 tokens stay in fp16 as a normal KV cache, while older tokens are compressed to 1 bit and written to disk at about 320 bytes per token, enabling up to 100M tokens of retrievable history \(1M tokens ≈ 320 MB\). The vocabulary uses fixed 512-bit codes for all 131k tokens \(8.4 MB, zero trained parameters\), and the model was trained to retrieve from the disk cache but not to reason over those tokens. On held-out English web text, it achieves a cross-entropy of 3.15 nats per token, perplexity 23.3, and 0.99 bits per byte; on WordSim-353 it scores 0.619 Spearman correlation versus 0.029 for random codes. The full kit, including master weights for fine-tuning, is available on GitHub and Hugging Face.

reddit · r/MachineLearning · /u/Final-Data-1410 · Aug 22, 04:39

**「Background」** Quantization is a common technique to reduce the memory footprint and computational cost of large language models \(LLMs\) by lowering the precision of weights and activations, enabling deployment on resource-constrained devices. Tools like the vLLM llm-compressor library provide standardized quantization methods for weight, activation, and KV cache compression, often integrated with Hugging Face models. This project pushes quantization to an extreme by compressing a 250M-parameter model to under 2 bits per weight, resulting in a 60 MB deployment that runs efficiently on CPU.

**「Impact」** This demonstrates a practical path to running a capable LLM on edge devices with minimal memory and no GPU, potentially enabling on-device AI applications with long-context retrieval, though its limited reasoning over retrieved tokens and modest size mean it is not a replacement for larger models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/llm-compressor">GitHub - vllm-project/ llm -compressor: Transformers-compatible library...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#efficient inference`, `#long context`, `#edge AI`

---

<a id="item-tech-news-4"></a>
### [Munder Difflin: Run an Office of Your Coding Agents Locally](https://munderdiffl.in/) ⭐️ 7.0/10

Munder Difflin is a local multi-agent harness that wraps existing coding agents such as Claude Code and Codex, allowing developers to run deterministic simulations of multiple agents working together. The tool, built by Chaitanya, reportedly supports almost all major coding agent harnesses and has attracted over 20,000 users within a week, with many reporting reduced token consumption. Simulations are deterministic and do not consume tokens, making it a cost-effective way to test multi-agent workflows. The project has gained significant community traction on Hacker News, with 112 comments discussing its features and limitations. While not a paradigm shift, it addresses practical needs in AI-assisted software engineering by enabling structured, repeatable multi-agent interactions.

hackernews · simonpure · Aug 22, 09:49 · [Discussion](https://news.ycombinator.com/item?id=49398152)

**「Background」** A multi-agent harness is a tool that coordinates several AI coding agents into a single team, allowing them to work together on tasks, as opposed to using a single agent or a framework. Munder Difflin, developed by Chaitanya Giri, is a local multi-agent harness that wraps existing coding agents like Claude Code and Codex, enabling developers to orchestrate them into a self-coordinating team. It runs simulations deterministically without consuming tokens, and has gained significant traction with over 20,000 users in a week.

**「Impact」** Developers using Claude Code, Codex, or similar coding agents can now run deterministic, token-free multi-agent simulations locally, potentially reducing token costs and enabling more reliable testing of agent workflows. The tool&\#x27;s rapid adoption \(20K+ users in a week\) suggests it fills a real need, though its long-term value depends on how well it integrates with evolving agent ecosystems.

**「Community Discussion」** Community feedback is largely positive, with users appreciating the Office-themed metaphor for agent dysfunction and the practical benefits of deterministic simulations. However, some users like joshstrange criticize the design as pipelines and roles rather than true agents, desiring more flexibility in defining roles and spinning up multiple agents. Others see it as a humorous yet useful tool for understanding multi-agent management challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://munderdiffl.in/blog/what-is-a-multi-agent-harness/">What Is a Multi - Agent Harness ? — Munder Difflin Blog</a></li>
<li><a href="https://www.stork.ai/en/munder-difflin">Munder Difflin Review (2026) | Stork.AI</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#AI tools`, `#coding agents`, `#LLM applications`, `#developer tools`

---

<a id="item-tech-news-5"></a>
### [MCP Roadmap: Agent Identity and HTTP Standardization](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) ⭐️ 7.0/10

The Model Context Protocol \(MCP\) roadmap outlines future improvements focusing on agent identity, HTTP standardization, and broader adoption. The roadmap aims to make remote MCP servers indistinguishable from other HTTP workloads by the 2026-07-28 release, addressing a key criticism of the initial bespoke protocol. It also proposes standardized ways for MCP servers to recognize and trust agent identities, particularly for cloud workloads acting on behalf of users or delegating authority to sub-agents. The community discussion highlights both interest and skepticism, with some praising the move toward HTTP standardization while others question the complexity and value compared to simpler REST endpoints.

hackernews · pentagrama · Aug 22, 13:31 · [Discussion](https://news.ycombinator.com/item?id=49399591)

**「Background」** The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 to connect AI assistants to external data sources and tools. It defines a client-server architecture where AI applications can discover and invoke tools, resources, and prompts from servers. The protocol has gained broad industry adoption, with major vendors like Microsoft and Google supporting it, and it is now hosted by the Linux Foundation. The roadmap discussed in the blog post outlines planned improvements to MCP, including standardized agent identity, HTTP-based transport, and broader adoption, building on the protocol&\#x27;s existing foundation.

**「Impact」** The roadmap&\#x27;s changes will affect developers and organizations building MCP servers and clients, potentially simplifying integration by aligning with standard HTTP practices and enabling more robust agent authentication. However, the impact is uncertain until the roadmap is fully implemented and adopted, as some community members remain skeptical about the protocol&\#x27;s complexity.

**「Community Discussion」** Community comments show mixed reactions: some praise the move to standard HTTP as a correction of an initial misstep, while others question whether MCP offers advantages over simpler REST endpoints with documentation. A cybersecurity professional expressed disappointment with MCP&\#x27;s evolution, citing multiple standards and complexity, and has shifted to local tools and APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI agents`, `#protocols`, `#API design`, `#roadmap`

---

<a id="item-tech-news-6"></a>
### [DelveRL: Open-Source Roguelike for Training Game-Playing Agents](https://www.reddit.com/r/MachineLearning/comments/1vvii1j/i_built_an_opensource_roguelike_specifically_for/) ⭐️ 7.0/10

DelveRL is a new open-source, human-playable roguelike designed specifically for training game-playing agents. It features a structured API, deterministic simulation, procedural levels, and partial observability, addressing the common difficulty of integrating games with agent harnesses. The project includes a recurrent PPO trainer and a baseline that reaches a median floor of 18, with extended runs reaching floor 33. All components—game, training code, checkpoint, bridge documentation, and raw benchmarks—are open source. This tool aims to provide a practical benchmark for reinforcement learning research, inspired by projects from DeepMind and OpenAI.

reddit · r/MachineLearning · /u/SnyderConsulting · Aug 22, 17:32

**「Background」** Reinforcement learning \(RL\) research often relies on game environments to test agents, but many existing games are difficult to integrate with agent harnesses due to complex APIs or non-deterministic behavior. Roguelikes, with their turn-based mechanics and procedural levels, offer strategic depth and partial observability, making them suitable for RL benchmarks. DelveRL was built from the ground up to overcome integration hurdles, providing a structured API and deterministic simulation to facilitate agent training.

**「Impact」** DelveRL provides the RL community with a ready-to-use, open-source benchmark that simplifies the process of training and evaluating agents in a roguelike environment, potentially accelerating research in areas like exploration and risk management. Its deterministic simulation and structured API lower the barrier to entry for researchers and developers, though its long-term impact will depend on community adoption and the performance of future agents.

**Tags**: `#reinforcement learning`, `#open source`, `#game AI`, `#roguelike`, `#benchmark`

---

<a id="item-tech-news-7"></a>
### [Evaluation Resolution Artifact in Model-Brain Comparisons](https://www.reddit.com/r/MachineLearning/comments/1vvdxwt/the_evaluation_resolution_has_been_shown_to_have/) ⭐️ 7.0/10

A new preprint demonstrates that evaluation resolution significantly affects model-brain similarity results, revealing that untrained CNNs&\#x27; apparent match to V1 is an artifact. The study used a small CNN trained at 32px on a CIFAR-10 subset, five learning rules \(random init, backprop, feedback alignment, predictive coding, STDP\), and evaluated on THINGS-fMRI stimuli at six resolutions from 32px to 224px. The gap between trained and untrained backpropagation V1 similarity narrowed from −0.001±0.007 at 32 pixels to +0.044±0.006 at 224 pixels, a non-monotonic trend consistent across five seeds. The artifact persists even with off-the-shelf 224px-trained models \(ResNet-50, Swin-Tiny\), ruling out train/eval resolution mismatch. The study also found that a backprop &gt; untrained effect at LOC survived across all resolutions, and identified a batch-norm evaluation mode bug in three earlier preprints. Code is available at https://github.com/nilsleut/evaluation-resolution-rsa.

reddit · r/MachineLearning · /u/ConfusionSpiritual19 · Aug 22, 14:30

**「Background」** Model-brain comparisons use representational similarity analysis \(RSA\) to measure how well artificial neural networks match brain activity, such as fMRI responses in the visual cortex. A common claim is that untrained CNNs can match or surpass trained CNNs at early visual cortex \(V1\), which would challenge the importance of learning. This study investigates whether such results are artifacts of the evaluation resolution used in the comparison.

**「Impact」** Researchers in computational neuroscience and machine learning must control for evaluation resolution when comparing models to brain data, as low-resolution evaluations can produce misleading conclusions about untrained networks. The finding that untrained CNNs do not genuinely match V1 at higher resolutions corrects a common artifact and reinforces the value of learning in shaping brain-like representations.

**Tags**: `#computational neuroscience`, `#model-brain comparison`, `#evaluation methodology`, `#CNN`, `#learning rules`

---

<a id="item-tech-news-8"></a>
### [Nintendo Wipes Out 400+ Switch Emulator Repos in One Day](https://torrentfreak.com/nintendo-wipes-out-400-switch-emulator-repos-in-single-day-github-sweep/) ⭐️ 7.0/10

Nintendo filed seven DMCA anti-circumvention notices with GitHub on the same day, resulting in the removal of over 400 Switch emulator repositories and their forks. The takedown targeted repositories that use unauthorized keys to decrypt games, citing DMCA violations. Among the affected repos, 311 were associated with the suyu emulator, and 29 belonged to the discontinued Android emulator Skyline. The notices reference precedents such as the Yuzu settlement, though neither case has been fully adjudicated in court. This action significantly impacts the emulation community and open-source developers.

telegram · zaihuapd · Aug 22, 00:28

**「Background」** Nintendo has a history of aggressively enforcing its intellectual property rights against Switch emulators. In May 2024, it issued a single DMCA notice to GitHub that led to the removal of 8,535 repositories containing versions of the Yuzu emulator. Earlier in 2024, Nintendo settled with Tropic Haze, the company behind Yuzu, for $2.4 million, leading to Yuzu&\#x27;s shutdown. Suyu is a fork of Yuzu that gained popularity after Yuzu was discontinued, and Skyline is an Android emulator for the Switch.

**「Impact」** Developers and users of Switch emulators, particularly those involved with suyu and Skyline forks, will lose access to these repositories, potentially stalling development and distribution. The legal basis remains contested, as the cited precedents were settlements, not court rulings, leaving uncertainty about the DMCA&\#x27;s application to emulators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.videogameschronicle.com/news/nintendo-wipes-out-400-more-switch-emulator-repositories-on-github-as-it-continues-its-fight-on-piracy/">Nintendo wipes out 400 more Switch emulator repositories on GitHub as it continues its fight on piracy | VGC</a></li>
<li><a href="https://www.polygon.com/nintendo-emulation-take-downs-piracy/">Nintendo Goes After Switch Emulation With Aggressive New Takedowns</a></li>

</ul>
</details>

**Tags**: `#Nintendo`, `#DMCA`, `#emulation`, `#GitHub`, `#open-source`

---

<a id="item-tech-news-9"></a>
### [Open Models Halve Time to Parity Each Generation](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 7.0/10

SemiAnalysis reports that open-source models are catching up to closed-source frontier models at an accelerating pace, with each generation halving the time to parity. The analysis divides AI model history into three eras—early scaling, reasoning, and agentic—and finds that the capability gap fluctuates cyclically. In the agentic era, catch-up is fastest: Kimi K2.6 surpassed Opus 4.5 in 4.8 months, and GLM-5.2 exceeded GPT-5.2 in 6 months. The report notes that open models like GLM 5.3 and Kimi K3 can now handle many coding and agentic tasks that helped Anthropic achieve over $65 billion in annualized revenue, raising concerns about model-layer commoditization. However, benchmarks are not everything, and Anthropic&\#x27;s productization capabilities remain a key advantage.

telegram · zaihuapd · Aug 22, 08:26

**「Background」** Open-source AI models have historically lagged behind proprietary frontier models from companies like OpenAI and Anthropic. SemiAnalysis, a technology research firm, tracks the capability gap between open and closed models over time, using benchmarks and real-world task performance to measure progress. The analysis identifies distinct eras in model development, with the current agentic era emphasizing autonomous task execution and coding abilities.

**「Impact」** The accelerating catch-up of open models threatens the competitive moat of closed-source AI providers, potentially commoditizing the model layer and pressuring revenue models like Anthropic&\#x27;s, which relies on coding and agentic capabilities. However, productization and user experience remain differentiators that benchmarks do not capture.

**Tags**: `#open-source`, `#AI models`, `#industry analysis`, `#model capabilities`, `#SemiAnalysis`

---

<a id="item-tech-news-10"></a>
### [Apple Cuts Over 200 Jobs in Siri and Vision Pro Teams to Focus on AI](https://www.bloomberg.com/news/articles/2026-08-21/apple-cuts-jobs-in-siri-vision-pro-immersive-video-and-gaming-teams) ⭐️ 7.0/10

Apple is laying off more than 200 employees across its Siri digital assistant and Vision Pro headset teams as part of a strategic refocus on artificial intelligence and new devices. The cuts affect roughly 100 positions in the Vision Pro division and about 100 in Siri and software teams. Apple has essentially shut down the Vision Pro gaming team, reduced its immersive video content team, and eliminated some roles in the intelligent systems experience team. The company says it will create new positions and that the impact is limited to a small number of existing roles. The report comes from Bloomberg and signals a shift in Apple&\#x27;s priorities toward AI and upcoming hardware.

telegram · zaihuapd · Aug 22, 12:31

**「Background」** Apple has been developing Siri as its voice assistant since 2011 and launched the Vision Pro mixed-reality headset in 2024. The Vision Pro has faced high prices and limited sales, while Siri&\#x27;s underlying architecture has been criticized as outdated, prompting Apple to shift resources toward new AI initiatives and devices.

**「Impact」** The layoffs will directly affect over 200 Apple employees, particularly those working on Vision Pro gaming and immersive content, and indicate a strategic pivot away from these areas toward AI and new device development.

<details><summary>References</summary>
<ul>
<li><a href="https://easternherald.com/2026/08/22/apple-siri-vision-pro-layoffs-ai-restructuring/">Apple Siri Vision Pro Layoffs : 200 Jobs Cut in AI Shift</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#Vision Pro`, `#AI`, `#layoffs`

---

<a id="item-tech-news-11"></a>
### [US Groups Urge FTC to Probe AI Firms&\#x27; Book Destruction](https://www.axios.com/2026/08/21/ftc-ai-companies-book-destruction-investigate) ⭐️ 7.0/10

On August 21, 2026, more than a dozen U.S. civil society groups, including Demand Progress Education Fund and the Consumer Federation of America, sent a joint letter to the Federal Trade Commission \(FTC\) urging an investigation into AI companies that purchase, scan, and destroy physical books to train their models. The groups argue that this &quot;hoarding and destroying&quot; practice constitutes an unfair method of competition under Section 5 of the Federal Trade Commission Act, as it removes key materials from the market and may permanently eliminate rare editions. The letter specifically cites Anthropic, which reportedly spent millions of dollars buying books, cutting off their spines, and feeding the scanned pages to its Claude model, while Google, Microsoft, and OpenAI face similar copyright lawsuits. The groups do not advocate restricting AI training itself but claim the practice raises rivals&\#x27; costs and builds a moat. If the FTC takes up the case, the dispute over AI training data would expand from copyright law into competition regulation.

telegram · zaihuapd · Aug 22, 15:40

**「Background」** AI companies have been acquiring physical books in bulk, scanning their contents to train large language models, and then destroying the physical copies. This practice has drawn criticism because it removes rare or out-of-print works from circulation, potentially losing them permanently. The Federal Trade Commission \(FTC\) enforces Section 5 of the Federal Trade Commission Act, which prohibits unfair methods of competition, and has been increasingly scrutinizing AI industry practices. The letter from consumer groups asks the FTC to examine whether this book destruction constitutes an unfair competitive practice, which would extend the ongoing legal battles over AI training data from copyright law into competition regulation.

**「Impact」** If the FTC investigates, AI companies could face new antitrust scrutiny over their data acquisition practices, potentially forcing changes in how they source training materials and affecting the broader AI industry&\#x27;s access to copyrighted works.

<details><summary>References</summary>
<ul>
<li><a href="https://www.axios.com/2026/08/21/ftc-ai-companies-book-destruction-investigate">Exclusive: FTC urged to investigate AI firms for destroying books</a></li>
<li><a href="https://www.cbsnews.com/news/ftc-ai-companies-destroying-books/">AI companies accused of hoarding and destroying millions of books - CBS News</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#FTC`, `#antitrust`, `#training data`, `#Anthropic`

---