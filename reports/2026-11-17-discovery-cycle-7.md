# Discovery Cycle 7 — 2026-11-17

Regular run following cycle 6 (2026-11-16). This cycle picks up cycle 6's three open items and
runs fresh discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence.
- Klaviyo, Make.com, Zapier, n8n, and Mailchimp remain PROHIBITED claims; HubSpot hands-on
  experience is also PROHIBITED. Both came up again this cycle (Dr. Berg Nutritionals/Klaviyo
  below).
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (seventh cycle running).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com opportunity.

Checked `db/email_marketing_system.db` first — 38 opportunities on file from cycles 1-6. Nothing
below duplicates an existing URL except where explicitly noted as the same listing re-checked.

## Headline

**No new P0 or P1 opportunities this cycle. 1 new URL found and logged (already closed before
discovery, so effectively 0 live new candidates). All three of cycle 6's open items were followed
up on.** The most consequential finding this cycle is methodological, not a new job: the Reddit
r/forhire access-method problem that blocked 6 straight cycles is now solved (see (c) below),
even though it produced zero matching posts this time. Not recommending an application package.

## Cycle 6 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo — rate still unconfirmed, but activity changed
Re-scraped the listing
(https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/)
one more time. **The hourly rate still does not render** — second consecutive cycle confirming
this. Per the owner's standing instruction, **this is the last routine re-scrape of this listing**;
going forward it will just be noted as "unchanged, rate still unconfirmed, needs a human with
Upwork login" unless something actually changes.

Something *did* change this time, though, so it's worth recording rather than filing as a pure
non-event: **"Interviewing" went from 0 to 3**, "last viewed by client" moved from "4 days ago" to
"yesterday," and the client's totals ticked up ($68K spent vs $65K, 35 hires vs 34, 16 active vs
15; proposals still 20-50, hours still 1,973). This reads as the client actively moving toward a
hire. It doesn't change the score or tier (the rate is still the fact that would make or break
this, and it's still invisible), but if anything it narrows the window rather than widening it —
worth flagging plainly rather than quietly re-confirming "unchanged" when the activity picture
moved. Appended to the DB row (id 31) rather than re-scored.

### (b) PeoplePerHour page 1 — rechecked, no new listings
Per cycle 6's finding that the `?page=` parameter only paginates the closed archive, only page 1
was re-checked this cycle (no pages 2-7 sweep). **Identical to cycle 6**: exactly 2 open listings —
a $10 "Gmail account" Google Workspace admin task (not email marketing) and the already-logged UK
Kajabi listing (duplicate). No new candidate. This confirms re-checking page 1 going forward is
sufficient.

### (c) Reddit r/forhire — a working access method found, but no matching posts this time
Tried once more, as instructed, using a method not yet tried: instead of `firecrawl_scrape`
against reddit.com (blocked for 6 consecutive cycles with "currently not supported"), this cycle
used the **`scrapecreators` `reddit/subreddit-posts` structured-data provider via Alexandria**
(`alexandria_library_read`). **This worked** — it returned 25 real, current r/forhire posts with
full post data (title, author, body text, timestamps, comment counts), something no prior cycle
achieved. This changes the framing from "structurally unscrapable" to "accessible via a different
tool, at a small per-call cost." However, **none of the 25 most recent posts (roughly the
subreddit's last 13 hours of activity) mentioned email marketing, Brevo, or newsletters** — so
this attempt produced a working method but zero scorable candidates. New total: 7 cycles with zero
scorable Reddit results, but for the first time, with a demonstrated way to actually read the
subreddit. Recommend the owner decide whether to adopt `scrapecreators` as the standing method for
this source (unlike the free failed scrapes, each call here has a real, small Firecrawl-credit
cost) now that a path exists, versus still dropping the source for cost/value reasons.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (unchanged carryover, see (a) above)

## New candidates checked this cycle (1 — closed before discovery)

| Opportunity | Source | Client | Reason rejected |
|---|---|---|---|
| Brevo Promotional Automation Workflow Build | Freelancer.com | Individual, Madrid, Spain (0 reviews) | Already closed and awarded to another freelancer (for €0) roughly 2 months before this cycle's discovery, with 40 competing bids on record. Fails the payment-horizon test outright — no live opportunity exists. Logged for audit-trail completeness since the URL wasn't previously on file; the underlying scope (Brevo automation workflow building) would otherwise have been a reasonable skill match. |

### Screened and rejected on sight (no DB row — out of scope or not a real listing)

- **Contra community post, "Email Marketing Expert with deep expertise in SMTP setup,
  deliverability optimization... Brevo"** — tagged with Brevo/Email Automation and looked
  promising in search results, but on scrape it's a freelancer's own self-promotion/portfolio
  post (by Sohit Sharma, showcasing *his* services), not a client hiring post. No budget, no
  client, no application path. Confirms Contra's 7th-cycle-running pattern: public pages expose
  freelancer-for-hire directories and self-promotion, never actual client job postings.
- **"Email & SMS Production Specialist," Dr. Berg Nutritionals** (surfaced via a new
  health/wellness-niche + Brevo search angle) — a real, well-paid ($32-40/hr) remote posting, but
  it's a **salaried full-time W2 role**, out of scope for this freelance-opportunity workstream,
  and explicitly runs on **Klaviyo**, a PROHIBITED hands-on claim per the claims register. Doubly
  disqualifying; not logged as an opportunity row since it was never a freelance candidate.
- **"Email Marketing Expert" via freelance.de** — surfaced only as a "find a Brevo/Newsletter
  freelancer" directory page, same pattern as Contra. No client postings exposed.
- Several Upwork "explore similar jobs" / search hits requiring tools or scope outside the
  evidenced skill set or niche (MailWizz, Klaviyo email expert, cold-email/LinkedIn outbound
  infrastructure, GTM/outbound campaign research) — screened out on title/snippet alone, not
  scraped.

## Source coverage this cycle

- **Upwork**: re-scraped the one carried-over P1 listing (see follow-up (a)); fresh Brevo-specific
  and generic searches surfaced only listings already on file, plus the off-scope items noted
  above. No new candidate found.
- **PeoplePerHour**: page 1 only, per cycle 6's recommendation — confirmed identical to cycle 6,
  no new candidate.
- **Freelancer.com**: search surfaced one new URL, already closed/awarded (see table above) —
  logged for the record, not a live opportunity.
- **Contra**: 7th consecutive cycle with no genuine client job posting exposed on public pages —
  this cycle's near-miss (a Brevo-tagged community post) turned out to be freelancer self-
  promotion, not a hiring post.
- **Reddit r/forhire**: see follow-up (c) — new access method works, no matching posts this time.
- **German-market search**: re-ran the same query — seventh consecutive cycle with no live
  German-market opening found.
- **freelance.de** (new source tried this cycle): German freelance marketplace — same directory-
  only limitation as Contra, no client postings exposed. Not worth a dedicated pass unless a
  future query surfaces an actual project listing rather than a directory page.
- **Health/wellness-niche + Brevo search angle** (new angle tried this cycle, combining the
  claims register's chosen niche with the platform-specific term): surfaced one real but
  out-of-scope posting (Dr. Berg Nutritionals, full-time + Klaviyo) and otherwise general
  email-platform blog content, not client postings.
- **Useme.com**: re-checked the category page — still exactly the one open listing already logged
  and rejected in cycle 6 (same posting, now showing fewer days remaining), still zero Brevo
  listings found across two cycles of checking.
- **EmailJobs.io**: not re-touched this cycle (cycle 6 established it has no freelance listings
  section, only salaried roles) — no new information to gain from a repeat visit so soon.
- **Direct business prospecting**: out of scope for this workstream per the recurring instruction
  (same as cycles 3-6) — not touched.

## System health

- Sources touched: 9 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit [new method],
  German-market direct search, Useme.com, freelance.de [new], health/wellness+Brevo angle [new]).
- Opportunities found and logged as full rows: 1 new (already closed, 0 live new candidates). 0
  collisions with the existing 38 on file.
- 0 reached P0/P1 this cycle as *new* findings; the one carried-over P1 from cycles 5-6 was
  re-checked and remains unchanged in tier, with a new activity signal recorded (see (a)).
- No automation failures this cycle. The long-standing Reddit access restriction was
  **resolved with a different tool** (not fixed on the original method, but a working path now
  exists) — see follow-up (c). Contra's continued lack of genuine client-posting data is now a
  7-cycle-running, well-documented structural limitation, not a transient error.

## Recommended next 3 actions

1. **Decide whether to adopt the `scrapecreators` Reddit provider going forward**, now that a
   working access method for r/forhire exists (unlike the prior free-but-blocked scrape). It has
   a small real cost per call and returned zero relevant posts this time, so this is a cost/value
   call for the owner, not a technical blocker anymore.
2. **Check the Newsletter Specialist for Campaigns / Brevo listing directly on Upwork soon if
   interested** — the rate is still unconfirmed, but "Interviewing: 3" and "last viewed yesterday"
   suggest the client may be close to filling this role. Per the owner's own instruction, this
   project will not keep re-scraping it every cycle; the window for the owner to check it
   personally may be narrowing.
3. **Keep rotating source/angle experiments** (this cycle: freelance.de, health/wellness+Brevo
   combined search) — six-plus cycles of the standard rotation (Freelancer.com, Contra,
   German-market) have not produced a clean candidate, so new angles remain the more promising
   lever than repeating the same queries.
