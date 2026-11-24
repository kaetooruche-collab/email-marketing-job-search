# Discovery Cycle 14 — 2026-11-24

Regular run following cycle 13 (2026-11-23). Picks up cycle 13's open items and runs fresh
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
  way (14th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` would apply to any new
  candidate scored this cycle (only one new candidate reached scoring, and it was rejected on
  scope before payment-routing became relevant).

Checked `db/email_marketing_system.db` first — 61 opportunities on file from cycles 1–13. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** One new candidate was found and logged this
cycle (Freelancer.com) — **REJECTED** on scope and compensation grounds, not a Brevo/email-
marketing-specialist role. All of cycle 13's open items were followed up on exactly as
instructed. The Newsletter Specialist listing (id 31) showed one real signal this cycle — the
client's "active" count ticked down 16→15 — but nothing job-specific confirms this listing itself
closed, so per the owner's standing instruction it is noted, not re-flagged. The Brevo CRM and
Email Setup listing (id 40) is now confirmed stalled at Interviewing=4 for a **third** consecutive
cycle, still no hire. Reddit's free-method scrape failed for a 9th consecutive cycle, now
confirmed blocked at both the subreddit-homepage level and the individual-post level; the paid
provider question remains open and unused. Not recommending an application package.

## Cycle 13 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — one real signal, but not a closure signal
Rechecked once more as a quiet status check, not a re-flag, per the owner's standing instruction.
Current state: **still open**. Hourly rate **still does not render** in the public scrape — the
**9th consecutive cycle** this has failed. Interviewing is unchanged at 2 (same as cycle 13).
Invites sent/unanswered unchanged at 0/0. Last viewed by client: "4 days ago" (vs "3 days ago" in
cycle 13 — ordinary noise). The one thing that did move: the client's **active contract count
dropped from 16 to 15**, while total spend ticked up ($68K→$69K) and hours jumped noticeably
(1,985→2,002). This is a real change in the client's account, but there is no job-specific
"Hires" field on this listing, and nothing else here (proposals, interviewing, invites) indicates
*this* job closed — a long-time, highly active buyer (36 hires, 15 active, 2,002 hours) losing one
active contract while gaining substantial new hours logged is at least as consistent with another
of their many contracts wrapping up as with this one. Per the instruction: since there is no clear
"Hires" signal on this listing and nothing indicates it specifically is gone or closed, this is
**noted on the DB row and left at that** — not retired and not re-flagged as "needs attention."

### (b) Brevo CRM and Email Setup (id 40) — now a third consecutive stalled cycle
Rechecked closely again, per the owner's instruction to watch this one most closely. Result: **it
has still not moved again**. Still open. Rate unchanged ($10–28/hr). Client still shows 1 hire, 1
active — no new hires, no change from cycles 8–13. **Interviewing is still at 4** — this is now the
**third** consecutive cycle at exactly 4 (cycles 12, 13, 14), following the genuine 2→3→4 climb in
cycles 9–11. Invites-sent/unanswered unchanged at 2/0. Stated plainly: this reads as **stalled, not
progressing further, and not closed/filled**, now confirmed over three cycles rather than one or
two. Tier left at `PAYMENT_TIMELINE_UNCERTAIN`: nothing here warrants retiring it (no hire, no
closure) or escalating it (the climb has not resumed).

### (c) Reddit r/forhire — direct scrape attempted again, still blocked at every level, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page itself: failed identically, *"Firecrawl can't scrape this site because
it is currently not supported."* This is the **9th consecutive cycle** this has failed via the
free method. This cycle also went one step further: a generic web search surfaced a specific
r/forhire thread title that read as plausibly current ("\[HIRING\] Help me set up a Brevo email
campaign"), so a direct `firecrawl_scrape` was attempted against that individual post URL rather
than just the subreddit homepage — it failed with the exact same "not supported" error. This
confirms the restriction is platform-wide (Reddit itself), not just the particular listing-page
URL pattern tried in earlier cycles. The post could not be independently verified as live or
stale, so it was **not** logged as a DB row. No cost incurred, no new data gained, as expected.
**Still awaiting the owner's decision** on whether the paid `scrapecreators` route is worth
adopting going forward.

### (d) PeoplePerHour page 1 — rechecked, no genuinely new in-scope candidate
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The current-listings section held the same two out-of-scope items as cycle 13, plus one new
cosmetic variant: "Find 75 Property Owners for Free Listings" ($131, lead generation/outreach for
a UK holiday-house listings business — no email-marketing-platform skill involved, out of scope)
and "Cold Email Marketing Specialist" (the same Dubai B2B tax-consultancy cold-outreach role
already assessed as out of scope in cycle 13, now aged to "2 days ago" with 22 proposals, up from
16) and "Gmail account" (Google Workspace account configuration, unchanged, out of scope). None of
these involve Brevo or any documented email-marketing-platform skill. **9th cycle running** with
no genuinely new, in-scope, live candidate from this source.

### (e) Direct business prospecting — not run, same reasoning as cycles 8–13
Confirming a gap in this workstream ends in drafting a short, personalized cold-outreach message —
out of scope for this cycle's no-drafting instruction. Not attempted here; remains the separate,
manual, owner-reviewed workstream it has been since cycle 3
(`evidence/prospects-medical-wellness.md`).

### (f) Contra, German-market search, and freelance.de — checked again, kept brief as instructed
All three were checked again this cycle. Contra's featured-jobs page again rendered real job
cards, including the same "Email Marketing Specialist – Dual Campaigns for Parents & School
Leaders" card already on file (id 19, $25–40/hr) — no genuinely new client email-marketing posting
appeared. That makes **14 consecutive cycles** for Contra with no new genuine email-marketing
lead. The German-market search this cycle surfaced one new wrinkle worth recording: a third-party
aggregator (`freiguide.de`) mirroring a genuine German Kleinanzeigen.de classified ad titled
"BREVO Newsletter einrichten" (a private individual asking someone to set up a Brevo newsletter
for them). Checking the original Kleinanzeigen.de ad directly showed it is **already removed**
("Die gewünschte Anzeige ist nicht mehr verfügbar" — the requested ad is no longer available), with
no budget, client-credibility, or competition information ever available for it, so it was not
independently actionable and was not logged. That makes **14 consecutive cycles** for the
German-market search with nothing live and actionable (a genuine Brevo-specific German request did
surface for the first time, but was already dead by the time it was checked). freelance.de itself
again surfaced only freelancer profile/directory pages (individuals advertising Brevo/newsletter
skills), no client project posting — **8 consecutive cycles** confirming no reachable client-
posting section for this platform via search. Per instruction, keeping this brief rather than
re-explaining the dead end in full — nothing here changes the owner's standing option to
reconsider these three, which remains theirs to make.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–13 unchanged, see (a)
above)

## New candidates checked this cycle (1 logged, 4 noted but not logged)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Virtual Assistant: Phones & Newsletters | Freelancer.com | Matawan, US (new member, no reviews) | **REJECTED** — general admin/VA role, Brevo newsletter prep is one incidental duty among unrelated tasks, not an email-marketing-specialist role; also below a viable rate |

### Why it was rejected

- **Virtual Assistant: Phones & Newsletters** ($8–15/hr, posted 3 days before discovery, 29
  proposals, brand-new client account with no reviews): the job genuinely mentions Brevo
  ("prepare Brevo newsletters") but it is one line item inside a general front-desk/admin role —
  answering phones, responding to general business questions, scheduling interviews, keeping
  applicant records, updating spreadsheets, and handling "Apps Base 44" back-office work. This is
  not an email-marketing specialist engagement; Brevo newsletter prep reads as a minor recurring
  task bolted onto a receptionist/VA role, not the core scope. Separately, $8–15/hr is well below
  a viable rate once TRNC payment-routing friction (per `evidence/payment-routing.md`) and
  platform fees are factored in, and 29 competing proposals (mostly experienced general VAs
  bidding $8–12/hr) confirms this is being bid as a commodity admin role, not a specialist one.
  Clean scope-mismatch and compensation reject, not a close call.

### Hits read but not logged this cycle (stale or not independently actionable)

Four further items were read in full but **not** logged as DB rows, consistent with the project's
standard of only logging independently verified, live-and-actionable new-to-file URLs (or, per
cycle 13's precedent, recently-closed ones found via a deliberate Brevo-specific search):

- **"Email Marketing Expert Needed: Domain Setup & Brevo Configuration"** (Freelancer.com,
  project 38898157) — a genuine, client-stated Brevo requirement (domain setup, SPF/DKIM/DMARC,
  warm-up, Brevo configuration), but **closed almost 2 years ago**. Too old to carry any audit-
  trail value as a "near miss this cycle"; noted here only.
- **A specific r/forhire thread** ("\[HIRING\] Help me set up a Brevo email campaign") — found via
  generic web search, but Reddit itself remains fully unscrapeable (see follow-up (c)), so it
  could not be read, dated, or verified as live. Not logged.
- **"BREVO Newsletter einrichten"** (a German Kleinanzeigen.de classified, mirrored on
  `freiguide.de`) — see follow-up (f). Confirmed already removed from the source site; no budget
  or client information was ever available. Not logged.
- **"WordPress Developer Needed Replace Zapier with Brevo API"** (Freelancer.com, already
  awarded/closed before discovery) — genuinely out of scope regardless of status: this is backend
  developer work (PHP, WordPress, Stripe webhooks, token-based download systems), and the client's
  own posting explicitly says *"Please don't apply if you have only worked with Brevo email
  campaigns"* — i.e., it explicitly excludes the kind of Brevo experience on file. Not logged.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-
  specific and generic searches surfaced no new-to-file URLs this cycle — every Upwork result
  returned (Email Marketing Manager, Manage email campaigns, CRM and Mail Marketing Manager,
  Brevo Sendinblue Email Designer, B2B Cold Email & Lead Generation Specialist) was already on
  file from a prior cycle.
- **Freelancer.com**: Brevo-specific and generic searches surfaced 1 new-to-file URL logged as
  REJECTED (see table above), plus three further hits read but not logged as stale/out-of-scope
  (see above). No open, live, in-scope Freelancer.com candidate this cycle.
- **PeoplePerHour**: page 1 only, per cycles 6–13's finding — no genuinely new in-scope candidate
  this cycle (see follow-up (d)).
- **Contra**: 14th consecutive cycle with the same underlying limitation — real featured-job cards
  render, but none new and email-marketing-relevant (see follow-up (f)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked at both the subreddit and
  individual-post level; paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query and a follow-up on a specific hit —
  14th consecutive cycle with no live, actionable German-market opening (a genuine Brevo-specific
  German classified surfaced for the first time, but was already removed by the time it was
  checked — see follow-up (f)).
- **freelance.de**: tried a dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages, no client project listing at all —
  8th consecutive cycle confirming no client project-posting section is reachable for this
  platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–13: same
  Oliver Törnroth/Zoined posting (now 18 days left, down from 19 in cycle 13), still the only open
  listing, still zero live Brevo listings. Polish page 2 not re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycle 13's treatment; prior cycles' finding (job-board aggregator pages and
  Brevo's own healthcare-marketing blog content, no live candidate) assumed unchanged.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning as
  cycles 8–13 (see follow-up (e) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search [including a follow-up check on freiguide.de/
  Kleinanzeigen.de], freelance.de, Useme.com), plus the Indeed health-wellness angle assumed
  unchanged from prior cycles. Direct business prospecting flagged as out-of-scope-this-cycle
  rather than touched.
- Opportunities found and logged as full rows: 1 new (0 collisions with the existing 61 on file),
  `REJECTED`. 0 reached P0/P1. Database now holds 62 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) saw
  one real but ambiguous account-level signal (active contracts 16→15) with nothing job-specific
  to confirm closure, so it was noted and not re-flagged, per instruction. The Brevo CRM and Email
  Setup listing (id 40), tracked most closely this cycle per the owner's instruction, is now
  confirmed **stalled for a third consecutive cycle** at Interviewing=4 — no further climb, no
  hire, not closed. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 9th consecutive cycle, now confirmed at both the subreddit-page
  and individual-post level; the paid-provider question from cycle 7 remains open and unanswered,
  so it wasn't used again. Contra (14th), the German-market search (14th), and freelance.de (8th)
  each logged another consecutive cycle of the same structural limitations already established in
  prior cycles, checked again this cycle per instruction but written up briefly as agreed.
- This cycle's clearest lesson: a listing that merely *mentions* Brevo is not automatically in
  scope — the Virtual Assistant role this cycle named Brevo explicitly but buried it inside an
  unrelated general-admin job description, and the WordPress/Zapier-replacement role named Brevo
  explicitly while *requiring developer skills the project has never claimed and explicitly
  excluding the email-campaign skill set that is actually on file*. Both reinforce the same
  standing rule from cycle 13 (a platform match clears only the first screening bar) in a new
  direction: the platform match itself can be incidental to work that is not email-marketing
  specialist work at all.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open, now
   with slightly stronger evidence behind it (this cycle confirmed the block applies to individual
   post URLs too, not just listing pages, so a specific-sounding Reddit hit surfaced by web search
   still cannot be independently verified without it).
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded — per the owner's own instruction, it's been flagged enough. The account-level
   active-contracts dip (16→15) is worth having on record, but nothing here is a job-specific
   closure signal.
3. **No action needed on the Brevo CRM and Email Setup listing this cycle** beyond the note
   recorded — its earlier rising-interviewing signal is now confirmed stalled over three
   consecutive cycles (4, 4, 4), not reversed or resolved into a hire. Worth a continued close
   watch in future cycles rather than any fresh flag now, since it remains the one lead on file
   that has shown genuine movement at any point. Separately, the owner's still-open call from
   cycle 11 on whether to keep checking Contra, the German-market search angle, and freelance.de
   each cycle (14, 14, and 8 consecutive cycles with nothing new/live and actionable) remains
   unchanged and unforced.
