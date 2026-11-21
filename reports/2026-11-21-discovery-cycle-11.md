# Discovery Cycle 11 — 2026-11-21

Regular run following cycle 10 (2026-11-20). Picks up cycle 10's open items and runs fresh
discovery searches.

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
  way (11th cycle running).
- A/B testing remains an unresolved CONFLICT — one listing this cycle (the Dublin agency role)
  would have required it directly; flagged as a disqualifier rather than worked around.
- Paid social/Meta advertising remains an unevidenced, unclaimed skill ("none demonstrated, don't
  claim") — tested directly by one listing this cycle (WTF Giveaways) and treated as a hard
  disqualifier.
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com opportunity scored this cycle.
- Carried forward: a "Brevo" keyword hit is not always the ESP platform, and the distinction
  between Brevo as a firm requirement vs. one of several optional ESPs was applied explicitly to
  every new candidate's actual listing text this cycle, not just its title.

Checked `db/email_marketing_system.db` first — 53 opportunities on file from cycles 1-10. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Five new candidates were found and logged (3
Upwork, 2 Freelancer.com) — all **REJECTED**: a $15 academic duplicate posting by an already-
hired client, a UK growth-marketing role requiring unevidenced paid-ads/Meta-advertising skills
alongside Brevo, a Dublin agency role where Brevo is only one of five optional ESPs and structured
A/B testing is a firm requirement, and two long-stale/already-closed Freelancer.com listings. All
four of cycle 10's open items were followed up on exactly as instructed, with modest movement on
both carried-over Upwork leads. Reddit's free-method scrape failed for a 6th consecutive cycle; the
paid provider question remains open and unused. Not recommending an application package.

## Cycle 10 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — rechecked once, first movement in several cycles
Per the owner's standing instruction (flagged already, their call to act on, not something to
repeat again), this was checked once more as a quiet status check, not a re-flag. Current state:
**still open**. Hourly rate **still does not render** in the public scrape — the 6th consecutive
cycle this has failed. For the first time in three cycles there is movement: **Interviewing dropped
from 3 to 2**, and client totals ticked up slightly ($68K spent unchanged, 36 hires vs 35, 16
active unchanged, 1,983 hours vs 1,980) — a small step up after cycle 10's fully-flat snapshot.
Proposals still 20–50. Last viewed by client: "yesterday" (vs "3 days ago" in cycle 10). This
listing shows no job-specific "Hires" counter (unlike, e.g., cycle 10's Cybersecurity FYP listing,
which did), so there is no direct signal that this particular job has closed or been filled — the
interviewing drop could equally mean a candidate was screened out rather than hired. Per the
instruction, this is **noted on the DB row and left at that** — not retired (nothing indicates
closed/hired/gone) and not re-flagged as "needs attention."

### (b) Brevo CRM and Email Setup (id 40) — rechecked, outbound activity continues to build
Checked for completeness as the second-best lead on file. Still open. Rate unchanged ($10–28/hr).
Client still shows 1 hire, 1 active — no new hires. **Interviewing progressed further, from 3 to
4** — the second consecutive cycle of upward movement on this signal, continuing cycle 10's 2→3
move. Invites-sent/unanswered unchanged at 2/0. Proposals still 20–50. This is a genuine, if still
modest, continuation of outbound activity. Tier left at `PAYMENT_TIMELINE_UNCERTAIN`: the client's
total track record is still just 1 hire, but two consecutive cycles of rising interviewing counts
is worth continuing to watch rather than dismissing outright.

### (c) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page. Failed identically: *"Firecrawl can't scrape this site because it is
currently not supported."* This is the **6th consecutive cycle** this has failed via the free
method. No cost incurred, no new data gained, as expected. **Still awaiting the owner's decision**
on whether the paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — rechecked, no genuinely new live candidate
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The current-listings section held just two postings: "Gmail account" (Google Workspace account
configuration — out of email-marketing scope, not logged) and "UK Kajabi expert: email
automations, tagging & lead capture" (already on file, id 8, unchanged). "Help with Brevo"
(already logged and rejected as stale, id 46) reappeared again in the "Past Projects" section with
no material change (still 6 proposals, still "2 months ago"). **6th cycle running** with no
genuinely new, live candidate from this source.

### (e) Direct business prospecting — not run, same reasoning as cycles 8-10
Confirming a gap in this workstream ends in drafting a short, personalized cold-outreach message —
out of scope for this cycle's no-drafting instruction. Not attempted here; remains the separate,
manual, owner-reviewed workstream it has been since cycle 3
(`evidence/prospects-medical-wellness.md`).

### (f) "Brevo" keyword-match discipline — carried forward, applied
Every new candidate's actual job text was read before counting a "Brevo" hit as a scope match. Two
listings this cycle turned out to treat Brevo as something other than a firm requirement: the
Dublin, Ireland agency role (Brevo is one of five named optional ESPs) and the WTF Giveaways role
(Brevo is the *preferred* platform, but the role's essential skill set is actually paid Meta
advertising, not email). Both noted explicitly in their rejection reasons below rather than scored
as if Brevo were a confirmed, central requirement.

### (g) Contra, German-market search, and freelance.de — 11, 11, and 5 consecutive cycles with nothing live
This cycle again turned up nothing usable from any of these three sources (see Source coverage
below for specifics — notably, Contra this cycle did not even surface a directory-style page on
direct scrape, only its own generic landing content). That makes **11 consecutive cycles** for
Contra and the dedicated German-market search angle, and **5 consecutive cycles** for freelance.de
confirming no reachable client-posting section at all (as distinct from Contra/German-search, which
at least surface *some* content, just never a genuine client posting). Saying this plainly, as
instructed: these three sources have not produced a single live, testable candidate across this
project's history to date. Worth the owner's consideration — not a decision this project is making
unilaterally — whether continuing to spend a cycle checking all three is worth it relative to
investing that effort in a genuinely new source, the way Useme.com and EmailJobs.io were added
earlier in this project's history.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–10 unchanged, see (a)
above)

## New candidates checked this cycle (5)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Email Infrastructure & Domain Configuration Specialist | Upwork | Pakistan, same client as id 47 | **REJECTED** — duplicate posting, client already has 1 hire |
| Growth Marketing Specialist – Email, Meta Ads & AI Marketing | Upwork | UK, new account (WTF Giveaways) | **REJECTED** — unevidenced Meta/paid-ads requirement |
| Email Marketing Specialist (Automations, Campaigns & Revenue Growth) | Upwork | Ireland, thin history (1 hire) | **REJECTED** — Brevo optional; A/B testing required |
| Email Marketing Management for Local Business | Freelancer.com | Unknown, local business | **REJECTED** — stale, ~1 yr old, already In Progress |
| Brevo Workflow Automation Expert Needed -- 2 | Freelancer.com (.com.co) | Israel, established (11+ yrs, 5.0/66 reviews) | **REJECTED** — already awarded 10 months ago |

### Why each was rejected

- **Email Infrastructure & Domain Configuration Specialist** ($15 fixed, Pakistan client): the
  same client as cycle 10's id 47 ("Fix Brevo/Mailgun"), posting what is essentially the identical
  university Cybersecurity FYP Brevo/DNS subdomain scope a second time under a different title and
  category (Network & System Administration instead of Digital Marketing). The client already
  shows "1 hire, 1 active" — a contract has started on this client's job(s) — plus 7 interviewing
  and 11 invites sent on this specific listing, showing the client deep into its hiring funnel
  regardless. A $15 one-time academic project either way.
- **Growth Marketing Specialist – Email, Meta Ads & AI Marketing** ($1,000 fixed, contract-to-hire,
  UK prize-competition business): a genuine Brevo component ("proven email marketing experience,
  preferably with Brevo") and a decent budget, but the role's essential qualifications require
  hands-on Meta/Facebook paid-advertising campaign management — explicitly listed in the claims
  register as "none demonstrated, don't claim." The application itself asks for "examples of Meta
  campaigns you've managed and their results," which cannot be honestly supplied. The role also
  expects AI-content-tool production at volume and UK prize-competition/GDPR/PECR regulatory
  familiarity — a multi-skill growth-marketing role, not a close match once paid ads are accounted
  for.
- **Email Marketing Specialist (Automations, Campaigns & Revenue Growth)** ($10–20/hr, Dublin,
  Ireland agency): a credible client with a real track record (1 hire), but Brevo is listed as only
  one of five acceptable ESPs (Klaviyo, Mailchimp, ActiveCampaign, HubSpot, or Brevo) — the client
  has not committed to Brevo specifically. Separately, A/B testing and performance optimization is
  a required skill, not optional — directly testing the unresolved A/B-testing CONFLICT in the
  claims register. 20–50 competing proposals already on record.
- **Email Marketing Management for Local Business** ($2–8/hr, Freelancer.com): a genuine, narrow
  Brevo "take over my existing setup" scope, but the listing's own status is "In Progress," it was
  posted roughly a year before this cycle's discovery, and its stated deadline (Sept 31, 2025) has
  already long passed — this work was already awarded and is long over, not a live opportunity.
  The hourly rate ($2–8/hr) would also not have cleared a reasonable compensation bar even if open.
- **Brevo Workflow Automation Expert Needed -- 2** ($10–30 fixed, Freelancer.com/.com.co mirror,
  Israel client): the most credible client found this cycle by tenure and reputation (11+ years on
  the platform, 5.0 rating across 66 reviews, payment method verified), with a genuine Brevo
  workflow-automation scope — but the listing itself shows status "Terminado" (Finished) and was
  formally awarded to another freelancer 10 months before this cycle's discovery. Also tagged under
  the Make.com category alongside Email Marketing, suggesting middleware tooling may have been part
  of the real scope. Long closed either way.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-specific
  and generic searches surfaced 3 new-to-file URLs, all closed/rejected (see table above).
- **Freelancer.com**: fresh Brevo-specific and generic searches surfaced 2 new-to-file URLs, both
  rejected as long-stale/already-closed (one ~1 year old and "In Progress," one formally awarded
  10 months ago). Other hits matched URLs already on file or were freelancer self-promotion/
  portfolio pages.
- **PeoplePerHour**: page 1 only, per cycles 6–10's finding — no genuinely new live candidate this
  cycle (see follow-up (d)).
- **Contra**: 11th consecutive cycle with the same structural limitation — this cycle a direct
  scrape of the featured-jobs landing page returned only Contra's own generic marketing content
  with no job-posting anchors at all, not even the `/hire/brevo-freelancers`-style directory pages
  a parallel web search still surfaced. Never a genuine client job posting across 11 cycles.
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked; paid provider not used
  this cycle per instruction.
- **German-market search**: re-ran the German-language query — 11th consecutive cycle with no live
  German-market opening found via this search angle; results remain Brevo's own German marketing
  pages, freelance.de directory/profile pages, and Contra's directory page, not client project
  postings.
- **freelance.de**: tried a site-scoped query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile/directory pages (individuals advertising their own
  Brevo/E-Mail-Marketing skills) — no client project listing at all. 5th consecutive cycle
  confirming no client project-posting section is reachable for this platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–10: same
  Oliver Törnroth/Zoined posting (now 21 days left, down from 22 in cycle 10), still the only open
  listing, still zero live Brevo listings. Polish page 2 not re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle;
  covered instead by the broader generic email-marketing search pass, which surfaced only
  job-board aggregator/landing pages (Indeed, LinkedIn, ZipRecruiter, Toptal, Arc.dev), consistent
  with prior cycles' finding.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning as
  cycles 8–10 (see follow-up (e) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com), plus the Indeed health-wellness
  angle folded into the generic search pass. Direct business prospecting flagged as
  out-of-scope-this-cycle rather than touched.
- Opportunities found and logged as full rows: 5 new (0 collisions with the existing 53 on file),
  all `REJECTED`. 0 reached P0/P1. Database now holds 58 opportunities.
- The two carried-over leads were both re-checked, and both showed real (if modest) movement for
  the first time in a few cycles: the Newsletter Specialist listing (id 31) saw Interviewing drop
  3→2 after three flat cycles, with a small uptick in the client's aggregate hire/hours counters;
  the Brevo CRM and Email Setup listing (id 40) saw Interviewing continue climbing, 3→4, its second
  consecutive cycle of upward movement. Neither tier was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 6th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra, freelance.de, German-market
  search, and Useme.com page 1 each logged another consecutive cycle of the same structural
  limitations already established in prior cycles — see follow-up (g) above for the plain
  statement on Contra/German-search (11 cycles) and freelance.de (5 cycles).
- This cycle's clearest lesson: two listings that *named* Brevo prominently (WTF Giveaways,
  Dublin agency) were still clean rejects once the actual required skill set was read in full —
  reinforcing that a Brevo mention in the title or summary is not sufficient on its own, consistent
  with the keyword-match discipline carried forward from cycle 9.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open.
2. **No action needed on the Newsletter Specialist listing this cycle** beyond the quiet note
   already recorded — per the owner's own instruction, it's been flagged enough. Worth being aware
   that Interviewing dropped 3→2 this cycle (the first movement in three cycles), though there's no
   listing-level signal confirming whether that means the role was filled or a candidate was simply
   screened out.
3. **New this cycle**: consider whether Contra, the dedicated German-market search angle, and
   freelance.de are still worth a full check each cycle, given 11, 11, and 5 consecutive cycles
   respectively with no live, testable candidate produced. This project is not deprioritizing them
   unilaterally — flagging it for the owner's call, the same way Useme.com and EmailJobs.io were
   added as replacements/supplements earlier in this project's history.
