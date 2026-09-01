---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 45 items, 20 important content pieces were selected

---

**Technology News**
1. [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](#item-tech-news-1) ⭐️ 8.0/10
2. [Sliding-window attention outperforms linear attention on long-context reasoning](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenClaw 2.0: Largest Update with 16K Pull Requests](#item-tech-news-3) ⭐️ 8.0/10
4. [Tim Cook Steps Down as Apple CEO; John Ternus Takes Over](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek Releases Experimental Multimodal Model V4-Flash-Vision-Exp](#item-tech-news-5) ⭐️ 8.0/10
6. [Turning Security Cameras into Automatic Bird Identification with BirdNET-Go](#item-tech-news-6) ⭐️ 7.0/10
7. [Commissary Freezer Outages Spark Cyberattack Speculation](#item-tech-news-7) ⭐️ 7.0/10
8. [NAT and the Erosion of the Open Internet](#item-tech-news-8) ⭐️ 7.0/10
9. [Wrapture: Extending wrapt for Testing and Tracing](#item-tech-news-9) ⭐️ 7.0/10
10. [GNNs on Dynamic Graphs Suffer Temporal Leakage; SynthFin-AML Enforces Causal Splits](#item-tech-news-10) ⭐️ 7.0/10
11. [Entropic Scree: New Tool for Signal Assessment in Dirty Data](#item-tech-news-11) ⭐️ 7.0/10
12. [寒序科技发布MRAM推理路线，uHBM带宽24 TB/s](#item-tech-news-12) ⭐️ 7.0/10
13. [EU Designates ChatGPT, Reddit, Roblox as Very Large Services](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [Aon to Acquire USI for $17 Billion, Targeting U.S. Middle-Market Insurance](#item-finance-news-1) ⭐️ 8.0/10
2. [Warsh&\#x27;s Hawkish Jackson Hole Speech Raises September Rate Hike Odds](#item-finance-news-2) ⭐️ 8.0/10
3. [El Niño to Reach Super Strength by October, Pressuring Global Food and Shipping](#item-finance-news-3) ⭐️ 8.0/10
4. [Midday Stock Movers: PG&amp;E, Edison, Apple, Howmet, Eli Lilly and More](#item-finance-news-4) ⭐️ 7.0/10
5. [Huawei&\#x27;s H1 2026 Net Profit Drops 37% Despite Revenue Growth](#item-finance-news-5) ⭐️ 7.0/10
6. [Chinese Court Freezes Nexperia Assets in Wingtech Lawsuit](#item-finance-news-6) ⭐️ 7.0/10
7. [Tim Cook Steps Down as Apple CEO, Remains with Company](#item-finance-news-7) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed all Manifest V2 \(MV2\) extensions from the Chrome Web Store, including the popular ad blocker uBlock Origin, as part of its transition to Manifest V3. This change affects millions of users who relied on MV2 extensions for ad blocking and other functionalities. The removal has sparked significant community backlash, with users expressing concerns about browser control, user safety, and the future of ad blocking. Google&\#x27;s move is part of a broader effort to enhance security and performance, but critics argue it limits user choice and gives Google more control over the web ecosystem.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**「Background」** Google has been transitioning Chrome extensions from Manifest V2 \(MV2\) to Manifest V3 \(MV3\) for years, a change that restricts how extensions can operate, particularly limiting dynamic content filtering. uBlock Origin, a popular ad blocker, relies on MV2&\#x27;s capabilities, and its developer has stated that MV3&\#x27;s limitations prevent it from offering the same level of protection. The removal of MV2 extensions from the Chrome Web Store marks the final step in this transition, affecting users who have not yet migrated to MV3-compatible alternatives.

**「Impact」** Users of Chrome who depend on uBlock Origin and other MV2 extensions will lose access to these tools, potentially increasing their exposure to malicious ads and trackers. Developers of MV2 extensions must migrate to MV3 or risk losing their user base, while the ad-blocking community may shift toward alternatives like Firefox, which still supports MV2.

**「Community Discussion」** Community members express strong dissatisfaction with Google&\#x27;s decision, with many recommending Firefox as a more user-centric alternative. Some highlight the safety implications of ad blocking, noting that malicious ads pose a real threat to less tech-savvy users. Others recall Chrome&\#x27;s earlier positive impact and lament its current direction, while a few note that uBlock Origin has always worked well on Firefox.

<details><summary>References</summary>
<ul>
<li><a href="https://webiterate.dev/google-removed-extensions-ublock-origin-108/">Google Has Removed Manifest V2 Extensions From the Chrome Web Store, Including uBlock Origin</a></li>
<li><a href="https://thenextweb.com/news/chrome-manifest-v3-ublock-origin-content-blockers-disabled">Google is about to disable uBlock Origin and every other Manifest V2 extension in Chrome</a></li>
<li><a href="https://www.ghostery.com/blog/ublock-origin-not-supported-chrome">uBlock Origin No Longer Supported On Chrome: Best Fixes | Ghostery</a></li>

</ul>
</details>

**Tags**: `#Chrome`, `#Manifest V2`, `#ad blocking`, `#uBlock Origin`, `#browser extensions`

---

<a id="item-tech-news-2"></a>
### [Sliding-window attention outperforms linear attention on long-context reasoning](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

A new arXiv preprint by Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron, and Emy Gervais argues that sliding-window attention with sinks \(SWA\) achieves 2 to 10 times higher performance than linear attention variants on long-context reasoning benchmarks, specifically Needle-in-a-Haystack and BABILong. The authors claim that the post-training-to-linear-attention pipeline has not been properly compared to simpler baselines, and that SWA requires no post-training, runs fast, and maintains low memory usage. They strongly recommend switching to SWA instead of post-training linear models, noting that linear attention may require training from scratch or extensive post-training to match SWA. This challenges a major research direction in LLM efficiency, though it is a single preprint that needs replication.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**「Background」** Standard transformer attention scales quadratically with sequence length, making long-context processing computationally expensive. Linear attention variants aim to reduce this cost to linear scaling, but often require post-training or training from scratch to maintain performance. Sliding-window attention \(SWA\) is a simpler alternative that restricts attention to a local window, and adding &\#x27;sinks&\#x27; \(special tokens that retain global information\) helps preserve long-range context. This preprint compares SWA with sinks against post-trained linear attention models on long-context reasoning benchmarks.

**「Impact」** If replicated, this result could redirect research and engineering efforts away from linear attention post-training toward simpler sliding-window attention baselines, potentially saving significant compute and simplifying long-context model deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28444">[ 2608 . 28444 ] Sliding - window beats linear attention</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.28444">Sliding - window beats linear attention | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#attention mechanisms`, `#long-context reasoning`, `#LLM efficiency`, `#arXiv preprint`, `#benchmarking`

---

<a id="item-tech-news-3"></a>
### [OpenClaw 2.0: Largest Update with 16K Pull Requests](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw released version 2.0 on August 30, its largest update ever, incorporating over 16,000 pull requests from 933 contributors, including 569 first-time participants. This accounts for roughly half of all pull requests in the project&\#x27;s history. The update spans all major areas: installation, messaging, memory, skills, models, browser, plugins, and security. The team went nearly seven weeks without a new release to prepare this update. It simplifies the installation process, rebuilds the browser-side experience, and introduces shared cloud sessions for multi-user collaboration.

telegram · zaihuapd · Aug 31, 04:38

**「Background」** OpenClaw is an open-source AI agent platform that allows users to build and deploy autonomous agents. The 2.0 release, versioned v2026.8.1, follows a seven-week development pause and represents the project&\#x27;s largest update, incorporating over 16,000 pull requests from 933 contributors, including 569 first-time contributors. The update focuses on simplifying installation, rebuilding the browser-based Control UI, and introducing shared cloud sessions for multiplayer collaboration, alongside improvements across messaging, memory, skills, models, plugins, and security.

**「Impact」** Developers and users of OpenClaw will experience a significantly streamlined installation and a revamped browser interface, while teams can now collaborate in real-time through shared cloud sessions, enhancing productivity and coordination.

<details><summary>References</summary>
<ul>
<li><a href="https://openclaw.ai/blog/openclaw-2-accidentally">OpenClaw 2.0, Accidentally - OpenClaw Blog</a></li>
<li><a href="https://www.marktechpost.com/2026/08/30/openclaw-releases-openclaw-2-0-guided-model-setup-575-ms-control-ui-startup-and-one-trust-boundary-per-gateway/">OpenClaw Releases OpenClaw 2.0: Guided Model Setup, 575 ms Control UI Startup, and One Trust Boundary Per Gateway - MarkTechPost</a></li>
<li><a href="https://www.explainx.ai/blog/openclaw-2-0-release-august-2026">OpenClaw 2.0 Release — 16K PRs, Rebuilt UI (2026) | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**Tags**: `#OpenClaw`, `#software-release`, `#open-source`, `#collaboration`, `#AI-agent`

---

<a id="item-tech-news-4"></a>
### [Tim Cook Steps Down as Apple CEO; John Ternus Takes Over](https://www.bloomberg.com/news/articles/2026-08-30/apple-s-new-ceo-john-ternus-takes-reins-from-tim-cook-focusing-on-ai) ⭐️ 8.0/10

Tim Cook&\#x27;s final day as Apple CEO is August 31, 2026, with 51-year-old hardware engineering veteran John Ternus taking over on September 1. Cook will remain as executive chairman. Ternus&\#x27;s top priority is advancing Apple&\#x27;s AI efforts, addressing delays in Siri upgrades. At the September 9 fall event, Apple is expected to unveil its first foldable iPhone, reportedly featuring 12 GB RAM and deep Siri AI integration that can understand real-world contexts using the screen, calendar, and camera.

telegram · zaihuapd · Aug 31, 10:21

**「Background」** Tim Cook has served as Apple&\#x27;s CEO since 2011, succeeding co-founder Steve Jobs. John Ternus, born May 19, 1975, is an American engineer who has been Apple&\#x27;s senior vice president of Hardware Engineering since 2021 and a member of the executive leadership team. On September 1, 2026, Ternus succeeded Cook as CEO, with Cook becoming executive chairman of Apple&\#x27;s board.

**「Impact」** This leadership change signals a strategic shift toward AI and hardware innovation, with the upcoming foldable iPhone and Siri AI integration likely to shape Apple&\#x27;s product roadmap and competitive position in the AI-driven smartphone market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/John_Ternus">John Ternus - Wikipedia</a></li>
<li><a href="https://www.apple.com/leadership/john-ternus/">Apple Leadership - John Ternus - Apple</a></li>
<li><a href="https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/">Tim Cook to become Apple Executive Chairman John Ternus to become Apple CEO - Apple</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#CEO transition`, `#AI strategy`, `#foldable iPhone`, `#Siri`

---

<a id="item-tech-news-5"></a>
### [DeepSeek Releases Experimental Multimodal Model V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) ⭐️ 8.0/10

DeepSeek has released the weights for DeepSeek-V4-Flash-Vision-Exp, the first experimental multimodal model in its V4 series. Built on the V4-Flash architecture, it adds a vision module and undergoes continued training. Compared to V4-Flash-0731, its multimodal agent capabilities have significantly improved, with ApexBench scores rising from 26.2 to 36.5, while text agent task performance remains roughly unchanged. The model is available on Hugging Face under the deepseek-ai organization.

telegram · zaihuapd · Aug 31, 11:41

**「Background」** DeepSeek-V4-Flash-Vision-Exp is an experimental multimodal model released by DeepSeek, building on the V4-Flash architecture by adding a vision module and continuing training. It was made available on the DeepSeek API platform on August 21, 2026, as an API release rather than a full technical launch. The model is designed to match DeepSeek-V4-Flash on text capabilities, including agents, reasoning, and world knowledge, while significantly improving multimodal agent performance.

**「Impact」** Developers and researchers using DeepSeek models can now experiment with a multimodal variant that substantially boosts agent performance on benchmarks like ApexBench, potentially enabling more capable vision-language agent applications.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260821/">DeepSeek-V4-Flash-Vision-Exp Release: Multimodal API Now Live | DeepSeek API Docs</a></li>
<li><a href="https://x.com/deepseek_ai/status/2090730032574631962">DeepSeek on X: &quot;DeepSeek-V4-Flash-Vision-Exp is now live on the DeepSeek API Platform! 🚀 🔹 This experimental multimodal model matches DeepSeek-V4-Flash on text capabilities—including agents, reasoning, and world knowledge. 🔹 On multimodal agent benchmarks, V4-Flash-Vision-Exp makes a major&quot; / X</a></li>
<li><a href="https://kie.ai/blog/deepseek-v4-flash-vision-exp-analysis">DeepSeek V4 Flash Vision Exp Release</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#multimodal`, `#AI model`, `#benchmark`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Turning Security Cameras into Automatic Bird Identification with BirdNET-Go](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

A developer has detailed how to repurpose existing security cameras into an automatic bird identification system using BirdNET-Go, an open-source tool that listens to audio feeds and classifies bird species. The approach leverages RTSP streams from cameras like Unifi doorbells, allowing the software to continuously monitor and identify birds without dedicated hardware. Community members have successfully implemented similar setups, though some encountered challenges such as poor microphone quality and sampling rate limitations \(e.g., Aqara cameras only support 16kHz while BirdNET expects 48kHz\), leading them to use external microphones or Raspberry Pi devices. The project demonstrates a practical integration of IoT hardware and machine learning for hobbyist applications, with extensions like portable BirdNET-Pi builds and e-ink displays for real-time results.

hackernews · speckx · Aug 31, 16:47 · [Discussion](https://news.ycombinator.com/item?id=49511856)

**「Background」** BirdNET is a research project by the Cornell Lab of Ornithology and Chemnitz University of Technology that uses machine learning to identify bird species from audio recordings. BirdNET-Go is a community-developed, real-time soundscape analyzer that runs the BirdNET model locally, often on devices like Raspberry Pi, and can be integrated with other systems via MQTT or RTSP streams. Security cameras with built-in microphones can provide audio feeds that BirdNET-Go can analyze, enabling automated bird identification without dedicated hardware.

**「Impact」** Hobbyists and engineers can now transform existing security camera infrastructure into bird monitoring systems with minimal additional cost, though success depends on camera audio quality and sampling rate support, which may require external microphones or additional hardware like a Raspberry Pi.

**「Community Discussion」** Community members shared successful implementations and variations, including using Unifi doorbell cams with RTSP feeds, building portable BirdNET-Pi devices with e-ink displays, and noting the quality of Cornell&\#x27;s Merlin Bird ID app. Some reported technical hurdles such as wind noise and firmware limitations on certain cameras, leading to workarounds like external microphones.

<details><summary>References</summary>
<ul>
<li><a href="https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go.md">jasontucker.blog/how-i-turned-my- security - cameras -into-an-automatic...</a></li>
<li><a href="https://github.com/Jellman86/YetAnother-WhosAtMyFeeder/blob/main/docs/integrations/birdnet-go.md">YetAnother-WhosAtMyFeeder/docs/integrations/ birdnet - go .md at main...</a></li>
<li><a href="https://www.kyleniewiada.org/blog/2025/05/backyard-bird-tracking-with-ai/">Backyard Bird Tracking With AI-Powered BirdNET - Go</a></li>

</ul>
</details>

**Tags**: `#BirdNET`, `#security cameras`, `#machine learning`, `#IoT`, `#bird identification`

---

<a id="item-tech-news-7"></a>
### [Commissary Freezer Outages Spark Cyberattack Speculation](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 7.0/10

A blog post on Signal and Silence speculates that military commissary freezers may have been hacked, citing a series of unexplained outages. The author does not confirm a cyberattack but raises it as a possibility, prompting discussion about the security of industrial control systems \(ICS\) and critical infrastructure. Community experts, including a 20-year military IT veteran, suggest the outages are more likely due to misconfiguration or faulty updates rather than a hack, though the timing is concerning. The discussion references known vulnerabilities in PLCs, such as Siemens S7-1500, and notes that many contractors lack knowledge of enabling TLS, leaving systems with default credentials. The incident highlights broader risks to isolated overseas military locations like Guam and Hawaii, where such disruptions could have significant economic ripple effects.

hackernews · jcurbo · Aug 31, 11:45 · [Discussion](https://news.ycombinator.com/item?id=49508506)

**「Background」** U.S. military commissaries are retail stores on military installations that sell groceries and household goods at cost, offering at least a 25% discount compared to civilian stores, and are reserved for active-duty service members, their families, and retirees with base privileges. On August 26, freezers at commissaries across at least 14 bases reportedly entered an active defrost mode, dumping their contents, and the Department of Defense confirmed a &\#x27;refrigeration disruption&\#x27; without specifying a cause. Industrial control systems \(ICS\) that manage such equipment are often noted for weak security, with anecdotal reports of default credentials and outdated interfaces, making speculation about a cyberattack plausible but unconfirmed.

**「Impact」** If the outages were caused by a cyberattack, it would indicate a serious vulnerability in military supply chain infrastructure, potentially affecting food safety and operational readiness at overseas bases. However, without confirmation, the most immediate impact is heightened awareness and debate about the security of ICS in military settings, prompting calls for better security practices and monitoring.

**「Community Discussion」** Commenters are skeptical of the hack theory, with one expert attributing the outages to misconfiguration or bad updates, while another notes that PLCs often have poor security defaults and contractors lack TLS knowledge. A third commenter points out that the author doesn&\#x27;t firmly claim a hack and suggests that a few dozen failures could be normal maintenance issues, questioning the scale of the problem.

<details><summary>References</summary>
<ul>
<li><a href="https://genztech.blog/p/military-commissary-freezers-hack-theory/">Military Commissary Freezers Failed at 14+ Bases. Was It a Hack ?</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/08/28/dod-confirms-refrigeration-disruption-at-military-commissaries/">DoD confirms ‘refrigeration disruption’ at military commissaries</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#critical infrastructure`, `#industrial control systems`, `#military`, `#supply chain`

---

<a id="item-tech-news-8"></a>
### [NAT and the Erosion of the Open Internet](https://dreamstation.systems/personal/ntppost.html) ⭐️ 7.0/10

An essay argues that Network Address Translation \(NAT\) is a root cause of internet centralization, framing it as an early technical decision that undermined the ability to run servers and shaped a client-server mindset. The piece traces how NAT, born from IPv4 address scarcity, made incoming connections difficult and trained users to rely on centralized cloud services. Community commentary adds historical depth, including a notable admission from Rusty Russell, the Linux NAT implementer, who explains that his design prioritized squeezing more connections into one IP address, inadvertently eroding public endpoints. Critics counter that NAT is not inherently evil, with Carrier Grade NAT \(CGNAT\) being the real problem, and that NAT has also protected insecure devices. The discussion reflects broader debates about internet architecture, security, and the trade-offs of address scarcity.

hackernews · robinpie · Aug 31, 02:23 · [Discussion](https://news.ycombinator.com/item?id=49504905)

**「Background」** Network address translation \(NAT\) was first formally proposed in RFC 1631 in 1994 to address IP address depletion and routing scalability. NAT allows multiple devices on a private network to share a single public IP address by rewriting address and port information in packets, which also hides internal devices from direct inbound connections.

**「Impact」** For network engineers, protocol designers, and advocates of a decentralized internet, this analysis reinforces that NAT&\#x27;s legacy is a structural barrier to peer-to-peer connectivity and self-hosting, influencing ongoing debates about IPv6 adoption and the design of future internet protocols.

**「Community Discussion」** Commenters largely agree that NAT contributed to centralization, with Rusty Russell&\#x27;s confession adding weight, but some argue that regular NAT is manageable and that CGNAT is the true villain, while others note that NAT has shielded insecure devices from exposure.

<details><summary>References</summary>
<ul>
<li><a href="https://dreamstation.systems/personal/ntppost.html">Internet centralization and the original sin of NAT</a></li>

</ul>
</details>

**Tags**: `#networking`, `#NAT`, `#internet architecture`, `#centralization`, `#history`

---

<a id="item-tech-news-9"></a>
### [Wrapture: Extending wrapt for Testing and Tracing](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Graham Dumpleton, creator of wrapt, mod\_wsgi, and New Relic&\#x27;s Python agent, has introduced Wrapture, a new Python library that extends wrapt&\#x27;s monkeypatching capabilities to combine testing and tracing. Wrapture allows developers to wrap any function or method to trace all access or override return values, serving as an alternative to unittest.mock and a tool for adding tracing to existing projects. It includes OpenTelemetry support and a configuration-based mechanism for tracing, demonstrated with a TOML example that captures summary data and outputs JSON lines. The project is only a few weeks old but shows promise, and notably, every line of code and documentation was written by an AI assistant under Dumpleton&\#x27;s direction, which he emphasizes was careful engineering rather than &\#x27;vibe coding.&\#x27; A follow-up post demonstrates testing patterns, such as stubbing methods and transforming results, using Wrapture&\#x27;s binding API.

rss · Simon Willison · Aug 31, 23:59

**「Background」** Wrapture is a new Python library by Graham Dumpleton, the creator of wrapt, a widely used package for transparent function wrapping and monkeypatching. Dumpleton is also known for his work on mod\_wsgi and the New Relic Python agent, which uses wrapt to instrument code for performance monitoring. Wrapture extends wrapt&\#x27;s capabilities to combine testing and tracing, offering an alternative to unittest.mock and a way to add observability to existing projects.

**「Impact」** Python developers seeking a unified approach to testing and observability now have a new tool that can replace unittest.mock for certain use cases and add tracing to code they don&\#x27;t control, potentially simplifying their testing and monitoring workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://grahamdumpleton.me/posts/2011/11/new-relic-is-not-just-for-apachemodwsgi/">New Relic is not just for Apache/ mod _ wsgi . - Graham Dumpleton</a></li>
<li><a href="https://readwrite.com/new-relic-expands-performance/">New Relic Expands Performance Monitoring as a Service with Python</a></li>

</ul>
</details>

**Tags**: `#python`, `#testing`, `#tracing`, `#monkeypatching`, `#open-source`

---

<a id="item-tech-news-10"></a>
### [GNNs on Dynamic Graphs Suffer Temporal Leakage; SynthFin-AML Enforces Causal Splits](https://www.reddit.com/r/MachineLearning/comments/1w3imxy/your_gnn_is_probably_just_an_overcomplicated_mlp/) ⭐️ 7.0/10

A Reddit post by /u/Glabmayt2075 highlights widespread temporal leakage in GNN training on dynamic graphs, where standard transductive random splits allow models to see future edges, inflating performance. To address this, the authors released SynthFin-AML v10.0, a synthetic benchmark with 100k nodes and 1.2M edges, enforcing strict causal boundaries via a 3-snapshot point-in-time split \(train edges up to Day 7, validation up to Day 8, test up to Day 10\). They also eliminated distribution leakage by ensuring fraud and retail transaction amounts share the same lognormal distribution \(μ=8.517, σ=0.8\). Benchmarking on this strict temporal split, a tuned LightGBM with 11 point-in-time graph features achieved a PR-AUC of 0.848, while inductive GraphSAGE achieved 0.881, showing a modest but real improvement. The benchmark has been submitted upstream to PyTorch Geometric as PR \#10774, and the repository is available on GitHub.

reddit · r/MachineLearning · /u/Glabmayt2075 · Aug 31, 16:21

**「Background」** Graph neural networks \(GNNs\) are commonly used for tasks on dynamic graphs, such as detecting money laundering in financial transaction networks. A standard evaluation approach is to train on a static snapshot of the graph and test on another snapshot, but this can cause temporal leakage: the model may see edges from the future during training, inflating performance. SynthFin-AML is a synthetic benchmark dataset designed to address this issue by enforcing strict causal splits, ensuring that training, validation, and test graphs contain only edges up to specific time points. The dataset also controls for distribution leakage by making fraud and retail transaction amounts follow the same lognormal distribution, so that simple statistical separability is not possible.

**「Impact」** Researchers and practitioners working on dynamic graph learning, especially in financial domains like anti-money laundering, will need to adopt strict temporal splits to avoid overestimating model performance; the SynthFin-AML benchmark provides a concrete tool for this, though the reported performance gap suggests GNNs may offer only marginal gains over well-featured tree models on tabular financial data.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/valiyevoktay-cmd/synthfin-aml-">GitHub - valiyevoktay-cmd/ synthfin - aml -: A graph-native Anti-Money...</a></li>

</ul>
</details>

**Tags**: `#GNN`, `#temporal leakage`, `#benchmark`, `#anti-money laundering`, `#dynamic graphs`

---

<a id="item-tech-news-11"></a>
### [Entropic Scree: New Tool for Signal Assessment in Dirty Data](https://www.reddit.com/r/MachineLearning/comments/1w3br9c/how_to_assess_if_there_is_a_strong_signal_in_your/) ⭐️ 7.0/10

A new tabular data diagnostic tool called Entropic Scree has been introduced to estimate signal strength, signal-to-idiosyncratic volume ratio \(SNR\), intrinsic rank, and linear sufficiency in high-dimensional, real-world datasets. Unlike traditional PCA variants that rely on linear variance, rank order, or Euclidean distance, Entropic Scree evaluates a transformed mutual information metric, making it less dependent on strong parametric or distance assumptions. The tool also provides an exploratory map to identify decoupled sub-networks of variables and serves as a practical diagnostic for the &\#x27;From Garbage to Gold&\#x27; framework, which explains when uncurated, error-prone data can be used directly for accurate prediction models. The original R function is currently available on GitHub, with Python and R packages to be released soon. A preprint with full technical details is available at https://doi.org/10.5281/zenodo.22028087, and the GitHub repository is at https://github.com/tjleestjohn/entropic-scree.

reddit · r/MachineLearning · /u/Chocolate\_Milk\_Son · Aug 31, 12:02

**「Background」** Traditional dimensionality reduction methods like Principal Component Analysis \(PCA\) rely on linear variance, rank order, or Euclidean distance, which can be misleading for high-dimensional, real-world datasets that are noisy or contain non-linear relationships. Entropic Scree is a new diagnostic tool that instead uses a transformed mutual information metric to estimate signal strength, signal-to-noise ratio, intrinsic rank, and linear sufficiency, aiming to be less dependent on strong parametric or distance assumptions. It is positioned as a practical application of the &\#x27;From Garbage to Gold&\#x27; framework, which explores when uncurated, error-prone data can still be used to build accurate prediction models.

**「Impact」** Practitioners working with high-dimensional, noisy tabular data may benefit from a more robust diagnostic for assessing data quality and signal strength before modeling, potentially reducing wasted effort on datasets with insufficient signal. However, the tool&\#x27;s practical utility is not yet established, as no validation results or benchmarks are provided in the source.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tjleestjohn/Entropic-Scree">GitHub - tjleestjohn/ Entropic - Scree : Overcome the limits of standard...</a></li>
<li><a href="https://trendshift.io/repositories/198927">tjleestjohn/ Entropic - Scree — GitHub trending stats... | Trendshift</a></li>

</ul>
</details>

**Tags**: `#data-quality`, `#diagnostics`, `#mutual-information`, `#dimensionality-reduction`, `#machine-learning`

---

<a id="item-tech-news-12"></a>
### [寒序科技发布MRAM推理路线，uHBM带宽24 TB/s](https://mp.weixin.qq.com/s/adyFanNueXUHKnxr9m64kg) ⭐️ 7.0/10

中国MRAM磁计算初创公司寒序科技公布了其uHBM与uLPU推理计算架构及产品路线图。首代uHBM的片内读带宽设计值为24 TB/s，uLPU面向4B多模态模型设定了超过2000 Tokens/s的解码速度目标。该方案将模型权重驻留在Persistent MRAM阵列中，并在同一芯片上完成矩阵-向量运算，以减少权重重复搬运。其SpinPU-ED01验证芯片已通过第三方检测和24小时稳定运行验证。产品路线涵盖从芯片到2U Tray及Rack的完整层级。

telegram · zaihuapd · Aug 31, 13:41

**「Background」** MRAM \(Magnetoresistive Random-Access Memory\) is a non-volatile memory technology that stores data using magnetic states, offering high speed and endurance. In 2022, Samsung published a Nature paper on MRAM-based in-memory computing, which inspired startups like Hánxù Technology to pursue MRAM for AI inference acceleration. Hánxù, described as China&\#x27;s first MRAM magnetic computing company, has developed the SpinPU-ED01 test chip and is now outlining a product roadmap that uses persistent MRAM arrays to keep model weights on-chip, reducing data movement during inference.

**「影响」** 该路线图可能为AI推理硬件提供一种基于MRAM的新架构，若实现其性能目标，有望减少权重搬运开销并提升能效，但当前仍处于验证芯片阶段，实际产品化尚需时间。

<details><summary>References</summary>
<ul>
<li><a href="https://www.163.com/dy/article/KJA9AIJH0511CPMT.html">带宽战争前夜，“中国版Groq”浮出水面|gpu|英伟达|存储器|sram| mram ...</a></li>
<li><a href="https://semi.ofweek.com/2026-05/ART-202530-8420-30687618.html">MRAM 产业化进入“临界点” - OFweek半导体网</a></li>

</ul>
</details>

**Tags**: `#MRAM`, `#AI hardware`, `#inference`, `#memory technology`, `#semiconductors`

---

<a id="item-tech-news-13"></a>
### [EU Designates ChatGPT, Reddit, Roblox as Very Large Services](https://www.euronews.com/next/2026/08/31/eu-places-chatgpt-reddit-and-roblox-under-strictest-digital-safety-rules) ⭐️ 7.0/10

On August 31, the European Commission designated ChatGPT as a very large online search engine and Reddit and Roblox as very large online platforms under the Digital Services Act \(DSA\). The classification applies because each service has more than 45 million average monthly active users in the EU. The three services now have a four-month transition period to comply with stricter obligations, including conducting annual systemic risk assessments, undergoing independent audits, and sharing data with regulators and vetted researchers. These requirements focus on illegal content, protection of minors, and users&\#x27; physical and mental well-being. This move subjects the platforms to the DSA&\#x27;s most stringent digital safety rules.

telegram · zaihuapd · Aug 31, 14:39

**「Background」** The Digital Services Act \(DSA\) is an EU regulation that imposes tiered obligations on online platforms and search engines based on their size. Services with more than 45 million monthly active users in the EU are designated as Very Large Online Platforms \(VLOPs\) or Very Large Online Search Engines \(VLOSEs\), subjecting them to stricter rules on content moderation, risk management, and transparency. This designation triggers additional responsibilities such as annual risk assessments, independent audits, and data sharing with regulators and vetted researchers.

**「Impact」** ChatGPT, Reddit, and Roblox must implement significant compliance measures within four months, potentially affecting their operations, data-sharing practices, and content moderation in the EU, with implications for user safety and platform accountability.

<details><summary>References</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/news/commission-designates-chatgpt-reddit-roblox-under-digital-services-act">Commission designates ChatGPT , Reddit , Roblox under Digital ...</a></li>
<li><a href="https://techxplore.com/news/2026-08-chatgpt-ai-chatbot-tougher-eu.html">ChatGPT becomes first AI chatbot to face tougher EU rules</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#digital-services-act`, `#AI`, `#online-platforms`, `#EU`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Aon to Acquire USI for $17 Billion, Targeting U.S. Middle-Market Insurance](https://www.cnbc.com/2026/08/31/aon-ceo-says-usi-deal-seeks-to-build-premiere-middle-market-insurance-platform.html) ⭐️ 8.0/10

Aon announced it will buy rival USI Insurance Services from private equity firm KKR for $17 billion, a deal expected to close in the fourth quarter pending regulatory approval. The acquisition aims to create the &quot;premier U.S. middle-market platform,&quot; according to CEO Greg Case, and Aon&\#x27;s shares fell 7% on the announcement.

rss · CNBC Finance · Aug 31, 15:15

**「Background」** Aon, a London-based insurance broker, has been expanding its U.S. middle-market business, which serves smaller companies, through acquisitions. In 2024, it bought NFP, another broker focused on this segment. The middle market is attractive because it grows faster than large-account business, according to analysts.

**「Impact」** If completed, the deal would expand Aon&\#x27;s reach to about 200,000 U.S. middle-market companies and their 48 million employees, potentially intensifying competition in that segment. USI CEO Mike Sicard would become Aon&\#x27;s president and global CEO of middle market.

<details><summary>References</summary>
<ul>
<li><a href="https://time.news/aon-nears-17-billion-deal-to-acquire-usi-insurance-services-from-kkr/">Aon Nears $17 Billion Deal to Acquire USI Insurance ... - Time News</a></li>
<li><a href="https://www.reinsurancene.ws/aon-confirms-it-will-acquire-usi-for-17bn-to-advance-its-u-s-middle-market-platform/">Aon confirms it will acquire USI for $17bn, to advance its U.S. middle ...</a></li>

</ul>
</details>

**Tags**: `#M&amp;A`, `#Insurance`, `#Aon`, `#USI`, `#Middle Market`

---

<a id="item-finance-news-2"></a>
### [Warsh&\#x27;s Hawkish Jackson Hole Speech Raises September Rate Hike Odds](https://www.cnbc.com/2026/08/31/jackson-hole-fed-chair-kevin-warsh-hawkish-rate-hikes-analysts.html) ⭐️ 8.0/10

Federal Reserve Chair Kevin Warsh&\#x27;s unexpectedly hawkish speech at Jackson Hole raised market expectations for a September rate hike, with fed funds futures now pricing a 60.4% chance of a quarter-point increase, up from about 56% on Friday. The shift follows Warsh&\#x27;s emphasis on inflation risks and his commitment to the 2% target, though some analysts question the empirical basis for a hike.

rss · CNBC Finance · Aug 31, 11:28

**「Background」** The Federal Reserve&\#x27;s annual Jackson Hole symposium is a key venue for signaling monetary policy. Chair Kevin Warsh&\#x27;s August 28 speech emphasized the need to ensure inflation returns to the 2% target, which markets interpreted as a hawkish signal. This shifted expectations toward a possible rate hike at the upcoming Federal Open Market Committee meeting.

**「Impact」** The hawkish signal weighed on gold and Asian stocks, with gold falling after a 14% August gain, and could put the Fed at odds with the Treasury&\#x27;s efforts to support long-term bond prices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/28/kevin-warsh-jackson-hole-federal-reserve-inflation.html">Fed Chairman Warsh warns on inflation at Jackson Hole</a></li>
<li><a href="https://www.federalreserve.gov/newsevents/speech/warsh20260828a.htm">Keynote remarks by Chairman Warsh at the 2026 Jackson Hole Economic Policy Symposium - Federal Reserve Board</a></li>
<li><a href="https://finance.yahoo.com/economy/live/jackson-hole-fed-summit-live-kevin-warsh-keynote-speech-180442096.html">Jackson Hole Fed summit live: Kevin Warsh&#x27;s keynote speech comes at a pivotal moment for the Federal Reserve</a></li>

</ul>
</details>

**Tags**: `#Federal Reserve`, `#Monetary Policy`, `#Interest Rates`, `#Jackson Hole`, `#Market Reaction`

---

<a id="item-finance-news-3"></a>
### [El Niño to Reach Super Strength by October, Pressuring Global Food and Shipping](https://m.thepaper.cn/newsDetail_forward_33846426) ⭐️ 8.0/10

The El Niño event in the tropical Pacific is strengthening rapidly and is expected to reach &\#x27;super El Niño&\#x27; intensity by October 2026, with nearly a 70% probability of becoming the strongest on record by year-end, according to projections. This has already caused crop losses in France \(broccoli down 60%, lettuce down 35%, zucchini down about 25%\) and restrictions on Panama Canal transits due to water shortages, with the World Food Programme warning that up to 50 million more people could face severe acute food insecurity by the end of 2027.

telegram · zaihuapd · Aug 31, 04:01

**「Background」** El Niño is a natural climate pattern marked by warmer-than-average sea surface temperatures in the central and eastern tropical Pacific Ocean, which can disrupt weather worldwide. The World Meteorological Organization \(WMO\) has forecast that the current El Niño will strengthen into a strong event between August and October 2026, with some models indicating an 81% chance of a very strong event from October to December.

**「Impact」** The projected El Niño is expected to reduce transit capacity at the Panama Canal, a key route for global shipping, potentially raising costs and delays for shippers and consumers. Additionally, crop losses in France and other regions could tighten food supplies and contribute to higher food prices, with the World Food Programme warning that up to 50 million people may face severe food insecurity by 2027.

<details><summary>References</summary>
<ul>
<li><a href="https://wmo.int/news/media-centre/strong-el-nino-expected-intensify">Strong El Niño expected to intensify</a></li>
<li><a href="https://www.newsweek.com/super-el-nino-2026-forecast-prediction-experts-12241456">Super El Niño Threat Grows: Map Shows At-Risk States This Winter - Newsweek</a></li>
<li><a href="https://www.theguardian.com/world/2026/aug/21/panama-canal-reduce-shipping-el-nino-drought">Panama canal to reduce shipping as El Niño strikes vital route | Panama canal | The Guardian</a></li>
<li><a href="https://www.aljazeera.com/news/2026/8/21/panama-canal-to-limit-shipping-ahead-of-extreme-weather-during-el-nino">Panama Canal to limit shipping ahead of extreme weather during El Nino | Transport News | Al Jazeera</a></li>

</ul>
</details>

**Tags**: `#El Niño`, `#climate`, `#agriculture`, `#shipping`, `#food security`

---

<a id="item-finance-news-4"></a>
### [Midday Stock Movers: PG&amp;E, Edison, Apple, Howmet, Eli Lilly and More](https://www.cnbc.com/2026/08/31/stocks-making-the-biggest-moves-midday-pcg-eix-agco-hwm-more-.html) ⭐️ 7.0/10

PG&amp;E and Edison International shares fell 19% and 24%, respectively, after California lawmakers blocked a proposal that would have limited wildfire liability for utilities. Other notable moves included Aon dropping over 7% after agreeing to buy USI Insurance Services for $17 billion, and Eli Lilly falling more than 1% after announcing a $2.9 billion acquisition of Merida Biosciences.

rss · CNBC Finance · Aug 31, 19:49

**「Background」** California lawmakers blocked a proposal backed by Governor Gavin Newsom that would have limited utility companies&\#x27; liability for wildfires caused by their equipment, leaving PG&amp;E and Edison International exposed to potentially large payouts. Separately, Aon agreed to buy USI Insurance Services from KKR for $17 billion to strengthen its U.S. middle-market insurance business, and Eli Lilly agreed to acquire Merida Biosciences for up to $2.875 billion to expand its immunology drug pipeline.

**「Impact」** The blocked proposal leaves PG&amp;E and Edison exposed to potentially large wildfire-related claims, prompting analyst downgrades and making utility investors more cautious about companies with wildfire liability risks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-28/newsom-blocked-on-push-to-shield-utilities-from-fire-liabilities">Newsom’s Plan to Shield Utilities From Wildfire Liabilities Blocked ...</a></li>
<li><a href="https://qz.com/aon-usi-insurance-services-kkr-acquisition-17-billion-083126">Aon acquires USI Insurance Services from KKR for $ 17 billion</a></li>
<li><a href="https://www.marketscreener.com/news/eli-lilly-and-company-entered-into-a-definitive-agreement-to-acquire-merida-biosciences-inc-from-a-ce7858dcd18af727">Eli Lilly and Company entered into a definitive agreement to acquire ...</a></li>

</ul>
</details>

**Tags**: `#utilities`, `#M&amp;A`, `#biotech`, `#earnings`, `#energy`

---

<a id="item-finance-news-5"></a>
### [Huawei&\#x27;s H1 2026 Net Profit Drops 37% Despite Revenue Growth](https://mp.weixin.qq.com/s/gfpojf6yfdmneU0iZ1xpbQ) ⭐️ 7.0/10

Huawei reported H1 2026 revenue of 467.8 billion yuan, up about 9.6% year-on-year, but net profit fell about 37% to 23.4 billion yuan, due to higher chip prices and increased semiconductor R&amp;D spending. The company also reported negative cash flow of 39.9 billion yuan from stockpiling raw materials.

telegram · zaihuapd · Aug 31, 11:10

**「Background」** Huawei&\#x27;s profit decline is attributed to rising storage chip prices and increased investment in semiconductor R&amp;D, as well as a buildup of raw material inventory. The company is preparing to launch a new flagship phone with its self-developed Kirin chip in September.

**「Impact」** The profit drop and negative cash flow may affect Huawei&\#x27;s ability to invest in future R&amp;D and could impact its supply chain partners and investors, though the company remains a leading smartphone seller in China.

**Tags**: `#Huawei`, `#earnings`, `#semiconductors`, `#smartphones`, `#China tech`

---

<a id="item-finance-news-6"></a>
### [Chinese Court Freezes Nexperia Assets in Wingtech Lawsuit](https://www.reuters.com/world/asia-pacific/chinese-court-freezes-dutch-chipmaker-nexperia-bvs-stakes-four-china-units-2026-08-31/) ⭐️ 7.0/10

A Chinese court has frozen up to 2.14 billion yuan \(about $300 million\) in assets of Dutch chipmaker Nexperia and its subsidiaries, following a lawsuit by Wingtech Technology seeking 8 billion yuan in damages over alleged discriminatory Dutch restrictions. The freeze, effective August 20-25, lasts until August 2029.

telegram · zaihuapd · Aug 31, 12:26

**「Background」** Wingtech, which previously controlled Nexperia, was stripped of that control by Dutch authorities last year. In May, Wingtech sued Nexperia, its equipment subsidiary, parent company, and three executives, accusing them of implementing the restrictions.

**「Impact」** The asset freeze could affect Nexperia&\#x27;s operations in China, as its stakes in four Chinese entities are now tied up in the legal dispute, potentially disrupting its semiconductor business in the region.

**Tags**: `#semiconductor`, `#legal dispute`, `#asset freeze`, `#China`, `#Nexperia`

---

<a id="item-finance-news-7"></a>
### [Tim Cook Steps Down as Apple CEO, Remains with Company](https://cj.sina.com.cn/articles/view/5115326071/130e5ae77020030d72) ⭐️ 7.0/10

Tim Cook has stepped down as Apple CEO, handing the role to John Ternus, but confirmed he will stay with the company. In a final memo to employees, Cook expressed his love for Apple and gratitude for the team, stating he is at peace with the transition.

telegram · zaihuapd · Sep 1, 00:00

**「Background」** Cook had been Apple&\#x27;s CEO since 2011, succeeding Steve Jobs. The transition marks a significant leadership change for one of the world&\#x27;s most valuable companies.

**「Impact」** The leadership change could affect Apple&\#x27;s strategic direction, impacting investors, employees, and the broader tech industry, though Cook&\#x27;s continued presence may ensure stability.

**Tags**: `#Apple`, `#CEO transition`, `#corporate governance`, `#tech industry`, `#leadership change`

---