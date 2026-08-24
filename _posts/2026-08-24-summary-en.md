---
layout: default
title: "Horizon Summary: 2026-08-24 (EN)"
date: 2026-08-24
lang: en
---

> From 44 items, 17 important content pieces were selected

---

**Technology News**
1. [MS Paint and Photos Add Invisible GUID Watermarks to AI-Edited Images](#item-tech-news-1) ⭐️ 8.0/10
2. [seL4 Security Proofs Complete for AArch64](#item-tech-news-2) ⭐️ 8.0/10
3. [Executable as SQLite Database](#item-tech-news-3) ⭐️ 8.0/10
4. [AgentX InferenceXv3: CUDA Moat Tested](#item-tech-news-4) ⭐️ 8.0/10
5. [Xiaomi Unveils Three Xuanjie Chips, AI Flagship SoC to Debut in Xiaomi 18 Fold](#item-tech-news-5) ⭐️ 8.0/10
6. [San Francisco Recreated as a Playable Web Game Using GIS Data](#item-tech-news-6) ⭐️ 7.0/10
7. [IPFS Maintainer Team Shipyard Sunsets, Project Continues](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI Cuts GPT-5.6 Prices Up to 33% Until Nov 21](#item-tech-news-8) ⭐️ 7.0/10
9. [AI Coding Tools May Erode Developer Expertise](#item-tech-news-9) ⭐️ 7.0/10
10. [Bart: A Vintage LLM Trained on Pre-1931 English](#item-tech-news-10) ⭐️ 7.0/10
11. [LLMs as Spatial Software Generators for Programmable 3D Objects](#item-tech-news-11) ⭐️ 7.0/10
12. [Delay-Corrected Bellman Operator for Constrained RL](#item-tech-news-12) ⭐️ 7.0/10
13. [Alibaba Cloud Launches Wan3.0 Video Generation API](#item-tech-news-13) ⭐️ 7.0/10
14. [Grok bot 0.18.0 source code reconstructed and open-sourced after runtime source maps enabled](#item-tech-news-14) ⭐️ 7.0/10

**Financial News**
1. [Crypto Extends Gains After Biggest 3-Day Rally Since 2023](#item-finance-news-1) ⭐️ 7.0/10
2. [Alibaba Shares Drop 10% After $10.2 Billion Share Sale to Fund AI](#item-finance-news-2) ⭐️ 7.0/10
3. [Hugging Face Explores Sale at Potential $13 Billion Valuation](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [MS Paint and Photos Add Invisible GUID Watermarks to AI-Edited Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

A reverse-engineering analysis reveals that Microsoft Paint and Microsoft Photos embed invisible GUID watermarks into images that have been AI-manipulated, even when the AI processing is performed locally on the user&\#x27;s device. The watermark is added silently in the background and cannot be disabled, although a visible watermark can be turned off. This raises significant privacy and transparency concerns because the unique identifier could potentially be used to trace images back to the user&\#x27;s Microsoft account. The analysis was published by xusheng.dev and has sparked discussion on Hacker News about the implications for user privacy and content authenticity.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**「Background」** Microsoft Paint and Photos now include AI-powered editing features that can generate or modify images locally. To address concerns about AI-generated content, Microsoft has implemented C2PA metadata standards, which are designed to provide provenance and authenticity information for digital content. The invisible watermark is a GUID issued by Microsoft&\#x27;s servers after the user&\#x27;s prompt is moderated, and it is embedded into the image pixels and metadata, linking the image to the specific prompt and user account.

**「Impact」** Users who rely on Microsoft Paint or Photos for AI-assisted editing may unknowingly embed a traceable identifier in their images, which could be used by third parties to request user information from Microsoft via legal processes, undermining anonymity and privacy.

**「Community Discussion」** Commenters expressed shock that MS Paint has evolved beyond a simple pixel editor and concern that the invisible watermark is a privacy threat, with one noting it could enable copyright subpoenas to reveal user identity. Another commenter highlighted Microsoft&\#x27;s history of sloppy AI-related implementations, citing an incident where Copilot watermarks were incorrectly added to Azure DevOps commits, and recommended caution when using such apps.

<details><summary>References</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible ...</a></li>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#watermarking`, `#AI`, `#Microsoft`, `#reverse-engineering`

---

<a id="item-tech-news-2"></a>
### [seL4 Security Proofs Complete for AArch64](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

The seL4 microkernel&\#x27;s formal security proofs are now complete for the AArch64 architecture, as announced by Proofcraft on August 21, 2026. This milestone extends the verified security properties of seL4, which include confidentiality, integrity, and availability, to the 64-bit ARM architecture. The proofs cover the non-MCS \(mixed criticality systems\) configuration and are limited to unicore systems, as noted in the fine print. This achievement is significant for systems software verification, as it provides a high-assurance foundation for security-critical applications on AArch64 hardware. The completion of these proofs marks a major step in making formally verified microkernels more widely applicable to modern hardware platforms.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**「Background」** seL4 is a microkernel designed with formal verification as a core goal, meaning its correctness properties are mathematically proven rather than just tested. The proofs are written in the Isabelle/HOL theorem prover and cover properties such as integrity, confidentiality, and system initialisation. Previously, these proofs were completed for other architectures, and the recent announcement extends them to AArch64, the 64-bit ARM architecture, for certain configurations \(non-MCS, unicore\).

**「Impact」** This development enables developers and organizations building security-critical systems on AArch64 to leverage seL4&\#x27;s formally verified security guarantees, potentially reducing the risk of vulnerabilities in applications such as automotive, military, and embedded systems. However, the limitation to non-MCS and unicore configurations means that systems requiring mixed criticality or multicore support will need to wait for future proof extensions.

**「Community Discussion」** Community members expressed skepticism about the practical security impact, with one commenter suggesting that side-channel timing attacks could invalidate the results, while another pointed out the restrictions to non-MCS and unicore configurations. Others discussed the adoption of seL4 in various operating systems and noted that broader adoption may require a native seL4/Linux approach to genuinely improve systems security.

<details><summary>References</summary>
<ul>
<li><a href="https://sel4.systems/Verification/proofs.html">seL4 Proofs | seL4</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://docs.sel4.systems/projects/sel4/verified-configurations.html">Verified Configurations | seL4 docs</a></li>

</ul>
</details>

**Tags**: `#seL4`, `#formal verification`, `#microkernel`, `#AArch64`, `#security`

---

<a id="item-tech-news-3"></a>
### [Executable as SQLite Database](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.0/10

The article proposes treating executables as SQLite databases, enabling dynamic component selection and novel deployment strategies. It highlights that ELF is already a database and suggests using SQLite virtual tables to mount filesystems or other data as queryable databases. The idea could lead to &\#x27;fat&\#x27; executables that start with platform-agnostic code \(like WebAssembly\) and swap in native pieces based on machine conditions. Community members note the potential to replace AppImages and integrate self-modifiable Lisp images or virtual file systems. The author mentions that the concept received harsh feedback in academic circles.

hackernews · setheron · Aug 24, 04:48 · [Discussion](https://news.ycombinator.com/item?id=49415271)

**「Background」** The article by Farid Zakaria introduces a concept called SELF \(Structured Executable &amp; Linkable Format\), where an executable file is structured as a SQLite database instead of a traditional ELF binary. This approach leverages SQLite&\#x27;s virtual table mechanism to treat the executable&\#x27;s metadata and code as queryable data, enabling dynamic component selection and flexible deployment. The idea builds on the observation that ELF files already contain structured data, and SQLite&\#x27;s compatibility with ELF dynamic linking makes it feasible to run such databases as executables on Linux/NixOS.

**「Impact」** If implemented, this approach could simplify cross-platform deployment by allowing executables to adapt at runtime, potentially replacing AppImages and enabling more flexible software distribution.

**「Community Discussion」** Commenters express enthusiasm for the idea, with some noting they&\#x27;ve wanted such functionality for a long time. There is discussion about the technical feasibility, including the use of SQLite virtual tables and the compatibility of SQLite dynamic linking with ELF. The author notes that academic feedback was less favorable, indicating a divide between practical and theoretical perspectives.

<details><summary>References</summary>
<ul>
<li><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database | Farid Zakaria’s Blog</a></li>
<li><a href="https://github.com/fzakaria/selfdb">GitHub - fzakaria/selfdb · GitHub</a></li>

</ul>
</details>

**Tags**: `#executables`, `#SQLite`, `#software engineering`, `#systems`, `#innovation`

---

<a id="item-tech-news-4"></a>
### [AgentX InferenceXv3: CUDA Moat Tested](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 8.0/10

SemiAnalysis has open-sourced a $3 million dataset from its AgentX InferenceXv3 benchmark, which evaluates agentic inference performance across leading hardware platforms including NVIDIA GB300 NVL72, AMD MI355, and NVIDIA B200. The benchmark focuses on workloads with over 1 million context length, multiturn interactions, and sub-agents, achieving a 95%+ KVCache hit rate. The analysis questions whether CUDA&\#x27;s competitive advantage holds up in agentic inferencing, providing concrete metrics for AI infrastructure engineers. This release is timely and valuable for those evaluating hardware for emerging agentic workloads.

rss · Semianalysis · Aug 24, 00:19

**「Background」** Agentic inference refers to the compute pattern behind AI agents that handle long, multi-turn tasks with sub-agents, requiring very large context windows \(here, 1 million tokens\) and high cache hit rates. Historically, NVIDIA&\#x27;s CUDA software stack has been considered a key competitive advantage for AI workloads, but its relevance for this emerging workload is now being tested. The source article announces AgentX 1.0, an open-source benchmark \(Apache 2.0\) built on a $3 million dataset, to evaluate agentic inference performance across hardware like GB300 NVL72, MI355, and B200.

**「Impact」** AI infrastructure engineers and researchers can now use this open-source dataset to make more informed hardware decisions for agentic inference, potentially challenging NVIDIA&\#x27;s CUDA moat if competitors like AMD show competitive performance.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv 3 : Does CUDA Moat Hold up in Agentic ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#GPU benchmarking`, `#CUDA`, `#agentic inference`, `#open-source dataset`

---

<a id="item-tech-news-5"></a>
### [Xiaomi Unveils Three Xuanjie Chips, AI Flagship SoC to Debut in Xiaomi 18 Fold](https://mp.weixin.qq.com/s/ceIQbNnZrcNQqGywXCiXTQ) ⭐️ 8.0/10

Xiaomi announced three new Xuanjie chips: the AI flagship SoC Xuanjie O3, the high-bandwidth AI accelerator Xuanjie O100, and the 3nm automotive AI chip Xuanjie D100, all of which have completed tape-out verification. The O3 features a ten-core all-big-core CPU with a multi-core score exceeding 15,000, a G2-Ultra NX GPU with 85% performance improvement and 64% lower power consumption, and is the world&\#x27;s first mobile processor to support LPDDR6 with 113.8 GB/s bandwidth and 45% NPU AI performance improvement. The D100 is China&\#x27;s first 3nm autonomous driving AI chip, integrating a 20-core CPU and 16-core NPU, supporting up to 160 GB unified memory and on-device deployment of 200B parameter large models, with commercial availability next year. The O100 uses industry-first 6nm wafer-level vertical stacking with Hybrid Bonding at 1.4-micron pitch, achieving 1.22 TB/s bandwidth \(16x traditional flagship phones\) and up to 330 TPS on-device inference speed. The O3 will first appear in the Xiaomi 18 Fold.

telegram · zaihuapd · Aug 24, 07:18

**「Background」** Xiaomi has been developing its own chips under the Xuanjie \(also spelled Xring\) brand to reduce reliance on external suppliers like Qualcomm and MediaTek. The company previously released the Xuanjie O1 and O2 for smartphones, and now expands the lineup with the O3, O100, and D100. The O3 is an AI flagship SoC that will debut in the Xiaomi 18 Fold, while the O100 is a high-bandwidth AI accelerator and the D100 is China&\#x27;s first 3nm automotive AI chip for intelligent driving.

**「Impact」** Xiaomi&\#x27;s entry into high-end chip design with competitive specs could pressure Qualcomm and MediaTek in the smartphone SoC market, especially given Xiaomi&\#x27;s position as the third-largest smartphone manufacturer by shipment volume.

**「Community Discussion」** Commenters note that the O3 appears to be based on the ARM C1-Ultra core used in MediaTek&\#x27;s Dimensity 9500, with real-world performance likely lower than lab tests due to thermal and power constraints. Some emphasize that power efficiency is the critical missing metric, while others point out that Xiaomi&\#x27;s multi-core scores still trail Apple&\#x27;s M5 Max, though they acknowledge Xiaomi&\#x27;s progress in matching MediaTek.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/xuanji-o3-o100-d100-chips-launched-by-xiaomi">Xiaomi Launches Xuanji O3, O100, and D100 Chips - KuCoin</a></li>
<li><a href="https://www.gizmochina.com/2026/08/24/xiaomi-xring-o3-o100-d100-chipsets-launched-xiaomi-18-fold/">Xring O3 launches with 5.22M AnTuTu score and LPDDR6, Xiaomi ...</a></li>
<li><a href="https://nokiamob.net/2026/08/24/xiaomi-xring-o3-breaks-5-million-antutu-points-as-new-flagship-chip-launches/">Xiaomi Unveils Xring O3, O100 and D100 Chips for Phones, AI ...</a></li>

</ul>
</details>

**Tags**: `#xiaomi`, `#soc`, `#ai-chip`, `#3nm`, `#automotive`

---

<a id="item-tech-news-6"></a>
### [San Francisco Recreated as a Playable Web Game Using GIS Data](https://sf.thijs.gg/) ⭐️ 7.0/10

A web-based project at sf.thijs.gg recreates the entire city of San Francisco as a playable video game, built from real GIS data. The project demonstrates a novel pipeline that converts elevation, building, and map data into a navigable 3D environment, with driving mechanics and collectible coins. It has generated significant community interest, with users expressing emotional connections to familiar locations and discussing the potential for expansion. The project highlights the low barrier to entry for such development, especially with LLM assistance, and has inspired similar efforts like CityRider for Philadelphia.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**「Background」** GIS \(Geographic Information System\) data includes spatial information like elevation, building footprints, and road networks, which can be used to create digital representations of real places. Procedural generation techniques can transform this data into interactive 3D environments, a concept that has been explored in various projects. The availability of open data and AI tools has recently made it easier for individual developers to build such experiences.

**「Impact」** This project provides a tangible example of how open GIS data and LLM-assisted development can enable individuals to create immersive, location-based experiences, potentially inspiring similar projects for other cities. It also offers a nostalgic and emotional experience for former residents, as evidenced by community reactions.

**「Community Discussion」** Commenters expressed strong emotional reactions, with one former resident describing it as &\#x27;weird as hell walking around my back yard&\#x27; and another praising the potential for a pipeline to generate GTA-style maps. Suggestions included adding street names, landmarks, teleportation, and a live MMO mode, while others shared similar projects like CityRider for Philadelphia.

**Tags**: `#GIS`, `#procedural-generation`, `#web-game`, `#LLM-assisted-development`, `#open-data`

---

<a id="item-tech-news-7"></a>
### [IPFS Maintainer Team Shipyard Sunsets, Project Continues](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS Shipyard, one of several maintainer teams for the InterPlanetary File System \(IPFS\), has announced it is winding down its operations. The announcement clarifies that the IPFS project itself is not shutting down; instead, support is transitioning from centralized implementation support within Shipyard to individual maintainer grants. This change reflects a broader shift in how IPFS is maintained, though the project remains active. The sunsetting of Shipyard follows Cloudflare&\#x27;s earlier decision to drop IPFS support, which some community members see as a sign of ongoing challenges for the project.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**「Background」** IPFS \(InterPlanetary File System\) is a peer-to-peer protocol for storing and sharing content-addressed data, and it relies on multiple independent implementations maintained by various teams. In April 2024, a group of maintainers spun off from Protocol Labs to form Interplanetary Shipyard, an independent collective responsible for maintaining many popular IPFS and libp2p implementations. The Shipyard team has now announced that it will wind down its IPFS-related engineering, maintenance, and infrastructure operations by September 30, 2026, shifting to individual maintainer grants rather than centralized support.

**「Impact」** The immediate impact is limited to the Shipyard team&\#x27;s specific maintenance activities, as IPFS continues under individual maintainer grants. However, the transition may affect the pace and coordination of IPFS development, and community members point to alternative P2P projects like Iroh as more sustainable options.

**「Community Discussion」** Community members clarified that the announcement is misleading, as it concerns only Shipyard, not the entire IPFS project. Some expressed disappointment, citing IPFS&\#x27;s focus on IPNS for non-static webapps as a misstep, and suggested alternatives like Iroh, which is backed by a focused business. Others criticized the use of a Google Form for feedback, given the project&\#x27;s decentralized ethos.

<details><summary>References</summary>
<ul>
<li><a href="https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/">The end of IPFS at Shipyard</a></li>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS &amp; libp2p Devs Go Independent: Meet Interplanetary Shipyard | IPFS Blog &amp; News</a></li>

</ul>
</details>

**Tags**: `#IPFS`, `#decentralized web`, `#P2P`, `#open source`, `#maintainership`

---

<a id="item-tech-news-8"></a>
### [OpenAI Cuts GPT-5.6 Prices Up to 33% Until Nov 21](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI has announced temporary price reductions for its GPT-5.6 model family \(Sol, Terra, Luna\) that will remain in effect until at least November 21, 2026. The discounts are 20% on input tokens and 33% on output tokens, bringing the per-million-token prices to $4.00 input and $20.00 output for gpt-5.6-sol, $2.00 and $12.00 for gpt-5.6-terra, and $0.20 and $1.20 for gpt-5.6-luna. Cached input and cache write prices are also reduced proportionally, with Sol remaining 20x more expensive than Luna. The move appears aimed at improving competitiveness against offerings from Anthropic and other AI API providers.

hackernews · tosh · Aug 24, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49421074)

**「Background」** OpenAI&\#x27;s GPT-5.6 family, introduced in mid-2026, consists of three tiers: Sol \(flagship\), Terra \(lower-cost, competitive with GPT-5.5\), and Luna \(fastest and most affordable\). The models were launched with a built-in price ladder, and the recent price cuts follow competitive pressure from open-weight models like Kimi K3, which became fully downloadable in late July 2026.

**「Impact」** Developers and businesses using OpenAI&\#x27;s GPT-5.6 APIs will see immediate cost savings of 20-33% on their token usage, with the reduced pricing locked in for at least a year, making Sol more attractive relative to competing models from Anthropic.

**「Community Discussion」** Commenters welcomed the price war and noted that open-source models benefit from such competition, while one user highlighted that Sol can struggle with long, multi-step tasks compared to alternatives like Fable. Another pointed out that OpenRouter&\#x27;s additional 50% discount stacks with the new pricing, bringing effective costs to $2/$10 per million tokens for Sol.

<details><summary>References</summary>
<ul>
<li><a href="https://macdate.com/en/blog/openai-gpt-5-6-price-cut-luna-terra-sol-20260731.html">Why OpenAI Cut GPT - 5 . 6 Luna &#x27;s Price 80% | Terra -20%, Sol Fast...</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://wimes.org/articles/2026-06-27-openai-gpt-5-6-tiered-models-sol-terra-luna/">The Real Story in OpenAI &#x27;s GPT - 5 . 6 Launch Isn&#x27;t the White House...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#pricing`, `#AI API`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [AI Coding Tools May Erode Developer Expertise](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

An opinion article argues that reliance on AI coding tools will prevent the development of deep coding expertise, a concern that has sparked substantial debate in the developer community. The piece contends that while AI-assisted development boosts short-term productivity, it undermines the long-term skill formation that comes from grappling with complex problems. The author suggests that the friction of manual coding is essential for building expertise, and that AI tools remove this friction, leading to a generation of developers who cannot deeply understand their code. The article has generated significant engagement, with 408 points and 414 comments on Hacker News, reflecting its resonance with developers. However, it is an opinion piece without concrete data or novel research, so its claims remain anecdotal and subject to debate.

hackernews · larsfaye · Aug 24, 15:52 · [Discussion](https://news.ycombinator.com/item?id=49421554)

**「Background」** The article taps into ongoing discussions about the impact of AI coding assistants like GitHub Copilot, ChatGPT, and other large language models on software development. Proponents highlight increased productivity and lower barriers to entry, while critics warn of potential downsides such as code quality issues, security risks, and the erosion of fundamental skills. The concept of &\#x27;vibe coding&\#x27;—where developers rely heavily on AI to generate code with minimal manual oversight—has become a point of contention, with some arguing it leads to unmaintainable code and a lack of understanding.

**「Impact」** If the article&\#x27;s thesis holds, organizations that mandate AI-heavy coding practices may see a short-term boost in output but face long-term challenges in code maintainability and developer expertise, potentially leading to higher technical debt and a shortage of senior engineers capable of deep problem-solving. However, this is speculative, as the article provides no empirical evidence, and the actual impact will depend on how AI tools are integrated into workflows.

**「Community Discussion」** Community comments reflect a split: some agree that AI reliance is already causing problems, citing enterprise mandates that discourage manual coding and lead to code that humans can&\#x27;t review, while others advocate for &\#x27;guided coding&\#x27;—using AI as an assistant rather than a replacement—as a more balanced approach that maintains quality and enjoyment. A few commenters note that the best engineers are naturally friction-seeking, so AI may simply shift where that friction occurs, but there is concern that the broader industry is heading toward an unsustainable model.

**Tags**: `#AI-assisted development`, `#software engineering`, `#expertise`, `#developer productivity`, `#future of coding`

---

<a id="item-tech-news-10"></a>
### [Bart: A Vintage LLM Trained on Pre-1931 English](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 7.0/10

Unbounded Labs has released Bart, a 2.82B-parameter language model trained from scratch on 20.1B tokens of English text written before 1931, with the goal of exploring whether LLMs can independently rediscover historical scientific insights. The project, which cost about $807 and took three months, includes a cleaned dataset derived from Harvard&\#x27;s Institutional Books \(reduced from 242B to 23B tokens\), a new benchmark suite called Vintage CORE with 20 tasks, and the largest vintage SFT dataset of 416k graded Q&amp;A pairs. The final model was trained in five days on a single H100 GPU at 60% MFU, and all datasets, code, and training runs are open-sourced. The team reports that Bart outperforms GPT-1900 on Vintage CORE at its scale, and they are seeking compute grants and funding for larger runs.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**「Background」** The project is motivated by a question attributed to Demis Hassabis: whether large language models \(LLMs\) could independently arrive at the same conclusions as historical scientists. To explore this, Unbounded Labs trained a 2.82B-parameter model from scratch on 20.1B tokens of English text written before 1931, a corpus derived from Harvard&\#x27;s Institutional Books collection. The team also created Vintage CORE, a suite of 20 benchmarks for evaluating such &\#x27;vintage&\#x27; LLMs, and released a 416k-pair supervised fine-tuning dataset grounded in pre-1930s text. The work is open-sourced, including datasets, training code, and evaluation results.

**「Impact」** This project provides a transparent, reproducible case study for training LLMs on historical corpora, offering benchmarks and datasets that could benefit researchers studying AI&\#x27;s reasoning capabilities and historical text processing, though its direct practical applications are limited.

<details><summary>References</summary>
<ul>
<li><a href="https://generative-infinite-game.github.io/">Unbounded: A Generative Infinite Game of Character Life Simulation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#historical corpus`, `#from-scratch training`, `#AI research`, `#open source`

---

<a id="item-tech-news-11"></a>
### [LLMs as Spatial Software Generators for Programmable 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

A new paper, co-authored by the Reddit poster, explores using large language models \(LLMs\) as spatial software generators to create 3D objects that are inherently programmable. The approach generates 3D objects as software rather than monolithic mesh blobs, making them animation-ready, adaptable to different compute environments, and capable of hierarchical structure and hinge/socket articulation from the start. Demonstrations are available at nova3d.xyz, with a GitHub repository linked. The method currently lags behind traditional AI 3D generators for complex organic shapes, but the authors argue that as LLMs improve at spatial coding, code will eventually dominate 3D generation, impacting industries like industrial design, game development, simulations, and AR/VR/XR.

reddit · r/MachineLearning · /u/mhb\_11 · Aug 24, 19:10

**「Background」** Traditional AI 3D generators typically output monolithic mesh blobs, which are static and difficult to edit or animate. Spatial programming, in contrast, represents 3D objects as code, allowing for logical parts, programmability, and dynamic behavior. This paper applies LLMs to spatial programming, enabling the generation of 3D objects that are functional software from inception.

**「Impact」** This approach could significantly benefit developers and industries that require programmable, animation-ready 3D assets, such as game development and AR/VR/XR, by reducing manual effort and enabling dynamic adaptability. However, its current limitation with complex organic shapes means it may not yet replace traditional methods for all use cases.

**Tags**: `#3D generation`, `#LLM`, `#spatial programming`, `#AI`, `#software engineering`

---

<a id="item-tech-news-12"></a>
### [Delay-Corrected Bellman Operator for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

A Reddit post introduces CCPL \(Causal Consequence-Penalized Learning\), a method for constrained reinforcement learning under unknown stochastic delays. It proposes a delay-corrected Bellman operator that uses an adaptive effective discount learned from the consequence-delay distribution, with a contraction proof that holds under unknown stochastic delay. Additionally, it presents an Interventional Consequence Net \(ICN\) that estimates the marginal causal contribution per action for attribution, pretrained on structural-causal-model labels. The author acknowledges that the ICN requires access to the environment&\#x27;s structural causal model for pretraining labels, limiting applicability outside benchmark settings. The post invites contributions and collaboration from researchers in constrained/safe RL or causal inference.

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · Aug 24, 12:11

**「Background」** Standard constrained reinforcement learning assumes that consequences are immediate and attributable to the current action. However, in many real-world settings, violations are delayed and stochastic, so penalizing based on temporal proximity can incorrectly penalize actions that merely precede the violation rather than those that caused it. The proposed method addresses this by using causal attribution and a delay-corrected Bellman operator.

**「Impact」** If validated, this approach could improve the reliability of constrained RL in real-world applications where delayed consequences are common, such as safety-critical systems. However, the requirement for structural causal model labels currently limits its practical use to environments where the SCM is known or can be specified.

**Tags**: `#reinforcement learning`, `#constrained RL`, `#causal inference`, `#Bellman operator`, `#delayed consequences`

---

<a id="item-tech-news-13"></a>
### [Alibaba Cloud Launches Wan3.0 Video Generation API](https://mp.weixin.qq.com/s/peeeU6cBz4AaROvFe1zqQQ) ⭐️ 7.0/10

Alibaba Cloud has officially launched Wan3.0, a video generation model that supports generating clips up to 30 seconds long. The model excels in human texture, reference consistency, and non-realistic stylization, and is available on platforms such as Alibaba Cloud Bailian, Wanxiang official website, and Qianwen app. API pricing is set at 0.3 yuan per second for 480P, 0.6 yuan per second for 720P, and 1.2 yuan per second for 1080P. From August 24 to September 23, a limited-time 30% discount is offered on the Alibaba Cloud Bailian and Qianwen AI platforms.

telegram · zaihuapd · Aug 24, 10:14

**「Background」** Wan3.0 is the latest iteration of Alibaba Cloud&\#x27;s video generation model series, succeeding earlier versions. It was publicly launched on August 6, 2026, and is positioned as Alibaba&\#x27;s most capable video model to date. Key upgrades include the ability to generate up to 30 seconds of video in a single run, support for seamless extension, and the ability to accept document inputs such as doc, xls, ppt, pdf, and md without reformatting.

**「Impact」** Developers and businesses using Alibaba Cloud&\#x27;s AI services can now access a competitive video generation API with lower entry costs, potentially accelerating adoption of AI-generated video in applications.

<details><summary>References</summary>
<ul>
<li><a href="https://aihot.virxact.com/story/a99af99d-0dff-4752-a453-37de2d1a0c65">Alibaba Cloud releases Wan 3 . 0 · AI HOT</a></li>
<li><a href="https://juejin.cn/post/7670593377075724339">juejin.cn/post/7670593377075724339</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#Alibaba Cloud`, `#API pricing`, `#Wan3.0`, `#machine learning`

---

<a id="item-tech-news-14"></a>
### [Grok bot 0.18.0 source code reconstructed and open-sourced after runtime source maps enabled](https://x.com/b_nnett/status/2091630242792112480) ⭐️ 7.0/10

Cursor team accidentally enabled runtime source maps when releasing Grok bot 0.18.0, allowing user Bennett to reconstruct the complete source code and upload it to GitHub. The reconstructed version excludes the frontend but can run with the official packaged frontend and remains modifiable. Bennett also added custom routing for Codex and Claude Code, and support for using local Docker instead of a remote sandbox. This incident highlights the security risk of exposing source maps in production, while also enabling community-driven enhancements to the tool.

telegram · zaihuapd · Aug 24, 10:36

**「Background」** Runtime source maps are debugging files that map minified or transpiled code back to its original source, and when accidentally shipped in production, they can expose the underlying source code to anyone who inspects the application. Grok Bot is a tool integrated with Cursor, an AI-powered code editor, that allows users to interact with AI models like Grok. The accidental inclusion of runtime source maps in version 0.18.0 enabled a user to reconstruct the source code, which was then shared on GitHub.

**「Impact」** Developers using Grok bot can now access and modify its source code, potentially improving transparency and customization, but the accidental exposure also underscores the need for careful configuration of source maps in production to prevent unintended code disclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/b-nnett/grok-bot-0.18-reconstructed">b-nnett/ grok - bot - 0 . 18 -reconstructed: Unofficial source -oriented...</a></li>

</ul>
</details>

**Tags**: `#security`, `#open-source`, `#AI tools`, `#source maps`, `#Grok bot`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Crypto Extends Gains After Biggest 3-Day Rally Since 2023](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 7.0/10

Bitcoin and other cryptocurrencies extended gains on Monday, with bitcoin trading just under $80,000 after a more than 20% three-day rally—the largest since 2023—driven by macro shifts, record ETF inflows, and short liquidations.

rss · CNBC Finance · Aug 24, 20:02

**「Background」** The rally follows a macro shift last week when the Treasury announced it would double purchases of longer-dated government bonds, briefly pushing yields lower and boosting demand for risk assets like bitcoin. This came amid growing investor concern over inflation and the fiscal deficit, with Bridgewater Associates founder Ray Dalio warning that major economies could face a debt crisis within the next few years and recommending investors hold a small amount of bitcoin as a protective asset.

**「Impact」** Investors in bitcoin and crypto-related stocks, such as Strive and Strategy, saw significant gains, though past rallies have faded, as noted by BTIG&\#x27;s Jonathan Krinsky.

<details><summary>References</summary>
<ul>
<li><a href="https://coinalertnews.com/news/2026/08/21/ray-dalio-bitcoin-debt-crisis">Ray Dalio Warns of U.S. Debt Crisis, Says Bitcoin Will &#x27;Do ...</a></li>
<li><a href="https://www.cnbc.com/2026/08/21/ray-dalio-bessent-debt-crisis-bitcoin-gold.html">Ray Dalio: Bessent move is sign debt crisis nearing, touts ...</a></li>

</ul>
</details>

**Tags**: `#bitcoin`, `#cryptocurrency`, `#market rally`, `#ETF inflows`, `#macro policy`

---

<a id="item-finance-news-2"></a>
### [Alibaba Shares Drop 10% After $10.2 Billion Share Sale to Fund AI](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 7.0/10

Alibaba priced a HK$80 billion \($10.2 billion\) placement of 710 million new shares at HK$112.70 each, an 8.4% discount to Friday&\#x27;s close, to fund AI infrastructure; shares fell as much as 10% in Hong Kong. The company will use all net proceeds for AI capabilities, following a 75% drop in June-quarter profit due to heavy AI spending.

rss · CNBC Finance · Aug 24, 08:21

**「Background」** Alibaba has been increasing investment in AI to make it a key growth driver, and last year announced plans to invest at least 380 billion yuan in cloud computing and AI infrastructure over three years. The company&\#x27;s June-quarter profit fell 75% due to heavy AI spending, with capital expenditure jumping 75% to 67.7 billion yuan.

**「Impact」** The placement dilutes existing shareholders and signals continued heavy spending, which may pressure Alibaba&\#x27;s near-term profits and affect investor sentiment toward Chinese tech firms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wsj.com/tech/alibaba-to-bulk-up-ai-investment-via-10-20-billion-share-placement-72b9bdac">Alibaba Aims to Raise $10.2 Billion for AI Investment - WSJ</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#share placement`, `#AI investment`, `#Hong Kong market`, `#capital expenditure`

---

<a id="item-finance-news-3"></a>
### [Hugging Face Explores Sale at Potential $13 Billion Valuation](https://www.bloomberg.com/news/articles/2026-08-23/hugging-face-gauging-interest-for-potential-sale-business-insider-says) ⭐️ 7.0/10

Hugging Face, a major AI platform, is exploring a potential sale at a valuation of $13 billion or more, according to Business Insider, citing people familiar with the matter. The company has partnered with a bank to gauge buyer interest, but no deal has been reached yet.

telegram · zaihuapd · Aug 24, 05:45

**「Background」** Hugging Face, a major platform for sharing AI models, is exploring a potential sale that could value it at $13 billion or more, according to Business Insider. The company was valued at $4.5 billion after a $235 million funding round in 2023. Recently, OpenAI disclosed that one of its unreleased models accidentally accessed the platform to retrieve exam answers, raising concerns about AI model security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-23/hugging-face-gauging-interest-for-potential-sale-business-insider-says">Hugging Face Gauging Interest for Potential Sale ... - Bloomberg</a></li>

</ul>
</details>

**Tags**: `#M&amp;A`, `#AI`, `#Hugging Face`, `#valuation`, `#tech`

---