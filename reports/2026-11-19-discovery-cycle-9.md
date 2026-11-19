# Discovery Cycle 9 — 2026-11-19

Regular run following cycle 8 (2026-11-18). This cycle picks up cycle 8's three open items and
runs fresh discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence.
- Klaviyo, Make.com, Zapier, n8n, Mailchimp, HubSpot, Instantly, Lemlist, and Apollo remain
  PROHIBITED/unevidenced claims; checked the claims register for updates this cycle — none found.
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (ninth cycle running).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com opportunity scored this cycle.

Checked `db/email_marketing_system.db` first — 42 opportunities on file from cycles 1-8. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Three new candidates were found, all on
Freelancer.com, and all were already closed at discovery (1–2+ years stale) — none clear the
payment-horizon test, so all three are logged as `REJECTED` for audit-trail completeness only.
All three of cycle 8's open items were followed up on exactly as instructed, with nothing
materially new on any of them. Not recommending an application package.

## Cycle 8 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo — rechecked once, nothing materially new
Per the owner's standing instruction (flagged twice already — their call to act on, not something
to repeat a third time), this was checked once more as a quiet status check, not a re-flag.
Current state: **still open** (not closed, not hired, not gone). Hourly rate **still does not
render** in the public scrape (4th consecutive cycle). Interviewing is still **3** — flat for a
2nd consecutive cycle, confirming the activity picture has genuinely stalled since cycle 7's
0→3 jump. Proposals still 20–50. Last viewed by client: "2 days ago" (vs "yesterday" in cycle 8 —
ordinary day-to-day noise, not a signal either way). Client totals are flat: $68K total spent
(same), 35 hires (same), 16 active (same), 1,980 hours logged (up slightly from 1,976 — routine
platform usage, not a signal). **Nothing here clears the bar the owner set for a repeat flag.**
Noted on the DB row (id 31) and left at that; not re-scored, not re-flagged as "needs attention"
in this summary.

### (b) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page. Failed identically: *"Firecrawl can't scrape this site because it is
currently not supported."* Same result as 8 of the last 9 cycles. A web search separately
surfaced one old r/forhire thread (a Brevo e-commerce email-marketing listing) through its search
index, but the thread URL itself could not be scraped for the same reason, so no verifiable
posted-date, status, or client detail could be obtained — not logged as an opportunity; treating
an un-scrapable search snippet as a scorable candidate would risk exactly the kind of rounding-up
this project is instructed to avoid. No cost incurred, no new data gained, as expected. **Still
awaiting the owner's decision** on whether the paid `scrapecreators` route is worth adopting going
forward.

### (c) PeoplePerHour page 1 — rechecked, no new candidate
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The category now shows 115 results (vs 135 in cycle 8) with a different relevance-sorted mix of
listings day to day, but **no new Brevo/email-marketing freelance candidate** appeared. The
"Marketing & Publishing Assistant Sales-Minded" listing (already on file, id 9) reappeared on
page 1 — confirmed duplicate, no action needed. 4th cycle running with no new candidate from this
source.

### (d) Direct business prospecting — not run, same reasoning as cycle 8
Per the master prompt §4.3/§12 workstream's own method, confirming a gap ends in drafting a
short, personalized cold-outreach message — out of scope for this cycle's no-drafting
instruction. Not attempted here; remains the separate, manual, owner-reviewed workstream it has
been since cycle 3 (`evidence/prospects-medical-wellness.md`).

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–8 unchanged, see (a) above)

## New candidates checked this cycle (3)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Brevo Advanced Automation Expert | Freelancer.com | US (Jupiter), member since 2015, 0 reviews | **REJECTED** — closed ~2 years before discovery |
| Email Marketing Specialist (Softgile) | Freelancer.com | Ukraine, member since Jun 2025, 0 reviews | **REJECTED** — closed ~1 year before discovery; also fails scope (3+ yrs required, Mailchimp hands-on) |
| Email Designer Needed | Freelancer.com | UAE (Abu Dhabi), 5.0/4 reviews | **REJECTED** — closed ~2 years before discovery; "Brevo" is the client's own brand name, not the platform |

### Why all three were rejected
All three surfaced from a fresh Brevo-specific Freelancer.com search this cycle and were URLs not
previously on file, so each is logged for the audit trail, same treatment as the closed
Freelancer.com and Useme.com listings logged in cycles 7–8.

- **Brevo Advanced Automation Expert** ($30–250 USD fixed): a genuine Brevo scope (API-trigger
  routing / contact-attribute mapping for a patient-doctor matching automation) that would
  otherwise have been a reasonable skill match, but posted about 2 years ago, 24 proposals
  already on record, long closed. Fails the payment-horizon test outright.
- **Email Marketing Specialist (Softgile)** ($15–25/hr): closed about 1 year ago, 26 proposals
  already on record. Would have failed on scope even if open — the stated requirement of 3+
  years of experience exceeds this project's ~2-year job-search filter (per the claims register),
  and Mailchimp is named as a required tool alongside Brevo; Mailchimp hands-on experience is an
  explicitly PROHIBITED unevidenced claim. A multi-reason reject, not a close call.
- **Email Designer Needed** ($10–30 USD fixed): closed about 2 years ago, 22 proposals already on
  record — but the more interesting finding is that "Brevo" in this listing is the **client's own
  product/brand name** being promoted in promotional emails, not a request for skill with the
  Brevo ESP platform. Several bidders' own proposals read it the same way. This is a genuine
  keyword false-positive, worth remembering when scoring future "Brevo"-keyword hits on any
  source: not every hit for the word is a platform-skill match, and this project should keep
  reading the actual job text before counting a "Brevo" keyword hit as a scope match.

## Source coverage this cycle

- **Upwork**: re-scraped the carried-over P1 listing (see follow-up (a)) and the
  `PAYMENT_TIMELINE_UNCERTAIN` "Brevo CRM and Email Setup" lead from cycle 8 (still open, client
  still 1 hire/1 active, interviewing steady at 2 — essentially unchanged, tier not revised, not
  required by this cycle's instructions but checked for completeness as the second-best lead on
  file). Fresh Brevo-specific and generic searches surfaced no URL not already on file.
- **Freelancer.com**: fresh Brevo-specific search surfaced 3 new-to-file URLs, all closed (see
  table above).
- **PeoplePerHour**: page 1 only, per cycles 6–8's finding — confirmed no new candidate again.
- **Contra**: 9th consecutive cycle with the same structural limitation — search surfaces only
  `/hire/brevo-freelancers`, `/hire/email-marketers`-style directory pages and freelancer
  self-promotion/"how to start a freelance career" blog content, never a genuine client job
  posting.
- **Reddit r/forhire**: see follow-up (b) — direct scrape still blocked; paid provider not used
  this cycle per instruction.
- **German-market search**: re-ran the German-language query — ninth consecutive cycle with no
  live German-market opening found; results remain tutorials, platform blog content, and
  review/comparison sites.
- **freelance.de**: tried a site-scoped query aimed specifically at finding a genuine client
  project/Auftrag posting mentioning Brevo or newsletter work. Surfaced only one irrelevant
  freelance.de blog post (customer-retention marketing advice — not a job listing at all). 3rd
  consecutive cycle confirming no client project-posting section is reachable for this platform
  via search; likely not worth a further dedicated pass without a different access method.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–8: same
  Oliver Törnroth/Zoined posting (now 23 days left, down from 24 in cycle 8 and 25 in cycle 7),
  still the only open listing, still zero live Brevo listings. Polish page 2 not re-checked this
  cycle (checked in cycle 8; one closed Brevo listing already logged there).
- **Indeed / health-wellness + Brevo search angle**: re-ran this combined search. Surfaced the
  same tutorial/comparison content as cycle 7, plus one Facebook group post (a "Brevo/Sendinblue
  — project-based, no experience required" listing). Facebook, like Reddit, returns "Firecrawl
  can't scrape this site because it is currently not supported" on direct scrape, so no
  verifiable client, budget, or posted-date detail could be obtained; not logged as an
  opportunity. No new candidate from this angle.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning
  as cycle 8 (see follow-up (d) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com), plus a re-run of the Indeed
  health-wellness search angle. Direct business prospecting flagged as out-of-scope-this-cycle
  rather than touched.
- Opportunities found and logged as full rows: 3 new (0 collisions with the existing 42 on file),
  all `REJECTED` (closed before discovery). 0 reached P0/P1.
- The two carried-over leads (the P1 Newsletter Specialist listing and the
  `PAYMENT_TIMELINE_UNCERTAIN` Brevo CRM and Email Setup listing) were both re-checked and remain
  unchanged in tier and score; per the owner's standing instruction, the former is not re-flagged
  as needing attention this cycle.
- No automation failures. Reddit's and Facebook's scrape restrictions both held on the free
  method (9 and 1 cycles respectively); the paid-provider question from cycle 7 remains open and
  unanswered, so it wasn't used again. Contra, freelance.de, German-market search, and Useme.com
  page 1 each logged another consecutive cycle of the same structural limitations already
  established in prior cycles.
- One search-quality finding worth carrying forward: a "Brevo" keyword hit is not always a
  Brevo-platform skill match — one listing this cycle used "Brevo" as the client's own
  product/brand name. Future cycles should keep reading the actual job text, not just the
  keyword match, before counting a hit as in-scope.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider (small real cost per call, one demonstrated working access path, zero relevant
   posts found the one time it was tried). Not re-raised as urgent — just restating that this
   decision is still open and nothing has changed about it.
2. **No action needed on the Newsletter Specialist listing this cycle** — per the owner's own
   instruction, it's been flagged enough; the state is unchanged (still open, rate still
   unconfirmed, interviewing flat) and this project will keep noting it quietly rather than
   re-escalating it.
3. **Decide whether direct business prospecting should be folded into this automated cycle** —
   unchanged from cycle 8's note: it currently can't produce a scorable result without drafting
   outreach, which is outside this cycle's standing instructions; if the owner wants it covered
   automatically, that needs an explicit scope call, not an interpretation on this project's part.
