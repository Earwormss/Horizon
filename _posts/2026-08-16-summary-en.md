---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 33 items, 11 important content pieces were selected

---

**Technology News**
1. [Anthropic Publishes Claude System Prompts for Transparency](#item-tech-news-1) ⭐️ 8.0/10
2. [AI Models Are Getting Dumber on Purpose](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B: Strong but Overthinks by Default](#item-tech-news-3) ⭐️ 8.0/10
4. [US Grid&\#x27;s $12B Modeling Mistake Risks Repeating](#item-tech-news-4) ⭐️ 8.0/10
5. [SSOG-Attention: Sub-quadratic Attention via Separable Gaussians](#item-tech-news-5) ⭐️ 8.0/10
6. [Cloudflare silently injects analytics when switching nameservers](#item-tech-news-6) ⭐️ 7.0/10
7. [Solving Long-Range Recall in Linear Attention for DNA](#item-tech-news-7) ⭐️ 7.0/10
8. [Revisiting ECA-Net: Cross-Channel Interaction Hypothesis Questioned](#item-tech-news-8) ⭐️ 7.0/10
9. [US asks allies to pick sides in AI cooperation](#item-tech-news-9) ⭐️ 7.0/10
10. [AI Tool Helps Shut Down 524 Pirated Telegram Channels in 61 Days](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Anthropic Q2 Preliminary Revenue Surpasses $11.5 Billion](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
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

---

<a id="item-tech-news-2"></a>
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

---

<a id="item-tech-news-3"></a>
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

---

<a id="item-tech-news-4"></a>
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

---

<a id="item-tech-news-5"></a>
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

---

<a id="item-tech-news-6"></a>
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

---

<a id="item-tech-news-7"></a>
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

---

<a id="item-tech-news-8"></a>
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

---

<a id="item-tech-news-9"></a>
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

---

<a id="item-tech-news-10"></a>
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

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic Q2 Preliminary Revenue Surpasses $11.5 Billion](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic&\#x27;s preliminary Q2 revenue exceeded $11.5 billion, up over 14 times year-over-year from $787 million in Q2 2025, and the company reported positive adjusted operating income for the quarter.

telegram · zaihuapd · Aug 16, 07:26

**「Background」** The figures are preliminary and may be adjusted, according to a Bloomberg report citing documents. The company is preparing for a potential IPO that could launch this fall.

**「Impact」** The revenue surge and positive operating income could strengthen Anthropic&\#x27;s position ahead of a potential IPO, affecting investors and the AI industry.

**Tags**: `#Anthropic`, `#revenue`, `#AI`, `#IPO`, `#earnings`

---