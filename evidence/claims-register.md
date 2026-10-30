# Central Evidence & Claims Register

## ⚠ GOVERNING SOURCE (2026-10-30): the claim bank supersedes this file where they conflict

A new document, `kaeto-source-material-raw.txt`, was supplied 2026-10-30 — explicitly addressed to "Kaeto or any LLM drafting on his behalf." It's built from **actual re-counted Brevo export data** (33 export files, merged and scripted, not re-typed from memory), with an explicit evidence-grading system (A = re-counted from exports, B = stated by Kaeto with no outcome metric, R = restricted/use only on instruction, X = never use) and hard rules. **This is now the primary source for any public-facing claim.** This file's job going forward is to flag conflicts and track what's resolved, not to be the first place to look.

### Corrections this forced to already-produced material (fixed 2026-10-30)
- `applications/2026-10-29_UnderdogSales_BrevoDeliverability/proposal-draft.md` named HIBARR directly — **fixed**, employer no longer named anywhere in that file (hard rule: never name HIBARR in public-facing material; use "a German-market financial advisory company," or omit the employer entirely as the final chat-approved email does).
- Same file used the exact figures "245 campaigns," "90K+ sends," "bounce rates down 10%." The export re-count does not reproduce these: use **"roughly 230 campaigns," "91,000+ delivered," "under 0.02% spam complaints."** The "10% bounce rate decrease" claim has no A-grade or B-grade support at all in the claim bank — drop it. — **fixed**, the final approved email cites no exact figures.
- **"67% unsubscribe reduction" is not reproduced by the export re-count.** Actual: ~62% drop month-over-month (Jan 0.598% → Aug 0.226%), or ~37% on a quarterly view. Stop using "67%" anywhere, including the portfolio audit I wrote and the evidence table below (not yet corrected in the table itself — treat the table's "67%" row as superseded by this note until the table is rewritten).

### Two unresolved conflicts — need Kaeto's direct confirmation, not my guess
1. **German proficiency.** DOC-2 (Email Marketing CV) claims "German (working level, sufficient to write and QA campaigns)." The claim bank explicitly excludes this: *"KT does not speak German... languages are English and very basic Turkish... Confirm with KT before writing anything stronger [than 'managed email for a German-market audience']."* These flatly contradict each other. **Not usable in either direction until Kaeto says which is true.**
2. **A/B testing.** DOC-2 has a full bullet claiming A/B testing with a 12% CTR result ("Managed end-to-end A/B testing for promotional emails... increased click-through rates by an average of 12%"). The claim bank states: *"A/B testing has not been implemented (ruled 6 October 2026)."* Also contradictory. **Not usable in either direction until resolved.** This matters for the HIBARR CV line and any future proposal that mentions A/B testing.

### New hard rules now in force everywhere (encoded here so they're not lost)
- Never write "pharmacist," "licensed pharmacist," or "as a pharmacist." Use "MPharm graduate," "pharmacy graduate," or "worked in community pharmacy."
- Never name HIBARR in public-facing material (portfolio, Upwork, pitches, LinkedIn). CVs follow Kaeto's per-application instruction; default to generic if unsure.
- Public-facing location wording: **"Kyrenia, Cyprus."** (This doesn't replace the TRNC-specific accuracy needed for the payment-routing research in `payment-routing.md` — that's a different purpose and stays as is.)
- De Montfort University certificate: stays off all CVs/letters.
- n8n and Klaviyo: confirmed excluded (n8n is in the employer's stack but Kaeto doesn't operate it; Klaviyo gap already cost a job application — consistent with what this file already had marked PROHIBITED).
- SQL, GA4, CSS/scripting, Liquid, AMPscript, paid ads, SMS/push, organic social: none demonstrated, don't claim.
- Open and click rates: below benchmark, restricted — never on a CV, never volunteered in a bid.
- Soft bounce rate actually **rose** (2.56% → 3.54%, Jan–Aug 2026) — a real, self-acknowledged weak spot. Restricted: don't volunteer it, but state it plainly if directly asked.
- Job-search filter: opportunities requiring more than ~2 years of experience are outside Kaeto's stated search criteria.
- Chosen first freelance niche, confirmed independently in this document too: health/medical/wellness, specifically because the MPharm + pharmacy background is a genuine differentiator there — consistent with the niche decision already made earlier in this project.

Full raw document: `evidence/kaeto-source-material-raw.txt`.

---


Source of truth for every factual claim used in CVs, proposals, outreach, and the opportunity-matching engine. Every claim below traces to one of the three source documents supplied on 2026-10-30:

- **DOC-1**: `KAETOCHUKWU_EUGENE_ORUCHE_MPharm_Master_CV_Information.pdf`
- **DOC-2**: `Kaeto_Oruche_Email_Marketing_CV.pdf`
- **DOC-3**: `Kaeto_Oruche_Email_Marketing_Systems_Portfolio.pdf` (also published at kaeto-oruche-email-marketing.netlify.app)

**Verification status key** (per master prompt §9.5):
- **VERIFIED** — independently confirmed (dashboard export, screenshot, third-party reference). None of the metrics below currently qualify.
- **PARTIALLY VERIFIED** — self-reported consistently across 2+ of your own documents, internally consistent, no independent corroboration supplied yet.
- **UNVERIFIED** — appears in only one document, or cannot be cross-checked.
- **CONFLICT** — your own documents disagree with each other or with the master prompt and need your confirmation.
- **PROHIBITED** — not usable without more evidence.

No claim below has been checked against a Brevo dashboard export, employer reference, or other third party. Until you supply one of those, everything from HIBARR is PARTIALLY VERIFIED at best, not VERIFIED. I'm not disputing the numbers — I have no independent basis to confirm or contest them — I'm flagging that "self-reported, internally consistent" and "independently verified" are different claims, and only the first is currently true.

---

## 1. Identity & contact

| Field | Value | Source | Status |
|---|---|---|---|
| Name | Kaetochukwu Eugene Oruche (Kaeto Oruche) | DOC-1, DOC-2, DOC-3 | PARTIALLY VERIFIED |
| Email | kaetooruche@gmail.com | DOC-1, DOC-2, DOC-3 | PARTIALLY VERIFIED |
| Phone | +90 533 822 5854 | DOC-1, DOC-2, DOC-3 | PARTIALLY VERIFIED |
| Location | Kyrenia, Northern Cyprus (TRNC) | DOC-1, DOC-2, DOC-3 — **all three agree** | PARTIALLY VERIFIED |
| Location per master prompt §6.2 | "currently based in Türkiye" | Master prompt text | **CONFLICT — see below** |
| Portfolio | kaeto-oruche-email-marketing.netlify.app | DOC-1, DOC-2, DOC-3, user message | PARTIALLY VERIFIED |

**CONFLICT-1 (location) — RESOLVED 2026-10-30, confirmed by owner: Northern Cyprus (TRNC).** All three source documents agreed on this already; the master prompt's "Türkiye" reference was not used. Payment-rail research proceeds on this basis — see `evidence/payment-routing.md`.

## 2. Education

| Claim | Source | Status |
|---|---|---|
| MPharm, Eastern Mediterranean University, graduated 3 July 2024, CGPA 2.65/4.00, final-semester GPA 3.81/4.00 | DOC-1 (detailed); DOC-2 states only "Graduated 2024" with no GPA | PARTIALLY VERIFIED — DOC-2 omits the GPA figures DOC-1 states; not a contradiction, just a different level of detail (resume vs. master record). Fine to use DOC-1's detail. |
| Cert. HE Pharmaceutical Studies, De Montfort University, UK, June 2018 | DOC-1 only | UNVERIFIED (single source) |
| IELTS Academic 8.0 / C1, March 2025 | DOC-1 only | UNVERIFIED (single source, not in DOC-2/DOC-3) |

## 3. HIBARR employment — core metrics (appear consistently across all 3 docs)

| Metric | DOC-1 | DOC-2 | DOC-3 | Status |
|---|---|---|---|---|
| Contacts managed | 85,000+ across 41 segmented lists | 85,000+ (no list count) | 85K+ | PARTIALLY VERIFIED — "41 segmented lists" appears only in DOC-1; not contradicted elsewhere, just not repeated. |
| Campaigns | 245 | 245 | 245 | PARTIALLY VERIFIED |
| Emails delivered | 90,103 | 90,103 | 90,103 | PARTIALLY VERIFIED |
| Spam complaint rate | 0.019% | 0.019% | 0.019% | PARTIALLY VERIFIED |
| Unsubscribe rate reduction | 67% | not stated | 67% | **SUPERSEDED — see top of file.** Export re-count: ~62% (monthly) or ~37% (quarterly). Do not use "67%." |
| Qualified lead conversion increase | 15% | 15% | not restated as headline, consistent with case studies | PARTIALLY VERIFIED |
| Reactivation rate / recovered contacts | 25% reactivation, 5,000 contacts | 25%, 5,000 contacts | implied in Scandinavian case study (481 leads is a *different*, smaller cohort) | PARTIALLY VERIFIED |
| Bounce rate decrease | 10% | 10% | not restated | PARTIALLY VERIFIED |
| CTR increase from A/B testing | 12% | 12% | not restated | PARTIALLY VERIFIED |
| Campaign engagement uplift from segmentation | not stated | **10% uplift** (new claim) | not stated | **UNVERIFIED — appears only in DOC-2.** Don't use this figure until corroborated; it's not contradicted, just unconfirmed outside one document. |
| 216 campaigns forensically audited, 20 reusable frameworks, 6 banking angles, 4 property angles | DOC-1 (briefer) | not mentioned | DOC-3 (detailed case study) | PARTIALLY VERIFIED |
| 750+ UTM-tagged URLs | DOC-1 | not mentioned | DOC-3 (750+, across 30+ agents / 5 platforms) | PARTIALLY VERIFIED |
| 11 lead magnets | DOC-1 | not mentioned | DOC-3 ("11 lead magnets with sequences") | PARTIALLY VERIFIED |
| Scandinavian re-engagement: 481 leads, 3-email sequence over 10 days | DOC-1 (brief) | not mentioned | DOC-3 (full case study) | PARTIALLY VERIFIED |
| 1,000+ LinkedIn followers from thought leadership | DOC-1 only | not mentioned | not mentioned | UNVERIFIED (single source) |

**Employment dates:** HIBARR "January 2026 – Present" (all 3 docs). Today is 2026-10-30, so this is ~10 months of tenure — **this is the actual professional email-marketing experience window: under one year, at one employer.** Any CV or proposal must not imply multi-year "senior" tenure. "Sole owner of email marketing" (DOC-3) and "built from scratch" are consistent across documents and fine to state as self-reported — they describe scope/ownership, not years of experience.

## 4. Tools & platform claims

| Claim | Source | Status |
|---|---|---|
| Brevo (Sendinblue) — hands-on, built infrastructure from scratch | All 3 docs | PARTIALLY VERIFIED — this is the one platform with consistent, detailed, cross-document support. Treat as your strongest documented tool claim. |
| German-language copywriting/QA, "working level" | DOC-2, DOC-3 (German webinar/angle work) | **CONFLICT — see top of file. Claim bank explicitly excludes German proficiency. Do not use until Kaeto confirms which is true.** |
| n8n, API-based automation | **Master prompt owner-profile section only** | **PROHIBITED until evidenced — not in any of the 3 CVs/portfolio.** Do not claim n8n experience in applications. If you've actually used n8n, say so and I'll add it as UNVERIFIED pending detail. |
| Make.com / Zapier | Not in any of the 3 documents | **PROHIBITED** — several live job postings specifically require this (see discovery report); do not claim it. |
| Klaviyo | Not in any of the 3 documents | **PROHIBITED** — several live job postings specifically require this; your documented platform experience is Brevo, not Klaviyo. |
| RemoteNC / True Remote job board, northcyprusremotejobboard.vercel.app | DOC-1 ("True Remote," since June 2026), DOC-2 ("RemoteNC," since June 2026) | PARTIALLY VERIFIED — same project, two slightly different names across documents (True Remote vs. RemoteNC) and same URL/start date. Worth using one consistent name going forward. |

## 5. What this means for applications right now

- Safe to claim without qualification: Brevo platform depth (segmentation, lifecycle states, deliverability/list hygiene, UTM tracking, lead scoring, German-language copy), the 85K+/245/90,103/0.019% headline numbers (consistently self-reported), MPharm degree.
- Use with a qualifier ("in my experience," not as a guaranteed outcome) or omit: the single-document figures (41 lists, 10% engagement uplift, 1,000+ LinkedIn followers, IELTS score) — fine as color, not as headline proof points.
- Do not claim: n8n, Make.com, Zapier, Klaviyo, Mailchimp, HubSpot hands-on experience. These show up as hard requirements on live jobs (see discovery report) — better to disclose the gap honestly than get caught in a work sample.
- Unresolved: Türkiye vs. Northern Cyprus location, which gates which payment rails are even checkable.
