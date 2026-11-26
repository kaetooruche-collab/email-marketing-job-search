# Discovery Cycle 16 — 2026-11-26

Regular run following cycle 15 (2026-11-25). Picks up cycle 15's open items and runs fresh
discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence (and specifically,
  deliverability/SPF/DKIM/DMARC/list-hygiene is the single strongest sub-area).
- Klaviyo, Make.com, Zapier, n8n, Mailchimp, HubSpot, Instantly, Lemlist, Apollo, Expandi, and
  Meta-ads remain PROHIBITED/unevidenced claims; checked the claims register for updates this
  cycle — none found. GoHighLevel and Shopify/e-commerce-revenue-growth experience, both named
  as requirements on new candidates this cycle, are likewise not in the register and were treated
  as unevidenced.
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (16th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` apply to every new candidate
  scored this cycle (five Upwork, one Guru.com, one PeoplePerHour; none independently tested for
  TRNC).

Checked `db/email_marketing_system.db` first — 64 opportunities on file from cycles 1–15. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Seven new candidates were found and logged this
cycle (five Upwork, one from a newly-touched source, Guru.com, and one PeoplePerHour) — all
**REJECTED**, mostly on a pattern not seen as cleanly before: two of the five Upwork listings
already show a job-specific "Hires" field despite still being publicly listed, meaning they are
functionally closed even though they appear open. Of the rest, one requires an unevidenced
platform (GoHighLevel), one has zero client track record and no disclosed budget, one requires
e-commerce/Shopify revenue-growth experience not in the claims register, the Guru.com listing's
genuine Brevo work is undercut by low pay and a performance-pay phase requiring owned cold-email
infrastructure, and the PeoplePerHour listing combines a zero-history client with an unresolved
scope question. All of cycle 15's open items were followed up on exactly as instructed. The
Newsletter Specialist listing (id 31) remains flat (11th cycle, rate never renders). The Brevo CRM
and Email Setup listing (id 40) is now stalled at Interviewing=4 for a **fifth** consecutive
cycle, and its account-level active-hires dip has now **held** for a second cycle rather than
moving further. Reddit's free-method scrape failed for an **11th** consecutive cycle. The
German-market freiguide.de/Kleinanzeigen.de dead-mirror pattern recurred for a **third**
consecutive cycle and is now called confirmed structural, per instruction, rather than
re-described as new. Not recommending an application package.

## Cycle 15 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — flat again, nothing to flag
Rechecked once more as a quiet status check, not a re-flag, per the owner's standing instruction.
Current state: **still open**. Hourly rate **still does not render** in the public scrape — the
**11th consecutive cycle** this has failed. Interviewing unchanged at 2. Invites sent/unanswered
unchanged at 0/0. Last viewed by client: "2 days ago" (vs "yesterday" in cycle 15 — ordinary
noise). Account-level figures: $69K total spent (flat), 36 hires, 15 active (unchanged from cycle
15's settled value), hours rose again (2,020→2,026) — ongoing activity on this buyer's other
contracts, nothing new. Per the owner's standing instruction, this is noted on the DB row and left
at that — not retired (no hire/closure signal) and not re-flagged.

### (b) Brevo CRM and Email Setup (id 40) — fifth consecutive stall, and the account-level signal has now stabilized
Rechecked closely again, per the owner's instruction to watch this one most closely. Result: **it
has still not moved on this listing**. Still open. Rate unchanged ($10–28/hr). **Interviewing is
still at 4** — now the **fifth** consecutive cycle at exactly 4 (cycles 12, 13, 14, 15, 16).
Invites-sent/unanswered unchanged at 2/0. The account-level active-hires figure that dropped from
1 to 0 in cycle 15 **held at 0** this cycle — no further movement in either direction. Total spent
still flat at $15. Two consecutive cycles of total stability on both the listing itself and its
buyer account. Noted on the DB row, not treated as closure, tier not revised
(`PAYMENT_TIMELINE_UNCERTAIN`).

### (c) Reddit r/forhire — still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). A direct `firecrawl_scrape` attempt against the subreddit
listing page failed identically: *"Firecrawl can't scrape this site because it is currently not
supported."* This is the **11th consecutive cycle** this has failed via the free method. No cost
incurred, no new data gained, as expected. **Still awaiting the owner's decision** on whether the
paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — a genuinely new in-scope listing, logged and rejected
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
One listing stood out as genuinely new and in-scope this cycle: **"Markerters wanted for sale of
products email campaigns thank u"** ($175 fixed, 26 proposals, a 0%-rating/0-projects-completed
buyer account) — a multi-vertical (beauty/wellness, real estate investment, business coaching,
consumer products) email marketing specialist role with no platform named, so no PROHIBITED-tool
conflict. Read in full and **logged** this cycle (see table below) — the first in-scope
PeoplePerHour find logged in several cycles. The recurring out-of-scope postings persist in
substance: "Cold Email Marketing Specialist" (the Dubai B2B tax-consultancy cold-outreach role,
now aged to 4 days/24 proposals, up from 4 days/24 — essentially flat), "B2B Lead Generation &
Email Outreach for Established VO Artist" (now 2 days/30 proposals, up from 27), and a new
out-of-scope listing this cycle, "I need an outreach marketing professional" ($522, 32 proposals,
requiring Instantly.ai and Meta Ads — both PROHIBITED per the claims register, and the role is
outreach/ads management, not email-platform specialist work). None of these three were logged.

### (e) Contra (16 cycles), German-market search (16 cycles — dead-mirror pattern now confirmed structural on its third occurrence), and freelance.de (10 cycles)
All three were checked again this cycle. Contra's featured-jobs page again rendered real job
cards, including the same "Email Marketing Specialist – Dual Campaigns for Parents & School
Leaders" card already on file (id 19, $25–40/hr) plus the same two recurring non-Brevo listings
("Marketing Assistant for Launch Campaign," "Prepping Digital Assets Before Launching
Campaigns") — no genuinely new client email-marketing posting appeared. That makes **16
consecutive cycles** for Contra with no new genuine email-marketing lead.

The German-market search surfaced the same `freiguide.de`-mirrored Kleinanzeigen.de classified,
"BREVO Newsletter einrichten." Checking the original Kleinanzeigen.de URL directly
(`kleinanzeigen.de/s-anzeige/brevo-newsletter-einrichten/2736294866-298-3833`) again returned "Die
gewünschte Anzeige ist nicht mehr verfügbar" (the ad is no longer available), with the category
page showing only unrelated Dresden-area service listings. This is now the **third** consecutive
cycle (14, 15, 16) this exact dead-mirror pattern has occurred. Per the owner's instruction, this
is no longer described as a fresh finding each cycle — it is **confirmed structural**:
`freiguide.de`'s index reliably lags behind Kleinanzeigen.de's own live removals for this specific
ad. That makes **16 consecutive cycles** for the German-market search with nothing live and
actionable.

freelance.de again surfaced only freelancer profile/directory pages (Brevo-Freelancer finden, a
freelancerteam.de referral-tool hit) plus a Fiverr gig-directory hit — no client project posting.
**10 consecutive cycles** confirming no reachable client-posting section for this platform via
search.

**Useme.com — a notable change worth flagging, though not actionable.** Re-checked page 1
(English) only this cycle. Every one of the 20 listed jobs on the category page now shows status
**"Finished"** (spanning Mailchimp, GetResponse, Klaviyo, MailerLite, Edrone, and Snov.io work).
The long-running Oliver Törnroth/Zoined posting — the sole open listing on this page across
cycles 7–15, last seen with 17 days remaining in cycle 15 — is **no longer present on the page at
all**. This reads as ordinary listing turnover/expiry rather than a scraping failure: the page
rendered correctly and shows real (closed) data. It is nonetheless the first state change on this
specific listing in 9 cycles. Still zero live Brevo listings either way. Polish page 2 not
re-checked this cycle.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–15 unchanged, see (a)
above)

## New candidates checked this cycle (7 logged, 2 noted but not logged)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Email Deliverability Specialist for CRM | Upwork | Small client, Spain ($300 spent, 3 hires, 1 active) | **REJECTED** — functionally closed (Hires:1 already shown) |
| Email Deliverability & Domain Reputation Expert | Upwork | Established US client ($218K spent, 228 hires, 44 active) | **REJECTED** — strong skill match, but 50+ proposals, 9 interviewing, 9 invites sent |
| Senior Email Marketing & Deliverability Expert | Upwork | Hong Kong education company ($346K spent, 106 hires) | **REJECTED** — functionally closed (Hires:2) plus requires GoHighLevel, unevidenced |
| Email Marketing Specialist \| Domain Safety & Deliverability Experience Required | Upwork | Brand-new agency, US (no spend/hire history) | **REJECTED** — no budget disclosed, zero client track record |
| Email Marketing Specialist | Upwork | Livable Hair, small Canadian e-commerce client ($15K spent, 11 hires) | **REJECTED** — requires Shopify/e-commerce revenue-growth experience, unevidenced; heavy competition |
| Brevo CRM Automation + B2B Cold Email Lead Generation | Guru.com (new source) | Unverified individual/consulting client, US | **REJECTED** — $100 fixed underpays the Phase-1 scope; Phase-2 requires owned cold-email infrastructure, unevidenced |
| Markerters wanted for sale of products email campaigns thank u | PeoplePerHour | Brand-new buyer, Australia (0% rating, 0 projects completed) | **REJECTED** — low budget, zero client history, unresolved scope |

### Why they were rejected

- **Email Deliverability Specialist for CRM** ($10–28/hr, <1 month, Spain): decent generic
  deliverability skill match and a small but real client — rejected because the job's own
  activity panel already shows **Hires: 1**, with Interviewing dropped to 0 and only 1 invite
  sent. This listing is functionally closed even though it remains publicly viewable; applying now
  would mean bidding on an already-awarded job.
- **Email Deliverability & Domain Reputation Expert** ($8–50/hr, 1–3 months, established US
  client): the strongest skill match of this cycle's new finds — pure deliverability/domain-
  reputation audit work, squarely the project's best-documented area — from an exceptionally
  credible client ($218K spent, 228 hires, 44 active, 2018 member). Still rejected on
  competition/timing alone, per the owner's standing instruction: 50+ proposals, 9 candidates
  already Interviewing, 9 invites already sent (1 unanswered). This is the same pattern as cycle
  15's "Email Deliverability Specialist" reject, repeated with an even further-advanced funnel.
- **Senior Email Marketing & Deliverability Expert** ($50–120/hr, 1–3 months, Hong Kong): a double
  reject — the listing already shows **Hires: 2** (functionally closed despite 6 still
  Interviewing), and the platform named, GoHighLevel, has no support in the claims register at
  all (Brevo is the project's only evidenced platform).
- **Email Marketing Specialist | Domain Safety & Deliverability Experience Required** (rate not
  disclosed, 1–3 months, Finish Green agency): good skill-area overlap (SPF/DKIM/DMARC, domain
  reputation, deliverability monitoring, no prohibited tool required) undercut by three
  compounding problems — no budget disclosed at all (fails the compensation/payment-horizon test
  outright, since it cannot be evaluated), a brand-new agency account with zero spend or hire
  history, and 5 candidates already Interviewing.
- **Email Marketing Specialist** ($20–120/hr, 1–3 months, Livable Hair, Canada): a credible client
  and reasonable rate, but the role explicitly wants proven e-commerce email-revenue growth and
  Shopify experience — neither supported by the claims register, which documents B2B
  financial-advisory email marketing (HIBARR), not e-commerce flow revenue attribution. Combined
  with heavy competition (50+ proposals, 4 Interviewing, 7 invites sent with 3 unanswered), this
  is a skill-mismatch-plus-competition reject.
- **Brevo CRM Automation + B2B Cold Email Lead Generation** ($100 fixed Phase 1 + performance pay
  Phase 2, Guru.com — a source not previously checked by this project): Phase 1 is genuine Brevo
  CRM/automation work the project's documented skills cover well (Calendly/Acuity integration,
  40+ templated and triggered emails, pipeline setup), but $100 fixed is low pay for that scope.
  More decisively, the client wants a freelancer who can execute both phases, and the application
  itself requires answering detailed questions about owned cold-email sending infrastructure
  ("10+ email inboxes") and B2B appointment-setting track record — capabilities not in evidence.
  Taking Phase 1 alone while unable to credibly answer the Phase 2 screening questions is not a
  clean path in, and client credibility on this new-to-project marketplace is unverified.
- **Markerters wanted for sale of products email campaigns thank u** ($175 fixed, PeoplePerHour,
  Australia): no prohibited-tool conflict and a nominally in-scope skill ask, but three
  compounding problems — $175 does not match the described ongoing, multi-vertical (four
  unrelated business types) campaign-management scope; the buyer account has 0% rating and 0
  completed projects, with zero track record to assess; and the client's own clarification-board
  answers show the basic question of whether email platforms/subscriber lists already exist is
  still unresolved, meaning the real scope could exceed the posted budget by a wide margin.

### Hits read but not logged this cycle (closed, scope-mismatched, or pure search noise)

- **"Cold Email Deliverability Specialist Needed"** (Upwork) — found already removed from the
  platform ("This job is no longer available") when scraped directly; no longer independently
  actionable, so not logged.
- **"Marketing Email Outreach Infrastructure"** (Upwork, Australia, $207K-spent established
  client, 50+ proposals, 0 Interviewing/0 invites) — cold-email domain-warming infrastructure
  setup from Google Workspace for enterprise outreach, not platform-operation or campaign-
  management work; consistent with the project's treatment of cold-outreach-infrastructure roles
  as out of scope. Not logged.
- **"I need an outreach marketing professional"** (PeoplePerHour) — see follow-up (d). Requires
  Instantly.ai (PROHIBITED) and Meta Ads; outreach/ads management, not email-platform specialist
  work. Not logged.
- **"Mailing to 400000 emails"** (Freelancer.com) — surfaced by a generic Brevo/deliverability
  search but is a decade-old, long-since-cancelled project (posted ~10 years ago, status
  "Cancelled," 35 proposals from 2016). Pure search-index noise, not a live opportunity by any
  reading. Not logged.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-
  specific and generic searches surfaced 5 new-to-file URLs, all logged and REJECTED (see table
  above), plus one further hit found already removed and one read but not logged as out of scope
  (see above).
- **Freelancer.com**: Brevo-specific and generic searches surfaced no new-to-file *live* URLs
  this cycle — every Brevo-specific hit returned was already on file, plus one decade-old
  cancelled project that was pure search noise.
- **Guru.com** *(new source this cycle)*: surfaced by a Brevo-specific search; one listing found
  and logged (see table above). Kept on the source list for future cycles as a live,
  Brevo-relevant marketplace not previously checked.
- **PeoplePerHour**: page 1 only, per cycles 6–15's finding — one new-to-page, in-scope listing
  found and logged this cycle (see follow-up (d)), the first such find in several cycles.
- **Contra**: 16th consecutive cycle with the same structural limitation — real featured-job
  cards render, but none new and email-marketing-relevant (see follow-up (e)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked at the subreddit level;
  paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query and a follow-up check on the hit it
  surfaced — 16th consecutive cycle with no live, actionable German-market opening; the
  dead-mirror pattern on `freiguide.de`/Kleinanzeigen.de recurred for a third consecutive cycle
  and is now treated as confirmed structural (see follow-up (e)).
- **freelance.de**: tried the dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages — 10th consecutive cycle confirming
  no client project-posting section is reachable for this platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Notable change from cycles 7–15:
  every listing now shows status "Finished," and the long-running sole-open Oliver Törnroth/Zoined
  posting is gone from the page entirely (see follow-up (e)). Polish page 2 not re-checked.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycles 13–15's treatment; prior cycles' finding (job-board aggregator pages and
  Brevo's own healthcare-marketing blog content, no live candidate) assumed unchanged.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle, out of scope for
  this automated run, per the task instruction.

## System health

- Sources touched: 9 (Upwork, Freelancer.com, Guru.com [new], PeoplePerHour, Contra, Reddit
  [blocked, no paid provider], German-market direct search [including a follow-up check on
  freiguide.de/Kleinanzeigen.de], freelance.de, Useme.com), plus the Indeed health-wellness angle
  assumed unchanged from prior cycles. Direct business prospecting flagged as out-of-scope-this-
  cycle rather than touched.
- Opportunities found and logged as full rows: 7 new (0 collisions with the existing 64 on file),
  all `REJECTED`. 0 reached P0/P1. Database now holds 71 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) saw
  no change worth flagging beyond ordinary account-level activity (11th consecutive cycle of the
  hourly-rate-never-renders oddity) — noted, not re-flagged. The Brevo CRM and Email Setup listing
  (id 40), tracked most closely this cycle per the owner's instruction, is now confirmed
  **stalled for a fifth consecutive cycle** at Interviewing=4, and its account-level active-hires
  figure has now **held at 0 for a second cycle** rather than moving further in either direction —
  a period of total stability on both the listing and its buyer account. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for an 11th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra (16th) and freelance.de (10th) each
  logged another consecutive cycle of the same structural limitations already established in
  prior cycles. The German-market search's dead-mirror pattern, seen twice before, recurred a
  third time with the identical ad — per the owner's instruction, now confirmed structural rather
  than re-described as new each cycle. Useme.com's long-running sole-open listing finally expired
  or was removed after 9 cycles of persistence — worth noting as the first change there in a long
  while, though not itself actionable.
- This cycle's clearest lesson: a listing that *looks* open on a category page can already be
  functionally closed. Two of the five new Upwork candidates (and arguably a third, counting the
  one found outright removed) carried a job-specific "Hires" field already populated — a signal
  the project should keep checking explicitly on every new Upwork candidate going forward, not
  just competition counts, since "20–50 proposals, Interviewing: N" alone does not reveal whether
  the role has already been filled.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open,
   now at an 11th consecutive blocked cycle on the free method.
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded — nothing new to watch here beyond the standing rate-never-renders oddity,
   now at 11 consecutive cycles.
3. **No action needed on the Brevo CRM and Email Setup listing this cycle** beyond the note
   recorded — its earlier rising-interviewing signal remains stalled over five consecutive cycles
   (4, 4, 4, 4, 4), and the account-level signal that moved once (1→0 in cycle 15) has now held
   steady for a second cycle, suggesting it was a one-off account event rather than an ongoing
   trend. Worth a continued watch in future cycles rather than any fresh flag now. Separately, the
   owner's still-open call from cycle 11 on whether to keep checking Contra, the German-market
   search angle, and freelance.de each cycle (16, 16, and 10 consecutive cycles with nothing
   new/live and actionable) remains unchanged and unforced.
