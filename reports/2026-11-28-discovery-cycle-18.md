# Discovery Cycle 18 — 2026-11-28

Regular run following cycle 17 (2026-11-27). Picks up cycle 17's open items and runs fresh
discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged:
- Brevo remains the one platform with strong, consistent documented evidence (and specifically,
  deliverability/SPF/DKIM/DMARC/list-hygiene is the single strongest sub-area).
- Klaviyo, Make.com, Zapier, n8n, Mailchimp, HubSpot, Instantly, Lemlist, Apollo, Expandi,
  Meta-ads, and GoHighLevel remain PROHIBITED/unevidenced claims; checked the claims register for
  updates this cycle — none found.
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (18th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` apply to every new candidate
  scored this cycle; none independently tested for TRNC.

Checked `db/email_marketing_system.db` first — 73 opportunities on file from cycles 1–17. Nothing
below duplicates an existing URL.

## Headline

**No new P0 or P1 this cycle — and the one pending owner decision from cycle 17 is still
genuinely live, not mooted.** Per the task's explicit instruction, "Email Deliverability
Specialist for 3 Companies" (Upwork) was rechecked but **no application package was prepared** —
that decision remains the owner's. The listing is **still open, not closed, not quietly filled**:
Interviewing is still 0, the single invite sent is still unanswered, and no job-specific "Hires"
field has appeared. The owner can act on it whenever they choose; nothing about this cycle's check
changes the recommendation already on file. Two fresh Upwork candidates were found, scraped, and
both **REJECTED**: one shows an explicit "Hires: 1" field (confirmed filled) and separately
requires PROHIBITED tools (Klaviyo, Omnisend); the other looks active on paper (Interviewing: 4,
5 invites sent) but was last viewed by the client four weeks ago — read as effectively
abandoned/quietly filled, consistent with this project's established methodology for that
combination of signals. A third hit ("Marketing Email Outreach Infrastructure") was read but not
logged — it is cold-email domain-warming infrastructure work, not email-marketing-platform work,
and was additionally stale (2 weeks unviewed) and highly competitive (50+ proposals). All of
cycle 17's open items were followed up on exactly as instructed. The Newsletter Specialist listing
(id 31) remains flat (13th cycle, rate never renders, no Hires field has ever appeared). The Brevo
CRM and Email Setup listing (id 40) is still stalled at Interviewing=4 for a **seventh** consecutive
cycle, but its buyer account showed its first movement in three cycles — 1→2 hires, 0→1 active —
which is noted plainly below without being over-read as a signal on this specific job. Reddit's
free-method scrape failed for a **13th** consecutive cycle. The German-market search surfaced
something different from the usual dead mirror — a freelancer's own service-offer ad, itself
already deleted/reserved — still zero actionable client postings for an **18th** consecutive
cycle. Contra (18 cycles) and freelance.de (12 cycles) were checked again and stay brief, per
instruction.

## Cycle 17 follow-ups

### Owner's pending decision (IMPORTANT) — "Email Deliverability Specialist for 3 Companies" (Upwork, id 72)

Rechecked per the task's explicit instruction. **No application package, draft, or proposal has
been prepared — that decision remains pending and is the owner's to make, not mine.** Plain status
update for whenever the owner does decide:

- **Still open.** Not closed, not withdrawn.
- **Interviewing: 0** — unchanged from cycle 17. The client has not started shortlisting.
- **Invites sent: 1, unanswered: 0** — unchanged from cycle 17.
- **No job-specific "Hires" field appears** on this listing's Activity panel (only
  Proposals/Last viewed/Interviewing/Invites render) — consistent with every prior cycle on this
  listing.
- **Last viewed by client: "last week"** (cycle 17 recorded "6 days ago" — the same recency,
  just rendered in a coarser bucket this time; not a fresh signal either way).
- **Client account unchanged**: $2.5K total spent, 9 hires, 5 active (same as cycle 17); hours
  logged ticked up 75→76 (routine, this client's other active contracts).
- Proposals still in the 20–50 band (unchanged).

**Bottom line: nothing about this cycle's check makes the owner's pending decision moot.** The
listing is exactly as open and exactly as under-the-radar (0 Interviewing, no Hires field) as it
was when flagged in cycle 17. If the owner wants to move on it, the window described in cycle 17
still appears to be open.

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — flat again, nothing to flag

Rechecked once more as a quiet status check, not a re-flag, per the owner's standing instruction.
Current state: **still open**. Hourly rate **still does not render** in the public scrape — the
**13th consecutive cycle** this has failed. No job-specific "Hires" field has ever appeared on
this listing's Activity panel, on this cycle's scrape or any prior one on file. Interviewing
unchanged at 2. Invites sent/unanswered unchanged at 0/0. Last viewed by client "4 days ago" (vs
"3 days ago" in cycle 17 — ordinary noise). Account-level figures: $69K total spent (flat), 36
hires (flat), 15 active (flat), hours rose again (2,030→2,039) — ongoing activity on this buyer's
other contracts, nothing new. No clear "Hires" signal and the listing is not gone — per the
owner's instruction, this is noted on the DB row and left at that, not retired and not
re-flagged.

### (b) Brevo CRM and Email Setup (id 40) — seventh consecutive Interviewing stall, but first account-level movement in three cycles

Rechecked with the listing's own Activity-on-this-job panel read directly, as in prior cycles: no
job-specific "Hires" line appears on it at all — only Proposals (20–50), Last viewed by client
("last week"), Interviewing, and Invites sent render. Interviewing is **still at 4** — now the
**seventh** consecutive cycle (12, 13, 14, 15, 16, 17, 18) at exactly 4, with no further climb.
Invites-sent/unanswered unchanged at 2/0. **One real change this cycle**: the "About the client"
account-level figures moved from "$15 total spent, 1 hire, 0 active" (stable across cycles 15–17)
to **"$15 total spent, 2 hires, 1 active"** — the first movement on this buyer's account in three
cycles. Stated plainly and not over-read: total spend is still flat at $15 (so this is not a large
new contract), and — critically — **Interviewing on this specific job is unchanged at 4 and no
job-specific Hires field appeared on it**, so this new hire most plausibly belongs to a *different*
job this same buyer posted, not this one. Noted on the DB row as the first account-level activity
in three cycles; tier not revised (`PAYMENT_TIMELINE_UNCERTAIN`), and this specific listing is not
treated as closed or advanced.

### (c) Reddit r/forhire — still blocked, no paid provider used

Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). A direct `firecrawl_scrape` attempt against the subreddit
listing page failed identically: *"Firecrawl can't scrape this site because it is currently not
supported."* This is the **13th consecutive cycle** this has failed via the free method. No cost
incurred, no new data gained, as expected. **Still awaiting the owner's decision** on whether the
paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — no genuinely new in-scope listing this cycle

Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The "Markerters wanted for sale of products email campaigns thank u" listing logged in cycle 16
(id 71) is still the same posting, now 13 days old / 26 proposals (vs cycle 17's 12 days/26 — flat
proposal count, routine aging). The recurring out-of-scope postings persist in substance: "Cold
Email Marketing Specialist" (the Dubai B2B tax-consultancy cold-outreach role, now aged to 6
days/24 proposals, up from 5 days/24); "I need an outreach marketing professional" (requiring
Instantly.ai and Meta Ads — both PROHIBITED per the claims register — now 4 days/34 proposals, up
from 3 days/33); and "B2B Lead Generation & Email Outreach for Established VO Artist" (now showing
2 days/32 proposals, up from 2 days/31 — ordinary feed movement). None of these three were
logged.

### (e) Contra (18 cycles), German-market search (18 cycles — something different turned up, still nothing actionable), and freelance.de (12 cycles)

All three were checked again this cycle, kept brief as instructed. Contra's featured-jobs page
again rendered real job cards, including the same "Email Marketing Specialist – Dual Campaigns for
Parents & School Leaders" card already on file (id 19, $25–40/hr) plus the same two recurring
non-Brevo listings ("Marketing Assistant for Launch Campaign," "Prepping Digital Assets Before
Launching Campaigns") — no genuinely new client email-marketing posting appeared. That makes **18
consecutive cycles** for Contra with no new genuine email-marketing lead.

The German-market search did **not** surface the usual freiguide.de-mirrored Kleinanzeigen.de
dead-mirror this cycle. Something different turned up instead: a direct Kleinanzeigen.de listing,
**"Biete: E-Mail-Marketing einrichten – Newsletter endlich starten"** (Düsseldorf, €850). On
inspection this is **not a client job posting at all** — "Biete" means a freelancer (Nina Mamsch)
is *offering* her own email-setup service (Brevo/ActiveCampaign, SPF/DKIM/DMARC, double opt-in),
i.e. a competitor's ad, not a hiring opportunity. It is additionally shown as **"Gelöscht" /
"Reserviert"** (deleted / reserved) on the page itself. So even setting the role-reversal aside,
there is nothing live here either. Net result: still **zero** actionable German-market
email-marketing opportunities, now the **18th** consecutive cycle, with the specific dead-mirror
pattern not recurring this time but a different kind of non-result taking its place.

freelance.de again surfaced only freelancer-portfolio/privacy-policy pages mentioning Brevo in
passing, no client project (Auftrag) posting. **12 consecutive cycles** confirming no reachable
client-posting section for this platform via search.

**Useme.com** was not re-run this cycle; cycle 16's finding (every listing on the English page 1
"Finished," the long-running Oliver Törnroth/Zoined posting gone) is assumed unchanged, consistent
with lower-priority sources not needing a fresh scrape every single cycle once a stable state is
confirmed.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none new this cycle. Carryover from cycles 5–17 unchanged:
"Email Deliverability Specialist for 3 Companies" (id 72), rechecked above — still open, still
awaiting the owner's go-ahead, not actioned.

## New candidates checked this cycle (2 logged, both REJECTED)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Email Marketing Specialist for Black Friday | Upwork | Qatar-based, no spend/hire history shown | **REJECTED** — likely quietly filled (stale last-viewed despite active interview funnel) |
| Email marketing Developer | Upwork | Australian retail agency ($67K spent, 86 hires, 19 active) | **REJECTED** — already hired (explicit "Hires: 1" field) + requires PROHIBITED tools (Klaviyo, Omnisend) |

### Why "Email Marketing Specialist for Black Friday" was rejected

$12–25/hr, Qatar-based client, member since April 2026, no total-spent/hires/active figures shown
at all (an essentially blank track record on this metric). On its face the skill match is fine —
generic list segmentation, re-engagement, and holiday sales-email work, no PROHIBITED-tool
conflict. The reject is a **staleness/quietly-filled signal, stated plainly rather than minimized**:
Interviewing is at 4 and 5 invites have been sent with 0 unanswered (i.e., the client has actively
engaged and gotten responses from every invite) — but the client **last viewed applicants four
weeks ago**. A hiring funnel that active combined with a client who hasn't looked in a month reads,
by this project's own established methodology (cycle 16's "check for closure signals beyond raw
proposal counts" fix), as a job that has most likely already been filled through the invite/
interview channel, with the public page simply not yet reflecting it. Applying now would mean
competing for a slot that in all likelihood no longer exists. Discounted honestly rather than
rounded up.

### Why "Email marketing Developer" was rejected

$5–20/hr, Melbourne retail-technology agency, a well-established client ($67K total spent, 86
hires, 19 active contracts — genuinely credible). This one is unambiguous: the listing's own
Activity panel shows **"Hires: 1"** rendering explicitly — the first time in this project's run
that a job-specific Hires field has actually appeared and shown a non-zero value (prior cycles'
checks on ids 31 and 40 established that this field often does *not* render at all; this listing
confirms it does render when a hire has genuinely happened). The job is filled, full stop.
Independently, the role also required **Klaviyo and Omnisend** experience — both PROHIBITED per
the claims register — so even had it still been open, it would have failed on skill-evidence
grounds alone. Logged for audit-trail completeness: a clean double-disqualifier, and useful
confirmation that the "Hires" field is a real, working signal on Upwork, not a field that simply
never renders.

### Hits read but not logged this cycle (closed, duplicate, scope-mismatch, or pure search noise)

- **"Marketing Email Outreach Infrastructure"** (Upwork, $207K-total-spent Australian client) —
  not an email-marketing-platform role; it is cold-outreach domain-warming/authentication
  infrastructure setup for an enterprise cold-email operation ("Expert" level required). Further
  disqualified on its own terms even if scope fit: 50+ proposals (the highest competition band),
  last viewed by client 2 weeks ago, Interviewing/Invites both at 0. Out of scope, not logged.
- **Freelancer.com**: fresh Brevo-specific and generic searches surfaced only listings already on
  file (ids 34, 27, 57 — same slugs, same projects) — no new-to-file URL this cycle.
- **Guru.com**: fresh Brevo-specific search surfaced only the listing already on file (id 70,
  unchanged tier). Kept on the source list for future cycles.
- The German-market Kleinanzeigen.de hit discussed in follow-up (e) above — not a client posting
  at all (a freelancer's own deleted/reserved service ad), not logged as an opportunity.

## Source coverage this cycle

- **Upwork**: re-scraped all three carried-over leads (the owner's pending-decision listing, and
  follow-ups (a) and (b)). Fresh Brevo-specific and generic searches surfaced 3 new-to-file URLs:
  2 logged as REJECTED (see table above), 1 read but not logged as a scope mismatch (see above).
- **Freelancer.com**: fresh searches surfaced no new-to-file URLs this cycle — all hits matched
  listings already on file under their existing slugs.
- **Guru.com**: fresh Brevo-specific search surfaced only the listing already on file (id 70,
  unchanged tier). Kept on the source list for future cycles.
- **PeoplePerHour**: page 1 only, per cycles 6–17's finding — no genuinely new in-scope listing
  this cycle (see follow-up (d)).
- **Contra**: 18th consecutive cycle with the same structural limitation — real featured-job
  cards render, but none new and email-marketing-relevant (see follow-up (e)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked at the subreddit level;
  paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query — 18th consecutive cycle with no
  live, actionable German-market opening; this cycle a different kind of non-result turned up (a
  freelancer's own deleted/reserved service ad) rather than the usual dead mirror (see follow-up
  (e)).
- **freelance.de**: tried the dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only portfolio/privacy-policy mentions of Brevo — 12th consecutive cycle
  confirming no reachable client-posting section for this platform via search.
- **Useme.com**: not re-run this cycle; cycle 16's finding assumed unchanged.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycles 13–17's treatment.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle, out of scope for
  this automated run, per the task instruction.

## System health

- Sources touched: 8 (Upwork, Freelancer.com, Guru.com, PeoplePerHour, Contra, Reddit [blocked, no
  paid provider], German-market direct search [including the follow-up check on the Kleinanzeigen.de
  hit it surfaced], freelance.de), plus Useme.com and the Indeed health-wellness angle assumed
  unchanged from cycle 16. Direct business prospecting flagged as out-of-scope-this-cycle rather
  than touched.
- Opportunities found and logged as full rows: 2 new (0 collisions with the existing 73 on file),
  both `REJECTED`. Database now holds 75 opportunities.
- The owner's pending-decision listing (id 72) and both carried-over tracked leads (ids 31, 40)
  were all re-checked and had notes appended: id 72 remains genuinely open with no closure signal
  (see the dedicated section above); id 31 saw no change worth flagging beyond ordinary
  account-level activity (13th consecutive cycle of the hourly-rate-never-renders oddity); id 40
  saw its first account-level movement in three cycles (1→2 hires, 0→1 active on the buyer's
  account), read plainly as most likely unrelated to this specific job given Interviewing stayed
  flat at 4 with no job-specific Hires field appearing. No tier was revised on any of the three.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 13th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra (18th) and freelance.de (12th) each
  logged another consecutive cycle of the same structural limitations already established in
  prior cycles. The German-market search's usual dead-mirror pattern did not recur this cycle, but
  a different non-actionable result (a deleted/reserved competitor service ad) took its place —
  still zero live client postings, now an 18th consecutive cycle.
- This cycle's clearest lesson: the "Email marketing Developer" listing's explicit, rendering
  "Hires: 1" field is the first direct confirmation in this project's run that Upwork's
  job-specific Hires field *does* render when a hire has actually happened — it simply has not
  happened yet on any of the long-tracked listings (ids 31, 40, 72) where it has never appeared.
  That strengthens confidence in the absence-of-the-field reasoning already applied to those three
  listings across many cycles: it is not a field that silently never renders, it is a field that
  renders specifically when there is something to report.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 17**: "Email Deliverability Specialist for 3
   Companies" (Upwork, id 72) remains open, unfilled, and well-matched. Nothing has changed that
   would make this decision moot — it is exactly as live now as it was when flagged. No
   application package has been prepared. Awaiting the owner's go-ahead.
2. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open,
   now at a 13th consecutive blocked cycle on the free method.
3. **No action needed** on the Newsletter Specialist listing beyond the notes already recorded.
   The Brevo CRM and Email Setup listing's buyer account showed its first movement in three
   cycles (see follow-up (b)) — worth a glance next cycle to see if it develops further, but not
   urgent. Separately, the owner's still-open call from cycle 11 on whether to keep checking
   Contra, the German-market search angle, and freelance.de each cycle (18, 18, and 12 consecutive
   cycles with nothing new/live and actionable) remains unchanged and unforced.
