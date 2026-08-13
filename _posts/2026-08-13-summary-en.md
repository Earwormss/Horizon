---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 41 items, 18 important content pieces were selected

---

**Technology News**
1. [OpenAI and Cerebras Launch GPT-5.6 Sol Ultrafast](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepSeek Harness Developer Preview Released](#item-tech-news-2) ⭐️ 8.0/10
3. [DRAM Attack Achieves Arbitrary Code Execution](#item-tech-news-3) ⭐️ 8.0/10
4. [Choose Boring Technology](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek V4 Pro 0813 Released with Open Weights](#item-tech-news-5) ⭐️ 8.0/10
6. [DeepMind SL2T Brings Sign Language AI to Pixel 11](#item-tech-news-6) ⭐️ 8.0/10
7. [Google Unveils Gemini 3.7 Flash with Competitive Pricing](#item-tech-news-7) ⭐️ 7.0/10
8. [Gloomberb: Open-Source TUI for Financial Data](#item-tech-news-8) ⭐️ 7.0/10
9. [City2Graph: Python Library for Urban Heterogeneous Graphs](#item-tech-news-9) ⭐️ 7.0/10
10. [WorldProof: Diagnosing World-Model Failures and Pixel Metric Limits](#item-tech-news-10) ⭐️ 7.0/10
11. [Ablating One Attention Head Breaks Chess Transformer&\#x27;s Sacrifice Finding](#item-tech-news-11) ⭐️ 7.0/10
12. [Claude Chrome Extension Syncs Sessions Across Devices](#item-tech-news-12) ⭐️ 7.0/10

**Financial News**
1. [S&amp;P 500 Profit Margins Hit Record High, Boosting Stocks](#item-finance-news-1) ⭐️ 8.0/10
2. [CXMT Overtakes Tencent as Most Valuable Chinese Company](#item-finance-news-2) ⭐️ 8.0/10
3. [Bill Ackman&\#x27;s Pershing Square Re-enters Netflix, Citing Streaming Victory](#item-finance-news-3) ⭐️ 7.0/10
4. [Chinese chipmaker YMTC overtakes Micron and Kioxia in NAND memory shipments](#item-finance-news-4) ⭐️ 7.0/10
5. [EVs Dominate China&\#x27;s Car Market: 5 Takeaways from Latest Auto Sales Data](#item-finance-news-5) ⭐️ 7.0/10
6. [China&\#x27;s Economic Slowdown Pushes Gig Work to 53 Million, Yet Oversupply Persists](#item-finance-news-6) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
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

---

<a id="item-tech-news-2"></a>
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

---

<a id="item-tech-news-3"></a>
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

---

<a id="item-tech-news-4"></a>
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

---

<a id="item-tech-news-5"></a>
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

---

<a id="item-tech-news-6"></a>
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

---

<a id="item-tech-news-7"></a>
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

---

<a id="item-tech-news-8"></a>
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

---

<a id="item-tech-news-9"></a>
### [City2Graph: Python Library for Urban Heterogeneous Graphs](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph is a new Python library that converts geospatial urban data into heterogeneous graphs for spatial analysis, network analysis, and Graph Neural Networks \(GNNs\). It supports building morphological graphs from OpenStreetMap and Overture Maps data, transit graphs from GTFS and GBFS feeds via DuckDB, mobility graphs from origin-destination matrices, and proximity/contiguity graphs using KNN, Delaunay, Gilbert, Waxman, and queen/rook methods. The library integrates with PyTorch Geometric, NetworkX, rustworkx, and GeoDataFrames, preserving geometry and attributes across conversions. The accompanying paper by Sato, Pietrostefani, Mahabir, and Arribas-Bel was published in Computers, Environment and Urban Systems \(2026\), volume 130, article 102492. The library is available on GitHub at https://github.com/c2g-dev/city2graph.

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · Aug 13, 11:59

**「Background」** Urban data is often stored as flat feature tables, which lose the relational structure inherent in cities, such as how buildings connect to streets or how people move between areas. Heterogeneous graphs represent multiple types of nodes and edges, enabling more expressive models for tasks like urban planning and mobility prediction. City2Graph addresses the gap by providing a unified tool to construct such graphs from diverse geospatial data sources.

**「Impact」** Researchers and practitioners in urban computing and GeoAI can now use City2Graph to streamline the conversion of raw geospatial data into graph formats compatible with popular GNN frameworks, potentially accelerating work in urban analytics and machine learning. However, as a new tool, its adoption and long-term maintenance remain to be seen.

**Tags**: `#graph-neural-networks`, `#geospatial`, `#urban-computing`, `#python-library`, `#spatial-analysis`

---

<a id="item-tech-news-10"></a>
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

---

<a id="item-tech-news-11"></a>
### [Ablating One Attention Head Breaks Chess Transformer&\#x27;s Sacrifice Finding](https://www.reddit.com/r/MachineLearning/comments/1vmvl4w/chessformer_lens_demo_ablating_1_of_a_chess/) ⭐️ 7.0/10

A Reddit post on r/MachineLearning demonstrates that ablating a single attention head in a chess transformer, named chessformer\_lens, causes the model to stop finding Morphy&\#x27;s queen sacrifice. The demo includes GIFs and links to GitHub notebooks for replication. This finding highlights the critical role of specific attention heads in learned behaviors, offering a concrete example of mechanistic interpretability in transformers. The post is brief and lacks detailed analysis, but the reproducible nature of the result makes it valuable for understanding transformer internals.

reddit · r/MachineLearning · /u/Weird-Asparagus4136 · Aug 13, 00:29

**「Background」** Mechanistic interpretability aims to reverse-engineer the internal computations of neural networks, often by studying attention heads in transformers. Ablation studies, where parts of a model are removed or disabled, help identify which components are responsible for specific behaviors. Morphy&\#x27;s queen sacrifice is a famous chess tactic from a historic game, used here as a test case for the model&\#x27;s ability to recognize complex patterns.

**「Impact」** This demonstration provides evidence that individual attention heads can be responsible for specific high-level behaviors in transformers, which could inform future interpretability research and model debugging. However, the result is from a single demo and may not generalize across all models or tasks.

**Tags**: `#mechanistic interpretability`, `#transformers`, `#chess AI`, `#attention heads`, `#ablation study`

---

<a id="item-tech-news-12"></a>
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

---

## Financial News

<a id="item-finance-news-1"></a>
### [S&amp;P 500 Profit Margins Hit Record High, Boosting Stocks](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 8.0/10

S&amp;P 500 companies&\#x27; net profit margin reached a record 16.9% in the second quarter, up from 14.8% in the first quarter and 12.9% a year ago, according to FactSet data. This is the highest since FactSet began tracking in 2009, driven by strong demand and contributions from mega-caps like Alphabet and Amazon.

rss · CNBC Finance · Aug 13, 20:21

**「Background」** Net profit margin is the percentage of revenue a company keeps after paying all expenses. The five-year average for the S&amp;P 500 is 12.4%, so the current figure is well above the norm. Eight of 11 sectors reported higher margins than a year ago, led by technology and communication services.

**「Impact」** Higher profit margins mean companies are more efficient at converting sales into profit, which supports stock valuations and can benefit investors. However, competitive pressure in tech could pose a future risk to margins, according to Vanguard economist Adam Schickling.

**Tags**: `#S&amp;P 500`, `#profit margins`, `#earnings`, `#stock market`, `#FactSet`

---

<a id="item-finance-news-2"></a>
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

---

<a id="item-finance-news-3"></a>
### [Bill Ackman&\#x27;s Pershing Square Re-enters Netflix, Citing Streaming Victory](https://www.cnbc.com/2026/08/13/ackman-buys-netflix-again-four-years-later-says-it-won-streaming-wars.html) ⭐️ 7.0/10

Bill Ackman&\#x27;s Pershing Square Capital Management has disclosed a new stake in Netflix, saying the company has &quot;effectively won the streaming wars&quot; with over 325 million subscribers and an attractive valuation after a sharp sell-off. Netflix shares rose nearly 4% on the news.

rss · CNBC Finance · Aug 13, 18:04

**「Background」** Ackman previously bought Netflix in early 2022 but sold the entire stake about three months later after the company reported its first subscriber decline in over a decade, citing uncertainty about its business model. Since then, Netflix shares have fallen roughly 50% from their June 2025 high, cutting its valuation to about 21 times forward earnings from over 40 times.

**「Impact」** The disclosure signals confidence in Netflix&\#x27;s competitive position and could influence investor sentiment, potentially affecting the company&\#x27;s stock price and the broader streaming sector.

**Tags**: `#Netflix`, `#Bill Ackman`, `#Pershing Square`, `#Streaming`, `#Investments`

---

<a id="item-finance-news-4"></a>
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

---

<a id="item-finance-news-5"></a>
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

---

<a id="item-finance-news-6"></a>
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

---