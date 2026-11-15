# Discovery Cycle 5 — 2026-11-15

**Administrative note on this run:** this is a single consolidated discovery cycle. A backlog of
14 identical daily-scheduled firings queued up while the session was idle (2026-11-02 through
2026-11-15). Per the owner's instruction, this run does **not** replay 14 separate cycles — it is
one cycle, run once, reflecting the live market as of today (2026-11-15), picking up from cycle 4
(`reports/2026-11-01-discovery-cycle-4.md`), the last cycle actually completed.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged from cycle 4:
- Brevo remains the one platform with strong, consistent documented evidence — prioritized in
  search, and the only platform that produced a scorable P1 lead this cycle.
- Klaviyo, Make.com, Zapier, n8n, and Mailchimp remain PROHIBITED claims. No listing this cycle
  required one of these as a hard requirement *and* otherwise fit — the one Klaviyo-requiring
  listing found (a German-market web-design role) was rejected on platform grounds and a role-type
  mismatch, not solely the tool gap.
- German proficiency remains an **unresolved CONFLICT** in the claims register — checked
  specifically again this cycle per instruction, still not resolved. No live posting this cycle
  turned on the answer either way (see German-market section below).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged:
  Upwork/Freelancer.com escrow rails remain UNVERIFIED-not-VERIFIED for actually landing in a
  TRNC-accessible account. This discounts every Upwork/Freelancer.com opportunity's
  `score_payment_certainty`, same as every prior cycle.
- The experience-threshold filter (claims register: "opportunities requiring more than ~2 years of
  experience are outside Kaeto's stated search criteria") was invoked for the first time this
  cycle as the primary rejection reason for a listing (see B2B CRM Specialist — Brevo, below).

Checked `db/email_marketing_system.db` first — 28 opportunities already on file from cycles 1-4.
Nothing below duplicates an existing URL.

## Headline

**8 new candidates checked this cycle (full scrape/scoring). 1 reached P1 — the strongest lead
found across all 5 cycles of this project to date, but still discounted, not a clean
recommendation. 7 rejected outright.** Several additional candidates were screened and rejected on
sight from search-result text alone (title/description sufficient to reject without a full
scrape) — listed separately below for transparency, not padded into the main count.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — one found, discounted

### Newsletter Specialist for Campaigns / Brevo — Upwork
- **URL:** https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/
- **Score: 64/100** (probability_win 11/20, time_to_payment 14/25, skill_match 13/15,
  payment_certainty 8/15, compensation 5/10, client_credibility 9/10, repeat_potential 4/5)
- **Why it's the best lead so far:** ongoing (6+ months) part-time role to improve Brevo email
  delivery rate and strengthen newsletter campaigns — list management, performance optimization,
  engagement improvement. This is squarely inside the one platform with strong documented
  evidence (Brevo deliverability/list hygiene). Zero hires and zero interviewing so far despite
  20-50 proposals, and the client last reviewed applicants only **3 days ago** — fresh, not stale,
  unlike most listings rejected in prior cycles. Client credibility is the strongest seen in this
  project to date: $65K total spent, 34 hires, 15 active contracts, 1,972 hours logged.
- **Why it's still discounted, not a clean go:** the exact hourly rate is **not shown** in this
  scrape (every other listing checked this cycle rendered a `$X.XX Hourly` figure; this one did
  not) — compensation cannot be confirmed as viable without opening the listing directly on
  Upwork, which requires a login this session doesn't have. 20-50 competing proposals is still
  real competition even with no hires yet. TRNC payment-routing remains UNVERIFIED for Upwork, the
  same caveat applied to every Upwork opportunity in this project.
- **Not recommending an application package.** Flagging this one for the owner: if the rate turns
  out to be viable when checked directly on Upwork, this is the cleanest-looking lead this project
  has surfaced in 5 cycles and would be worth revisiting for a package. As found, with the rate
  unconfirmed, it does not clear the bar for "clean, well-matched, no disqualifying signal."

## Rejected this cycle (7 full-scrape rejections — see table)

| Opportunity | Source | Client | Reason rejected |
|---|---|---|---|
| Brevo Expert for Email Campaigns | Upwork | Individual, Pennington PA, US | Already shows Hires: 1, Interviewing: 1, last viewed 2 weeks ago — effectively filled or deep in selection despite not being formally closed. |
| Brevo Admin Automation Setup | Upwork | Individual, Stuart FL, US | Hard skill mismatch — required skills are mail server/DNS/Exchange/Linux sysadmin work, explicitly "no email copywriting needed." Also already Hires: 1, stale (5 weeks). |
| Brevo to Hubspot Leads Automation | Upwork | Media company, Newton Highlands MA, US | Already Hires: 1, 50+ proposals, stale (2 weeks). Scope is a two-system API sync/automation build, not email-lifecycle content work. |
| B2B CRM Specialist - Brevo | Upwork | Small email/CRM consultancy, Manchester, UK | Hard requirement for 3+ years hands-on email marketing/CRM experience — exceeds the project's own ~2-year experience-filter ceiling (Kaeto's documented tenure is under 1 year, HIBARR only). Already 3 interviewing. |
| Brevo Email Marketing Specialist | Freelancer.com | Recruitment agency buyer | Closed over a year; EUR 2-6/hr rate far below any sustainable freelance rate. |
| Brevo Email Deliverability Warmup Specialist | Freelancer.com | Established buyer (10 reviews), Casselberry FL, US | Closed; $10-30 fixed budget too low for the actual multi-week scope requested, even though the client itself is credible. |
| Brevo and Hubspot Client Engagement Assistant | Freelancer.com | Brand-new buyer (0 reviews), Indonesia | Closed, zero-credibility client, and the scope is a client-engagement/VA role (reply-chasing, CRM bookkeeping, WhatsApp calls), not email-marketing strategy or content work. |

## Screened and rejected on sight (search-result text only, no full scrape)

These were not worth spending a scrape call on — the search snippet alone gave enough to reject
with a clear, specific reason:

- **"Upload completed emails to brevo right now -- 2"** (Freelancer.com, $10-30 fixed) — a
  trivial data-entry task (upload 8 pre-built HTML emails into an existing automation), not
  specialist-level email marketing work, and too low-value to be worth qualifying further.
- **WordPress/WooCommerce Expert for Meta CAPI, Brevo automation** (Freelancer.com) — primarily a
  WordPress/WooCommerce developer role (Meta Pixel/CAPI integration) with Brevo as a secondary
  requirement; a technical web-development skill mismatch, not an email-marketing-specialist fit.
- **Freelance Webdesigner:in mit Copywriting Fähigkeit für E-Mail-Marketing (Klaviyo)**
  (jobgether.com, German-market) — hard-requires Klaviyo, which is PROHIBITED per the claims
  register, and the role itself is web design with an email-copywriting component, not an
  email-marketing-specialist role. Rejected on both grounds without a full scrape.
- **"Brevo Promotional Automation Workflow Build"** (Freelancer.com) — on inspection this reads as
  a freelancer's own bid/portfolio description ("I have over 9 years of experience...") surfaced
  by search, not a live client job posting. Not pursued further; flagged here so a future cycle
  doesn't waste a scrape re-discovering the same ambiguity.

## Source coverage this cycle

- **Upwork**: 5 new listings scraped in full (Brevo-specific searches, per the recurring priority
  on the one platform with strong documented evidence). All but one rejected — see table above.
  The one P1 (Newsletter Specialist for Campaigns / Brevo) is discussed above.
- **PeoplePerHour**: pages 2, 3, and 4 of the category listing page scraped this cycle (continuing
  from cycle 4, which covered only page 1), per this cycle's instruction to rotate through pages
  2-7. 119 results total across the category. No new Brevo- or email-marketing-specific listing
  turned up on these three pages — they're dominated by unrelated gig categories (virtual
  assistant, translation, social media strategy, legal services, etc). Pages 5-7 were not reached
  this cycle; recommend picking up there next time.
- **Freelancer.com**: 6 individual listings checked (3 fully scraped and logged as rejections
  above, 2 screened on sight, 1 ambiguous bid-vs-posting flagged above). All either closed, too
  low-budget for scope, or a role-type mismatch — continues the pattern from cycles 3-4 of
  stale/closed, low-rate Brevo listings on this platform.
- **Contra**: checked via search. Results were dominated by Contra's "hire a freelancer by skill"
  category pages (Klaviyo freelancers, Mailchimp freelancers, etc) rather than individual job
  postings. No new distinct, scorable listing surfaced — same structural limitation as every prior
  cycle (no posted date, applicant count, or client history exposed on Contra's public pages).
- **Reddit r/forhire**: individual threads confirmed blocked for a **fifth consecutive cycle** —
  `firecrawl_scrape` now returns "Firecrawl can't scrape this site because it is currently not
  supported" for reddit.com (the exact wording has shifted slightly cycle to cycle, but the
  practical effect — individual threads unreachable — has not). Search surfaced several
  Brevo/email-marketing hiring post titles, but every one carries an old post ID (2024-2025 era)
  with no way to confirm current status, posted date, or still-open state without opening the
  thread itself, which this session cannot do. This is now firmly a structural platform
  restriction. Recommend the owner decide whether this source is worth continuing to check at all
  going forward, since five consecutive cycles have produced zero scorable Reddit listings.
- **German-market search**: searched directly (not tied to one platform) per the master prompt's
  instruction to leverage Kaeto's working-level German, and specifically re-checked whether this
  would finally force a resolution of the unresolved German-proficiency conflict in the claims
  register. It did not — results were almost entirely freelancer-profile directories (Malt.com,
  freelance.de, freelancermap.de, junico.de), which list freelancers available for hire rather
  than open roles, so nothing scorable there. The one actual live job posting surfaced required
  Klaviyo and was a web-design role (see "screened and rejected on sight" above) — rejected before
  German relevance could even be tested. No live German-market email-marketing-specialist opening
  found this cycle; the conflict remains untested in practice for a fifth cycle running.
- **Direct business prospecting**: out of scope for this workstream per this cycle's instructions
  (same as cycles 3-4) — the project's separate direct-prospecting track
  (`evidence/prospects-medical-wellness.md`, `evidence/direct-prospecting-playbook.md`) was
  deliberately not touched.

## System health

- Sources touched: 6 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit-attempted,
  German-market direct search).
- Opportunities found and logged as full rows: 8 new (0 collisions with the existing 28 on file).
  3 additional candidates were screened and rejected on sight from search-result text without a
  full scrape or DB row — documented above for transparency, not counted toward the 8.
- 1 reached P1 this cycle (score 64/100, discounted — see above); 7 rejected outright at the
  full-scrape stage.
- No automation failures beyond the confirmed Reddit scrape restriction (now 5 cycles running) and
  Contra's continued lack of per-listing verification data (both expected, both documented in the
  DB's `sources` table `last_error`/`terms_notes` fields).

## Recommended next 3 actions

1. **Check the actual hourly rate on the Newsletter Specialist for Campaigns / Brevo listing**
   (requires an Upwork login this session doesn't have) before deciding whether to prepare an
   application package. This is the one lead this cycle worth a second look, but the undisclosed
   rate keeps it from being a clean recommendation as found.
2. **Finish the PeoplePerHour page sweep (pages 5-7)** next cycle — pages 2-4 are now covered and
   turned up nothing new, so the remaining three pages are the last unchecked part of that
   platform's category listing.
3. **Decide whether r/forhire is worth continuing to check** — individual threads have now been
   structurally blocked for firecrawl_scrape across five consecutive cycles with zero scorable
   results. If the owner wants this source covered, it likely needs a different method (manual
   check, a different tool, or an account-based approach) rather than retrying the same scrape a
   sixth time.
