# Discovery Cycle 10 — 2026-11-20

Regular run following cycle 9 (2026-11-19). Picks up cycle 9's open items and runs fresh discovery
searches.

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
  way (10th cycle running) despite a genuine German-market client being found (see below).
- A/B testing remains an unresolved CONFLICT — one listing this cycle would have required it
  directly; flagged as a disqualifier rather than worked around.
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com/PeoplePerHour opportunity scored this cycle.
- Carried forward from cycle 9's finding: a "Brevo" keyword hit is not always the ESP platform, and
  a title match alone was not treated as a scope match anywhere this cycle (no false-positive like
  cycle 9's "client's own brand name" case recurred, but each listing's actual text was checked).

Checked `db/email_marketing_system.db` first — 45 opportunities on file from cycles 1-9. Nothing
below duplicates an existing URL.

## Headline

**No clean new P0 or P1 opportunity this cycle.** Eight new candidates were found and logged (1
PeoplePerHour, 5 Upwork, 2 Freelancer.com) — all **REJECTED**, for a mix of reasons: a listing that
already shows a hire made against it, extreme proposal competition, required PROHIBITED tools
(Apollo, Mailchimp, HubSpot, Klaviyo, Zapier/Make.com/N8N, Lemlist/Instantly/Expandi), an
experience-floor mismatch (2-4 years required vs. Kaeto's ~10 months), a brand-new
zero-track-record client, and one listing already closed at discovery. The best-credentialed
client found this cycle (a well-established German marketing agency, 7+ years on Upwork, $45K
spent) still failed cleanly on required unevidenced tools. All four of cycle 9's open items were
followed up on exactly as instructed. Not recommending an application package.

## Cycle 9 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo (id 31) — rechecked once, fully flat
Per the owner's standing instruction (flagged twice already — their call to act on, not something
to repeat again), this was checked once more as a quiet status check, not a re-flag. Current
state: **still open**. Hourly rate **still does not render** in the public scrape — the 5th
consecutive cycle this has failed. Interviewing is still **3** — flat for a 3rd consecutive cycle
(since cycle 7's 0→3 jump). Proposals still 20–50. Last viewed by client: "3 days ago" (vs "2 days
ago" in cycle 9 — ordinary noise, not a signal). For the first time, **every** client metric is
fully unchanged from the prior cycle: $68K total spent, 35 hires, 16 active, 1,980 hours logged —
identical to cycle 9's snapshot, with zero movement on anything. Noted on the DB row (id 31) and
left at that; not re-scored, not re-flagged as "needs attention" in this summary.

### (b) Brevo CRM and Email Setup (id 40) — rechecked, slightly more active but tier unchanged
Not required by the owner's standing instruction, but checked for completeness as the second-best
lead on file, per the task's explicit ask. Still open. The hourly rate now renders clearly
($10–28/hr, consistent with the figure already on file — last cycle's note didn't flag a render
issue here, so this isn't a new fix, just a clean read). Client still shows 1 hire, 1 active — no
new hires. **Interviewing moved from 2 to 3, and invites-sent appeared for the first time (2 sent,
0 answered)** — the first sign of outbound activity from this client since discovery. Proposals
still 20–50. This is a genuine (if small) change, but not enough to revise the tier: the client
account is still only about 10 days old with the same thin 1-hire history that kept this below the
P1 bar last cycle. Tier left at `PAYMENT_TIMELINE_UNCERTAIN`; worth a second look if a real
hire/review history develops.

### (c) Reddit r/forhire — direct scrape attempted again, still blocked, no paid provider used
Per instruction, did **not** use the `scrapecreators` Alexandria provider again without the
owner's go-ahead (open since cycle 7). Fell back to a direct `firecrawl_scrape` attempt against
the subreddit listing page. Failed identically: *"Firecrawl can't scrape this site because it is
currently not supported."* This is the **5th consecutive cycle** this has failed via the free
method. No cost incurred, no new data gained, as expected. **Still awaiting the owner's decision**
on whether the paid `scrapecreators` route is worth adopting going forward.

### (d) PeoplePerHour page 1 — rechecked, one new-to-file URL (rejected as stale)
Only page 1 checked, per the confirmed finding that `?page=` only paginates the closed archive. The
"HTLM Email Design" listing (already on file, id 7) reappeared on page 1 — confirmed duplicate, no
action needed. One genuinely new-to-file URL surfaced: "Help with Brevo" (Mick O., UK). It appears
under the category page's **"Past Projects"** section, not the current/latest listings at the top
— posted roughly 2 months before this discovery with 6 proposals already on record and no visible
client activity since 30 Sep 2026. Logged and rejected as stale (see table below). 5th cycle
running with no genuinely new, live candidate from this source.

### (e) Direct business prospecting — not run, same reasoning as cycles 8-9
Per the master prompt §4.3/§12 workstream's own method, confirming a gap ends in drafting a short,
personalized cold-outreach message — out of scope for this cycle's no-drafting instruction. Not
attempted here; remains the separate, manual, owner-reviewed workstream it has been since cycle 3
(`evidence/prospects-medical-wellness.md`).

### (f) "Brevo" keyword-match discipline — carried forward, applied
Every new candidate's actual job text was read before counting a "Brevo" hit as a scope match, per
cycle 9's lesson. No client-brand-name false positive recurred this cycle, but two listings turned
out to treat Brevo as only one of several optional/acceptable ESPs rather than a firm requirement
(the WordPress/newsletter-launch job and the cold-email-campaign job) — both noted explicitly in
their rejection reasons below rather than scored as if Brevo were the confirmed platform.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (carryover from cycles 5–9 unchanged, see (a)
above)

## New candidates checked this cycle (8)

| Opportunity | Source | Client | Outcome |
|---|---|---|---|
| Help with Brevo | PeoplePerHour | UK, 91%/14 reviews, established small buyer | **REJECTED** — stale, listed under "Past Projects" |
| Fix Brevo/Mailgun (Cybersecurity FYP) | Upwork | Pakistan, <1 month old account | **REJECTED** — already shows 1 hire; academic one-off |
| Manage email campaigns | Upwork | US, established (7+ yrs, $19K spent) | **REJECTED** — Apollo named as acceptable tool; heavy competition |
| Email Marketing Manager | Upwork | Slovenia agency, established | **REJECTED** — 2-4 yrs required; A/B testing + prohibited outreach tools |
| WordPress & Newsletter Setup (B2B Advisory) | Upwork | US, 8-day-old account, no history | **REJECTED** — 50+ proposals vs. zero track record; WordPress skill unevidenced |
| CRM and E-Mail Marketing Manager | Upwork | Germany agency, established (7+ yrs, $45K spent) | **REJECTED** — Mailchimp/HubSpot/Zapier-Make-N8N all required |
| Squarespace-Brevo Signup Integration | Freelancer.com | Australia, 4+ yr account, 0 reviews | **REJECTED** — 229 proposals, closes in 1 day |
| Urgent: Social Media & Email Marketing Expert | Freelancer.com | India, new account | **REJECTED** — already closed; 2+ yrs + portfolio requirement |

### Why each was rejected

- **Help with Brevo** ($10 EUR starting bid, ongoing ad hoc): a small, credible UK client already
  using Brevo for direct mail and needing bounce/list-hygiene help — on its face a reasonable skill
  match. But the listing sits in PeoplePerHour's "Past Projects" section rather than the
  current/latest section, was posted roughly 2 months before this discovery, already has 6
  proposals on record, and the client's own "last project" date (30 Sep 2026) shows no recent
  activity. The brief also later asks for "Google maps scraper activities" — outside email-marketing
  scope and a mild red flag in its own right. Doesn't clear the payment-horizon test with any
  confidence.
- **Fix Brevo/Mailgun — Cybersecurity University FYP** (hourly, rate unrendered): a genuine Brevo
  deliverability/DNS scope (SPF/DKIM/DMARC on a subdomain), but the listing itself shows **"Hires:
  1"** — a contract has already started on this exact posting, so it's effectively filled even
  though still publicly reachable. Separately, it's a one-off student academic project, not a
  sustainable freelance relationship.
- **Manage email campaigns** (hourly, rate unrendered, $19K-spend client): names Apollo as one of
  four acceptable tools alongside Brevo, Insightly, and Gmass — Apollo is explicitly PROHIBITED per
  the claims register, and the client hasn't committed to Brevo specifically. The scope (25,000
  purchased/prospected addresses, drip campaigns) reads as cold-email list management rather than
  lifecycle/newsletter marketing in this project's chosen niche, and the activity signals (6
  interviewing, 25 invites sent, 17 unanswered) show the client already deep into its hiring
  funnel.
- **Email Marketing Manager** ($12–15/hr, Slovenia agency): a credible, established client, but
  requires 2–4 years of hands-on ESP experience — well past Kaeto's actual ~10-month tenure and
  this project's own ~2-year filter — plus Figma-to-HTML/CSS production skill that isn't an
  evidenced claim, plus running/reporting structured A/B tests (a direct test of the unresolved A/B
  testing CONFLICT), plus "nice to have" Lemlist/Instantly/Apollo/Expandi outreach tools, all
  PROHIBITED. A clean multi-reason reject, not a close call.
- **WordPress & Email Newsletter Setup (B2B Executive Advisory)** ($500 fixed): 50+ proposals
  already on record against a client account only 8 days old with **zero** spend/hire history — a
  severe competition signal stacked on a severe credibility/payment-risk signal. Brevo is only one
  of three ESPs the client would accept (Kit or Mailchimp equally fine), not a confirmed
  requirement, and the core deliverable (a WordPress landing page with signup forms) rests on a
  skill not evidenced for Kaeto.
- **CRM and E-Mail Marketing Manager** ($20–30/hr, Germany agency): the most credible client found
  this cycle — 7+ years on Upwork, $45K total spent, 31 hires, a mid-sized established company —
  with a genuine Brevo scope. But the stated qualifications explicitly require hands-on experience
  across Mailchimp and HubSpot (named directly, not as alternatives), plus required middleware
  experience in Zapier, Make.com, or N8N under "Technical Skills." Every one of these is explicitly
  PROHIBITED per the claims register; Brevo is only one of five named platforms. The same
  multi-tool disqualifier pattern as cycle 9's Softgile listing. Worth noting: English is the
  stated working-communication language here, so this genuinely German-market employer doesn't
  actually test the unresolved German-proficiency conflict either way.
- **Squarespace-Brevo Signup Integration** ($25–50 AUD/hr): a genuine, narrow Brevo API-integration
  scope, but **229 competing proposals** already on record (average bid $34 AUD/hr) with the
  listing closing within **1 day** of discovery — an extreme, effectively unwinnable competition
  signal regardless of skill match. Also closer to a lightweight developer/API task than an
  email-marketing strategy role.
- **Urgent: Social Media & Email Marketing Expert** (₹12,500–37,500 fixed): already **closed** at
  discovery (posted 15 days earlier, 29 proposals on record). Would have failed on scope even if
  open: requires 2+ years' experience and a mandatory social-media-management portfolio Kaeto
  doesn't have, and names Mailchimp and Klaviyo as acceptable tools alongside Brevo — both
  explicitly PROHIBITED.

## Source coverage this cycle

- **Upwork**: re-scraped both carried-over leads (see follow-ups (a) and (b)). Fresh Brevo-specific
  and generic searches surfaced 5 new-to-file URLs, all closed/rejected (see table above) — the
  highest single-cycle Upwork yield of new candidates so far, though none qualified.
- **Freelancer.com**: fresh Brevo-specific and generic searches surfaced 2 new-to-file URLs, both
  rejected (extreme competition on one, already-closed plus scope mismatch on the other). Other
  hits matched URLs already on file or were freelancer self-promotion/portfolio pages.
- **PeoplePerHour**: page 1 only, per cycles 6–9's finding — one new-to-file candidate, rejected as
  stale (see follow-up (d)).
- **Contra**: 10th consecutive cycle with the same structural limitation — search surfaces only
  `/hire/brevo-freelancers`, `/hire/constantcontact-freelancers`-style directory pages and
  freelancer self-promotion/community posts, never a genuine client job posting.
- **Reddit r/forhire**: see follow-up (c) — direct scrape still blocked; paid provider not used
  this cycle per instruction.
- **German-market search**: re-ran the German-language query — 10th consecutive cycle with no live
  German-market opening found via this search angle; results remain freelancer profile/portfolio
  pages (freelance.de), Fiverr gig listings, and the Brevo careers page. Notably, a genuine
  German-market client (the Idstein, Germany agency above) was found this cycle, but via a
  Brevo-specific Upwork search, not via this dedicated angle — logged under Upwork and rejected on
  required-tools grounds, not a German-market search success.
- **freelance.de**: tried a site-scoped query again aimed at a genuine client project/Auftrag
  posting. Surfaced only freelancer profile pages (individuals advertising their own Brevo/E-Mail-
  Marketing skills) — no client project listing at all. 4th consecutive cycle confirming no client
  project-posting section is reachable for this platform via search.
- **Useme.com**: re-checked the English page 1 only this cycle. Unchanged from cycles 7–9: same
  Oliver Törnroth/Zoined posting (now 22 days left, down from 23 in cycle 9, 24 in cycle 8, 25 in
  cycle 7), still the only open listing, still zero live Brevo listings. Polish page 2 not
  re-checked this cycle.
- **Indeed / health-wellness + Brevo search angle**: not re-run as a dedicated search this cycle;
  covered instead by the broader generic email-marketing search pass, which surfaced only
  job-board aggregator/landing pages, consistent with prior cycles' finding.
- **Direct business prospecting** (master prompt §4.3/§12): not run this cycle — same reasoning as
  cycles 8–9 (see follow-up (e) above).

## System health

- Sources touched: 8 (Upwork, Freelancer.com, PeoplePerHour, Contra, Reddit [blocked, no paid
  provider], German-market direct search, freelance.de, Useme.com), plus the Indeed health-wellness
  angle folded into the generic search pass. Direct business prospecting flagged as
  out-of-scope-this-cycle rather than touched.
- Opportunities found and logged as full rows: 8 new (0 collisions with the existing 45 on file),
  all `REJECTED`. 0 reached P0/P1. Database now holds 53 opportunities.
- The two carried-over leads (the P1 Newsletter Specialist listing and the
  `PAYMENT_TIMELINE_UNCERTAIN` Brevo CRM and Email Setup listing) were both re-checked. The former
  is fully flat for the first time (per the owner's standing instruction, not re-flagged); the
  latter shows its first sign of outbound client activity (interviewing 2→3, invites-sent
  appeared) but the tier was not revised.
- No automation failures. Reddit's scrape restriction held on the free method for a 5th
  consecutive cycle; the paid-provider question from cycle 7 remains open and unanswered, so it
  wasn't used again. Contra, freelance.de, German-market search, and Useme.com page 1 each logged
  another consecutive cycle of the same structural limitations already established in prior
  cycles.
- This cycle's highest-volume source was Upwork (5 new candidates), and it also produced the
  single most credible client found to date (the Germany-based agency, 7+ years/$45K spent) — but
  that listing's required-tools list (Mailchimp, HubSpot, Zapier/Make.com/N8N) made it a clean
  reject regardless of client quality. Worth remembering going forward: client credibility and
  skill-match are independent axes, and a strong client doesn't offset a hard tool-requirement
  disqualifier.

## Recommended next 3 actions

1. **Still awaiting the owner's decision from cycle 7**: whether to adopt the `scrapecreators`
   Reddit provider (small real cost per call, one demonstrated working access path, zero relevant
   posts found the one time it was tried). Not re-raised as urgent — just restating that this
   decision is still open and nothing has changed about it.
2. **No action needed on the Newsletter Specialist listing this cycle** — per the owner's own
   instruction, it's been flagged enough; the state is unchanged (still open, rate still
   unconfirmed, interviewing flat, and now every client metric is fully flat too) and this project
   will keep noting it quietly rather than re-escalating it.
3. **Decide whether direct business prospecting should be folded into this automated cycle** —
   unchanged from cycles 8–9's note: it currently can't produce a scorable result without drafting
   outreach, which is outside this cycle's standing instructions; if the owner wants it covered
   automatically, that needs an explicit scope call, not an interpretation on this project's part.
