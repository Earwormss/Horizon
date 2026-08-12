---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 48 items, 25 important content pieces were selected

---

**Technology News**
1. [DeepSeek V4 Pro 0813: Competitive Benchmarks, Aggressive Pricing](#item-tech-news-1) ⭐️ 8.0/10
2. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen3.8-2.4T-A95B: Massive MoE Model Released](#item-tech-news-3) ⭐️ 8.0/10
4. [Gowers on LLM Math Strengths: Sampling and Test-Time Scaling](#item-tech-news-4) ⭐️ 8.0/10
5. [Woxi: Open-Source Wolfram Language Interpreter in Rust](#item-tech-news-5) ⭐️ 8.0/10
6. [Researchers Steal Hidden Reasoning Traces from LLM APIs](#item-tech-news-6) ⭐️ 8.0/10
7. [Adam&\#x27;s Basis Dependence Breaks Implicit Low-Rank Bias](#item-tech-news-7) ⭐️ 8.0/10
8. [LTX-2.5: Open-Source Video Model Runs on RTX 5090](#item-tech-news-8) ⭐️ 8.0/10
9. [xAI Releases Grok 4.6 for Long-Running Agentic Tasks](#item-tech-news-9) ⭐️ 8.0/10
10. [Live Webcam Aggregation for 2026 Solar Eclipse](#item-tech-news-10) ⭐️ 7.0/10
11. [License Plate Reader Searches Should Require a Warrant](#item-tech-news-11) ⭐️ 7.0/10
12. [AI&\#x27;s Squeeze on Mid-Level Software Engineers](#item-tech-news-12) ⭐️ 7.0/10
13. [No Lossless AI Text Rewrites: Engineers Must Own Every Sentence](#item-tech-news-13) ⭐️ 7.0/10
14. [Honest CS Conference Ranking by Destination Quality](#item-tech-news-14) ⭐️ 7.0/10
15. [Decoupled Descent: Exact Train-Test Error Tracking via AMP](#item-tech-news-15) ⭐️ 7.0/10
16. [Enterprise SSDs Hit 48% of NAND Shipments; YMTC Enters Top Three](#item-tech-news-16) ⭐️ 7.0/10
17. [WeChat Releases Resource-Efficient WeLM LLM Family](#item-tech-news-17) ⭐️ 7.0/10

**Technology Blog**
1. [Day 0 Support for Qwen3.8-2.4T-A95B on vLLM](#item-tech-blog-1) ⭐️ 5.0/10

**Financial News**
1. [CME to Launch First AI Compute Futures Contracts](#item-finance-news-1) ⭐️ 8.0/10
2. [Former Chinese Premier Zhu Rongji Dies at 98](#item-finance-news-2) ⭐️ 8.0/10
3. [Tencent Q2 Revenue Beats Expectations, Capex Surge Turns Free Cash Flow Negative](#item-finance-news-3) ⭐️ 8.0/10
4. [Premarket Stock Movers: AI Names Surge on Strong Earnings and Guidance](#item-finance-news-4) ⭐️ 7.0/10
5. [EVs Dominate China&\#x27;s Car Market: 5 Takeaways from Latest Auto Sales Data](#item-finance-news-5) ⭐️ 7.0/10
6. [Nvidia&\#x27;s $500 Billion AI Financing Plan Faces China Risk](#item-finance-news-6) ⭐️ 7.0/10
7. [Election Betting Bans and Prediction Markets: A State-by-State Legal Patchwork](#item-finance-news-7) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [DeepSeek V4 Pro 0813: Competitive Benchmarks, Aggressive Pricing](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 is a newly released AI model available on OpenRouter, positioned as a competitive alternative to leading models like Opus 4.8, GLM-5.2, and Kimi-K3. Community benchmarks show it achieving a score of 42.7 without tools and 60.0 with tools on the HLE benchmark, while the V4 Flash 0731 variant scores 37.8 and 51.0 respectively. The model is noted for being roughly 20x cheaper than Opus 4.8, though it is considered weaker than some rivals like Sol or Fable. DeepSeek has also announced pricing increases starting today, and the V4 Flash 0731 is praised as one of the most outstanding models of recent months.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**「Background」** DeepSeek is a Chinese AI company known for releasing open-source models under the MIT License, starting with DeepSeek Coder in November 2023. In April 2026, DeepSeek released a preview of its V4 model series, which introduced a cost-effective 1M token context length. The V4 Pro 0813 is a large-scale mixture-of-experts model with 1.6 trillion total parameters and 49 billion active parameters, priced at $0.435 per million input tokens and $0.87 per million output tokens, with a 1,048,576 token context window and a maximum output of 384,000 tokens.

**「Impact」** For AI practitioners and developers, DeepSeek V4 Pro 0813 offers a cost-effective option for tasks that do not require top-tier intelligence, potentially reducing operational costs significantly compared to premium models like Opus 4.8.

**「Community Discussion」** Community members are actively comparing DeepSeek V4 Pro 0813 against other models, with some noting that while it is competitive with Opus 4.8, it is weaker than Sol or Fable. There is also concern about DeepSeek&\#x27;s pricing increases, with one user stating they are &\#x27;burning money quickly&\#x27; on the official API, while another highlights the V4 Flash 0731 as the most outstanding model of recent months.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine-learning`, `#model-release`, `#benchmarks`, `#pricing`

---

<a id="item-tech-news-2"></a>
### [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale has documented a 16-year-old SQLite WAL-reset race condition that corrupted databases in their control plane, despite a single-writer design that is the intended use of SQLite. The bug, which could only occur under specific concurrency conditions, was isolated with the help of an open-source SQLite VFS shim that Tailscale funded. The company paid SQLite developers to fix the bug, and the tooling will aid in tracking down similar issues in the future. The debugging journey is detailed in a blog post, highlighting the subtlety of the race and the value of investing in open-source debugging tools.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**「Background」** SQLite is a widely used embedded database that relies on a write-ahead log \(WAL\) to ensure durability and concurrency. In WAL mode, changes are first appended to a separate WAL file before being checkpointed into the main database file. The bug, named the &\#x27;WAL-Reset bug&\#x27; by SQLite developers, is a race condition that can occur when the WAL file is reset \(e.g., after a checkpoint\) while another process or thread is reading it, leading to lost writes and corrupted indexes. This bug has been present in SQLite for at least 16 years, dating back to at least version 3.7.0 \(released in 2010\), and was discovered by Tailscale after experiencing database corruption incidents.

**「Impact」** Tailscale users experienced outages due to database corruption, but the fix prevents future occurrences and provides a reusable tool for the broader SQLite community to diagnose similar concurrency bugs.

**「Community Discussion」** Commenters praised Tailscale for funding the open-source fix, with some noting the rarity of corporations paying for open-source maintenance. Others appreciated the technical depth, though one commenter pointed out a minor wording issue in the post.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://dzen.ru/b/anyfp4r4NVwmOoA8">16-летний баг SQLite вызвал 19 повреждений у Tailscale ... | Дзен</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#database`, `#bug`, `#concurrency`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [Qwen3.8-2.4T-A95B: Massive MoE Model Released](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10

Qwen has released Qwen3.8-2.4T-A95B, a large Mixture-of-Experts \(MoE\) model with 2.4 trillion total parameters and 95 billion active parameters. The model supports a native context length of 262,144 tokens, extendable to 1,010,000 tokens. Initial releases include BF16 and FP8 formats, with no QAT-quantized version, making deployment challenging; the BF16 model is approximately 4.9TB, while a 1-bit quantized version is around 397GB. The model card claims performance between Opus 4.8 and Fable 5, positioning it as a rival to Kimi k3, though it lacks vision input and non-thinking support compared to the official Qwen3.8-Max.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**「Background」** Qwen3.8-2.4T-A95B is a Mixture-of-Experts \(MoE\) large language model released by Alibaba&\#x27;s Qwen team, with 2.4 trillion total parameters and 95 billion active parameters per token. It supports a native context length of 262,144 tokens, extendable to 1,010,000 tokens. The model is positioned as a rival to Kimi k3 and is claimed to perform between Opus 4.8 and Fable 5 on benchmarks. Initial releases include BF16 and FP8 formats, with no quantized versions provided at launch.

**「Impact」** For practitioners, the release of Qwen3.8-2.4T-A95B with only BF16 and FP8 weights means that serving it at launch is harder than Kimi K3, and the lack of QAT on q4 forces well-resourced parties to quantize it, potentially bringing it to ~1.3TB, similar to K3&\#x27;s size. The 1-bit quantized version at 397GB with 95B active parameters reportedly brings Opus 4.5-level performance to consumer hardware, while the full BF16 model requires ~4.9TB, making deployment feasible only for those with substantial memory. The open-weight model lacks vision input, non-thinking support, and the 1M context length of the official Qwen3.8-Max, which may limit its appeal for some use cases.

**「Community Discussion」** Community members note that Qwen3.8-2.4T-A95B is a direct competitor to Kimi k3, but its large size and lack of QAT quantization make it harder to serve initially; some suggest that a well-funded entity will need to perform quantization. Others highlight that the 1-bit quantized version \(397GB\) could bring Opus 4.5-level performance to consumer hardware, while some express disappointment that the open-weight model lacks vision support and the full 1M context length, calling the capability loss intentional.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://www.edenai.co/post/kimi-k3-vs-qwen-3-8-max-benchmarks-pricing-api-access">Kimi K3 vs Qwen 3 . 8 -Max: Benchmarks , Pricing &amp; API Access</a></li>
<li><a href="https://autollab.ru/blog/claude-fable-5-vs-opus-4-8-vs-sonnet-4-6">Claude Fable 5 vs Opus 4.8 vs Sonnet 4.6: какую брать... — autollab</a></li>
<li><a href="https://habr.com/ru/articles/1068706/">Qwen 3 . 8 Max вышла: выше Claude Fable 5 в агентном... / Хабр</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Qwen`, `#MoE`, `#Model Release`

---

<a id="item-tech-news-4"></a>
### [Gowers on LLM Math Strengths: Sampling and Test-Time Scaling](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

In a recent blog post, Fields Medalist Timothy Gowers analyzes the mathematical capabilities of large language models \(LLMs\), focusing on their strengths in sampling and test-time scaling. He suggests that LLMs are particularly effective at generating many candidate solutions and filtering them, a method that has shown surprising results in mathematics and programming. The post also touches on the potential for LLMs to discover new and elegant proofs, though Gowers notes that recognizing such proofs may be challenging. The discussion highlights that while LLMs excel at certain tasks, their role in proving theorems and finding counterexamples remains an active area of exploration.

hackernews · ColinWright · Aug 12, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49270022)

**「Background」** Timothy Gowers is a British mathematician and Fields Medalist \(1998\), known for his work in functional analysis and combinatorics. He is currently a professor at the Collège de France and the University of Cambridge. His blog post analyzes the mathematical capabilities of large language models, focusing on sampling and test-time scaling.

**「Impact」** For researchers and engineers working on AI-driven mathematics, Gowers&\#x27; analysis underscores the practical value of sampling-based approaches and test-time scaling, which could guide future tool development and research priorities. The community discussion also points to a growing interest in using LLMs to find counterexamples and solve clearly stated problems, which may influence how AI is integrated into mathematical research workflows.

**「Community Discussion」** Commenters note that the post is essentially about test-time scaling, citing Google&\#x27;s AlphaCode as an early example of sampling success. There is also discussion about AI&\#x27;s affinity for finding counterexamples and the sociological trend of pursuing prominent problems, with some pointing to Gowers&\#x27; earlier prediction that machines would take over creative mathematics by 2100.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Timothy_Gowers">Timothy Gowers - Wikipedia</a></li>
<li><a href="https://www.britannica.com/biography/William-Timothy-Gowers">Timothy Gowers | Mathematician, Fields Medal, Cambridge ... Timothy Gowers (1963 - ) - Biography - MacTutor History of ... Timothy Gowers&#x27;s web page - University of Cambridge Timothy Gowers, Fields Medal Winner - advancedmath.org Biography and publications | Timothy Gowers - Combinatorics ... The Mathematics of Everyday Life, with Sir Tim Gowers</a></li>
<li><a href="https://mathshistory.st-andrews.ac.uk/Biographies/Gowers/">Timothy Gowers (1963 - ) - Biography - MacTutor History of ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#mathematics`, `#test-time scaling`, `#AI research`, `#machine learning`

---

<a id="item-tech-news-5"></a>
### [Woxi: Open-Source Wolfram Language Interpreter in Rust](https://woxi.ad-si.com/) ⭐️ 8.0/10

Woxi is an open-source interpreter for the Wolfram Language written in Rust, offering a Mathematica-like GUI called Woxi Studio built with iced, as well as CLI, Jupyter kernel, Python package, npm package, and WASM module interfaces. It aims to provide a fast, embeddable alternative to Mathematica, with startup times typically in milliseconds compared to seconds for the Wolfram kernel, making it practical for shell scripts and short-lived processes. The project ensures conformance with approximately 26,000 unit tests and about 900 .wls script snapshot tests, and is currently focused on fixing edge cases, improving performance, and growing the community. Woxi is free and open source, and can run in a browser via WASM or be embedded as a scripting language in other applications. The project is hosted on GitHub and welcomes contributions and bug reports.

hackernews · adius · Aug 12, 10:06 · [Discussion](https://news.ycombinator.com/item?id=49270040)

**「Background」** The Wolfram Language is the programming language underlying Mathematica, a proprietary computational system widely used in scientific, engineering, and mathematical computing. Mathematica&\#x27;s kernel typically takes seconds to start, which makes it impractical for short-lived scripts or embedding. Woxi is an open-source interpreter for the Wolfram Language written in Rust, designed to start in milliseconds and be embeddable in browsers via WebAssembly or in other applications. It was previously posted on Hacker News six months ago, and the project has been under active development since then.

**「Impact」** Woxi provides a viable open-source alternative for developers and researchers who need a fast, embeddable Wolfram Language interpreter, potentially reducing reliance on proprietary Mathematica licenses for certain use cases. Its WASM support and embeddability could enable new applications in web-based and embedded scientific computing, though it is not yet a full replacement for Mathematica.

**「Community Discussion」** Community members have tested Woxi&\#x27;s multivariable calculus visualizations and found them displayable, though correctness is uncertain without Mathematica for comparison. Some users miss features like out-of-order execution and the % variable for quick calculations, and there is interest in a control systems module. Others express hope that Woxi could become a well-integrated, fast open-source CAS alternative to Sage, and note that it has successfully handled algebra problems that Sympy, Sage, Xcas, and Maxima could not.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=47155526">Woxi: Wolfram Mathematica Reimplementation in Rust | Hacker News</a></li>

</ul>
</details>

**Tags**: `#Wolfram Language`, `#Rust`, `#open-source`, `#scientific computing`, `#interpreter`

---

<a id="item-tech-news-6"></a>
### [Researchers Steal Hidden Reasoning Traces from LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 8.0/10

Researchers demonstrated a method to steal hidden chain-of-thought reasoning from proprietary LLM APIs by replaying encrypted reasoning blocks into weaker sibling models and jailbreaking them. The attack worked because Anthropic, OpenAI, and Google used the same encryption key across models in a family, allowing encrypted traces from frontier models to be decrypted by weaker models. The paper, hosted at stolen-thoughts.com, includes examples of extracted reasoning traces and a prompt injection variant that exploits models&\#x27; tendency to trust their own reasoning. All providers acknowledged the report and have since fixed the vulnerability, but the paper provides a detailed look at the raw reasoning traces of proprietary models. The attack was easiest against Claude Haiku 4.5, using a simple prompt to transcribe the reasoning verbatim.

rss · Simon Willison · Aug 11, 22:40

**「Background」** Proprietary LLM APIs from OpenAI, Anthropic, and Google return encrypted chain-of-thought blocks to clients, intended to hide the model&\#x27;s internal reasoning. The paper \(arXiv:2608.09867\) reveals that these encrypted blocks can be replayed into weaker sibling models, which can be jailbroken to reveal the stronger model&\#x27;s hidden reasoning in plaintext. The attack exploits the fact that models within the same family share the same encryption key, and that weaker models are more susceptible to jailbreaking. The researchers demonstrated the attack on Claude Haiku 4.5, and the providers have since fixed the vulnerability.

**「Impact」** This vulnerability exposed hidden reasoning traces from major LLM APIs, potentially revealing proprietary model internals and enabling prompt injection attacks that could exfiltrate data. The fix by providers mitigates the immediate risk, but the paper&\#x27;s findings highlight the need for stronger encryption and isolation of reasoning traces in future models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs - arXiv.org</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#chain-of-thought`, `#API vulnerability`, `#AI privacy`, `#proprietary models`

---

<a id="item-tech-news-7"></a>
### [Adam&\#x27;s Basis Dependence Breaks Implicit Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A Reddit post by /u/EtherealGlyph argues that Adam&\#x27;s per-coordinate second moment breaks rotation invariance, which is key to preserving gradient descent&\#x27;s implicit low-rank bias in factored models. The author ran nine update rules on underdetermined matrix sensing at matched training loss, finding two clusters: GD, shared-scalar Adam, Muon, and Shampoo keep the bias, while Adam, RMSProp, Lion, signum, and Adafactor lose it. A one-parameter family interpolating Adam&\#x27;s denominator from per-coordinate to a shared scalar shows monotonic recovery improvement, pinpointing anisotropy as the culprit. Muon behaves unexpectedly: it is exact on truly low-rank targets but degrades fastest with added spectral tail, ceding to GD near 4% tail energy. The author also found their own optimizer&\#x27;s per-coordinate clip was harmful; switching to global norm clip improved recovery error from 0.347 to 0.220. The post includes a caveat that the 43-44% held-out error reduction on hyperspectral data uses a train-only learning rate rule that disadvantages Adam, and theory covers only memoryless rules.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**「Background」** In factored models like W = UV^T, the loss is invariant to rotations \(U,V\) → \(UQ, VQ\), and gradient descent respects this invariance. Adam&\#x27;s per-coordinate second moment depends on the basis in which factors are written, breaking this invariance. Implicit low-rank bias refers to the tendency of certain optimizers to converge to low-rank solutions, which is beneficial in underdetermined settings like matrix sensing.

**「Impact」** This insight provides a mechanistic explanation for why adaptive optimizers like Adam lose implicit low-rank bias, guiding practitioners to choose optimizers \(e.g., shared-scalar Adam, Muon\) when low-rank solutions are desired, and suggests that modifying Adam&\#x27;s denominator to be more isotropic could improve recovery in matrix sensing tasks.

**Tags**: `#optimization`, `#low-rank bias`, `#Adam`, `#matrix sensing`, `#implicit regularization`

---

<a id="item-tech-news-8"></a>
### [LTX-2.5: Open-Source Video Model Runs on RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX has released LTX-2.5, an open-source video generation foundation model, with weights, training code, and inference pipeline fully open. It can run locally on a single RTX 5090 and is free for commercial use for companies with annual revenue under $10 million. The model supports text-to-video and image-to-video generation, featuring improved multi-shot coherence and prompt adherence, and incorporates a new diffusion video decoder and a Gemma 4 12B text encoder. In a benchmark of 98 text-to-video prompts, LTX 2.5 Pro ranked first among ten models.

telegram · zaihuapd · Aug 12, 02:15

**「Background」** LTX is an AI video-generation ecosystem developed by Lightricks, an Israeli tech company. It includes the LTX Studio platform, launched in February 2024, as well as open-source models and commercial API access. The LTX-2.5 release continues this open-source approach, offering open weights that can be run locally, fine-tuned, and deployed on user-controlled hardware, with free commercial use for companies under $10 million in annual recurring revenue.

**「Impact」** This release enables individual developers and small companies to run a state-of-the-art video generation model locally on consumer hardware, potentially accelerating innovation in video generation applications. The free commercial use threshold may attract startups, though the benchmark&\#x27;s limited scope \(98 prompts\) means real-world performance may vary.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LTX_Studio">LTX Studio - Wikipedia</a></li>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX&#x27;s Latest AI Open - Source Foundation Model | LTX</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#open-source`, `#AI models`, `#diffusion`, `#LTX`

---

<a id="item-tech-news-9"></a>
### [xAI Releases Grok 4.6 for Long-Running Agentic Tasks](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI released Grok 4.6 on August 12, 2026, building on Grok 4.5 with enhanced capabilities for long-running agentic and interactive tasks, as well as improved vision performance. The model matches GPT-5.6 Sol on the Artificial Analysis intelligence index, which aggregates nine benchmarks. Grok 4.6 is available immediately on Cursor, Grok Build, and the API, priced at $2 per million input tokens and $6 per million output tokens, with a faster version at double the price. To promote adoption, xAI is offering double usage for the first week on Grok Build and Cursor.

telegram · zaihuapd · Aug 12, 15:54

**「Background」** Grok is a series of large language models developed by xAI, launched in November 2023 by Elon Musk. Grok 4.6 is the latest iteration, building on Grok 4.5 with a focus on long-running agents and more ambitious interactive and visual work.

**「Impact」** Developers and enterprises using Cursor, Grok Build, or the xAI API can now deploy Grok 4.6 for long-running agentic workflows and vision tasks, with a promotional double-usage period in the first week.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_%28chatbot%29">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4 . 6 | SpaceXAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Grok`, `#xAI`, `#agentic AI`, `#model release`

---

<a id="item-tech-news-10"></a>
### [Live Webcam Aggregation for 2026 Solar Eclipse](https://jonty.github.io/2026_eclipse_webcams/) ⭐️ 7.0/10

A developer named jonty has created a live webcam aggregation page for the 2026 solar eclipse, available at https://jonty.github.io/2026\_eclipse\_webcams/. The page coordinates webcams across Iceland and Spain, where the eclipse is visible, and was built quickly in 2024 for the US eclipse, finishing minutes before totality. The author shared it on Hacker News, noting that coordinating the cameras was unexpected and hoping the site doesn&\#x27;t break. The page is a practical resource for viewing the eclipse live, with community members sharing additional trackers and webcam links.

hackernews · zoenolan · Aug 12, 11:53 · [Discussion](https://news.ycombinator.com/item?id=49270953)

**「Background」** A total solar eclipse occurs when the Moon passes directly between the Sun and Earth, completely blocking the Sun&\#x27;s disk for observers within a narrow path of totality. The eclipse on August 12, 2026, is notable as the first total solar eclipse visible in Europe in 27 years, with totality crossing parts of Russia, Greenland, Iceland, and Spain, and a large partial eclipse across the rest of Europe. Webcam aggregation pages like the one described compile live camera feeds from locations along the path of totality, allowing remote viewers to watch the event in real time.

**「Impact」** Viewers of the 2026 solar eclipse can use this aggregation page to watch live webcam feeds from Iceland and Spain, providing a centralized resource during the event. The page may experience high traffic or technical issues, as the author expressed uncertainty about its stability.

**「Community Discussion」** Community members shared historical context about eclipses, such as Thales&\#x27; prediction in 585 BC, and personal experiences traveling to view eclipses. Others recommended alternative trackers like eclipsefan.org and YouTube webcams, noting that some sites were overwhelmed by traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solar_eclipse_of_August_12,_2026">Solar eclipse of August 12, 2026 - Wikipedia</a></li>
<li><a href="https://www.timeanddate.com/live/eclipse-solar-2026-august-12">LIVE Stream: Total Solar Eclipse August 2026</a></li>

</ul>
</details>

**Tags**: `#solar eclipse`, `#webcams`, `#astronomy`, `#live streaming`, `#community`

---

<a id="item-tech-news-11"></a>
### [License Plate Reader Searches Should Require a Warrant](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/) ⭐️ 7.0/10

The article argues that warrantless searches of license plate reader \(LPR\) data are unconstitutional and require legal reform. It highlights that current practices allow police to access historical location data without a warrant, creating a significant privacy gap. The author contends that this violates Fourth Amendment protections and calls for statutory or constitutional changes to require judicial oversight. The piece emphasizes the need for a warrant for historical searches, while allowing warrant-free access for ongoing emergencies. This position is supported by concerns over police misuse, such as stalking and unauthorized data access.

hackernews · apwheele · Aug 12, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49273165)

**「Background」** License plate readers are automated cameras that capture license plate numbers and locations, often mounted on police cars or infrastructure. These systems generate vast databases of historical movement data, which law enforcement can query without a warrant. The Fourth Amendment protects against unreasonable searches, but courts have not consistently applied it to data collected by third parties, such as LPR systems. This legal ambiguity has led to calls for clearer rules governing access to such surveillance data.

**「Impact」** If adopted, a warrant requirement would significantly restrict police access to historical LPR data, reducing potential abuses and enhancing privacy protections for all individuals. However, the impact depends on legislative or judicial action, which may vary by jurisdiction and could face opposition from law enforcement agencies.

**「Community Discussion」** Commenters generally agree that warrantless access to LPR data is problematic, with some suggesting a middle ground of warrants for historical searches and warrant-free flags for ongoing issues. Others argue that LPRs are essentially general-purpose cameras that could be repurposed, and that the current legal framework is untenable. There is also debate about whether the Fourth Amendment applies to data held by third parties, with some calling for statutory or constitutional fixes.

**Tags**: `#privacy`, `#surveillance`, `#civil-liberties`, `#law`, `#technology-policy`

---

<a id="item-tech-news-12"></a>
### [AI&\#x27;s Squeeze on Mid-Level Software Engineers](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 7.0/10

The article argues that AI is disproportionately impacting mid-level software engineers, effectively removing the &\#x27;middle class&\#x27; of the profession. It suggests that AI tools enable senior engineers to handle tasks that were previously delegated to mid-level developers, reducing the need for that tier of expertise. The piece highlights concerns about career progression, as junior engineers may lack opportunities to develop the skills needed to advance. It also notes that &\#x27;bad&\#x27; engineers can amplify their poor practices across organizations with AI, while emphasizing the importance of critical thinking and proper learning. The article has sparked substantial discussion, with 383 points and 320 comments on Hacker News, reflecting its relevance to the software engineering community.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**「Background」** The software engineering job market has traditionally had a clear hierarchy: senior engineers handle complex design and architecture, mid-level engineers implement features and fix bugs, and junior engineers learn on the job. AI coding assistants, such as GitHub Copilot and ChatGPT, have rapidly improved in capability, allowing developers to generate code faster and automate routine tasks. This has led to speculation about how AI will reshape the industry, with some predicting a &\#x27;hollowing out&\#x27; of mid-level roles as AI takes over more routine coding work.

**「Impact」** Mid-level software engineers may face reduced job opportunities and slower career advancement as AI tools allow senior engineers to handle more work independently, potentially leading to a more polarized job market with junior and senior roles. However, the long-term impact remains uncertain, as AI could also create new roles and shift the nature of engineering work.

**「Community Discussion」** Commenters largely agree that AI is automating the work of &\#x27;Stack Overflow engineers&\#x27; who rely on copying code, but they express concern about the loss of learning opportunities for junior engineers. Some highlight that AI can amplify the impact of &\#x27;bad&\#x27; engineers, while others emphasize the need to maintain critical thinking and avoid over-reliance on AI. There is also debate about whether the next generation of top engineers will have the same opportunities to gain experience through struggle and failure.

**Tags**: `#AI`, `#software-engineering`, `#job-market`, `#career`, `#LLM`

---

<a id="item-tech-news-13"></a>
### [No Lossless AI Text Rewrites: Engineers Must Own Every Sentence](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything) ⭐️ 7.0/10

Sophie Alpert published an internal policy on acceptable AI use by engineers, arguing that there are no lossless transformations of natural-language text. She emphasizes that every rewrite or rephrase by an LLM changes meaning, and if the AI lacks the writer&\#x27;s detailed mental model, information is lost. The policy requires engineers to stand behind every idea and sentence in their documentation, ensuring the entire document reflects their own thoughts. If a reviewer questions a line, it is unacceptable to dismiss it as AI-generated. Simon Willison highlights this rule as crucial for teams using LLMs to massage writing.

rss · Simon Willison · Aug 11, 23:48

**「Background」** Large language models are increasingly used to assist with writing, including documentation and code comments. However, these models do not have access to the author&\#x27;s unexpressed intentions, so any rewrite may subtly alter the intended meaning. Alpert&\#x27;s policy addresses this by mandating that engineers take full responsibility for AI-assisted text, ensuring it accurately represents their thoughts.

**「Impact」** This policy provides a concrete, actionable standard for engineering teams adopting AI writing tools: every sentence must be personally vetted and owned by the author, preventing the spread of misleading or inaccurate documentation. It also sets a precedent for accountability in AI-assisted workflows, potentially influencing how other organizations formalize their own guidelines.

**Tags**: `#AI-assisted writing`, `#engineering policy`, `#LLM usage`, `#documentation`, `#accountability`

---

<a id="item-tech-news-14"></a>
### [Honest CS Conference Ranking by Destination Quality](https://www.reddit.com/r/MachineLearning/comments/1vmbdk6/i_built_an_honest_cs_conference_ranking_sorted_by/) ⭐️ 7.0/10

A new website, honestcsrankings.org, ranks approximately 540 upcoming CORE-ranked computer science conferences by destination quality rather than academic prestige. The ranking incorporates real climate data for the conference month, safety from the Global Peace Index, cost from World Bank price levels, accessibility, and a &\#x27;City Vibe&\#x27; factor. Users can filter by field, rank, or open deadlines, set a home city to rank by distance, export deadlines to .ics files, and share deep links with coauthors. The site includes an &\#x27;Upsets&\#x27; tab highlighting A\* venues in poor destinations. ICML/ICLR 2027 are missing because they are not yet announced, and COLM is absent because CORE has not ranked it; smaller conferences are scraped from WikiCFP and may contain errors.

reddit · r/MachineLearning · /u/JohnAZoidberg77 · Aug 12, 11:23

**「Background」** Traditional conference rankings like the CORE ranking assess academic quality and impact, but researchers often consider the travel destination when deciding where to submit. This tool provides a data-driven alternative that prioritizes the conference experience, using publicly available datasets for climate, safety, cost, and accessibility.

**「Impact」** Researchers and students in computer science can use this tool to make more informed decisions about which conferences to attend, potentially saving money and improving travel experiences. The tool may also encourage conference organizers to consider destination quality when planning events.

**Tags**: `#conference ranking`, `#CS conferences`, `#research tools`, `#academic travel`, `#data-driven`

---

<a id="item-tech-news-15"></a>
### [Decoupled Descent: Exact Train-Test Error Tracking via AMP](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 7.0/10

A new research paper introduces Decoupled Descent \(DD\), a training method that uses approximate message passing \(AMP\) Onsager corrections to enforce exact train-test error tracking in neural networks. The method addresses the common problem where training error decreases to zero while test error stagnates or increases, attributing this to data reuse bias. By applying DD, the training error asymptotically equals the testing error at each parameter iterate, as demonstrated on stylized Gaussian mixture models and a high-dimensional XOR model with a two-layer network. The paper is theoretical and not yet scaled to large models, but the author plans to develop a PyTorch-compatible package and suggests applications in optimal stopping and hyperparameter tuning.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**「Background」** In standard gradient descent training, models often overfit, achieving low training error but poor generalization, a phenomenon linked to data reuse bias. Approximate message passing is a high-dimensional statistical technique that provides corrections \(Onsager terms\) to account for dependencies introduced by iterative algorithms, enabling more accurate tracking of generalization error.

**「Impact」** For researchers and practitioners in machine learning, Decoupled Descent offers a principled way to monitor and control generalization during training, potentially improving model selection and early stopping, though its practical applicability to large-scale models remains unproven.

**Tags**: `#machine learning`, `#neural networks`, `#generalization`, `#approximate message passing`, `#optimization`

---

<a id="item-tech-news-16"></a>
### [Enterprise SSDs Hit 48% of NAND Shipments; YMTC Enters Top Three](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 7.0/10

According to a Counterpoint report, enterprise SSDs accounted for 48% of global NAND shipments in Q2 2026, nearly doubling year-over-year, driven by AI inference workloads. Industry revenue grew fivefold compared to the same period last year. Samsung led with a 25% share, SK Hynix followed with 22%, and YMTC \(Yangtze Memory Technologies\) surpassed Kioxia to take third place with 14% for the first time. However, YMTC&\#x27;s revenue ranked only fifth due to its product mix being more consumer-oriented. The report projects that enterprise SSDs will consume more than half of total NAND bits by the end of the year.

telegram · zaihuapd · Aug 12, 11:00

**「Background」** NAND flash memory is the storage medium used in SSDs, USB drives, and memory cards. Enterprise SSDs are high-performance drives designed for data centers and servers, often used to handle AI workloads. Counterpoint Research is a market research firm that tracks the semiconductor industry. YMTC \(Yangtze Memory Technologies Co.\) is a Chinese NAND manufacturer that has been expanding its market presence. The Q2 2026 data marks the first time YMTC has entered the top three in NAND shipment share, according to Counterpoint&\#x27;s tracker.

**「Impact」** The shift toward enterprise SSDs, fueled by AI workloads, is reshaping the NAND market, with YMTC&\#x27;s rise to third place in shipments signaling a competitive challenge to established players, though its lower revenue share highlights the importance of product mix in capturing value.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time">YMTC breaks into the top three NAND makers for the first time as AI servers swallow 48% of all flash — Chinese vendor has 14% share, according to research | Tom&#x27;s Hardware</a></li>
<li><a href="https://finance.biggo.com/news/0d947490-529d-486e-9181-37a9219aaf44">Samsung Holds Q2 NAND Shipment Crown; China&#x27;s YMTC Breaks Into Top 3 for First Time — BigGo Finance</a></li>

</ul>
</details>

**Tags**: `#enterprise SSD`, `#NAND flash`, `#AI workloads`, `#storage market`, `#YMTC`

---

<a id="item-tech-news-17"></a>
### [WeChat Releases Resource-Efficient WeLM LLM Family](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 7.0/10

WeChat&\#x27;s team has announced WeLM, a family of general-purpose large language models focused on resource efficiency. The WeLM-80B model, which activates only 3B parameters, is already deployed in WeChat&\#x27;s AI agent Xiaowei, enabling conversational search, native WeChat operations, and mini-program services. A larger WeLM-617B model with 23B active parameters, using a mixture-of-experts \(MoE\) architecture, is under development and aims to deliver stronger reasoning and understanding at moderate activation sizes. This model is intended for complex tasks within WeChat&\#x27;s ecosystem, such as intelligent mini-program development and tool generation for Xiaowei. The release underscores WeChat&\#x27;s strategy to scale AI capabilities across its massive user base while managing computational costs.

telegram · zaihuapd · Aug 12, 13:58

**「Background」** WeLM is a family of general-purpose large language models developed by Tencent&\#x27;s WeChat team, announced on August 12, 2025. The series emphasizes resource efficiency, with the WeLM-80B model \(3B active parameters\) already deployed in WeChat&\#x27;s AI agent Xiaowei, and a larger WeLM-617B model \(23B active parameters\) using a mixture-of-experts \(MoE\) architecture in development. MoE models activate only a subset of parameters per token, enabling larger total parameter counts while keeping computational costs lower, a design choice that aligns with the resource-efficiency focus of the release.

**「Impact」** WeChat&\#x27;s deployment of WeLM-80B in production and the development of the 617B MoE model signal a practical shift toward resource-efficient LLMs, potentially influencing how large-scale AI is integrated into consumer platforms. This could lower the barrier for deploying advanced AI in high-traffic applications, but the impact depends on the performance and reliability of the MoE model in real-world tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/wechat-releases-welm-large-language-model-series-with-welm-80b-active-in-ai-23402318">WeChat Releases WeLM Large Language Model Series... | Gate News</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#WeChat`, `#AI`, `#resource-efficiency`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Day 0 Support for Qwen3.8-2.4T-A95B on vLLM](https://vllm.ai/blog/2026-08-12-qwen3.8) ⭐️ 5.0/10

rss · vLLM Blog · Aug 12, 00:00

**「Background」** The Qwen3.8-2.4T-A95B model is a 2.4-trillion-parameter sparse Mixture-of-Experts \(MoE\) model with 512 experts, built on the Qwen 3.5 architecture. As one of the largest open-weight models released, it presents significant inference challenges due to its massive size and memory requirements.

**「Solution」** The vLLM team, in collaboration with Inferact, NVIDIA, and AMD, announced Day-0 support for Qwen3.8-2.4T-A95B, leveraging the existing Qwen 3.5 architecture to run the model out of the box. To reduce memory and bandwidth overhead, Inferact released MXFP4 and NVFP4-quantized weights that match full-precision quality, using Round-to-Nearest \(RTN\) quantization with activation calibration for 4-bit activations. Initial benchmarks show NVFP4 even outperforming FP8 on GSM8K and AIME25. Optimizations include fused kernels for linear attention, GQA, dense GEMMs, and MoE routing on NVIDIA, and AITER-fused kernels with hipBLASLt GEMMs on AMD, combining data, tensor, and expert parallelism. Deployment requires at least two NVIDIA B300 or AMD MI355X nodes, or a single node for FP4, with recommended generation parameters and a high max\_tokens for reasoning tasks.

**「Takeaway」** The author concludes that Day-0 support for Qwen3.8-2.4T-A95B on vLLM is achieved through architecture reuse and collaborative kernel optimizations, with FP4 quantization offering a cost-effective path to run this massive MoE model without sacrificing accuracy.

**Tags**: `#vLLM`, `#Qwen3.8`, `#MoE`, `#FP4 quantization`, `#inference optimization`

---

## Financial News

<a id="item-finance-news-1"></a>
### [CME to Launch First AI Compute Futures Contracts](https://www.cnbc.com/2026/08/11/ai-computing-power-becomes-a-tradable-asset-class-as-cme-starts-futures.html) ⭐️ 8.0/10

CME Group, in partnership with Silicon Data, plans to launch the first futures contracts tied to AI computing power on Oct. 5, pending regulatory approval. These contracts will allow trading based on hourly rental prices of Nvidia&\#x27;s H100 and Blackwell B200 GPUs, with each contract representing one month&\#x27;s rent for an H100.

rss · CNBC Finance · Aug 12, 14:14

**「Background」** CME Group and Silicon Data first announced their partnership on May 12, 2026. Silicon Data, backed by trading firm DRW, provides the underlying rental rate indexes that the futures will track. The H100 contract targets what is currently the workhorse GPU of the AI industry.

**「Impact」** These futures could give AI developers and data-center operators a way to hedge their costs, while offering investors a new asset class to gain exposure to AI computing capacity without directly investing in hardware or companies.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/cme-group-compute-futures-launch/">CME Group launches compute futures for trading on October 5</a></li>

</ul>
</details>

**Tags**: `#CME`, `#AI infrastructure`, `#futures`, `#GPU pricing`, `#financial innovation`

---

<a id="item-finance-news-2"></a>
### [Former Chinese Premier Zhu Rongji Dies at 98](https://www.news.cn/politics/20260812/4c2c72e299ef4561915d2e507393a81f/c.html) ⭐️ 8.0/10

Former Chinese Premier Zhu Rongji died in Beijing on August 12, 2026, at the age of 98, according to an official announcement from the Communist Party and state bodies. He served as premier from 1998 to 2003, during which he implemented major economic reforms and led China&\#x27;s accession to the World Trade Organization.

telegram · zaihuapd · Aug 12, 10:11

**「Background」** Zhu Rongji was a key architect of China&\#x27;s economic reforms in the late 1990s and early 2000s, including fiscal, financial, and state-owned enterprise reforms, and he maintained the yuan&\#x27;s value during the Asian financial crisis.

**「Impact」** His death is a significant historical event, but it has no direct impact on current financial markets or policies.

**Tags**: `#China`, `#Zhu Rongji`, `#Obituary`, `#Economic Reform`, `#Political Event`

---

<a id="item-finance-news-3"></a>
### [Tencent Q2 Revenue Beats Expectations, Capex Surge Turns Free Cash Flow Negative](https://wallstreetcn.com/articles/3779275) ⭐️ 8.0/10

Tencent&\#x27;s Q2 2026 revenue rose 11% year-over-year to 204.8 billion yuan, slightly beating Bloomberg expectations, but net profit grew only 0.7% to 56 billion yuan, missing estimates. Capital expenditure nearly tripled to 52.8 billion yuan, driving free cash flow to -13.8 billion yuan; excluding AI computing prepayments, free cash flow was 37.6 billion yuan.

telegram · zaihuapd · Aug 12, 10:30

**「Background」** Tencent has been aggressively investing in AI infrastructure, which is reflected in the sharp increase in capital expenditure. The company&\#x27;s marketing services revenue led growth at 22%, while domestic games grew 17% and international games dipped 0.8% due to currency effects.

**「Impact」** The negative free cash flow may concern investors focused on cash generation, but the company&\#x27;s AI investments could support long-term growth in its cloud and AI services.

**Tags**: `#Tencent`, `#earnings`, `#capital expenditure`, `#AI investment`, `#free cash flow`

---

<a id="item-finance-news-4"></a>
### [Premarket Stock Movers: AI Names Surge on Strong Earnings and Guidance](https://www.cnbc.com/2026/08/12/stocks-making-the-biggest-moves-premarket-crwv-smic-cohr.html) ⭐️ 7.0/10

AI-related stocks rallied in premarket trading after several companies reported strong earnings and raised guidance. CoreWeave jumped over 18.5% after its second-quarter revenue rose 112% year over year to $2.58 billion, beating estimates, and its adjusted operating margin of 5% topped the 2.7% consensus. Super Micro Computer gained over 7.5% after issuing first-quarter adjusted earnings guidance of $1.01–$1.10 per share, well above the 76-cent consensus, and revenue guidance of $14.5–$15.5 billion, above the $11.68 billion expected. H&amp;R Block surged 11% after forecasting fiscal 2027 adjusted earnings of $6.04–$6.24 per share on revenue of $4.11–$4.16 billion, both above consensus.

rss · CNBC Finance · Aug 12, 12:12

**「Background」** These moves follow quarterly earnings reports and forward guidance from the companies. Consensus estimates are analyst forecasts compiled by firms like LSEG and FactSet, used as benchmarks for company performance.

**「Impact」** Investors in these companies are directly affected by the stock price movements, which reflect market reactions to the earnings and guidance. The strong performance of AI-related names contrasts with declines in some software stocks, indicating sector rotation within the tech industry.

**Tags**: `#earnings`, `#guidance`, `#AI stocks`, `#premarket movers`, `#stock market`

---

<a id="item-finance-news-5"></a>
### [EVs Dominate China&\#x27;s Car Market: 5 Takeaways from Latest Auto Sales Data](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

China&\#x27;s auto market is increasingly dominated by electric vehicles \(EVs\), which made up 65.1% of new passenger car sales in July, up from 54% a year earlier, according to the China Passenger Car Association. Geely&\#x27;s Xingyuan hatchback was the best-selling model in the six months through July with nearly 197,500 units sold, while Tesla&\#x27;s Model Y ranked second with over 180,000 units.

rss · CNBC Finance · Aug 12, 01:20

**「Background」** China&\#x27;s auto market has been shifting rapidly toward electric vehicles \(EVs\), with new energy vehicles \(battery and hybrid cars\) making up 65.1% of new passenger car sales in July, up from 54% a year earlier. This shift has intensified competition among automakers, with domestic brands like Geely and BYD gaining ground, while traditional foreign brands like Volkswagen have struggled to maintain their market share.

**「Impact」** The shift toward EVs is reshaping competition, with traditional foreign brands like Volkswagen holding only a small presence, while domestic players like Geely and BYD lead the market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/jean-pierre-palomba-marin-14508b162_geely-wuling-surpass-tesla-byd-in-china-activity-7432325214094557184-0AaQ">Geely , Wuling surpass Tesla , BYD in China EV sales | Jean-Pierre...</a></li>
<li><a href="https://chinaevhome.com/2026/08/12/xiaomi-su7-ranks-2-in-china-july-ev-sedan-top-10-as-highest-priced-model/">Xiaomi SU7 Ranks #2 in China July EV Sedan Top 10... | ChinaEVHome</a></li>
<li><a href="https://carnewschina.com/2026/08/11/china-july-model-sales-rank-geely-xingyuan-1st-leapmotor-a10-2nd-tesla-model-y-3rd/">China July model sales rank: Geely Xingyuan 1st, Leapmotor A10 2nd...</a></li>

</ul>
</details>

**Tags**: `#China auto market`, `#EV sales`, `#Geely`, `#Tesla`, `#BYD`

---

<a id="item-finance-news-6"></a>
### [Nvidia&\#x27;s $500 Billion AI Financing Plan Faces China Risk](https://www.cnbc.com/2026/08/11/nvidia-ai-funding-jensen-huang-china-risk.html) ⭐️ 7.0/10

Nvidia announced a $500 billion financing pipeline with six major asset managers to fund AI data centers and GPU clusters, but analysts warn that a potential Chinese chip oversupply could erode GPU collateral values faster than expected, posing a key risk to the plan.

rss · CNBC Finance · Aug 11, 21:01

**「Background」** Nvidia has announced partnerships with six major asset managers to create financing platforms that aim to mobilize over $500 billion for AI infrastructure. The plan treats Nvidia&\#x27;s GPUs as collateral that retains value over time, similar to traditional assets like real estate. However, analysts warn that rapid depreciation of GPUs, potentially accelerated by a Chinese chip oversupply, could undermine the value of that collateral.

**「Impact」** If Chinese chip production triggers a price war, investors in these asset-backed loans could face losses as collateral values fall, and borrowers—likely non-investment grade AI startups—may struggle to refinance.

<details><summary>References</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital">NVIDIA Partners With Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to Establish AI Compute Infrastructure Financing Platforms to Mobilize Over $500 Billion of Third-Party Capital | NVIDIA Newsroom</a></li>
<li><a href="https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html">Nvidia lines up $500 billion in financing as CEO Jensen Huang tells CNBC his chips are ‘investable asset’</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-10/nvidia-to-team-with-wall-street-on-500-billion-package-ft-says">Nvidia Taps Wall Street for $500 Billion Funding Commitment - Bloomberg</a></li>
<li><a href="https://spectrum.ieee.org/china-ai-chip">China&#x27;s AI Chip Race: Tech Giants Challenge Nvidia - IEEE ...</a></li>
<li><a href="https://techjournal.org/us-imposes-25-tariff-on-nvidia-h200-ai-chips-bound-for-china">US-China AI Chip War 2026: Nvidia, Tariffs &amp; the H200</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI infrastructure`, `#asset-backed finance`, `#China risk`, `#GPU market`

---

<a id="item-finance-news-7"></a>
### [Election Betting Bans and Prediction Markets: A State-by-State Legal Patchwork](https://www.cnbc.com/2026/08/11/do-state-election-betting-bans-apply-to-prediction-markets.html) ⭐️ 7.0/10

As the midterms approach, states are uncertain whether their election betting bans apply to prediction markets, with Wisconsin and Colorado taking firm stances and platforms like Kalshi and Polymarket facing legal challenges.

rss · CNBC Finance · Aug 11, 18:44

**「Background」** Prediction markets are platforms where people trade contracts whose payouts depend on the outcome of future events, such as elections. The Commodity Futures Trading Commission \(CFTC\), a U.S. federal agency, considers these contracts to be swaps and claims exclusive authority to regulate them, which would override state laws. However, states argue that their constitutional power to manage elections gives them the right to ban betting on them. This dispute has led to legal battles, with some states like Wisconsin and Colorado enforcing their bans, while others are uncertain how their laws apply to these platforms.

**「Impact」** Users of prediction markets in states with strict bans could face penalties including fines, jail time, or loss of voting rights, while platforms may be forced to restrict access in certain states.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cftc.gov/PressRoom/PressReleases/9183-26">CFTC Reaffirms Exclusive Jurisdiction over Prediction Markets ...</a></li>
<li><a href="https://www.cftc.gov/LearnandProtect/PredictionMarkets">Understanding Prediction Markets and Event Contracts | CFTC</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#election betting`, `#state regulation`, `#legal uncertainty`, `#midterms`

---