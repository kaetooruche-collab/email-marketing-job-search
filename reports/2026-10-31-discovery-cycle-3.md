# Discovery Cycle 3 — 2026-10-31

Third live discovery run. Scope per the recurring discovery mandate: job-board/freelance-opportunity
discovery only (the direct-prospecting workstream in `evidence/prospects-medical-wellness.md` and
`evidence/direct-prospecting-playbook.md` is a separate track and was not touched this cycle).

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key things
carried into scoring this cycle:
- Brevo remains the one platform with strong, consistent documented evidence — prioritized in search.
- Klaviyo, Make.com, Zapier, n8n remain PROHIBITED claims — any listing hard-requiring these is an
  automatic reject regardless of other fit.
- **German proficiency is still an unresolved CONFLICT** in the claims register (DOC-2 claims working-level
  German; the authoritative claim-bank document says Kaeto does not speak German) — not resolved as of this
  cycle, so still not usable in either direction. This did not end up mattering: no live job posting
  requiring German turned up this cycle (see below).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through: Upwork/PeoplePerHour/
  Freelancer.com escrow rails remain UNVERIFIED-not-VERIFIED for actually landing in a TRNC-accessible
  account; this affects every est_days_to_accessible_payment figure below the same way it did in prior
  cycles (estimate assumes the platform's stated hold period, not confirmed TRNC withdrawal).

Checked `db/email_marketing_system.db` first — 9 opportunities already on file from cycles 1-2 (6 Upwork,
3 PeoplePerHour), including the Underdog Sales Brevo deliverability job, which the DB now shows as
`status: submitted` — i.e. the owner evidently proceeded with that one outside this discovery workstream.
Nothing below duplicates an existing URL.

## Headline

**10 new candidates checked this cycle. 1 reached P1 but only as a discounted lead with a real
fill-risk signal — not a clean go. 9 rejected outright. 0 P0. No clean, currently-open, well-matched
opportunity survived qualification.** This is a genuine result, not padding — see per-opportunity notes.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — 1 found, discounted (not recommended without confirmation)

### Brevo Email Marketing Manager — Subscription App (Re-engagement & Lifecycle) — Upwork
- **URL:** https://www.upwork.com/freelance-jobs/apply/Brevo-Email-Marketing-Manager-Subscription-App-engagement-Lifecycle_~022107889186699907933/
- **Client:** Consumer language-learning app, USA (Orange, CA). Member since Apr 2026, $13K total
  spent, 47 hires (25 active), 635 hours logged — highly credible, active buyer.
- **Scope:** Own the lifecycle/retention email program — onboarding, re-engagement, win-back, lapsed-user,
  renewal-reminder automations; segment by lifecycle stage; feature/update campaigns; report on
  open/click/conversion/churn. Contract-to-hire.
- **Skill match: strong.** This is close to a direct match for the documented HIBARR scope (lifecycle
  states, segmentation, churn/reactivation reporting).
- **Budget:** Hourly, $5.00–$10.00/hr, listed as "Expert" level — unusually low for the stated
  experience bar.
- **Score: 66/100.** Scored high on skill match (13/15), payment certainty (13/15, Upwork + very
  credible client) and client credibility (9/10), but **heavily discounted on probability of winning
  (5/20)**: the listing's own activity panel already shows "Hires: 1" and "Interviewing: 4" — a strong
  signal the client is already deep in selection or has already filled the role, the same pattern that
  got the Underdog Sales lead discounted in cycle 1. Compensation also scored low (4/10) given the rate.
- **Payment timeline estimate:** ~14 days to accessible funds (Upwork hourly weekly billing + standard
  security hold) — fits P1.
- **Action:** Not recommending an application package yet. If the owner wants to try anyway, they'd need
  to log into Upwork to confirm the role is genuinely still open before any proposal is drafted — this
  session has not drafted one and will not, per the discovery-only mandate.

## Rejected this cycle (10 checked, 9 outright reject — see table)

| Opportunity | Source | Client | Reason rejected |
|---|---|---|---|
| Brevo CRM, Email Marketing & Lead Automation Setup for Travel Company | Upwork | South African travel co. | Hard skill mismatch — client explicitly excludes "newsletter-only" Brevo experience, wants CRM pipeline architecture + Meta/LinkedIn ad integration + WordPress dev, none evidenced. Also 20-50 proposals, 18 interviewing, 1 hire already, thin client history ($150 spent). |
| Brevo Setup and Training | Upwork | Unnamed, Canada | Oversaturated — 20-50 proposals already for a small, simple setup/training task. |
| Fix Brevo Account So Can Send Transactional Emails | Upwork | Unnamed, USA | Stale (17 days old, last viewed 2 weeks ago), already "Hires: 1", and $10 budget fails the compensation test regardless. |
| Brevo Email Designer Needed — Quick Email Polish | Upwork | Not scraped | $10 fixed budget fails the compensation test outright — same pattern as a job rejected on this basis in cycle 1. |
| Mailchimp to Brevo Migration | Upwork | Not scraped | Stale — posted 23+ days before this cycle, no sign of recent activity. |
| Email Automation Specialist (Brevo) | PeoplePerHour | Nigeria (buyer profile shown) | No verifiable posted date; job-ID numbering implies it significantly predates the Aug-Oct 2026 listings confirmed fresh this cycle and last — treated as likely stale rather than assumed live on a modest 10-proposal count. |
| Email marketing flows in Brevo for BigCommerce website | PeoplePerHour | UK | Very stale (~82+ days, open clarification question since mid-August unresolved), 42 proposals, and scope is a platform-specific technical integration (BigCommerce↔Brevo) rather than lifecycle/segmentation work. |
| Brevo Email Marketing for Newsletters | Freelancer.com | New publication, unnamed | Already awarded and **"In Progress"** — posted 4 months ago, 141 proposals. Filled. |
| Email Marketing Specialist – Dual Campaigns for Parents & School Leaders | Contra | Unnamed | Unverifiable — Contra's public featured-jobs page exposes no posted date, applicant count, or client history, and no distinct per-job URL. Logged for completeness, not scored. |

## Source coverage this cycle

- **Upwork**: 6 new listings scraped (Brevo-focused search + direct scrape of job detail pages). Good
  data quality — proposal counts, "Hires" signal, and client spend history all visible without login.
- **PeoplePerHour**: 2 new listings scraped (beyond the page-1 pass from cycle 2); one lacked a reliable
  posted date, handled conservatively per the "don't round up" instruction.
- **Freelancer.com**: **Gap partially resolved.** Category/listing pages are still too large to scrape
  whole (confirmed again), but an **individual project page scraped cleanly** with `firecrawl_scrape` and
  gave full status/proposal-count/posted-date detail. Future cycles should search → then scrape individual
  project URLs directly, not the category page.
- **Contra**: Checked. The public featured-jobs landing page surfaced one real-looking email marketing
  title+rate but exposes no posted date, applicant count, or client credibility signal, and gave no
  distinct per-job URL — structurally unverifiable without a logged-in account. Logged, not scored.
- **Reddit r/forhire**: Still blocked for individual threads — `firecrawl_scrape` returns "we do not
  support this site" for reddit.com, confirmed for a third consecutive cycle (this is a structural
  platform restriction, not a one-off failure). Two "[Hiring]" titles surfaced via search snippet only:
  a small Brevo-campaign-setup walkthrough request, and the same UK Brevo/FreeAgent automation lead
  flagged as unconfirmed in cycles 1 and 2 (still unconfirmed — recommend the owner check manually if
  interested, same as before).
- **German-market search**: Ran `"deutschsprachig email marketing freelancer gesucht Brevo Newsletter"`.
  Surfaced only agency service pages (e.g. a German Brevo-implementation agency's own marketing page) and
  marketplace noise (Fiverr) — no live job posting requiring German turned up, so the unresolved
  German-proficiency conflict in the claims register was not triggered either way this cycle.
- **Direct business prospecting**: Out of scope for this workstream per this cycle's instructions — the
  project's separate direct-prospecting track (`evidence/prospects-medical-wellness.md`,
  `evidence/direct-prospecting-playbook.md`) was deliberately not touched.

## System health

- Sources touched: 5 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit-attempted).
- Opportunities found and logged: 10 (all new, 0 collisions with existing 9 on file).
- 1 reached P1 (discounted, not recommended), 9 rejected outright, 0 reached a clean P0.
- No automation failures beyond the confirmed Reddit scrape restriction and Contra's lack of
  per-listing verification data (both expected, both documented in the DB's `sources` table
  `last_error`/`terms_notes` fields).

## Recommended next 3 actions

1. **Do not act on the Brevo Email Marketing Manager (language app) lead without confirming it's still
   open** — the "Hires: 1 / Interviewing: 4" signal makes this a real fill-risk, not a clean P1.
2. **Decide whether to keep manually checking the two unconfirmed Reddit r/forhire leads** (Brevo
   campaign-setup walkthrough; UK Brevo/FreeAgent automation) — this session cannot open individual
   Reddit threads and that restriction has now held for three consecutive cycles.
3. **Nothing new to resolve on German proficiency or payment routing this cycle** — both remain as
   documented in the claims register and `evidence/payment-routing.md`; no live job this cycle turned on
   either one.
