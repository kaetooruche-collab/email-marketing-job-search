# Discovery Cycle 1 — 2026-10-30

First live discovery run. Sources checked: Upwork (public job pages), Freelancer.com, PeoplePerHour, Contra, Reddit r/forhire, r/Emailmarketing (via web search, no login). Searches covered both generic ("email marketing freelancer") and tool-specific ("Brevo") phrasing, per master prompt §4.4.

## Headline

**No currently-open, well-matched P0/P1 opportunity survived qualification this cycle.** One strong skill match was found (Brevo deliverability/list-cleanup) but shows signals of likely already being filled. This is a genuine first-cycle result, not padding — see the per-opportunity notes below for why each one was rejected or discounted.

## P0 (0–7 day payment) — none qualified
No opportunity found this cycle met the P0 bar.

## P1 (8–30 day payment) — 1 found, discounted

### Brevo deliverability and list cleanup specialist — Underdog Sales
- **URL:** https://www.upwork.com/freelance-jobs/apply/Brevo-deliverability-and-list-cleanup-specialist_~022115757776792063959/
- **Posted:** 2026-10-29 (1 day old)
- **Budget:** $350 fixed, 2 milestones ($150 audit/diagnosis, $200 segments/sunset/SOP), ~10-12 hrs over 2-3 weeks
- **Client:** Paphos, Cyprus. Member since Nov 2025, $2.5K spent, 9 hires (6 active) — credible, established buyer.
- **Skill match:** Strong. The scope (SPF/DKIM/DMARC audit, Apple MPP-aware engagement segmentation, sunset automation, bounce/list hygiene) is close to word-for-word what your HIBARR work describes.
- **Score: 73/100 *if genuinely still open*.** But the listing's activity panel already shows **"Hires: 1"** against a posting that's one day old, plus 15–20 competing proposals — a strong signal it may already be filled. I discounted the probability-of-winning component heavily rather than present this as a clean go.
- **Gap to disclose if you apply anyway:** the listing also wants Make.com/Zapier experience, which isn't in your evidence register (see claims-register.md) — don't claim it, offer to learn/adapt instead if you pursue this.
- **Payment timeline estimate:** ~18 days to first accessible funds (Upwork's standard 5-day security hold after milestone approval, plus withdrawal transfer time) — fits P1, not P0.
- **Action:** Before investing time on a proposal, check the listing directly (logged into Upwork) to confirm it isn't closed. I have not drafted outreach or a proposal for this — want me to, once you confirm it's still open?

## Rejected this cycle (with reasons — full detail in `db/email_marketing_system.db` and `scripts/init_and_seed.py`)

| Opportunity | Client | Reason rejected |
|---|---|---|
| Brevo Email Designer — Master Template | Audinc, Belgium | Stale (client inactive 2 weeks), 20-50 competing proposals, thin client history ($60 spent), scope is visual/HTML design rather than lifecycle work |
| Setup Brevo subdomain/DNS | Unnamed, Pakistan | $15 fixed budget doesn't clear a sane hourly rate; stale; brand-new client, no payment history |
| E-commerce Email Marketing Specialist | EcomGrowth, Ireland | **Speculative** — pre-launch agency recruiting into a "freelancer network," no funded project, no budget, no timeline; fails the payment-horizon test outright. Also requires Klaviyo+Shopify, not your documented platform (Brevo). |
| Email marketing specialist — real estate | Ola Estate, Portugal | Hard requirement: fluent Russian. You don't speak Russian — disqualifying, not a close call. |
| List Building & Email Marketing Specialist | Unnamed, New York | Already has 1 hire recorded, client inactive 2 weeks — functionally filled; scope leans cold-outreach/list-building over lifecycle email |

## Sources with gaps this cycle

- **Reddit r/forhire**: search surfaced several "[Hiring]" post titles (e.g. a UK-based Brevo automation request mentioning FreeAgent/Riskbase — plumbing/trades-adjacent small business) but `firecrawl_scrape` refuses to fetch individual Reddit threads directly, so I could not confirm recency, budget, or whether these are still open. Worth you checking manually if interested: search r/forhire for "Brevo" "email marketing".
- **PeoplePerHour, Freelancer.com, Contra**: appeared in search results as category/landing pages, not individual live postings — would need a second pass scraping those category pages directly (not yet done).
- **Direct business prospecting (master prompt §4.3/§12)**: not started this cycle — this is the highest-potential channel for P0 work (small businesses with an observable, specific email gap) but requires its own research pass per prospect, which I haven't run yet.
- **LinkedIn, Facebook groups, Slack/Discord communities**: not searched this cycle (need login/access this session doesn't have for most of these).

## System health
- Sources scanned: 2 effectively queryable (Upwork public pages, web search broadly); Reddit partially blocked.
- Opportunities found: 6 (raw), 1 reached P1 with a major caveat, 0 reached P0.
- No automation failures beyond the Reddit scrape restriction noted above.
- No scheduled/recurring discovery run is set up yet — this was a single manual cycle.

## Recommended next 3 actions
1. **Confirm the Underdog Sales job is still open** (log into Upwork yourself — I can't) before I spend time drafting a proposal for it.
2. **Decide on the Türkiye vs. Northern Cyprus conflict** (see `evidence/claims-register.md` CONFLICT-1) — this gates which payment rails are even worth checking for P0/P1 qualification.
3. **Tell me whether to set up a recurring scheduled discovery cycle** (I can do this via a scheduled task on this account) and whether to start a second, broader pass (PeoplePerHour/Freelancer.com category pages, direct business prospecting) now.
