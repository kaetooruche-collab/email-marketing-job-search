# Discovery Cycle 4 — 2026-11-01

Fourth live discovery run. Scope per the recurring discovery mandate: job-board/freelance-opportunity
discovery only (the direct-prospecting workstream in `evidence/prospects-medical-wellness.md` and
`evidence/direct-prospecting-playbook.md` is a separate track and was not touched this cycle).

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key things
carried into scoring this cycle:
- Brevo remains the one platform with strong, consistent documented evidence — prioritized in search.
- Klaviyo, Make.com, Zapier, n8n, and Mailchimp remain PROHIBITED claims — any listing hard-requiring
  these is an automatic reject regardless of other fit. (This cycle's new reject list includes the first
  Mailchimp-hard-requirement case seen in this project — see below.)
- **German proficiency is still an unresolved CONFLICT** in the claims register (DOC-2 claims working-level
  German; the authoritative claim-bank document says Kaeto does not speak German) — **still not resolved as
  of this cycle**, checked specifically per this cycle's instructions. One listing this cycle (PeoplePerHour,
  "Freelance Marketing Campaign Coordinator") listed German as "an advantage, not essential," so the conflict
  did not end up mattering — the listing was rejected on a hard Mailchimp requirement before German became
  relevant either way.
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through: Upwork/PeoplePerHour/
  Freelancer.com escrow rails remain UNVERIFIED-not-VERIFIED for actually landing in a TRNC-accessible
  account; this affects every est_days_to_accessible_payment figure the same way it did in prior cycles.

Checked `db/email_marketing_system.db` first — 19 opportunities already on file from cycles 1-3 (6+ Upwork,
3 PeoplePerHour, 1 Freelancer.com, 1 Contra, plus the earlier cycle-1/2 set), including the Underdog Sales
Brevo deliverability job (`status: submitted`, outside this discovery workstream) and the Brevo Email
Marketing Manager language-app lead (`status: researched`, P1, discounted). Nothing below duplicates an
existing URL.

## Headline

**9 new candidates checked this cycle. 0 reached P0 or P1. 9 rejected outright.** Also re-checked the
cycle-3 discounted P1 lead (Brevo Email Marketing Manager, language-learning app) — it is still open but
the same fill-risk signal persists unchanged, so it stays discounted, not a clean recommendation. **No
clean, currently-open, well-matched opportunity survived qualification this cycle.** This is a genuine
result, not padding — see per-opportunity notes below.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none newly found; one carried-forward lead re-checked, still discounted

### Brevo Email Marketing Manager — Subscription App (Re-engagement & Lifecycle) — Upwork (re-check only, first found cycle 3)
- **URL:** https://www.upwork.com/freelance-jobs/apply/Brevo-Email-Marketing-Manager-Subscription-App-engagement-Lifecycle_~022107889186699907933/
- **Re-check result (2026-11-01):** Still live, but the fill-risk signal from cycle 3 is **unchanged**:
  "Hires: 1," "Interviewing: 4," proposals now shown as "15 to 20," last viewed by client 2 weeks ago.
  Client's logged hours grew from 635 to 667 since cycle 3 (confirms the account is still active, not
  abandoned), and total spend/hires ($13K, 47 hires/25 active) are stable.
- **Conclusion:** No material change from cycle 3's assessment. Still scored 66/100, still discounted on
  probability of winning because of the existing hire + 4 interviewing. **Not recommending an application
  package.** If the owner wants to try anyway, they would need to log into Upwork to confirm the role is
  genuinely still accepting new candidates before any proposal is drafted — this session has not drafted
  one and will not, per the discovery-only mandate.

## Rejected this cycle (9 checked, 9 outright reject — see table)

| Opportunity | Source | Client | Reason rejected |
|---|---|---|---|
| Email Marketing Specialist | Upwork | Unnamed, Canada | Oversaturated (20-50 proposals, 5 interviewing) and stale (client last reviewed applicants 3 weeks ago); no named platform to differentiate on, and the listing's "improve open/click-through rates" ask runs into the claims register's restricted open/click-rate metric. |
| Email Marketing Specialist Needed | Upwork | Unnamed, UK | Brand-new client (account 5 days old, zero spend history) combined with a low $8-15/hr rate and 20-50 competing proposals already — high risk, low compensation, no credibility signal. |
| Ads marketing, digital skills, email marketing | Upwork | Unnamed, India | Stale (client hasn't reviewed applicants in 4 weeks) and scope bundles paid-ads marketing, which the claims register explicitly flags as not demonstrated; brand-new unverified client. |
| Growth Strategist — eCommerce & Digital Marketing Agency | Upwork | RiseUp (UK agency) | Hard skill mismatch — Senior/Expert multi-channel paid-ads/SEO/Shopify growth role, not email-marketing-specific; paid ads, SEO, and Shopify are all on the "none demonstrated, don't claim" list. |
| Freelance Marketing Campaign Coordinator | PeoplePerHour | Maria Nata, UK | Hard skill mismatch — explicitly requires "practical Mailchimp experience," and Mailchimp is PROHIBITED per the claims register (documented platform is Brevo, not Mailchimp). German was only "an advantage, not essential," so the unresolved German conflict never had to be invoked. |
| Bravo email marketing, | PeoplePerHour | Nigel R., UK | Extremely stale — a clarification-board question dated 28 Jun 2025 puts this listing at ~16 months old, far older than anything else treated as live this cycle or last. ~29 proposals already; scope also bundles WordPress/SEO/social beyond the documented Brevo lifecycle/segmentation strength. |
| Email Marketing Expert Needed: Domain Setup & Brevo Configuration | Freelancer.com | Buyer, India | Closed — posted almost 2 years before this cycle. Filled long ago. |
| Brevo Email Sales Strategist Needed | Freelancer.com | Buyer, Canada | Closed (32 proposals, client active as recently as 8 hours before this scrape); budget ($30-250 CAD fixed) also too low for the requested scope even if open, and the A/B-testing deliverable runs into the claims register's unresolved A/B-testing conflict. |
| Brevo Email Automation Expert Needed | Freelancer.com | Buyer, Netherlands | Closed, 138 proposals averaging EUR 16/hr — saturated, unsustainable rate; scope requires WooCommerce/PHP/MySQL technical integration outside the documented strength. Client's own description (3-4 prior freelancers already failed) is an independent red flag. |

## Source coverage this cycle

- **Upwork**: 4 new listings scraped (generic "email marketing specialist" search terms this cycle, per
  cycle 3's instruction to also cover non-Brevo generic terms). All rejected on staleness, oversaturation,
  thin/new client history, or skill-domain mismatch (paid ads/SEO breadth vs. documented email-lifecycle
  depth). Re-scraped the cycle-3 discounted P1 lead — same fill-risk signal persists, client account still
  active.
- **PeoplePerHour**: 2 new listings scraped, including the category listing page itself (which, unlike
  Upwork's, scrapes cleanly and surfaces posted-date/proposal-count for ~20 jobs at once — useful for faster
  triage in future cycles). One (Mailchimp-hard-requirement) is the first listing in this project's history
  rejected specifically on the newly-confirmed Mailchimp prohibition; the other (Bravo email marketing) is
  the most stale listing (~16 months) found in any cycle to date.
- **Freelancer.com**: 3 individual Brevo-specific project pages scraped cleanly (confirming cycle 3's
  finding that individual pages work while category pages don't). All 3 were already "Closed," ranging
  from 1 month to ~2 years old — this is now a consistent pattern across every Freelancer.com Brevo
  listing checked in cycles 3 and 4: open listings are rare, and bidding is heavily saturated at very low
  day rates (roughly EUR 12-30/hr or low fixed amounts) when they are open.
- **Contra**: Checked via search. No new distinct, scorable listing surfaced beyond the one already logged
  and rejected in cycle 3 — Contra continues to expose no posted date, applicant count, or client history
  from its public pages, so nothing new to log here this cycle.
- **Reddit r/forhire**: Still blocked for individual threads — `firecrawl_scrape` returns "we do not
  support this site" for reddit.com, confirmed for a **fourth consecutive cycle**. This is now a firmly
  established structural platform restriction rather than a transient failure; recommend the owner decide
  whether manual checking of this source is worth the time going forward, since this session cannot open
  individual Reddit threads at all.
- **German-market check**: No live job posting requiring German as a hard skill turned up this cycle
  either — the one listing that mentioned German treated it as "an advantage, not essential." The
  unresolved German-proficiency conflict in the claims register remains untested in practice for a fourth
  cycle running.
- **Direct business prospecting**: Out of scope for this workstream per this cycle's instructions — the
  project's separate direct-prospecting track (`evidence/prospects-medical-wellness.md`,
  `evidence/direct-prospecting-playbook.md`) was deliberately not touched.

## System health

- Sources touched: 5 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit-attempted).
- Opportunities found and logged: 9 new (0 collisions with the existing 19 on file); 1 existing P1 lead
  re-checked and its notes updated in place (no new row).
- 0 reached P0 or P1 this cycle; 9 rejected outright; the one carried-forward P1 lead remains discounted,
  not a clean go.
- No automation failures beyond the confirmed Reddit scrape restriction (now 4 cycles running) and
  Contra's continued lack of per-listing verification data (both expected, both documented in the DB's
  `sources` table `last_error`/`terms_notes` fields).

## Recommended next 3 actions

1. **Do not act on the Brevo Email Marketing Manager (language app) lead without confirming it's still
   open** — unchanged from cycle 3's recommendation; the "Hires: 1 / Interviewing: 4" signal is still
   present two cycles later.
2. **Decide whether r/forhire is worth continuing to check** — individual threads have now been
   structurally blocked for firecrawl_scrape across four consecutive cycles. If the owner wants this
   source covered, it likely needs a different method (manual check, a different tool, or an account-based
   approach) rather than retrying the same scrape.
3. **Nothing new to resolve on German proficiency, A/B testing, or payment routing this cycle** — all
   remain as documented in the claims register and `evidence/payment-routing.md`; no live job this cycle
   forced a decision on any of them (the one A/B-testing-adjacent listing found was already closed anyway).
