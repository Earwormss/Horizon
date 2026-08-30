---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 26 items, 12 important content pieces were selected

---

**Technology News**
1. [Tencent Open-Sources Hy4 Preview with Recursive Self-Improvement](#item-tech-news-1) ⭐️ 8.0/10
2. [100-Year-Old Algorithm Beats SOTA Time Series Anomaly Detection](#item-tech-news-2) ⭐️ 8.0/10
3. [DHS Uses Obscure Law to Snoop on Journalists and Groups](#item-tech-news-3) ⭐️ 7.0/10
4. [Samsung&\#x27;s PIM: Promise and Pitfalls](#item-tech-news-4) ⭐️ 7.0/10
5. [LLM API Scores Vary 3x More Between Days Than Within a Day](#item-tech-news-5) ⭐️ 7.0/10
6. [OpenAI Ends Cursor Model Supply After SpaceX Acquisition](#item-tech-news-6) ⭐️ 7.0/10
7. [South Korea Picks Consortia for Free National AI Service](#item-tech-news-7) ⭐️ 7.0/10
8. [Sony Music and Others Sue Anthropic Over Pirated Lyrics in Claude Training](#item-tech-news-8) ⭐️ 7.0/10

**Financial News**
1. [Appeals Court Rules Against Prediction Markets, Setting Up Supreme Court Fight](#item-finance-news-1) ⭐️ 8.0/10
2. [Landslide at Gyirong Port: 7 Dead, 544 Missing](#item-finance-news-2) ⭐️ 8.0/10
3. [Chinese Chipmaker CXMT Sues Pentagon to Be Removed from Military Blacklist](#item-finance-news-3) ⭐️ 7.0/10
4. [Four Departments Launch One-Year Special Action on Vehicle Quality](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Tencent Open-Sources Hy4 Preview with Recursive Self-Improvement](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

Tencent has released and open-sourced Hy4 preview, a new AI model that has gained rapid adoption on OpenRouter, processing trillions of tokens within days—more than GLM 5.3 in a week. The model is notable for its low cost, with a 5% cache cost compared to the typical 10-20% from other providers. Hy4 preview also marks a first for Tencent by participating in its own development through an automated optimization loop that refines training methods, data strategies, evaluation frameworks, and low-level operators, with results feeding back into subsequent iterations. This establishes an early-stage recursive self-improvement loop, a novel development in AI model training. The model is positioned as a general-purpose agentic model, with early user reports suggesting strong performance, though its coding capabilities remain unverified.

hackernews · shenli3514 · Aug 29, 19:33 · [Discussion](https://news.ycombinator.com/item?id=49492632)

**「Background」** Tencent Hy4 preview is a next-generation large language model released and open-sourced by Tencent on August 28, 2026. It features 770 billion total parameters with 49 billion active parameters \(a Mixture-of-Experts architecture\) and a context window exceeding 1 million tokens. The model weights are available on Hugging Face, ModelScope, GitCode, and CNB, including an FP8 quantized version. Notably, Hy4 preview participated in its own development by proposing and testing improvements to training methods, data strategies, evaluation frameworks, and low-level operators, establishing an early-stage recursive self-improvement loop.

**「Impact」** Developers and organizations using OpenRouter now have access to a cost-effective, high-traction AI model that may challenge existing options like GLM and DeepSeek, potentially shifting usage patterns due to its lower cache pricing and strong agentic performance.

**「Community Discussion」** Community members highlight Hy4&\#x27;s exceptional early traction on OpenRouter, with trillions of tokens processed in days, and note its competitive pricing advantage. One user reports that Hy3, a predecessor, performed nearly as well as DeepSeek in agentic tests, suggesting Hy4 may offer similar quality. Others criticize the presentation of benchmark charts in the release, calling for clearer data visualization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open-Sources Tencent Hy4 preview - Tencent</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview · Hugging Face</a></li>
<li><a href="https://technode.com/2026/08/28/tencent-open-sources-hy4-preview-with-770b-parameters-and-a-1m-token-context/">Tencent open-sources Hy4 preview with 770B parameters and a 1M-token context · TechNode</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Open Source`, `#Tencent`, `#Model Release`

---

<a id="item-tech-news-2"></a>
### [100-Year-Old Algorithm Beats SOTA Time Series Anomaly Detection](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

A researcher, Eamonn Keogh, reports that a simple 100-year-old Statistical Process Control \(SPC\) algorithm can outperform state-of-the-art \(SOTA\) time series anomaly detection \(TSAD\) methods on the popular TSB-AD-M benchmark, achieving perfect results on an ECG trace example. He argues that the TSB-AD benchmark is too trivial to support meaningful claims, noting that many traces labeled &\#x27;TAO&\#x27; are even easier to solve with SPC. Keogh emphasizes that he makes no claims about the proposed algorithms themselves but calls for community introspection, suggesting that most progress in TSAD over the last decade may be illusory. He has done 90% of the work to introduce more challenging TSAD problems, including sled dogs, Tuna, Fuel Cells, and Smart Manufacturing datasets.

reddit · r/MachineLearning · /u/eamonnkeogh · Aug 29, 20:16

**「Background」** TSB-AD is a benchmark suite for time-series anomaly detection, introduced by Paparrizos and colleagues, containing 1,070 time series from 40 datasets and proposing the VUS-PR evaluation measure. It was accepted to the NeurIPS 2024 Datasets and Benchmarks Track and is widely used to evaluate state-of-the-art anomaly detection methods. Statistical Process Control \(SPC\) is a classical quality-control method dating back about a century, which monitors process stability using control charts and flags points outside expected variation.

**「Impact」** This critique challenges the validity of numerous TSAD papers that rely on the TSB-AD benchmark, potentially undermining their reported performance gains and prompting researchers to adopt more rigorous benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD</a></li>
<li><a href="https://github.com/thedatumorg/TSB-AD">GitHub - thedatumorg/TSB-AD: Time-Series Anomaly Detection | Algorithms + Datasets + Tutorials · GitHub</a></li>

</ul>
</details>

**Tags**: `#time-series`, `#anomaly-detection`, `#benchmarking`, `#machine-learning`, `#research-critique`

---

<a id="item-tech-news-3"></a>
### [DHS Uses Obscure Law to Snoop on Journalists and Groups](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits) ⭐️ 7.0/10

The Department of Homeland Security \(DHS\) is using an obscure legal mechanism, known as a 1509 summons, to secretly obtain records from journalists, non-profits, and unions, raising serious privacy and Fourth Amendment concerns. The summons allows DHS to demand records without a judge&\#x27;s approval, and in several cases, the agency has withdrawn the summons after legal challenges, possibly to avoid a judicial ruling on its legality. In one instance, T-Mobile provided six months of phone records for a journalist, including over 10,000 calls and texts, while Google refused to comply. The journalist was not notified until mid-July, and her lawyers expressed shock at the unilateral access. This practice highlights the tension between national security investigations and constitutional protections.

hackernews · firefax · Aug 29, 18:44 · [Discussion](https://news.ycombinator.com/item?id=49492219)

**「Background」** The DHS is using an obscure legal mechanism, the 1509 summons, to secretly obtain records from journalists, non-profits, and unions. This summons allows the government to demand records without a judge&\#x27;s approval, raising significant Fourth Amendment concerns. In several cases, the DHS has withdrawn the summons after it was challenged in court, potentially to avoid a judicial ruling on its legality. The article highlights instances where T-Mobile complied with such a summons, providing six months of phone records for journalist Georgia Fort, while Google did not comply.

**「Impact」** Journalists, non-profits, and unions face heightened risk of having their communications metadata accessed without prior notice, potentially chilling investigative reporting and advocacy. Technology companies that comply with such summonses may inadvertently facilitate surveillance, while those that resist, like Google, set a precedent for challenging the legality of these demands.

**「Community Discussion」** Commenters noted that DHS&\#x27;s withdrawal of summonses after challenges may be a deliberate strategy to avoid judicial review, and that companies could simply ignore the summons since DHS must go to court to enforce them. Some suggested decentralized email solutions for journalists, while others debated the necessity of judicial oversight, with one commenter arguing that the Fourth Amendment does not require a judge in the loop and that such requirements could hinder law enforcement efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits">Trump’s DHS is using an obscure law to secretly snoop on journalists ...</a></li>
<li><a href="https://dzen.ru/b/apNh_c1e8VehKnyn">DHS получило 10 000 записей в обход суда DHS получило... | Дзен</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#surveillance`, `#legal`, `#data-protection`, `#civil-liberties`

---

<a id="item-tech-news-4"></a>
### [Samsung&\#x27;s PIM: Promise and Pitfalls](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) ⭐️ 7.0/10

Samsung&\#x27;s Processing-in-Memory \(PIM\) technology, detailed by Chips and Cheese, aims to reduce data movement in AI workloads by integrating compute directly into memory. While this approach can significantly cut energy and latency for memory-bound tasks, it requires precise knowledge of data placement, which suits regular patterns like AI, gaming, and crypto but not general-purpose computing. Community members note that similar concepts have been proposed for decades, and many exotic accelerators fail to reach production. The implementation faces challenges in matrix multiplication, where data movement remains a bottleneck, and some argue that a full architectural overhaul might be more effective.

hackernews · ingve · Aug 29, 06:06 · [Discussion](https://news.ycombinator.com/item?id=49487341)

**「Background」** Processing-in-Memory \(PIM\) is a computing paradigm that integrates processing capabilities directly into memory chips, reducing the need to move data between separate memory and compute units. Samsung has been developing PIM technology for years, showcasing its HBM-PIM \(High Bandwidth Memory with Processing-in-Memory\) at Hot Chips 33 in 2021, which integrates parallel data processing and DRAM on the same silicon. This approach aims to address the memory bandwidth bottleneck in AI workloads by performing computations where data resides, potentially improving energy efficiency and performance.

**「Impact」** For AI hardware engineers and data center operators, Samsung&\#x27;s PIM could offer a path to lower power consumption and faster inference if it matures, but its specialized nature and historical precedent of failed accelerators mean it is unlikely to disrupt mainstream computing soon.

**「Community Discussion」** Commenters are skeptical about PIM&\#x27;s practicality, noting that it constrains software development and that similar ideas have been around since the 1980s without widespread adoption. Some point out that matrix multiplication still requires significant data movement, and others suggest that a complete architecture change might be necessary to fully realize the benefits.

<details><summary>References</summary>
<ul>
<li><a href="https://semiconductor.samsung.com/news-events/tech-blog/how-the-ai-revolution-spurred-samsung-to-rethink-memory-and-data-processing/">How the AI Revolution Spurred Samsung to Rethink Memory and...</a></li>
<li><a href="https://news.samsungsemiconductor.com/global/samsung-brings-in-memory-processing-power-to-wider-range-of-applications/">Samsung Brings In - memory Processing Power to Wider Range of...</a></li>

</ul>
</details>

**Tags**: `#processing-in-memory`, `#hardware`, `#AI accelerators`, `#memory architecture`, `#Samsung`

---

<a id="item-tech-news-5"></a>
### [LLM API Scores Vary 3x More Between Days Than Within a Day](https://www.reddit.com/r/MachineLearning/comments/1w1jp1j/i_analyzed_31352_hourly_llm_benchmark_scores/) ⭐️ 7.0/10

An analysis of 31,352 hourly LLM benchmark scores found within-day variation of 2.8 points and between-day variation of 8.4 points, indicating that between-day variation is approximately 3 times greater. The study, conducted by the developer of the open-source AIStupidLevel system, used continuous evaluation across coding, deep reasoning, tool calling, and canary tasks, with coding responses executed and tool-calling tests run in isolated Docker environments. Tasks were repeated five times and aggregated into daily medians, with sequential change-point detection applied to identify sustained performance drift. The dataset has since grown to 169,858 benchmark runs, 104,458 measured scores, and 81 historical model identifiers across 22 currently monitored models and 6 providers. The system detected a 32% sustained performance decline in Gemini 3.1 Flash Lite, classifying it as a critical incident.

reddit · r/MachineLearning · /u/ionutvi · Aug 29, 11:08

**「Background」** Most LLM evaluations measure performance at a single point in time, which does not capture how production API models change over time. This analysis addresses that gap by repeatedly testing models with consistent tasks and scoring, separating ordinary stochastic variation from sustained performance changes.

**「Impact」** For developers and organizations relying on production LLM APIs, this finding implies that single-point benchmarks may be misleading, and continuous monitoring is necessary to detect performance drift that could affect application quality. The open-source AIStupidLevel system provides a practical tool for such monitoring, with an OpenAI-compatible router that selects models based on current task-specific performance, stability, tool-calling reliability, latency, and cost.

**Tags**: `#LLM evaluation`, `#benchmarking`, `#model stability`, `#time series analysis`, `#open source`

---

<a id="item-tech-news-6"></a>
### [OpenAI Ends Cursor Model Supply After SpaceX Acquisition](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 7.0/10

OpenAI has announced it will terminate its contract to provide models to Cursor, following SpaceX&\#x27;s acquisition of the company. The recommended service cutoff date is November 12, 2026, with OpenAI providing the maximum notice period allowed by the contract. OpenAI cited concerns that SpaceX may not comply with service terms, pointing to Musk&\#x27;s companies&\#x27; history of contract violations, including breaches after the Twitter acquisition and xAI&\#x27;s admission of violating OpenAI&\#x27;s service terms earlier this year. The custom agreement between OpenAI and Cursor, which had lasted nearly four years, permits cancellation within a limited time after a change of control. This move affects developers who rely on Cursor&\#x27;s AI-powered coding tools.

telegram · zaihuapd · Aug 29, 02:24

**「Background」** Cursor is an AI-powered code editor that integrates models from providers like OpenAI to assist developers. OpenAI and Cursor had a custom agreement allowing OpenAI to terminate the partnership within a limited time after a change of control. SpaceX acquired Cursor for $60 billion, triggering this clause and prompting OpenAI to wind down model access by November 12, 2026.

**「Impact」** Developers and organizations using Cursor&\#x27;s AI coding assistant will lose access to OpenAI models by November 12, 2026, potentially disrupting workflows and forcing migration to alternative models or tools. The exact impact depends on whether Cursor secures alternative model providers before the cutoff.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html">OpenAI to end model access to Cursor after acquisition by SpaceX - CNBC</a></li>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX - OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI industry`, `#contract termination`

---

<a id="item-tech-news-7"></a>
### [South Korea Picks Consortia for Free National AI Service](https://www.koreatimes.co.kr/business/tech-science/20260828/skt-kt-kakao-consortiums-selected-for-free-ai-service-for-public) ⭐️ 7.0/10

South Korea&\#x27;s Ministry of Science and ICT has selected three consortia led by SK Telecom, KT, and Kakao to operate the &\#x27;AI for All&\#x27; project, which will provide free AI services to all citizens with no token limits, using domestically developed large language models. A pilot test is scheduled for September, with a full launch expected by the end of this year. The government will supply 512 Nvidia B200 chips to the consortia and will subsidize nationwide operational costs starting in 2027. The services will integrate with government systems for use cases such as medical appointment booking, property search, and tax consultation. Notably, Naver is not participating in this initiative.

telegram · zaihuapd · Aug 29, 15:31

**「Background」** The &\#x27;AI for All&\#x27; project is a government-backed initiative aimed at democratizing access to artificial intelligence by offering free, unlimited AI services to the public. By leveraging domestically developed models, the project seeks to reduce reliance on foreign AI technologies and promote local AI ecosystems. The involvement of major South Korean tech companies like SK Telecom, KT, and Kakao underscores the strategic importance of this national effort.

**「Impact」** This initiative will provide all South Korean citizens with free, unlimited access to AI services, potentially transforming how they interact with government systems and daily tasks. It also strengthens the domestic AI industry by channeling government support and hardware resources to local companies, though the exclusion of Naver may affect competitive dynamics.

**Tags**: `#AI policy`, `#South Korea`, `#national AI service`, `#government initiative`, `#large language models`

---

<a id="item-tech-news-8"></a>
### [Sony Music and Others Sue Anthropic Over Pirated Lyrics in Claude Training](https://www.musicbusinessworldwide.com/files/2026/08/COMPLAINT-in-Sony_Music_Publishing_US_LLC_e.pdf) ⭐️ 7.0/10

Sony Music Publishing, Warner Chappell Music, and other music publishers have filed a lawsuit in the U.S. District Court for the Central District of California against Anthropic and its founders, alleging that the company illegally downloaded over 7 million books from pirate libraries such as LibGen and PiLiMi and scraped lyrics to train its Claude AI models. The complaint also claims Anthropic removed copyright management information from the lyrics. The plaintiffs are seeking statutory damages of up to $150,000 per work and a permanent injunction. This legal action follows a prior similar lawsuit that resulted in a $1.5 billion settlement, highlighting the significant financial stakes in AI training data disputes.

telegram · zaihuapd · Aug 30, 01:00

**「Background」** Anthropic develops the Claude family of large language models, which are trained on vast text corpora. The plaintiffs, Sony Music Publishing and Warner Chappell Music, are major music publishers that own or administer the copyrights to a large catalog of song lyrics. They allege that Anthropic used pirated book repositories and scraped lyrics without authorization to train Claude, and that this practice constitutes copyright infringement. The lawsuit follows earlier similar litigation against AI companies over training data, which reportedly resulted in a $1.5 billion settlement.

**「Impact」** If successful, this lawsuit could force Anthropic to alter its training data practices and pay substantial damages, potentially setting a precedent for how AI companies handle copyrighted material in training datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/anthropic-claude-training-copyright-music-lyrics-sony-lawsuit-2026-8">Sony accuses Anthropic of &#x27;brazen campaign&#x27; to train Claude on its music — and wants up to $150,000 a song</a></li>
<li><a href="https://www.musicbusinessworldwide.com/now-sony-music-publishing-and-warner-chappell-sue-anthropic-in-multi-billion-dollar-lawsuit-one-of-the-largest-and-most-blatant-ongoing-thefts-of-intellectual-property-in-history/">Sony Music Publishing and Warner Chappell sue Anthropic in multi-billion dollar lawsuit</a></li>
<li><a href="https://www.thenews.com.pk/latest/1414143-sony-and-warner-chappell-sue-anthropic-over-copyrighted-songs-used-in-ai-training">Sony and Warner Chappell sue Anthropic over copyrighted songs used in AI training | Technology | thenews.com.pk</a></li>

</ul>
</details>

**Tags**: `#AI`, `#legal`, `#copyright`, `#Anthropic`, `#training data`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Appeals Court Rules Against Prediction Markets, Setting Up Supreme Court Fight](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 8.0/10

A federal appeals court ruled that sports-related event contracts are not swaps, rejecting prediction market platforms&\#x27; claims of exclusive federal jurisdiction and allowing states to regulate them as sports betting. The decision conflicts with an earlier ruling by another appeals court, making Supreme Court review likely.

rss · CNBC Finance · Aug 29, 02:23

**「Background」** The Commodity Futures Trading Commission \(CFTC\), the U.S. federal regulator for derivatives, has argued that all event contracts—including those on sports—are swaps, a type of derivative, and thus fall under its exclusive jurisdiction. In April 2026, the Third Circuit Court of Appeals sided with the CFTC, ruling that sports-related event contracts are swaps and that the CFTC has exclusive authority over them. That decision created a conflict with the recent Ninth Circuit ruling, which found such contracts are not swaps and can be regulated by states.

**「Impact」** The ruling affects prediction market platforms like Kalshi, Crypto.com, and Robinhood, which may face state-level restrictions on sports event contracts, while online sportsbooks like DraftKings and Flutter Entertainment saw their shares rise on the news.

<details><summary>References</summary>
<ul>
<li><a href="https://clsbluesky.law.columbia.edu/2026/04/13/paul-weiss-discusses-third-circuit-ruling-on-exclusive-cftc-jurisdiction-over-sports-related-event-contracts/">Paul Weiss Discusses Third Circuit Ruling on Exclusive CFTC Jurisdiction Over Sports-Related Event Contracts | CLS Blue Sky Blog</a></li>
<li><a href="https://www.hklaw.com/en/insights/publications/2026/04/federal-appeals-court-cftc-jurisdiction-over-sports-event-contracts">Federal Appeals Court: CFTC Jurisdiction Over Sports Event Contracts Likely Exclusive | Insights | Holland &amp; Knight</a></li>
<li><a href="https://www.skadden.com/insights/publications/2026/04/third-circuit-affirms-kalshis-preliminary-injunction">Third Circuit Affirms Kalshi’s Preliminary Injunction | Skadden, Arps, Slate, Meagher &amp; Flom LLP</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#regulation`, `#CFTC`, `#circuit split`, `#sports betting`

---

<a id="item-finance-news-2"></a>
### [Landslide at Gyirong Port: 7 Dead, 544 Missing](https://mp.weixin.qq.com/s/bGIRxRtW0k42tTYCksrOEA) ⭐️ 8.0/10

A landslide triggered by debris flow on the Nepalese side on August 26 caused severe damage at Gyirong Port in Tibet, killing 7 people and leaving 544 missing as of 1:00 AM on August 29. The port building was reduced to steel frames, and roads were covered with rocks and sand, hampering rescue efforts.

telegram · zaihuapd · Aug 29, 11:34

**「Background」** On August 26, 2026, a landslide triggered on the Nepalese side struck Gyirong Port in Tibet, causing casualties and missing persons. The port is a key border crossing between China and Nepal, and the disaster has severely damaged infrastructure, complicating rescue efforts.

**「Impact」** The disaster has severely disrupted cross-border trade between China and Nepal and affected local communities, with rescue teams conducting grid searches and transport authorities working to restore nearly 1 kilometer of washed-out road.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/2026%E5%B9%B4%E4%B8%AD%E5%B0%BC%E8%BE%B9%E5%A2%83%E6%B3%A5%E7%9F%B3%E6%B5%81%E7%81%BE%E5%AE%B3">2026年中 尼 边境 泥 石 流 灾 害 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.news.cn/20260830/507b5300b0a448b0881ffa8b3b2b37a5/c.html">此次抢险救援为何难度极大？ -新华网</a></li>

</ul>
</details>

**Tags**: `#natural disaster`, `#infrastructure damage`, `#casualties`, `#border trade`, `#Nepal`

---

<a id="item-finance-news-3"></a>
### [Chinese Chipmaker CXMT Sues Pentagon to Be Removed from Military Blacklist](https://www.bloomberg.com/news/articles/2026-08-29/chinese-chipmaker-cxmt-sues-pentagon-to-get-off-us-blacklist) ⭐️ 7.0/10

Chinese DRAM maker CXMT has filed a lawsuit in the U.S. District Court for the District of Columbia against the U.S. Department of Defense, seeking removal from a blacklist of companies allegedly linked to China&\#x27;s military. The company, which claims its chips are for civilian and commercial use, says it has suffered reputational and commercial damage since being added to the list in January 2025.

telegram · zaihuapd · Aug 29, 05:43

**「Background」** The U.S. Department of Defense maintains a list of companies it says are affiliated with China&\#x27;s military, and being on it can restrict business with U.S. entities. CXMT, the world&\#x27;s fourth-largest DRAM maker, was added to this list in January 2025. The company says its chips are for civilian and commercial use, not military, and that the designation has hurt its reputation and business.

**「Impact」** If CXMT remains on the blacklist, U.S. and global tech companies that rely on its DRAM chips could face supply disruptions and higher costs, as seen in Apple&\#x27;s reported interest in sourcing from CXMT despite opposition from Micron.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-29/chinese-chipmaker-cxmt-sues-pentagon-to-get-off-us-blacklist">Chinese Chipmaker CXMT Sues Pentagon to Get Off US Blacklist - Bloomberg</a></li>
<li><a href="https://www.benzinga.com/news/legal/26/08/61510675/after-alibaba-chinas-top-memory-chipmaker-cxmt-sues-pentagon-over-chinese-military-company-label">After Alibaba, China’s Top Memory Chipmaker CXMT Sues Pentagon Over Chinese Military Company Label - Alib - Benzinga</a></li>
<li><a href="https://www.firstpost.com/tech/apples-memory-chip-gamble-could-sourcing-from-a-blacklisted-supplier-hurt-the-us-tech-industry-14033988.html">Apple&#x27;s memory chip gamble: Could sourcing from a blacklisted supplier hurt the US tech industry? – Firstpost</a></li>
<li><a href="https://www.whalesbook.com/news/English/technology/US-Pauses-Blacklist-on-Chinese-AI-and-Chip-Firms/6a32a203d017fdb50998e5b2">US Pauses Blacklist on Chinese AI and Chip Firms | Whalesbook</a></li>

</ul>
</details>

**Tags**: `#CXMT`, `#U.S.-China tech conflict`, `#semiconductor industry`, `#legal action`, `#blacklist`

---

<a id="item-finance-news-4"></a>
### [Four Departments Launch One-Year Special Action on Vehicle Quality](https://weibo.com/1893892941/5336817496754349) ⭐️ 7.0/10

On August 27, 2026, four government departments, including the Ministry of Industry and Information Technology, launched a one-year special action to inspect the production consistency and quality of road motor vehicles, covering six types of manufacturers, products, and testing institutions. The action includes unannounced spot checks, and violators may face penalties such as public notification, suspension of product announcements and certifications, or fines.

telegram · zaihuapd · Aug 29, 13:30

**「Background」** This action targets issues like production consistency, reliability, durability, and testing of new technologies, aiming to crack down on vehicles that are quickly assembled without meeting quality standards.

**「Impact」** Vehicle manufacturers and testing institutions will face stricter oversight, potentially leading to recalls or production adjustments, while consumers may benefit from improved vehicle quality and safety.

**Tags**: `#机动车质量`, `#专项行动`, `#生产一致性`, `#监管政策`, `#汽车行业`

---