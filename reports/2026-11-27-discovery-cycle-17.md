# Discovery Cycle 17 — 2026-11-27

Regular run following cycle 16 (2026-11-26). Picks up cycle 16's open items and runs fresh
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
  way (17th cycle running).
- A/B testing remains an unresolved CONFLICT — no listing this cycle directly tested it.
- TRNC payment-routing caveats from `evidence/payment-routing.md` apply to every new candidate
  scored this cycle (both new finds this cycle are Upwork); none independently tested for TRNC.

Checked `db/email_marketing_system.db` first — 71 opportunities on file from cycles 1–16. Nothing
below duplicates an existing URL.

## Headline

**One clean candidate this cycle, flagged for the owner's decision — not yet actioned.** Two new
candidates were found and logged this cycle, both on Upwork. **"Email Deliverability Specialist
for 3 Companies"** is escalated to **P1**: pure deliverability/domain-reputation audit work (the
project's single strongest documented skill area) for a small but genuinely established, currently
active client, with a hiring funnel that is *not* yet advanced (Interviewing: 0, one unanswered
invite, no job-specific "Hires" field rendering at all). This is flagged below for the owner's
go-ahead before any application package is prepared — per the task's own instruction, nothing
further has been done on it. The second new find, **"B2B Content Creator – LinkedIn & Email
Marketing"** (ShelfPerfect, Singapore), was REJECTED on skill mismatch: the role is mostly LinkedIn
content writing and Canva graphic design, with only a minor Brevo-or-similar email component, and
pay is thin for the described six-deliverable monthly scope. All of cycle 16's open items were
followed up on exactly as instructed. The Newsletter Specialist listing (id 31) remains flat (12th
cycle, rate never renders, no Hires field has ever appeared). The Brevo CRM and Email Setup listing
(id 40) is now stalled at Interviewing=4 for a **sixth** consecutive cycle; checking its own
Activity panel directly (per the cycle-16 methodology fix) confirms no job-specific Hires field
renders on it either. Reddit's free-method scrape failed for a **12th** consecutive cycle. The
German-market freiguide.de/Kleinanzeigen.de dead-mirror pattern recurred for a **fourth**
consecutive cycle (confirmed structural, not re-described). Contra (17 cycles) and freelance.de (11
cycles) were checked again and stay brief, per instruction.

## Cycle 16 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — flat again, nothing to flag
Rechecked once more as a quiet status check, not a re-flag, per the owner's standing instruction.
Current state: **still open**. Hourly rate **still does not render** in the public scrape — the
**12th consecutive cycle** this has failed. Checked explicitly this cycle whether a job-specific
"Hires" field has ever appeared on this listing's own Activity panel: it has **not**, on this
cycle's scrape or any prior one on file — only Proposals/Last viewed/Interviewing/Invites render.
Interviewing unchanged at 2. Invites sent/unanswered unchanged at 0/0. Last viewed by client "3
days ago" (vs "2 days ago" in cycle 16 — ordinary noise). Account-level figures: $69K total spent
(flat), 36 hires (flat), 15 active (flat), hours rose again (2,026→2,030) — ongoing activity on
this buyer's other contracts, nothing new. No clear "Hires" signal and the listing is not gone —
per the owner's instruction, this is noted on the DB row and left at that, not retired and not
re-flagged.

### (b) Brevo CRM and Email Setup (id 40) — sixth consecutive stall, Hires field checked directly
Rechecked with the cycle-16 methodology fix applied explicitly: the job's own Activity-on-this-job
panel was read directly rather than inferring from proposal/interviewing counts, and **no
job-specific "Hires" line appears on it at all** — only Proposals (20–50), Last viewed by client
("last week"), Interviewing, and Invites sent render. Result: **it has still not moved on this
listing**. Still open. Rate unchanged ($10–28/hr). **Interviewing is still at 4** — now the
**sixth** consecutive cycle at exactly 4 (cycles 12, 13, 14, 15, 16, 17). Invites-sent/unanswered
unchanged at 2/0. The "About the client" account-level figures ($15 total spent, 1 hire, 0 active)
are identical to cycle 16 — a **third** consecutive cycle of total stability on both the listing
and its buyer account. Noted on the DB row, not treated as closure, tier not revised
(`PAYMENT_TIMELINE_UNCERTAIN`).

### (c) Reddit r/forhire — still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). A direct `firecrawl_scrape` attempt against the subreddit
listing page failed identically: *"Firecrawl can't scrape this site because it is currently not
supported."* This is the **12th consecutive cycle** this has failed via the free method. No cost
incurred, no new data gained, as expected. **Still awaiting the owner's decision** on whether the
paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — no genuinely new in-scope listing this cycle
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive.
The "Markerters wanted for sale of products email campaigns thank u" listing logged last cycle (id
71) is still the same posting, now 12 days old / 26 proposals (unchanged from cycle 16's snapshot
— no state change to log). The recurring out-of-scope postings persist in substance: "Cold Email
Marketing Specialist" (the Dubai B2B tax-consultancy cold-outreach role, now aged to 5 days/24
proposals, up from 4 days/24); "I need an outreach marketing professional" (requiring Instantly.ai
and Meta Ads — both PROHIBITED per the claims register — now 3 days/33 proposals); and "B2B Lead
Generation & Email Outreach for Established VO Artist" (now showing 16 hours/31 proposals in this
cycle's relevance-sorted pull, essentially flat against cycle 16's 2 days/30 proposals — read as
ordinary feed-ordering variance, not a re-post). None of these three were logged.

### (e) Contra (17 cycles), German-market search (17 cycles — dead-mirror pattern now in its
fourth occurrence), and freelance.de (11 cycles)
All three were checked again this cycle, kept brief as instructed. Contra's featured-jobs page
again rendered real job cards, including the same "Email Marketing Specialist – Dual Campaigns for
Parents & School Leaders" card already on file (id 19, $25–40/hr) plus the same two recurring
non-Brevo listings ("Marketing Assistant for Launch Campaign," "Prepping Digital Assets Before
Launching Campaigns") — no genuinely new client email-marketing posting appeared. That makes **17
consecutive cycles** for Contra with no new genuine email-marketing lead.

The German-market search surfaced the same `freiguide.de`-mirrored Kleinanzeigen.de classified,
"BREVO Newsletter einrichten." Checking the original Kleinanzeigen.de URL directly again returned
"Die gewünschte Anzeige ist nicht mehr verfügbar" (the ad is no longer available), with the
category page showing only unrelated Dresden-area service listings. This is now the **fourth**
consecutive cycle (14, 15, 16, 17) this exact dead-mirror pattern has occurred. Per the owner's
instruction, this stays **confirmed structural** and is not re-described as a fresh finding. That
makes **17 consecutive cycles** for the German-market search with nothing live and actionable.

freelance.de again surfaced only the same freelancer-directory page (Brevo-Freelancer finden) plus
Fiverr/Upwork hire-page noise — no client project posting. **11 consecutive cycles** confirming no
reachable client-posting section for this platform via search.

**Useme.com** was not re-run this cycle; cycle 16's finding (every listing on the English page 1
now "Finished," the long-running Oliver Törnroth/Zoined posting gone) is assumed unchanged,
consistent with lower-priority sources not needing a fresh scrape every single cycle once a stable
state is confirmed.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — one found this cycle: "Email Deliverability Specialist for 3 Companies"
(see below). Carryover from cycles 5–16 unchanged (see (a) above).

## New candidates checked this cycle (2 logged)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Email Deliverability Specialist for 3 Companies | Upwork | Small, active US client ($2.5K spent, 9 hires, 5 active, member since 2020) | **P1 — flagged for owner decision** |
| B2B Content Creator – LinkedIn & Email Marketing (Long-Term Freelance) | Upwork | ShelfPerfect, Singapore retail-tech ($951 spent, 5 hires, 1 active) | **REJECTED** — skill mismatch (LinkedIn/Canva, not Brevo depth) + low pay for scope |

### Why "Email Deliverability Specialist for 3 Companies" is flagged, not yet actioned

- **Skill match**: pure email deliverability and domain-reputation audit work across three
  accounts — exactly the project's single best-documented skill area (SPF/DKIM/DMARC-adjacent
  audit/remediation work, the same category HIBARR experience sits in). No specific platform is
  named, so there is no PROHIBITED-tool conflict.
- **Client credibility**: small but real and currently active — member since 2020 (5+ years),
  $2.5K total spent, 9 hires, **5 active contracts right now**, 75 hours logged. This is a Sales &
  Marketing small business actually running concurrent work, not a brand-new or dormant account.
- **Competition — the decisive difference from this cycle's and prior cycles' rejected
  deliverability leads**: Interviewing is at **0** (not advancing), only **1 invite sent and still
  unanswered**, and the job's own Activity-on-this-job panel shows **no "Hires" field at all** —
  this listing is not functionally closed, unlike several recent Upwork finds that looked open on
  proposal counts alone but had already quietly filled. 20–50 proposals is still real competition,
  stated plainly rather than minimized, but the client has not yet begun shortlisting.
- **Compensation and payment timeline**: $10–28/hr (Upwork hourly, weekly billing once hired) —
  modest, not premium, but viable; fits the P1 (8–30 day) payment-horizon band once hired and
  through Upwork's standard hourly payment cycle.
- **Discounts applied, not rounded away**: last viewed by client "6 days ago" is mildly stale —
  not fresh, not dead; the rate band is on the lower end of what this project's deliverability
  skill set could reasonably command; and the standing TRNC payment-routing caveat from
  `evidence/payment-routing.md` applies uniformly here as it does to every Upwork opportunity in
  this project, and remains unresolved.

**Per master prompt §11.3 and the task's own instruction, no proposal has been drafted, nothing
submitted, and no contact made on this listing.** It is flagged here for the owner's explicit
go-ahead before any application package work begins.

### Why "B2B Content Creator – LinkedIn & Email Marketing" was rejected

ShelfPerfect (Singapore retail-tech, $180–250/month fixed, ongoing) wants a freelancer to produce 4
B2B LinkedIn posts (written copy plus branded Canva graphics/carousels) and 2 email marketing
campaigns per month, scheduled "in Brevo or a similar platform." The Brevo component is real and
would be acceptable on its own, but it is a minor part of a role whose core ask — LinkedIn content
writing and hands-on Canva graphic design — is not supported by the claims register, which
documents Brevo platform depth (deliverability, segmentation, lifecycle automation), not social
content design. The application itself requires a self-recorded 2–3 minute portfolio video walking
through a LinkedIn post and an email campaign the applicant personally designed — a credibility bar
this project cannot honestly meet. Combined with thin pay ($180–250/month for six recurring
monthly deliverables across two disciplines), this is a clean skill-mismatch-plus-compensation
reject, not a borderline one.

### Hits read but not logged this cycle (closed, duplicate, or pure search noise)

- **"Brevo Expert for Creative Email Mailings"** (Upwork) — already on file (id 60); re-surfaced by
  this cycle's fresh search, not a new candidate.
- Several **Freelancer.com** hits were country-subdomain mirrors of URLs already on file under the
  plain `www.freelancer.com` domain (`vn.freelancer.com`, `fr.freelancer.com` — same slugs, same
  underlying projects as ids 43 and 45), plus two freelancer user-portfolio pages (not job
  listings).
- **"Brevo and Hubspot Client Engagement Assistant – 15/07/2026" (`...-40583685`)** (Freelancer.com)
  — a second, extremely-low-pay ($2–8/hr) repost from the **same client** behind the already-logged
  id-36 listing, found **Closed**, posted 4 months ago. Pure search noise, not logged.
- **"Teach B2B Sales & Cold Email"** (Guru.com) — a teaching/coaching role around cold-email
  outreach, not email-platform specialist work. Out of scope, not logged.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-specific
  and generic searches surfaced 2 new-to-file URLs, one escalated to P1 and flagged, one REJECTED
  (see table above).
- **Freelancer.com**: fresh searches surfaced no new-to-file *live* URLs this cycle — several hits
  were country-subdomain mirrors of listings already on file, plus one closed, extremely-low-pay
  repost from an already-logged client (pure noise, not logged).
- **Guru.com**: a fresh Brevo-specific search surfaced only the listing already on file (id 70,
  unchanged tier) plus one unrelated teaching role (out of scope, not logged). Kept on the source
  list for future cycles.
- **PeoplePerHour**: page 1 only, per cycles 6–16's finding — no genuinely new in-scope listing
  this cycle (see follow-up (d)).
- **Contra**: 17th consecutive cycle with the same structural limitation — real featured-job
  cards render, but none new and email-marketing-relevant (see follow-up (e)).
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked at the subreddit level;
  paid provider not used this cycle per instruction.
- **German-market search**: re-ran the German-language query and the follow-up check on the hit it
  surfaced — 17th consecutive cycle with no live, actionable German-market opening; the
  dead-mirror pattern recurred for a fourth consecutive cycle, confirmed structural (see follow-up
  (e)).
- **freelance.de**: tried the dedicated query again aimed at a genuine client project/Auftrag
  posting. Surfaced only directory/hire-page noise — 11th consecutive cycle confirming no
  reachable client-posting section for this platform via search.
- **Useme.com**: not re-run this cycle; cycle 16's finding assumed unchanged.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle,
  consistent with cycles 13–16's treatment.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle, out of scope for
  this automated run, per the task instruction.

## System health

- Sources touched: 9 (Upwork, Freelancer.com, Guru.com, PeoplePerHour, Contra, Reddit [blocked, no
  paid provider], German-market direct search [including the follow-up check on
  freiguide.de/Kleinanzeigen.de], freelance.de), plus Useme.com and the Indeed health-wellness
  angle assumed unchanged from cycle 16. Direct business prospecting flagged as out-of-scope-this-
  cycle rather than touched.
- Opportunities found and logged as full rows: 2 new (0 collisions with the existing 71 on file) —
  1 escalated to `P1` and flagged, 1 `REJECTED`. Database now holds 73 opportunities.
- The two carried-over leads were both re-checked: the Newsletter Specialist listing (id 31) saw
  no change worth flagging beyond ordinary account-level activity (12th consecutive cycle of the
  hourly-rate-never-renders oddity, and no job-specific Hires field has ever appeared on it) —
  noted, not re-flagged. The Brevo CRM and Email Setup listing (id 40), checked with its own
  Activity panel read directly for a Hires field per the cycle-16 methodology fix, confirmed
  **no such field renders** and is now stalled for a **sixth** consecutive cycle at
  Interviewing=4, with account-level figures unchanged for a third consecutive cycle. Neither tier
  was revised.
- No automation failures beyond the expected, already-tracked ones. Reddit's scrape restriction
  held on the free method for a 12th consecutive cycle; the paid-provider question from cycle 7
  remains open and unanswered, so it wasn't used again. Contra (17th) and freelance.de (11th) each
  logged another consecutive cycle of the same structural limitations already established in
  prior cycles. The German-market search's dead-mirror pattern recurred for a fourth consecutive
  cycle, remaining confirmed structural per the owner's instruction.
- This cycle's clearest lesson, applying the cycle-16 methodology fix in practice: checking a
  listing's own "Hires" field directly (not just proposal/interviewing counts) worked both ways
  this cycle — it confirmed id 40 ("Brevo CRM and Email Setup") has no hidden closure signal
  despite its long interviewing stall, and it confirmed this cycle's flagged P1 candidate ("Email
  Deliverability Specialist for 3 Companies") is genuinely open rather than quietly filled. The
  field's *absence* is itself informative, not just its presence.

## Recommended next 3 actions

1. **New this cycle — awaiting owner go-ahead**: "Email Deliverability Specialist for 3 Companies"
   (Upwork) is a clean, currently-open, well-matched P1 candidate — strong skill match, credible
   active client, no disqualifying competition or closure signal. Flagged per the task's own
   instruction; no application package has been prepared. Awaiting the owner's decision on
   whether to proceed.
2. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider. Not re-raised as urgent — just restating that this decision is still open,
   now at a 12th consecutive blocked cycle on the free method.
3. **No action needed** on the Newsletter Specialist listing or the Brevo CRM and Email Setup
   listing this cycle beyond the notes already recorded. Separately, the owner's still-open call
   from cycle 11 on whether to keep checking Contra, the German-market search angle, and
   freelance.de each cycle (17, 17, and 11 consecutive cycles with nothing new/live and
   actionable) remains unchanged and unforced.
