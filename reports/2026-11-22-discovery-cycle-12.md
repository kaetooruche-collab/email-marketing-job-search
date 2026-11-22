# Discovery Cycle 12 — 2026-11-22

Regular run following cycle 11 (2026-11-21). Picks up cycle 11's open items and runs fresh
discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence.
- Klaviyo, Make.com, Zapier, n8n, Mailchimp, HubSpot, Instantly, Lemlist, Apollo, Expandi, and
  Meta-ads remain PROHIBITED/unevidenced claims; checked the claims register for updates this
  cycle — none found.
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (12th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  the one new Freelancer.com candidate scored this cycle.
- Carried forward: a "Brevo" keyword hit is not always the ESP platform, and the distinction
  between Brevo as a firm requirement vs. one component of a larger technical scope was applied
  explicitly to the one new candidate this cycle (see below).

Checked `db/email_marketing_system.db` first — 58 opportunities on file from cycles 1–11. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** One new candidate was found and logged (1
Freelancer.com) — **REJECTED**: a WordPress/Stripe/Brevo event-registration-automation job that
names Brevo but is fundamentally a web-development and payment-webhook integration task, drawing
419 competing proposals almost entirely from web developers, not email-marketing specialists. All
of cycle 11's open items were followed up on exactly as instructed. The two carried-over Upwork
leads were both essentially flat this cycle — the Newsletter Specialist listing (id 31) showed no
material change on any signal, and the Brevo CRM and Email Setup listing's (id 40) two-cycle
rising Interviewing trend has stalled at 4 with no hire appearing. Reddit's free-method scrape
failed for a 7th consecutive cycle; the paid provider question remains open and unused. Not
recommending an application package.

## Cycle 11 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — rechecked once, fully flat this cycle
Per the owner's standing instruction (flagged already, their call to act on, not something to
repeat again), this was checked once more as a quiet status check, not a re-flag. Current state:
**still open**. Hourly rate **still does not render** in the public scrape — the 7th consecutive
cycle this has failed. Unlike cycle 11 (which showed the first movement in three cycles), this
cycle is **fully flat** against cycle 11: Interviewing unchanged at 2 (no further movement after
cycle 11's 3→2 drop), and every client-total figure identical ($68K spent, 36 hires, 16 active,
1,983 hours — all the same as cycle 11). Last viewed by client: "2 days ago" (vs "yesterday" in
cycle 11 — ordinary noise). This listing still shows no job-specific "Hires" counter, so there is
still no direct signal that it has closed or been filled. Per the instruction: since there is no
clear "Hires" signal and nothing indicates the listing is gone or closed, this is **noted on the
DB row and left at that** — not retired and not re-flagged as "needs attention."

### (b) Brevo CRM and Email Setup (id 40) — rechecked, the rising trend has stalled
Checked for completeness as the second-best lead on file. Still open. Rate unchanged ($10–28/hr).
Client still shows 1 hire, 1 active — no new hires. **Interviewing is flat at 4 this cycle** — the
two-cycle rising trend (2→3→4 across cycles 9–11) has not continued; there is no further climb and
no hire has appeared. Invites-sent/unanswered unchanged at 2/0. Proposals still 20–50. Stated
plainly, per instruction: this reads as **stalled, not progressing further and not closed/filled**
— a meaningfully different signal from cycle 11's "two consecutive cycles of upward movement"
framing, which no longer holds. Tier left at `PAYMENT_TIMELINE_UNCERTAIN`: nothing here warrants
retiring it (no hire, no closure) or escalating it (the climb has stopped).

### (c) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page. Failed identically: *"Firecrawl can't scrape this site because it is
currently not supported."* This is the **7th consecutive cycle** this has failed via the free
method. No cost incurred, no new data gained, as expected. **Still awaiting the owner's decision**
on whether the paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — rechecked, no genuinely new live candidate
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The current-listings section held the same two postings as recent cycles: "Gmail account" (Google
Workspace account configuration — out of email-marketing scope, not logged) and "UK Kajabi expert:
email automations, tagging & lead capture" (already on file, id 8, unchanged scope, now 37
proposals). "Help with Brevo" (already logged and rejected as stale, id 46) reappeared again in
the "Past Projects" section with no material change (still 6 proposals, still "2 months ago").
**7th cycle running** with no genuinely new, live candidate from this source.

### (e) Direct business prospecting — not run, same reasoning as cycles 8–11
Confirming a gap in this workstream ends in drafting a short, personalized cold-outreach message —
out of scope for this cycle's no-drafting instruction. Not attempted here; remains the separate,
manual, owner-reviewed workstream it has been since cycle 3
(`evidence/prospects-medical-wellness.md`).

### (f) Contra, German-market search, and freelance.de — checked again, kept brief as instructed
All three were checked again this cycle. Contra's featured-jobs page did actually render real
job cards this time (e.g. "Marketing Assistant for Launch Campaign," "Social Media Carousel
Designer"), unlike cycle 11's content-free scrape — but none is an email-marketing or Brevo role,
so the underlying finding is unchanged: never a genuine client email-marketing posting across 12
cycles. The German-market search and freelance.de again surfaced only Brevo's own marketing pages
and freelancer profile/directory pages, no client project postings. That makes **12 consecutive
cycles** for Contra and the dedicated German-market search angle, and **6 consecutive cycles** for
freelance.de. Per instruction, keeping this brief rather than re-explaining the dead end in full —
nothing here changes the owner's standing option to reconsider these three, which remains theirs
to make.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–11 unchanged, see (a)
above)

## New candidates checked this cycle (1)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| WordPress Event Registration Integration | Freelancer.com | Toronto, Canada (5.0/1 review, verified) | **REJECTED** — WordPress/Stripe dev integration, not an email-marketing role |

### Why it was rejected

- **WordPress Event Registration Integration** ($30–250 CAD fixed, Toronto, Canada client): names
  Brevo as one of three integrated systems (WordPress registration form → Brevo
  contact lists/automations → Stripe Checkout → payment webhook back into Brevo for paid/unpaid
  list logic → timed reminder and event emails), but the actual deliverable is building/
  configuring a WordPress form, wiring a Stripe payment webhook into Brevo, and end-to-end
  technical testing across both systems — none of which (WordPress development, Stripe API/
  webhook integration) is documented experience per the claims register. All visible competing
  bids, out of 419 total proposals, are from web developers citing WordPress/PHP/Stripe
  portfolios, not email-marketing specialists — confirming the client and the market are treating
  this as a dev-integration job, not an email-marketing role. The budget is also thin once split
  against that level of competition ($30–250 CAD fixed, averaging $139 CAD across 419 bidders).
  The client itself is credible (verified, 5.0/1 review, several other recent postings), so the
  reject is about scope mismatch, not client risk.

A Facebook-group posting titled "FULLY REMOTE POSITION: Email Marketing Specialist (Brevo...)"
also surfaced in a generic search this cycle, but Facebook is not a supported `firecrawl_scrape`
target, so the full listing could not be independently verified — only a search snippet was seen,
showing a rate of $5.65/hr ($1,000/month), which would fail the compensation bar regardless. Per
the project's standard of only logging what has actually been scraped and verified, this was
**not** added as a DB row; noting it here for completeness only.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). A fresh Brevo-
  specific search and a direct scrape of the general email-marketing category listing (sorted
  newest-first) surfaced no new-to-file Brevo-specific candidate — the newest postings in the
  category were cold-email/lead-generation/Klaviyo/Meta-ads/AI-automation roles, none naming Brevo
  and none a close skill match once read.
- **Freelancer.com**: a direct scrape of the email-marketing category listing (pages 1–2) plus
  targeted Brevo searches surfaced 1 new-to-file URL, rejected as a dev-integration task (see
  table above). Page 2 held lead-generation, GoHighLevel, AI-chatbot, and bulk-Gmail-setup
  postings, none a fit. Other hits matched URLs already on file (including a freelancer.in mirror
  of the already-closed id-58 listing) or were freelancer self-promotion pages.
- **PeoplePerHour**: page 1 only, per cycles 6–11's finding — no genuinely new live candidate this
  cycle (see follow-up (d)).
- **Contra**: 12th consecutive cycle with the same underlying limitation, though this cycle's
  direct scrape did render real (non-email-marketing) featured-job cards for the first time in
  several cycles — see follow-up (f).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked; paid provider not used
  this cycle per instruction.
- **German-market search**: re-ran the German-language query — 12th consecutive cycle with no
  live German-market opening found via this search angle.
- **freelance.de**: tried a site-scoped query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages, no client project listing at all —
  6th consecutive cycle confirming no client project-posting section is reachable for this
  platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–11: same
  Oliver Törnroth/Zoined posting (now 20 days left, down from 21 in cycle 11), still the only open
  listing, still zero live Brevo listings. Polish page 2 not re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle;
  folded into the broader generic search pass, which surfaced only job-board aggregator pages and
  Brevo's own healthcare-marketing blog content, consistent with prior cycles' finding.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning as
  cycles 8–11 (see follow-up (e) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com), plus the Indeed health-
  wellness angle folded into the generic search pass. Direct business prospecting flagged as
  out-of-scope-this-cycle rather than touched.
- Opportunities found and logged as full rows: 1 new (0 collisions with the existing 58 on file),
  `REJECTED`. 0 reached P0/P1. Database now holds 59 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) was
  fully flat on every signal this cycle, a step down in activity from cycle 11's small uptick; the
  Brevo CRM and Email Setup listing (id 40) saw its two-cycle Interviewing climb (2→3→4) stall at
  4 with no further movement and no hire. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 7th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra, freelance.de, German-market
  search, and Useme.com page 1 each logged another consecutive cycle of the same structural
  limitations already established in prior cycles (12, 12, and 6 consecutive cycles
  respectively), checked again this cycle per instruction but written up briefly as agreed.
- This cycle's clearest lesson: a listing that named Brevo in its body text (the WordPress/Stripe
  integration job) was still a clean reject once the actual required skill set — and who was
  actually bidding on it — was read in full, reinforcing the "Brevo mention is not sufficient on
  its own" discipline carried forward since cycle 9, now extended from "Brevo as one of several
  optional ESPs" to "Brevo as one piece of a larger technical-integration scope."

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open.
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded — per the owner's own instruction, it's been flagged enough. Worth being aware
   that it went fully flat this cycle after cycle 11's small uptick, with still no listing-level
   signal on whether it will close.
3. **No action needed on the Brevo CRM and Email Setup listing this cycle** beyond the note
   recorded — its two-cycle rising-interviewing signal has stalled, not reversed or resolved into
   a hire. Worth a continued watch in future cycles rather than any fresh flag now. Separately,
   the owner's still-open call from cycle 11 on whether to keep checking Contra, the German-market
   search angle, and freelance.de each cycle (12, 12, and 6 consecutive cycles with nothing live)
   remains unchanged and unforced.
