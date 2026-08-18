---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 37 items, 15 important content pieces were selected

---

**Technology News**
1. [Mojo Programming Language Goes Open Source](#item-tech-news-1) ⭐️ 9.0/10
2. [Linux 7.3 Boosts Performance When VRAM Runs Out](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B Matches GPT-5.6 Luna on AI Index](#item-tech-news-3) ⭐️ 8.0/10
4. [Turbovec: Rust Implementation of Google&\#x27;s TurboQuant for Vector Search](#item-tech-news-4) ⭐️ 7.0/10
5. [Railway Network as Flatbed Scanner](#item-tech-news-5) ⭐️ 7.0/10
6. [Fixing a Bricked Framework Laptop with $20 Tools](#item-tech-news-6) ⭐️ 7.0/10
7. [Data Centers Raise Downwind Air Temperatures by 0.8°C](#item-tech-news-7) ⭐️ 7.0/10
8. [Diffusion Model on 264KB SRAM Microcontroller](#item-tech-news-8) ⭐️ 7.0/10
9. [WeCom 5.0.10 Opens CLI and MCP for AI Agents](#item-tech-news-9) ⭐️ 7.0/10
10. [China Orders Early Removal of Custom Windows 10](#item-tech-news-10) ⭐️ 7.0/10
11. [OpenAI and CodeAI Partner to Bring AI Education to Millions of Students](#item-tech-news-11) ⭐️ 7.0/10
12. [Chinese AI Chips to Supply Nearly 90% of Domestic Market by 2026](#item-tech-news-12) ⭐️ 7.0/10

**Financial News**
1. [Rising Treasury Yields Squeeze Households as Wall Street Waits on Fed Chair](#item-finance-news-1) ⭐️ 7.0/10
2. [Kalshi Files to Launch Perpetual Futures on Equity Indexes](#item-finance-news-2) ⭐️ 7.0/10
3. [US Buy-Now-Pay-Later Loans Hit $160 Billion in 2025](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Mojo Programming Language Goes Open Source](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Mojo, the programming language designed for AI and high-performance computing, has been released as open source. The compiler and toolchain are now available under the Apache 2.0 license, fulfilling a promise made in May 2023. This follows the release of Mojo 1.0 last week. Originally intended as a superset of Python, Mojo has evolved into its own language, focusing on making GPU programming as painless as possible with Python-inspired syntax, though not fully compatible with existing Python code. The open-source release is a significant milestone for developers and the AI ecosystem.

rss · Simon Willison · Aug 18, 21:39

**「Background」** Mojo is a systems programming language developed by Modular Inc., designed for AI and high-performance computing. It combines Python-like syntax with systems-level features such as static typing and a borrow checker, inspired by Rust. Initially announced in May 2023 as a potential superset of Python, Mojo&\#x27;s roadmap shifted in August 2025 to allow it to evolve independently. The language reached version 1.0 in August 2026, and its compiler and toolchain have now been released under the Apache 2.0 license.

**「Impact」** Developers and organizations using or evaluating Mojo can now inspect, modify, and contribute to the compiler and toolchain, potentially accelerating adoption and community-driven improvements in AI and high-performance computing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo ( programming language ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mojo`, `#open-source`, `#programming-language`, `#ai`, `#compiler`

---

<a id="item-tech-news-2"></a>
### [Linux 7.3 Boosts Performance When VRAM Runs Out](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

Linux kernel version 7.3 introduces performance improvements for scenarios where GPU VRAM is exhausted, addressing a common pain point for GPU-intensive workloads. The changes aim to reduce the performance degradation that occurs when the system must fall back to system RAM or swap, which is typically much slower than dedicated VRAM. This improvement is particularly relevant for developers and users running large machine learning models, rendering tasks, or other memory-hungry GPU applications. The article highlights that the kernel&\#x27;s ability to manage VRAM overcommit effectively can significantly enhance overall system responsiveness and throughput in such situations. While not a paradigm shift, the update is a meaningful step forward in kernel-level GPU memory management.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**「Background」** Linux 7.3 is the upcoming kernel release that will introduce initial code to improve video memory \(vRAM\) management, particularly for systems with limited vRAM. This work originates from patches by Natalie Vock of Valve&\#x27;s Linux graphics team, aimed at enhancing the gaming experience when vRAM is scarce. The kernel&\#x27;s GPU drivers have long supported vRAM overcommit, allowing applications to request more memory than physically available, with the driver deciding what fits in the GPU&\#x27;s memory. The new improvements aim to reduce performance degradation and crashes when vRAM is exhausted, which is especially relevant for AMD GPUs.

**「Impact」** Users and developers running GPU workloads that exceed VRAM capacity will experience improved performance and reduced stuttering when memory pressure occurs, especially on systems with limited VRAM. The impact is most pronounced for those using open-source drivers, as NVIDIA users may not benefit immediately due to lack of paging support.

**「Community Discussion」** Commenters expressed enthusiasm for the upcoming release, with some noting the contrast between Linux&\#x27;s rapid performance improvements and Windows&\#x27; update fatigue. Others highlighted the technical challenge of kernel-level memory allocation, suggesting that applications themselves are better positioned to inform the kernel about VRAM stickiness. A few users on NVIDIA hardware expressed frustration over the lack of paging support, while others praised the article&\#x27;s clarity and the dedication of kernel developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7 . 3 To Land Initial Code Improving vRAM ... - Phoronix</a></li>
<li><a href="https://dzen.ru/b/aoQ5NBsdD1HIvsGi">Linux 7 . 3 защищает игры при дефиците VRAM Патчи... | Дзен</a></li>
<li><a href="https://imasters.com.br/noticia/o-linux-7-3-melhora-a-performance-quando-falta-vram-na-gpu">Linux 7 . 3 : melhor gerenciamento de VRAM em GPUs AMD | iMasters</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#VRAM`, `#performance`, `#GPU`, `#kernel`

---

<a id="item-tech-news-3"></a>
### [Qwen 3.8 27B Matches GPT-5.6 Luna on AI Index](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B, a compact 27-billion-parameter model, has scored 52 on the Artificial Analysis Intelligence Index, matching the score of GPT-5.6 Luna \(max\) and trailing just one point behind GLM-5.2 \(max\) and DeepSeek V4 Pro 0813 \(max\). The comparison is notable because GLM-5.2 has 753B parameters and DeepSeek V4 Pro 0813 has 1.7T parameters, while Luna&\#x27;s size is unknown but presumed much larger than 27B. This achievement underscores a significant trend in AI efficiency, where smaller models can rival much larger counterparts. The model was highlighted by Simon Willison as &\#x27;a truly astonishing model&\#x27; in a separate post.

rss · Simon Willison · Aug 17, 23:58

**「Background」** The Artificial Analysis Intelligence Index is a benchmark that measures the overall intelligence of large language models, with scores typically ranging from single digits to the 50s for the most capable models. Qwen 3.8 27B is an open-weight dense model released by Alibaba&\#x27;s Qwen team, featuring a native context length of 262,144 tokens \(extendable to 1,000,000 via YaRN\). Its score of 52 places it well above the median of 9 for comparable models, and it matches or nearly matches much larger proprietary models, highlighting a trend toward efficiency in model scaling.

**「Impact」** This result signals that organizations with limited computational resources can deploy a 27B-parameter model that performs competitively with frontier models orders of magnitude larger, potentially lowering the barrier to high-quality AI inference.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen 3 . 8 27 B - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**Tags**: `#qwen`, `#ai`, `#llms`, `#model-efficiency`, `#benchmark`

---

<a id="item-tech-news-4"></a>
### [Turbovec: Rust Implementation of Google&\#x27;s TurboQuant for Vector Search](https://github.com/RyanCodrai/turbovec) ⭐️ 7.0/10

Turbovec is a new Rust library that implements Google&\#x27;s TurboQuant technique for efficient vector search, offering compact indexes that significantly reduce memory usage—for example, 4GB for 10 million documents. This enables faster reverse index building and smoother development processes like debugging and performance testing. The project is positioned as a local, privacy-first search solution, with community members noting it outperforms FAISS, which is no longer state-of-the-art according to ANN benchmarks. However, alternatives like Qdrant already integrate TurboQuant, and the project is still early-stage with no SQLite bindings yet. The library aims to provide a high-performance, memory-efficient vector search option for Rust developers.

hackernews · fittingopposite · Aug 18, 18:07 · [Discussion](https://news.ycombinator.com/item?id=49349898)

**「Background」** TurboQuant is a vector quantization method proposed in 2025 by researchers affiliated with Google Research, Google DeepMind, and New York University. It aims to achieve near-optimal distortion rates while compressing vectors, making it useful for applications such as large language model inference, key-value cache compression, vector databases, and nearest neighbor search. Turbovec is a Rust library that implements TurboQuant for vector search, offering compact indexes and the potential for local, privacy-first applications.

**「Impact」** For Rust developers building local or privacy-focused search applications, Turbovec offers a compact, high-performance vector index that could enable on-device search with reduced memory footprint, though its novelty is limited by existing integrations like Qdrant and the lack of mature bindings.

**「Community Discussion」** Commenters are enthusiastic about the memory efficiency and potential for local, privacy-first search, with some asking about WASM compilation for browser extensions. However, others point out that Qdrant already integrates TurboQuant, and there is a call for a more human-readable README to encourage adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant - Wikipedia</a></li>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>

</ul>
</details>

**Tags**: `#vector-search`, `#rust`, `#quantization`, `#ann-benchmarks`, `#local-search`

---

<a id="item-tech-news-5"></a>
### [Railway Network as Flatbed Scanner](https://philo.gay/linecam/) ⭐️ 7.0/10

A creative project by an author known as &\#x27;otherayden&\#x27; uses the railway network as a flatbed scanner through slit-scan imaging, capturing continuous strips of the landscape as trains pass. The technique involves a camera fixed to a train window, capturing a single line of pixels over time to create a stretched panoramic image. The project is documented at philo.gay/linecam/ and has gained attention on Hacker News for its novel approach and artistic merit. The write-up includes technical details and insights into the process, and the community has engaged with related tools and historical precedents. While not a major technological breakthrough, it showcases a creative application of computer vision and imaging techniques.

hackernews · otherayden · Aug 18, 12:43 · [Discussion](https://news.ycombinator.com/item?id=49344825)

**「Background」** Slit-scan imaging is a technique where a camera captures a narrow slice of a scene over time, and these slices are then combined to form a single image. This method is commonly used in industrial line-scan cameras, which read a one-pixel-wide line at high speed to inspect objects moving on a conveyor belt. In this project, the author applied the same principle to the railway network: by mounting a line-scan camera on a train or using a fixed camera to capture passing trains, the motion of the train effectively acts as the scanning mechanism, producing a high-resolution &\#x27;flatbed scan&\#x27; of the railway environment. The technique has been explored by others, including a 2008 experiment by Ward Cunningham and a similar approach using regular cameras and manual frame splicing.

**「Impact」** The project provides a practical and artistic example of slit-scan imaging that may inspire hobbyists and creative coders to experiment with similar techniques, as evidenced by community members sharing their own implementations and tools.

**「Community Discussion」** Community members shared related experiences and tools: one noted a similar setup from 2008 using an iSight camera, another creates animations with a similar process, and a third linked to an interactive slit-scan toy. The consensus is positive, with praise for the project&\#x27;s blend of practicality and artistry.

<details><summary>References</summary>
<ul>
<li><a href="https://elsolitario.org/en/2026/08/18/line-scan-camera-train-photo-scanner/">Line - Scan Camera: Photographing Trains at 56,894px</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#imaging`, `#creative coding`, `#hardware`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Fixing a Bricked Framework Laptop with $20 Tools](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 7.0/10

A detailed guide by quantum5.ca describes how to recover a bricked AMD 7040-series Framework 13 laptop using only $20 worth of tools, addressing a common issue of BIOS update failures. The article highlights that BIOS updates can fail and leave laptops unbootable, and that manufacturers often provide inadequate support for such failures. The guide provides step-by-step instructions for using low-cost hardware to flash the BIOS chip directly, offering a practical solution for users who might otherwise face expensive repairs or e-waste. This issue is particularly relevant for Framework laptop owners, as the company&\#x27;s modular design does not exempt it from BIOS-related failures. The guide underscores the importance of DIY repair skills and the need for better manufacturer accountability.

hackernews · jp\_sc · Aug 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49345220)

**「Background」** Framework Laptop 13 is a modular, user-repairable laptop, and the AMD Ryzen 7040 series models use a BIOS that can be updated via software. BIOS updates are critical for security and stability, but a failed or faulty update can &\#x27;brick&\#x27; the device, rendering it unusable. The article describes a recovery process using inexpensive tools, highlighting that such failures are common and often lack manufacturer support.

**「Impact」** Framework laptop owners who experience a bricked device due to a failed BIOS update can now follow this guide to recover their laptop with minimal cost, avoiding expensive repairs or replacement. This also puts pressure on manufacturers like Framework to improve BIOS update reliability and support, as users are increasingly finding workarounds.

**「Community Discussion」** Commenters expressed frustration with manufacturers&\#x27; handling of BIOS update failures, with some suggesting legal action and others sharing similar experiences with other brands. There is a consensus that BIOS updates are still a common cause of bricked devices, and that manufacturers should be more accountable, with one commenter proposing that official updates should extend warranty coverage.

<details><summary>References</summary>
<ul>
<li><a href="https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/">Fixing a bricked AMD 7040 series Framework 13” laptop with $20...</a></li>
<li><a href="https://community.frame.work/t/framework-13-amd-ryzen-7040-bios-3-03b/46479/23">Framework 13 AMD Ryzen 7040 BIOS 3.03b</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#BIOS`, `#repair`, `#Framework`, `#embedded`

---

<a id="item-tech-news-7"></a>
### [Data Centers Raise Downwind Air Temperatures by 0.8°C](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban) ⭐️ 7.0/10

A peer-reviewed study in ASME&\#x27;s Journal of Sustainable Buildings presents field measurements showing that a data center campus raises downwind neighborhood air temperatures by approximately 0.8°C, with the effect extending about 500 meters. The mean upwind temperature was 42.7°C, increasing to 43.5°C near the eastern boundary of the campus. This empirical evidence quantifies the local heat impact of data centers, a topic of growing concern as their proliferation continues. The findings provide concrete data for engineers and policymakers assessing the environmental footprint of data center infrastructure.

hackernews · cwwc · Aug 18, 17:24 · [Discussion](https://news.ycombinator.com/item?id=49349147)

**「Background」** Data centers are among the fastest-growing sources of concentrated anthropogenic heat in urban environments, with heat flux densities that can exceed peak solar irradiance by a factor of 2–6. Until now, their thermal impacts on adjacent communities had never been directly measured or reported in peer-reviewed literature. This study provides the first field measurements of such impacts, addressing a gap in empirical evidence.

**「Impact」** The measured 0.8°C increase over 500m downwind provides empirical evidence that data centers can measurably affect local microclimates, which may inform urban planning and data center siting decisions, particularly in hot climates where additional heat can exacerbate heat stress.

**「Community Discussion」** Commenters debated the significance of the findings, with some noting the 0.8°C average is smaller than the title suggests, while others expressed skepticism about the broader &\#x27;data center panic,&\#x27; citing geopolitical motives and the relatively small footprint compared to global scale. There was also frustration over the polarized nature of the discussion, with some suspecting inauthentic accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban">Data Center Waste Heat as an Emerging Urban Thermal Hazard: First Field ...</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#environmental impact`, `#urban heat`, `#measurements`, `#infrastructure`

---

<a id="item-tech-news-8"></a>
### [Diffusion Model on 264KB SRAM Microcontroller](https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/) ⭐️ 7.0/10

A developer trained a diffusion model to generate 32x32 pixel images on a Shrike Lite microcontroller with only 264KB of SRAM. To accelerate inference, they used the onboard FPGA to create two parallel INT8 MAC engines with 16-bit accumulation, but the system hit a memory wall due to high I/O operations, making it slower than the MCU-only model \(~220 seconds per image vs ~70 seconds per image\). Despite heavy quantization and memory limits, some images came out well, though many were noisy and weird. The project is documented in a full case study, highlighting the challenges and trade-offs of running generative models on constrained edge hardware.

reddit · r/MachineLearning · /u/PandaBean18 · Aug 18, 09:26

**「Background」** Diffusion models are a class of generative models that iteratively denoise random noise to produce images, typically requiring substantial computational resources. Running them on microcontrollers with limited memory and processing power is challenging, often necessitating quantization and hardware acceleration. The Shrike Lite is a microcontroller with an FPGA, allowing custom hardware accelerators to be built for specific tasks.

**「Impact」** This experiment demonstrates that diffusion models can run on extremely memory-constrained devices, but also shows that naive hardware acceleration can be counterproductive due to memory bottlenecks. It provides practical insights for developers working on edge AI, emphasizing the importance of balancing compute and memory bandwidth.

**Tags**: `#edge-ai`, `#diffusion-models`, `#microcontrollers`, `#quantization`, `#fpga`

---

<a id="item-tech-news-9"></a>
### [WeCom 5.0.10 Opens CLI and MCP for AI Agents](https://mp.weixin.qq.com/s/uJf57P15-FQL_u6jLHiGYA) ⭐️ 7.0/10

WeCom \(Enterprise WeChat\) version 5.0.10 has opened CLI and MCP \(Model Context Protocol\) capabilities to all enterprises, enabling AI agents such as WorkBuddy, DeepSeek Harness, and custom-built agents to directly access ten core office modules. The update includes security controls like permission isolation between personnel and AI, manual approval for critical operations, time-limited authorization, and complete audit trails. AI can read documents and spreadsheets, analyze data, and generate proposal presentations or business dashboards. This integration allows mainstream AI agents to interact with WeCom&\#x27;s office suite, enhancing automation and AI-driven workflows within enterprise environments.

telegram · zaihuapd · Aug 18, 06:22

**「Background」** WeCom \(Enterprise WeChat\) is Tencent&\#x27;s enterprise communication and collaboration platform, offering modules such as documents, spreadsheets, email, meetings, calendar, and contacts. The 5.0.10 update, announced on August 18, 2025, opens CLI and MCP \(Model Context Protocol\) interfaces to all enterprises, enabling AI agents like WorkBuddy, DeepSeek Harness, and MiniMax Code to directly invoke these core office modules. This represents a shift toward integrating AI agents into enterprise workflows through standardized protocols.

**「Impact」** Enterprises using WeCom can now integrate AI agents into their office workflows, enabling automated data analysis, document processing, and presentation generation while maintaining security through approval and audit mechanisms. This development is particularly significant for software engineers and AI practitioners seeking to deploy agents in enterprise settings, as it provides a standardized interface \(MCP\) and CLI for accessing core office modules.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/991/088.htm">企业微信 5.0.10 开放 CLI 与 MCP，10 大办公模块可接入主流 Agent - IT之家</a></li>
<li><a href="https://m.163.com/dy/article/L4KFRJVV0511B8LM.html">企业微信5.0.10开放CLI与MCP，10大办公模块可接入主流Agent</a></li>
<li><a href="https://www.msn.cn/zh-cn/%E6%8A%80%E6%9C%AF/%E6%8A%80%E6%9C%AF%E5%85%AC%E5%8F%B8/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A15-0-10%E6%97%A5%E5%89%8D%E4%B8%8A%E7%BA%BF-%E5%85%A8%E9%9D%A2%E5%BC%80%E6%94%BEcli%E4%B8%8Emcp/ar-AA2amILI">企业微信5.0.10日前上线，全面开放cli与mcp - Msn</a></li>

</ul>
</details>

**Tags**: `#WeCom`, `#MCP`, `#AI agents`, `#enterprise software`, `#CLI`

---

<a id="item-tech-news-10"></a>
### [China Orders Early Removal of Custom Windows 10](https://www.bloomberg.com/news/articles/2026-08-18/china-axing-microsoft-windows-from-state-agencies-ahead-of-plan) ⭐️ 7.0/10

China&\#x27;s Ministry of State Security has ordered some government-affiliated agencies to uninstall a customized version of Windows 10, moving the planned retirement date forward by several months from its original February 2027 deadline. The directive stems from data security concerns, though specific vulnerabilities were not disclosed. Microsoft stated it has found no security incidents affecting the product and that it continues to receive regular security updates. The move reflects heightened Chinese scrutiny of foreign software in government environments and could affect Microsoft&\#x27;s presence in China&\#x27;s public sector.

telegram · zaihuapd · Aug 18, 06:22

**「Background」** China has been promoting domestic software and reducing reliance on foreign technology, especially in government and state-affiliated sectors. The customized Windows 10 version was likely tailored for Chinese government use, and its planned retirement was part of a broader transition to locally developed operating systems. The early uninstall order aligns with China&\#x27;s ongoing efforts to enhance data security and self-sufficiency in critical infrastructure.

**「Impact」** Affected government agencies will need to accelerate migration to alternative operating systems, potentially disrupting workflows and increasing reliance on domestic OS solutions. Microsoft may face reduced revenue and influence in China&\#x27;s public sector, though the full scope of the order remains unclear.

**Tags**: `#China`, `#Windows 10`, `#government policy`, `#data security`, `#Microsoft`

---

<a id="item-tech-news-11"></a>
### [OpenAI and CodeAI Partner to Bring AI Education to Millions of Students](https://openai.com/index/chatgpt-for-teens/) ⭐️ 7.0/10

OpenAI announced on August 18, 2026, a partnership with CodeAI to help students and teachers learn responsible AI use, coinciding with the launch of ChatGPT for Teens, which includes teen protection features and parental controls. Over the next year, the collaboration will reach millions of students through a joint advisory council, AI literacy courses, student challenges, and career programs. The partnership will also support CodeAI in developing a free high school AI Foundations course. This initiative aims to expand AI education and promote responsible usage among younger audiences.

telegram · zaihuapd · Aug 18, 12:06

**「Background」** OpenAI and CodeAI have announced a partnership to expand AI education to millions of students, coinciding with the launch of ChatGPT for Teens, a version of ChatGPT designed for teenagers with protective features and parental controls. The collaboration will include a joint advisory council, AI literacy courses, student challenges, and career programs over the next year, and will support the development of a free high school AI Foundations course by CodeAI. This initiative aims to address the gap between students&\#x27; widespread use of AI and their lack of critical skills to evaluate AI outputs, as highlighted by recent education reports.

**「Impact」** The partnership will directly benefit millions of K-12 students and teachers by providing structured AI literacy resources and career pathways, while the launch of ChatGPT for Teens introduces protective measures for younger users. The free AI Foundations course for high schools could become a standard educational resource, though its adoption depends on school district decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/partnering-with-codeai/">Partnering with CodeAI to prepare the first AI generation | OpenAI</a></li>
<li><a href="https://beyondtmrw.org/article/openai-codeai-partnership-prepares-the-first-ai-generation-for-school">OpenAI CodeAI Partnership Prepares the First AI Generation f</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-partners-codeai-for-teen-ai-education">OpenAI Partners CodeAI for Teen AI Education | StartupHub. ai</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI education`, `#ChatGPT for Teens`, `#partnership`, `#K-12`

---

<a id="item-tech-news-12"></a>
### [Chinese AI Chips to Supply Nearly 90% of Domestic Market by 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd) ⭐️ 7.0/10

TrendForce projects that Chinese domestic AI accelerators will supply nearly 90% of the country&\#x27;s domestic market by 2026, a significant jump from 45% last year. In 2025, Nvidia held a 55% market share with 2.2 million units shipped, while Huawei shipped 812,000 units, capturing 20.3%. To achieve this shift, China must increase its high-end AI chip production by 2.2 times to approximately 1.96 million units within a year, raising questions about whether capacity can keep pace. Cambricon and Huawei are expected to be the biggest beneficiaries of this transition away from Nvidia and AMD.

telegram · zaihuapd · Aug 18, 13:03

**「Background」** TrendForce, a market research firm, tracks the global AI accelerator market, which includes chips designed to speed up AI workloads. In 2025, Nvidia held a dominant 55% share of the Chinese market with 2.2 million units shipped, while Huawei shipped 812,000 units for a 20.3% share. The forecast of domestic Chinese AI accelerators supplying nearly 90% of the local market by 2026 reflects a significant shift away from American suppliers like Nvidia and AMD, driven by US export controls and China&\#x27;s push for semiconductor self-sufficiency.

**「Impact」** Chinese AI chipmakers, particularly Cambricon and Huawei, are poised to gain significant market share, while Nvidia and AMD face reduced sales in China, potentially accelerating the decoupling of the Chinese AI hardware ecosystem from Western suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd">China &#x27;s homegrown AI accelerators to supply 90... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**Tags**: `#AI accelerators`, `#China tech`, `#market analysis`, `#Huawei`, `#Cambricon`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Rising Treasury Yields Squeeze Households as Wall Street Waits on Fed Chair](https://www.cnbc.com/2026/08/18/bond-market-treasury-yields-warsh-main-street.html) ⭐️ 7.0/10

A bond market sell-off has pushed the 10-year Treasury yield above 4.7%, raising mortgage rates to 6.75% and diesel prices to $5.46 a gallon \(up 48% from a year ago\), squeezing households while Wall Street remains insulated. The yield curve steepened by nearly 29 basis points since June 24, driven by fiscal concerns and supply shocks, and the new Fed chair, Kevin Warsh, has signaled acceptance of higher rates.

rss · CNBC Finance · Aug 18, 16:48

**「Background」** The Federal Reserve, led by Chair Kevin Warsh, has kept its policy rate steady, but long-term Treasury yields have risen sharply since late June, steepening the yield curve. This reflects market concerns about inflation, fiscal deficits, and supply shocks, including the Iran war and AI-related debt demand. Warsh has signaled acceptance of higher yields, which traders have interpreted as a reason to push rates further up.

**「Impact」** Higher Treasury yields directly raise borrowing costs for households, particularly through mortgages and fuel prices, making home buying and everyday expenses more expensive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fool.com/investing/2026/07/21/kevin-warsh-big-move-fed-bond-market-take-action/">Kevin Warsh Made His First Big Move as Fed Chair, and the Bond Market ...</a></li>
<li><a href="https://ecmsource.com/kevin-warsh-fed-chair-nomination-rates-bond-markets-2026/">Kevin Warsh Fed Nomination: What It Signals for Rates and Bonds</a></li>
<li><a href="https://www.cnn.com/2026/07/29/business/bond-yields-fed-warsh">The bond market to Kevin Warsh: What are you doing about inflation? - CNN</a></li>

</ul>
</details>

**Tags**: `#Treasury yields`, `#Bond market`, `#Mortgage rates`, `#Inflation`, `#Fiscal policy`

---

<a id="item-finance-news-2"></a>
### [Kalshi Files to Launch Perpetual Futures on Equity Indexes](https://www.cnbc.com/2026/08/18/kalshi-wants-to-launch-perps-tied-to-equity-indexes.html) ⭐️ 7.0/10

Kalshi has filed with the Commodity Futures Trading Commission \(CFTC\) to launch perpetual futures tied to equity indexes, specifically the MerQube U.S. Large Cap Index, which tracks the largest 500 U.S. companies. This move expands Kalshi&\#x27;s derivatives offerings beyond its existing crypto and precious metals perps, potentially increasing competition for traditional exchanges.

rss · CNBC Finance · Aug 18, 16:49

**「Background」** Kalshi, a prediction market platform, recently received approval from the Commodity Futures Trading Commission \(CFTC\) to offer perpetual futures tied to cryptocurrencies, marking the first time such contracts were available in the U.S. Perpetual futures, or &\#x27;perps,&\#x27; are contracts without an expiration date that track an asset&\#x27;s price, using funding payments to stay aligned with the market. The company has since filed to expand into precious metals and copper, and now seeks to launch a perp tied to the MerQube U.S. Large Cap Index, which tracks the 500 largest U.S. companies.

**「Impact」** If approved, these equity index perps could directly compete with traditional futures products offered by exchanges like CME and CBOE, potentially affecting their market share and revenue. However, the long-term impact remains uncertain, and shares of CME and CBOE were higher on the day of the announcement.

<details><summary>References</summary>
<ul>
<li><a href="https://coinunited.io/en/pulse/2026-08-18/kalshi-files-sp-500-perpetual-futures-what-a-new-247-leveraged-index-product-means-for-cme-vix-and-your-us500-positions">Kalshi Files S&amp;P 500 Perpetual Futures : What a New... | CoinUnited.io</a></li>
<li><a href="https://www.datawallet.com/crypto/what-are-kalshi-perpetuals">Kalshi Perpetuals: The First CFTC -Regulated Perps Explained</a></li>

</ul>
</details>

**Tags**: `#Kalshi`, `#perpetual futures`, `#equity indexes`, `#CFTC`, `#derivatives market`

---

<a id="item-finance-news-3"></a>
### [US Buy-Now-Pay-Later Loans Hit $160 Billion in 2025](https://www.nytimes.com/2026/08/17/business/buy-now-pay-later.html) ⭐️ 7.0/10

US buy-now-pay-later loans reached $160 billion in 2025, nearly doubling from 2023, as lenders expand into essential expenses like utilities and rent, raising debt concerns.

telegram · zaihuapd · Aug 18, 01:41

**「Background」** Buy-now-pay-later \(BNPL\) loans originally let online shoppers split purchases into installments without a traditional credit card. Lenders such as Klarna, Affirm, and Flex have since expanded into everyday costs like rent and utilities; Flex alone says it has financed nearly $40 billion in rent payments for 3 million tenants.

**「Impact」** Consumers using these loans for essentials may face overdraft fees and debt traps, especially since most loans are not yet reported to credit bureaus.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-us/money/loan/from-sneakers-to-rent-buy-now-pay-later-expands-as-americans-struggle-to-make-ends-meet/ar-AA2amzM9">From sneakers to rent : ‘ Buy now , pay later ’ expands as Americans...</a></li>

</ul>
</details>

**Tags**: `#buy-now-pay-later`, `#consumer debt`, `#US economy`, `#fintech`, `#household finance`

---