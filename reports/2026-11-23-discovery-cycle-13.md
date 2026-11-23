# Discovery Cycle 13 — 2026-11-23

Regular run following cycle 12 (2026-11-22). Picks up cycle 12's open items and runs fresh
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
  way (13th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  both new candidates scored this cycle.
- Carried forward: a "Brevo" keyword hit is not always the ESP platform, and Brevo mentioned only
  in a bidder's own comment (not the client's stated requirement) does not make a listing a Brevo
  job — applied explicitly to one of this cycle's search hits (see below).

Checked `db/email_marketing_system.db` first — 59 opportunities on file from cycles 1–12. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Two new candidates were found and logged this
cycle (1 Upwork, 1 Freelancer.com) — both **REJECTED**: a Brevo-specific Upwork listing on
compensation grounds ($7.00/hr, already at an advanced interviewing stage) and a Freelancer.com
listing that was already closed/awarded before this cycle's discovery. All of cycle 12's open
items were followed up on exactly as instructed. The two carried-over Upwork leads were both
essentially flat this cycle — the Newsletter Specialist listing (id 31) showed no material change
on any signal, and the Brevo CRM and Email Setup listing's (id 40) Interviewing count, which rose
2→3→4 across cycles 9–11 and stalled at 4 in cycle 12, is **still at 4** this cycle — a second
consecutive cycle with no further movement and no hire appearing. Reddit's free-method scrape
failed for an 8th consecutive cycle; the paid provider question remains open and unused. Not
recommending an application package.

## Cycle 12 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — rechecked once, essentially flat this cycle
Per the owner's standing instruction (flagged already, their call to act on, not something to
repeat again), this was checked once more as a quiet status check, not a re-flag. Current state:
**still open**. Hourly rate **still does not render** in the public scrape — the 8th consecutive
cycle this has failed. There is no clear "Hires" signal and nothing indicates the listing is gone
or closed: Interviewing is unchanged at 2 (same as cycle 12), and the only movement anywhere in
the client's totals is hours ticking from 1,983 to 1,985 — two hours over a full day, ordinary
account-level usage noise, not a signal about this specific job. Last viewed by client: "3 days
ago" (vs "2 days ago" in cycle 12 — also ordinary noise). Every other client total ($68K spent,
36 hires, 16 active) is identical to cycle 12. Per the instruction: since there is no clear
"Hires" signal and nothing indicates the listing is gone or closed, this is **noted on the DB row
and left at that** — not retired and not re-flagged as "needs attention."

### (b) Brevo CRM and Email Setup (id 40) — rechecked closely; it has not moved again
This is the lead the owner asked to watch most closely given its genuine prior movement
(Interviewing climbing 2→3→4 across cycles 9–11), so it got the closest look this cycle. Result:
**it has not moved again**. Still open. Rate unchanged ($10–28/hr). Client still shows 1 hire, 1
active — no new hires. **Interviewing is still at 4**, exactly where it stalled in cycle 12 — this
is now a second consecutive cycle with no further climb beyond 4 and no hire appearing.
Invites-sent/unanswered unchanged at 2/0. Proposals still 20–50. Stated plainly, per instruction:
this reads as **stalled, not progressing further, and not closed/filled** — the same read as
cycle 12, now confirmed over a second cycle rather than a one-off plateau. Tier left at
`PAYMENT_TIMELINE_UNCERTAIN`: nothing here warrants retiring it (no hire, no closure) or
escalating it (the climb has not resumed).

### (c) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page. Failed identically: *"Firecrawl can't scrape this site because it is
currently not supported."* This is the **8th consecutive cycle** this has failed via the free
method. A generic web search separately surfaced a Reddit thread ("Hiring Email Marketing
Specialist for E-commerce Business (Brevo)") whose URL pattern dates it to roughly 2024 — clearly
stale, and since Reddit itself remains unscrapeable this cycle, it could not be independently
verified as live, so it was **not** logged as a DB row. No cost incurred, no new data gained, as
expected. **Still awaiting the owner's decision** on whether the paid `scrapecreators` route is
worth adopting going forward.

### (d) PeoplePerHour page 1 — rechecked, no genuinely new in-scope candidate
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The current-listings section held one genuinely new posting this cycle — "Cold Email Marketing
Specialist" (a Dubai-based accounting/tax consultancy, $131 fixed, 16 proposals, posted 19 hours
before this cycle's discovery) — but it is **out of scope**: the work is B2B cold-outreach lead
generation (sourcing verified decision-maker emails, running ~1,000-email/day campaigns,
personalizing with AI), not Brevo or any documented email-marketing-platform skill, so it was not
logged. The other current-listing item, "Gmail account" (Google Workspace account configuration),
remains out of email-marketing scope, unchanged from prior cycles. "UK Kajabi expert" (id 8),
which had been in the current-listings section as recently as cycle 12, has now aged into the
Past Projects section with no change in scope. "Help with Brevo" (id 46, already rejected as
stale) remains unchanged in Past Projects. **8th cycle running** with no genuinely new, in-scope,
live candidate from this source.

### (e) Direct business prospecting — not run, same reasoning as cycles 8–12
Confirming a gap in this workstream ends in drafting a short, personalized cold-outreach message —
out of scope for this cycle's no-drafting instruction. Not attempted here; remains the separate,
manual, owner-reviewed workstream it has been since cycle 3
(`evidence/prospects-medical-wellness.md`).

### (f) Contra, German-market search, and freelance.de — checked again, kept brief as instructed
All three were checked again this cycle. Contra's featured-jobs page again rendered real job
cards, including the "Email Marketing Specialist – Dual Campaigns for Parents & School Leaders"
listing — but that card is already on file (id 19, $25–40/hr); no genuinely new client
email-marketing posting appeared. That makes **13 consecutive cycles** for Contra with no new
genuine email-marketing lead. The German-market search again surfaced only Brevo's own marketing
pages, Upwork's Brevo hire-page, and freelance.de directory pages — **13 consecutive cycles**
with nothing live. freelance.de itself again surfaced only freelancer profile/directory pages
(individuals advertising Brevo/newsletter skills), no client project posting — **7 consecutive
cycles** confirming no reachable client-posting section for this platform via search. Per
instruction, keeping this brief rather than re-explaining the dead end in full — nothing here
changes the owner's standing option to reconsider these three, which remains theirs to make.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–12 unchanged, see (a)
above)

## New candidates checked this cycle (2)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Brevo Expert for Creative Email Mailings | Upwork | San Miguel de Allende, Mexico (individual, member since 2018) | **REJECTED** — $7.00/hr fails the compensation bar; already at an advanced interviewing stage |
| Upload completed emails to brevo right now -- 2 | Freelancer.com | New York, US (4.9/346 reviews, verified) | **REJECTED** — already closed/awarded before discovery |

### Why each was rejected

- **Brevo Expert for Creative Email Mailings** ($7.00/hr, Mexico-based individual client, member
  since 2018, $1.5K total spent / 12 hires / 8 active): Brevo is the genuine, in-scope platform
  here — no claims-register conflict, unlike several past rejects. The reject is purely on
  compensation and timing: $7.00/hr is well below a viable rate once Upwork's service fee and the
  still-unresolved TRNC payment-routing friction (per `evidence/payment-routing.md`) are factored
  in, and the listing is already advanced — Interviewing: 4, with 4 invites already sent by the
  client out of only 15–20 total proposals — meaning the client is actively moving toward a hire
  on a budget this project's floor does not clear. This is a clean compensation/competition
  reject, not a skill-mismatch one.
- **Upload completed emails to brevo right now -- 2** ($10–30 USD fixed, New York client, 4.9/346
  reviews, verified, member since 2008): a scrape of this new-to-file URL showed it was already
  **closed and awarded** — to another freelancer, for $0 USD — before this cycle's discovery, so
  it was never an actionable opportunity regardless of fit. Logged for audit-trail completeness
  only, per the project's standard of recording independently verified new-to-file URLs even when
  they turn out to be already closed. Separately, even had it still been open, $10–30 for
  uploading 8 completed HTML emails against 25 competing bidders is too thin a scope to pursue as
  a standalone engagement.

Two further search hits were read in full but **not** logged as DB rows, since they were stale and
not independently actionable at discovery: "Automated Email Offer System Setup" (a real-estate
cold-email mail-merge job on Freelancer.com, closed over a year ago; Brevo appeared only in one
bidder's own proposal text, not the client's stated requirement, which named Mailchimp/SendGrid)
and "Email Marketing Campaign Setup" (Freelancer.com project 40554712, closed 5 months ago,
requiring Mailchimp or Klaviyo — both PROHIBITED per the claims register — with no Brevo mention
at all). Both are noted here for completeness only, consistent with how a Facebook-group posting
was handled in cycle 12.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). A fresh
  Brevo-specific search surfaced 1 new-to-file URL (see table above, REJECTED). A direct scrape of
  the general email-marketing category listing (sorted newest-first) surfaced no further new
  candidate — the newest postings in the category were Klaviyo/cold-email/lead-generation/B2B-sales
  roles, none naming Brevo and none a close match once read.
- **Freelancer.com**: Brevo-specific searches surfaced 1 new-to-file URL logged as closed/
  REJECTED (see table above), plus two further stale hits read but not logged (see above). No
  open, live, in-scope Freelancer.com candidate this cycle.
- **PeoplePerHour**: page 1 only, per cycles 6–12's finding — no genuinely new in-scope candidate
  this cycle (see follow-up (d)).
- **Contra**: 13th consecutive cycle with the same underlying limitation — real featured-job cards
  render, but none new and email-marketing-relevant (see follow-up (f)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked; paid provider not used
  this cycle per instruction.
- **German-market search**: re-ran the German-language query — 13th consecutive cycle with no
  live German-market opening found via this search angle.
- **freelance.de**: tried a dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages, no client project listing at all —
  7th consecutive cycle confirming no client project-posting section is reachable for this
  platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–12: same
  Oliver Törnroth/Zoined posting (now 19 days left, down from 20 in cycle 12), still the only open
  listing, still zero live Brevo listings. Polish page 2 not re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycle 12's treatment; prior cycles' finding (job-board aggregator pages and
  Brevo's own healthcare-marketing blog content, no live candidate) assumed unchanged.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning as
  cycles 8–12 (see follow-up (e) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com), plus the Indeed health-
  wellness angle assumed unchanged from prior cycles. Direct business prospecting flagged as
  out-of-scope-this-cycle rather than touched.
- Opportunities found and logged as full rows: 2 new (0 collisions with the existing 59 on file),
  both `REJECTED`. 0 reached P0/P1. Database now holds 61 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) was
  essentially flat on every meaningful signal this cycle (only a 2-hour tick in account-level
  usage); the Brevo CRM and Email Setup listing (id 40), tracked most closely this cycle per the
  owner's instruction, is confirmed **stalled for a second consecutive cycle** at
  Interviewing=4 — no further climb, no hire, not closed. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for an 8th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra, freelance.de, German-market
  search, and Useme.com page 1 each logged another consecutive cycle of the same structural
  limitations already established in prior cycles (13, 13, and 7 consecutive cycles
  respectively), checked again this cycle per instruction but written up briefly as agreed.
- This cycle's clearest lesson: the one genuinely new Brevo-specific listing found this cycle was
  a clean skill match on paper but failed on compensation and timing once read in full — a useful
  reminder that "Brevo named as the platform" clears the first screening bar but not the
  compensation/competition one, and that these two gates need checking independently rather than
  treating a platform match as sufficient on its own.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open.
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded — per the owner's own instruction, it's been flagged enough. It remains
   essentially flat with no listing-level signal on whether it will close.
3. **No action needed on the Brevo CRM and Email Setup listing this cycle** beyond the note
   recorded — its earlier rising-interviewing signal is now confirmed stalled over two
   consecutive cycles (4, then 4 again), not reversed or resolved into a hire. Worth a continued
   close watch in future cycles rather than any fresh flag now, since it remains the one lead on
   file that has shown genuine movement at any point. Separately, the owner's still-open call from
   cycle 11 on whether to keep checking Contra, the German-market search angle, and freelance.de
   each cycle (13, 13, and 7 consecutive cycles with nothing new/live) remains unchanged and
   unforced.
