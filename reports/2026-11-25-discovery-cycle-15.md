# Discovery Cycle 15 — 2026-11-25

Regular run following cycle 14 (2026-11-24). Picks up cycle 14's open items and runs fresh
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
  cycle — none found. This mattered directly this cycle (see "Email Marketing & Campaign
  Automation Specialist" below).
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (15th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` apply to both new candidates
  scored this cycle (both are Upwork hourly/fixed-price engagements, neither independently tested
  for TRNC).

Checked `db/email_marketing_system.db` first — 62 opportunities on file from cycles 1–14. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Two new candidates were found and logged this
cycle (both Upwork) — both **REJECTED**, for different reasons: one on pure competition/timing
despite a genuinely strong skill match, the other on compensation, a prohibited-tool-stack
requirement, and client credibility. All of cycle 14's open items were followed up on exactly as
instructed. The Newsletter Specialist listing (id 31) is now confirmed stable — last cycle's
active-contracts dip did not continue, which settles that it was unrelated to this listing. The
Brevo CRM and Email Setup listing (id 40) is now stalled at Interviewing=4 for a **fourth**
consecutive cycle, still no hire on the listing itself. Reddit's free-method scrape failed for a
**10th** consecutive cycle. The German-market search surfaced a second instance of the same
dead-mirror pattern first seen last cycle, which now looks structural rather than coincidental.
Not recommending an application package.

## Cycle 14 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — the account-level dip has settled, no closure signal
Rechecked once more as a quiet status check, not a re-flag, per the owner's standing instruction.
Current state: **still open**. Hourly rate **still does not render** in the public scrape — the
**10th consecutive cycle** this has failed. Interviewing unchanged at 2. Invites sent/unanswered
unchanged at 0/0. Last viewed by client: "yesterday" (vs "4 days ago" in cycle 14 — ordinary
noise, not a signal). The thing worth tracking from last cycle — the client's active-contract
count, which dropped 16→15 in cycle 14 — **held at 15 this cycle** rather than dropping further,
while total spend stayed flat at $69K and hours rose again (2,002→2,020, consistent with ongoing
work on the client's many *other* active contracts). This settles the question cycle 14 left open:
the dip was account-level noise from one of this buyer's other 14 active contracts, not a
job-specific signal about this listing. Per the owner's standing instruction, this is **noted on
the DB row and left at that** — not retired (no hire/closure signal) and not re-flagged.

### (b) Brevo CRM and Email Setup (id 40) — now a fourth consecutive stalled cycle, plus a new but equally ambiguous account-level signal
Rechecked closely again, per the owner's instruction to watch this one most closely. Result: **it
has still not moved on this listing**. Still open. Rate unchanged ($10–28/hr). **Interviewing is
still at 4** — now the **fourth** consecutive cycle at exactly 4 (cycles 12, 13, 14, 15), following
the genuine 2→3→4 climb in cycles 9–11. Invites-sent/unanswered unchanged at 2/0. One new
account-level data point: the client's "active contracts" figure dropped from 1 to 0 (their sole
all-time hire on Upwork no longer shows as active), while total spent is still flat at $15. Applying
exactly the same reasoning the project used for id 31's account-level dip last cycle: there is no
job-specific "Hires" field on *this* listing, and nothing else here (Interviewing still 4, invites
unchanged) indicates this particular job closed — a single hire elsewhere on this very new account
(member since Nov 10, 2026) concluding is at least as consistent an explanation as this listing
being the one that closed. Noted on the DB row, not treated as closure, tier not revised
(`PAYMENT_TIMELINE_UNCERTAIN`).

### (c) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). A direct `firecrawl_scrape` attempt against the subreddit
listing page failed identically: *"Firecrawl can't scrape this site because it is currently not
supported."* This is the **10th consecutive cycle** this has failed via the free method. No
specific-looking individual post was surfaced by general web search this cycle (unlike cycle 14),
so no individual-post-URL test was run this time. No cost incurred, no new data gained, as
expected. **Still awaiting the owner's decision** on whether the paid `scrapecreators` route is
worth adopting going forward.

### (d) PeoplePerHour page 1 — one new-to-page hit, still out of scope
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The current-listings section now shows a genuinely new posting, "B2B Lead Generation & Email
Outreach for Established VO Artist" (£150 budget shown as $138, 27 proposals, posted ~20 hours
before discovery) — a UK/US voiceover artist wanting an AI-assisted cold-outreach and lead-
generation system built and run for them. No Brevo mention, no email-marketing-platform skill
involved at all; this is prospect research, cold-email-sequence writing, and reply management, not
platform specialist work. Read in full, **not logged**, consistent with the project's standard.
The same three recurring out-of-scope postings persist alongside it: "Cold Email Marketing
Specialist" (the Dubai B2B tax-consultancy cold-outreach role, now aged to 3 days/22 proposals, up
from 2 days/22 in cycle 14), "Find 75 Property Owners for Free Listings" ($131, UK holiday-house
lead-gen, unchanged), and "Gmail account" (Google Workspace account configuration, unchanged).
**10th cycle running** with no genuinely new, in-scope, live candidate from this source.

### (e) Contra, German-market search, and freelance.de — checked again, kept brief as instructed
All three were checked again this cycle. Contra's featured-jobs page again rendered real job
cards, including the same "Email Marketing Specialist – Dual Campaigns for Parents & School
Leaders" card already on file (id 19, $25–40/hr), plus two other recurring non-Brevo listings
("Marketing Assistant for Launch Campaign," $1,500–$2,500 one-time; "Prepping Digital Assets
Before Launching Campaigns," $60–120/hr, web-dev/SEO scope) — no genuinely new client email-
marketing posting appeared. That makes **15 consecutive cycles** for Contra with no new genuine
email-marketing lead. The German-market search surfaced a second, different instance of last
cycle's exact pattern: a `freiguide.de`-mirrored Kleinanzeigen.de classified titled "BREVO
Newsletter einrichten" (a different ad ID than cycle 14's find — a private individual asking
someone to set up a Brevo newsletter). Checking the original Kleinanzeigen.de URL directly again
showed it **already removed** ("Die gewünschte Anzeige ist nicht mehr verfügbar"), exactly as in
cycle 14. This is now the **second time** this specific dead-mirror pattern has repeated — strong
enough to say plainly that `freiguide.de`'s index structurally lags behind Kleinanzeigen.de's live
removals, rather than this being a one-off coincidence. A separate German hit this cycle, "Biete:
E-Mail-Marketing einrichten – Newsletter endlich starten" (Düsseldorf), is a **freelancer's own
service ad** — a competitor advertising their skills, not a client request — so not actionable
either way. That makes **15 consecutive cycles** for the German-market search with nothing live
and actionable. freelance.de again surfaced only freelancer profile/directory pages (Brevo-
Freelancer finden, Newsletter-Freelancer finden, Newsletter-kampagnen-Freelancer finden) plus a
Fiverr gig-directory hit — no client project posting. **9 consecutive cycles** confirming no
reachable client-posting section for this platform via search.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–14 unchanged, see (a)
above)

## New candidates checked this cycle (2 logged, 2 noted but not logged)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Email Deliverability Specialist | Upwork | Travel & hospitality small company, Sydney, Australia (est. 2012, $68K spent, 61 hires) | **REJECTED** — genuine Brevo/deliverability skill match, but 50+ proposals with the client already Interviewing 3 and invites already out; late, low-probability bid |
| Email Marketing & Campaign Automation Specialist | Upwork | Brand-new individual client, India (19 days old, no spend/hire history) | **REJECTED** — $25 fixed price for a multi-week automation/infrastructure scope; requires Instantly/Lemlist/Apollo/Mailchimp alongside Brevo, several PROHIBITED per the claims register; zero client track record |

### Why they were rejected

- **Email Deliverability Specialist** ($12–35/hr, <1 month, one-time project): the job asks for
  exactly the project's strongest documented skill — fixing Brevo + Google Workspace email
  deliverability via SPF/DKIM/DMARC — from a long-established, high-spend, credible client (member
  since 2012, $68K spent, 61 hires, 10 active contracts). This is the closest skill match of any
  candidate checked this cycle. It was still rejected, on competition/timing grounds alone: 50+
  competing proposals, the client already Interviewing 3 candidates, and 3 invites already sent (2
  still unanswered) at the moment of discovery. Per the owner's standing instruction against
  rounding up marginal matches, a hiring funnel this far along before a proposal is even drafted
  is not a clean opportunity, regardless of skill fit.
- **Email Marketing & Campaign Automation Specialist** ($25.00 fixed price, ongoing project): a
  brand-new client (account 19 days old at discovery, no verified spend or hires at all) wants a
  specialist to evaluate their current Zoho setup, recommend a replacement platform, configure
  infrastructure, build bulk campaigns and automated multi-step sequences, set up authentication,
  and provide reporting and warm-up guidance — for $25 fixed. The posting explicitly names
  Instantly, Smartlead, Lemlist, and Apollo alongside Brevo and Mailchimp as acceptable platforms,
  and wants the freelancer to recommend across that whole stack rather than just operate Brevo.
  Instantly, Lemlist, Apollo, and Mailchimp are all PROHIBITED/unevidenced per
  `evidence/claims-register.md` — a Brevo-only skill set does not cover what this role is actually
  asking for. Combined with the token budget and the complete absence of client track record, this
  is a clean three-way reject (compensation, prohibited-tool-stack, credibility), not a close call.

### Hits read but not logged this cycle (stale, scope-mismatched, or not independently actionable)

Two further items were read in full but **not** logged as DB rows, consistent with the project's
standard of only logging independently verified, live-and-actionable new-to-file URLs (or, per
cycle 13's precedent, recently-closed ones found via a deliberate Brevo-specific search):

- **"Mail Merge & Personalized Email Outreach Specialist"** (Upwork, $150 fixed, posted September
  7, 2026 — roughly 2.5 months before this discovery) — mentions "the BREVO email campaign
  platform" once in passing, but the actual scope is Word/Excel mail-merge and cold personalized
  outreach for an "educational honors organization" (a solicitation/recognition-mailing business
  model), with required skills centered on Excel, Google Sheets, Word Mail Merge, and Outlook, not
  Brevo campaign management. 50+ proposals, 8 already Interviewing, and 9 invites sent with 0
  unanswered strongly suggest this role has long since been filled in practice. Too stale and
  scope-mismatched to carry audit-trail value; noted here only.
- **"B2B Lead Generation & Email Outreach for Established VO Artist"** (PeoplePerHour, $138, 27
  proposals, posted ~20 hours before discovery) — see follow-up (d). A live, genuinely new posting,
  but pure cold-outreach/lead-generation work for a voiceover artist, with no Brevo or email-
  marketing-platform skill requirement at all. Out of scope on the same basis as prior cycles'
  lead-gen rejects; not logged.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-
  specific and generic searches surfaced 2 new-to-file URLs, both logged and REJECTED (see table
  above), plus one further hit read but not logged as stale/scope-mismatched (see above).
- **Freelancer.com**: Brevo-specific and generic searches surfaced no new-to-file URLs this cycle
  — every Brevo-specific hit returned was already on file from a prior cycle.
- **PeoplePerHour**: page 1 only, per cycles 6–14's finding — one new-to-page hit found and read
  but out of scope (see follow-up (d)); no genuinely new in-scope candidate this cycle.
- **Contra**: 15th consecutive cycle with the same underlying limitation — real featured-job cards
  render, but none new and email-marketing-relevant (see follow-up (e)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked at the subreddit level;
  paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query and a follow-up check on the hit it
  surfaced — 15th consecutive cycle with no live, actionable German-market opening; the
  dead-mirror pattern on `freiguide.de`/Kleinanzeigen.de repeated for a second time (see follow-up
  (e)).
- **freelance.de**: tried the dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages plus a Fiverr gig-directory hit — 9th
  consecutive cycle confirming no client project-posting section is reachable for this platform
  via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–14: same
  Oliver Törnroth/Zoined posting (now 17 days left, down from 18 in cycle 14), still the only open
  listing, still zero live Brevo listings. Polish page 2 not re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycles 13–14's treatment; prior cycles' finding (job-board aggregator pages and
  Brevo's own healthcare-marketing blog content, no live candidate) assumed unchanged.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — out of scope for
  this automated run, per the task instruction.

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search [including a follow-up check on freiguide.de/
  Kleinanzeigen.de], freelance.de, Useme.com), plus the Indeed health-wellness angle assumed
  unchanged from prior cycles. Direct business prospecting flagged as out-of-scope-this-cycle
  rather than touched.
- Opportunities found and logged as full rows: 2 new (0 collisions with the existing 62 on file),
  both `REJECTED`. 0 reached P0/P1. Database now holds 64 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) saw
  its account-level active-contracts figure *hold* at the lower value noted last cycle rather than
  drop further, settling that last cycle's dip was unrelated to this listing — noted, not
  re-flagged. The Brevo CRM and Email Setup listing (id 40), tracked most closely this cycle per
  the owner's instruction, is now confirmed **stalled for a fourth consecutive cycle** at
  Interviewing=4, with a new but similarly ambiguous account-level signal (active hires 1→0) that
  does not read as a closure signal on this specific listing. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 10th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra (15th) and freelance.de (9th) each
  logged another consecutive cycle of the same structural limitations already established in prior
  cycles. The German-market search (15th consecutive cycle with nothing actionable) produced a
  notable but still-non-actionable new data point: the freiguide.de/Kleinanzeigen.de dead-mirror
  pattern first seen in cycle 14 repeated a second time with a different ad, which is worth
  tracking as a structural characteristic of that aggregator rather than a one-off.
- This cycle's clearest lesson: a genuinely strong skill match is not the same thing as a
  qualifying opportunity. "Email Deliverability Specialist" was the best skill fit found in weeks
  of cycles — squarely in the project's one area of strongest documented evidence — and was still
  a clean reject once the competition signals (50+ proposals, 3 already interviewing, invites
  already sent) were taken at face value instead of discounted. Separately, "Email Marketing &
  Campaign Automation Specialist" reinforced a now-familiar pattern: a posting that lists Brevo
  alongside several PROHIBITED tools (Instantly, Lemlist, Apollo, Mailchimp) is not a Brevo job
  with extra options — it's a job that wants cross-platform breadth the project does not have
  evidence for, dressed with one platform the project does.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open,
   now at a 10th consecutive blocked cycle on the free method.
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded. The account-level active-contracts figure has now stabilized at 15, which
   closes out the ambiguity cycle 14 flagged — there's nothing further to watch here beyond the
   standing rate-never-renders oddity, now at 10 consecutive cycles.
3. **No action needed on the Brevo CRM and Email Setup listing this cycle** beyond the note
   recorded — its earlier rising-interviewing signal is now confirmed stalled over four
   consecutive cycles (4, 4, 4, 4), not reversed or resolved into a hire. Worth a continued close
   watch in future cycles rather than any fresh flag now, since it remains the one lead on file
   that has shown genuine movement at any point. Separately, the owner's still-open call from
   cycle 11 on whether to keep checking Contra, the German-market search angle, and freelance.de
   each cycle (15, 15, and 9 consecutive cycles with nothing new/live and actionable) remains
   unchanged and unforced.
