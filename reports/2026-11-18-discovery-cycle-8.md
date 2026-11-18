# Discovery Cycle 8 — 2026-11-18

Regular run following cycle 7 (2026-11-17). This cycle picks up cycle 7's three open items and
runs fresh discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence.
- Klaviyo, Make.com, Zapier, n8n, Mailchimp, HubSpot, and now also Instantly/Lemlist/Apollo
  (cold-outreach tooling, surfaced this cycle, never claimed in any of the 3 source docs) remain
  PROHIBITED/unevidenced claims.
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (eighth cycle running).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com opportunity.

Checked `db/email_marketing_system.db` first — 39 opportunities on file from cycles 1-7. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** One new candidate (Brevo CRM and Email Setup,
Upwork) is a genuine skill match but scores below the P1 bar on client credibility and
competition, so it's logged as `PAYMENT_TIMELINE_UNCERTAIN`, not rounded up. One more candidate
was rejected on tool requirements (cold-outreach infrastructure, not email marketing). One
previously-unseen Useme.com URL was found already closed (11 months stale). All three of cycle
7's open items were followed up on exactly as instructed. Not recommending an application
package.

## Cycle 7 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo — rechecked once, nothing materially new
Per the owner's standing instruction (this listing has now been flagged twice and is the owner's
call to act on, not something to repeat), this was checked once more as a quiet status check, not
a re-flag. Current state: hourly rate **still does not render** in the public scrape (3rd
consecutive cycle). Interviewing is still **3** (unchanged from cycle 7's 0→3 jump — no further
movement). Last viewed by client: "yesterday" (same relative wording as cycle 7, consistent with
ongoing client activity, not stale). Client totals are essentially flat: $68K total spent (same),
35 hires (same), 16 active (same), 1,976 hours logged (up slightly from 1,973 in cycle 7 — routine
platform usage, not a signal). **Nothing here clears the bar the owner set for a repeat flag** —
the rate is still the one fact that would make or break this, still invisible, and the activity
picture hasn't moved since cycle 7. Noted on the DB row (id 31) and left at that; not re-scored,
not re-flagged as "needs attention" in this summary.

### (b) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead on adopting it (open since cycle 7). Fell back to a direct `firecrawl_scrape`
attempt instead, both against the subreddit listing page and an individual thread URL surfaced by
web search. Both failed identically: *"Firecrawl can't scrape this site because it is currently
not supported."* Same result as 7 of the last 8 cycles on the free method. No cost incurred, no
new data gained, as expected. **Still awaiting the owner's decision** on whether the paid
`scrapecreators` route is worth adopting going forward.

### (c) PeoplePerHour page 1 — rechecked, identical to cycles 6-7
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
**Identical to cycles 6 and 7**: exactly 2 open listings — the same $10 "Gmail account" Google
Workspace admin task (not email marketing) and the same already-logged UK Kajabi listing
(duplicate). No new candidate. Confirms page-1-only re-checks remain sufficient.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5-7 unchanged, see (a) above)

## New candidates checked this cycle (3)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Brevo CRM and Email Setup | Upwork | US (Washington), member since Nov 10, 2026 — 8 days old, 1 hire/1 active | **PAYMENT_TIMELINE_UNCERTAIN** (discounted, not P1) |
| B2B Cold Email & Lead Generation Specialist (Instantly/Apollo/Brevo) | Upwork | Pakistan (Karachi), member since 2018, $3.5K spent, 351 hires, mid-sized agency | **REJECTED** — tool/scope mismatch |
| ROZBUDOWA AUTOMATYZACJI BREVO (Brevo automation build-out, PrestaShop store) | Useme.com | Polish individual client ("MT") | **REJECTED** — already closed (posted 2025-12-30, 30-day listing window expired ~11 months before this cycle's discovery; 7 proposals already submitted against it) |

### Why "Brevo CRM and Email Setup" didn't clear the P1 bar

The scope itself is a real, direct skill match: configuring Brevo workflows/email sequences for
onboarding, retention, and e-commerce lifecycle stages — exactly the kind of lifecycle/segmentation
work documented at HIBARR. No PROHIBITED tool is required (the "Microsoft Dynamics CRM"/"Zoho CRM"
tags appear to be Upwork's auto-suggested skill tags, not stated requirements in the job text
itself). $10-28/hr hourly, 1-3 months, Upwork escrow (TRNC payment-routing caveats apply as for
every Upwork listing per `evidence/payment-routing.md`).

What keeps it out of P1: the client account is **8 days old** with exactly **1 hire, 1 active
contract** — effectively no track record to assess trust/payment-follow-through against, which is
a real, not cosmetic, risk on a platform where "client never funds the milestone" and "client
disappears after unpaid hours" are both known failure modes. On top of that, the listing already
has **20-50 competing proposals and 2 active interviews** against a brand-new, thin-budget client
— a weak probability-of-win signal regardless of fit. Scored and logged honestly rather than
rounded up to make the cycle look more productive; see the DB row for the full rubric breakdown.
Not recommending a proposal on the strength of this alone.

### Why "B2B Cold Email & Lead Generation Specialist" was rejected
Despite "Brevo" appearing in the title and in one line of the tool list, the actual scope is B2B
*cold outreach* infrastructure — Apollo.io/LinkedIn Sales Navigator list-building, Instantly/
Lemlist/Brevo cold-sequence configuration, SPF/DKIM/DMARC domain warm-up, and outbound deliverability
metrics. None of Instantly, Lemlist, or Apollo appear anywhere in the claims register (checked for
updates first — none found), and HubSpot/ActiveCampaign are explicitly PROHIBITED hands-on claims.
This is a different job family (outbound sales-development tooling) wearing an email-marketing
label, not a Brevo email-marketing-specialist role. $5-10/hr, entry-level, also well below a
reasonable rate for the stated scope. Rejected on tool/scope grounds, consistent with how the
near-identical "Klaviyo email expert" and "cold-email/LinkedIn outbound infrastructure" listings
were screened out in cycle 7.

### Why the Useme.com Brevo listing was rejected
A real, on-scope Brevo task (expanding an existing partial Brevo implementation — abandoned-cart
automation already live — into a fuller revenue-generating setup on a PrestaShop store) that would
otherwise be a reasonable skill match. But it was posted 2025-12-30 with a stated 30-day listing
window (expired roughly 2026-01-29) and already has 7 submitted proposals on record, all from
late 2025/early 2026. No live opportunity exists; fails the payment-horizon test outright. Logged
for the audit trail since the URL wasn't previously on file, same treatment as the closed
Freelancer.com listing found in cycle 7.

## Source coverage this cycle

- **Upwork**: re-scraped the one carried-over P1 listing (see follow-up (a)); fresh Brevo-specific
  and generic searches surfaced two new candidates (table above) plus listings already on file.
- **PeoplePerHour**: page 1 only, per cycles 6-7's finding — confirmed identical again, no new
  candidate.
- **Freelancer.com**: fresh Brevo-specific search surfaced only listings already on file (including
  the one closed listing logged in cycle 7) — no new URL this cycle.
- **Contra**: 8th consecutive cycle with no genuine client job posting exposed on public pages —
  search results remain limited to the `/hire/brevo-freelancers` directory page and freelancer
  self-promotion/directory content.
- **Reddit r/forhire**: see follow-up (b) — direct scrape still blocked on both the subreddit page
  and an individual thread URL; paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query — eighth consecutive cycle with no
  live German-market opening found; results remain tutorials, platform blog content, and a single
  German agency's own service page (web-labels.de, offering Brevo/Klaviyo services to clients, not
  hiring).
- **freelance.de**: tried both a directory-style query and a "Projekt gesucht" style query aimed
  specifically at finding an actual client posting rather than a freelancer directory. Still only
  surfaced `/Brevo-Freelancer` and `/Newsletter-Freelancer` — "find a freelancer" directory pages,
  same structural limitation as cycle 7. No client project-posting section found for this platform
  across two cycles of checking; likely not worth a further dedicated pass unless a future query
  surfaces a genuine Projekt/Auftrag listing page.
- **Useme.com**: re-checked both the English and Polish (page 2) category views. Page 1 unchanged
  from cycle 7 (same Oliver Törnroth/Zoined posting, now showing 24 days left instead of 25 — still
  the only currently-open listing, still zero live Brevo listings). Page 2 of the Polish listing
  surfaced the one new-to-this-project Brevo URL, which turned out to be closed (see table above).
  Category continues to be dominated by Klaviyo/Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/
  Omnisend/SendGrid listings.
- **Direct business prospecting** (master prompt §4.3/§12): **not run this cycle, and flagged here
  rather than silently skipped.** This workstream's own method (`evidence/direct-prospecting-
  playbook.md`) is audit-first but ends in drafting a short, personalized cold-outreach message to
  a named business once a gap is confirmed — that drafting step is explicitly out of scope for this
  cycle's instructions ("do NOT draft outreach messages... Discovery, verification, scoring, DB
  updates, and reporting only"). Running the research half without the drafting half wouldn't
  produce anything scorable against this project's P0/P1 payment-horizon framework either (there's
  no live "opportunity" with a budget/deadline until a pitch is actually sent and answered). This
  mirrors how cycles 3-7 treated it: a separate, manual, owner-reviewed workstream
  (`evidence/prospects-medical-wellness.md`, currently at batch 6, with batch 7 pending the owner's
  review and send), not something this automated job-board cycle runs on its own. If the owner
  wants direct prospecting folded into the automated cycle, that's a scope decision for them to
  make, since it would mean relaxing the no-drafting constraint for part of the run.

## System health

- Sources touched: 8 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com). Direct business prospecting
  flagged as out-of-scope-this-cycle rather than touched (see above).
- Opportunities found and logged as full rows: 3 new (0 collisions with the existing 39 on file).
  0 reached P0/P1; 1 reached `PAYMENT_TIMELINE_UNCERTAIN` on an honest score, 2 rejected.
- The one carried-over P1 from cycles 5-7 was re-checked and remains unchanged in tier and score;
  per the owner's standing instruction, not re-flagged as needing attention this cycle.
- No automation failures. Reddit's scrape restriction continues to hold on the free method (8
  cycles now); the paid-provider question from cycle 7 remains open and unanswered, so it wasn't
  used again. Contra and freelance.de both logged an 8th/2nd consecutive cycle respectively of the
  same "directory pages only, no client postings" structural limitation.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider (small real cost per call, one demonstrated working access path, zero relevant
   posts found the one time it was tried). Not re-raised as urgent — just restating that this
   decision is still open and nothing has changed about it.
2. **No action needed on the Newsletter Specialist listing this cycle** — per the owner's own
   instruction, it's been flagged enough; the state is unchanged from cycle 7 and this project will
   keep noting it quietly rather than re-escalating it.
3. **Decide whether direct business prospecting should be folded into this automated cycle** — it
   currently can't produce a scorable result without drafting outreach, which is outside this
   cycle's standing instructions; if the owner wants it covered automatically, that needs an
   explicit scope call (see the source-coverage note above), not an interpretation on this project's
   part.
