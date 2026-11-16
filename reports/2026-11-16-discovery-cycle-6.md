# Discovery Cycle 6 — 2026-11-16

Regular daily run following cycle 5 (2026-11-15, the consolidated catch-up for a 14-firing
backlog). This cycle picks up cycle 5's three open items and runs fresh discovery searches.

Scope per the recurring discovery mandate: job-board/freelance-opportunity discovery only. No
outreach, proposals, or CVs were drafted; nothing was submitted or applied to; no one was
contacted. Discovery, verification, scoring, DB updates, and reporting only, per master prompt
§11.3.

Read first, per protocol: `evidence/claims-register.md` and `evidence/payment-routing.md`. Key
things carried into scoring this cycle, unchanged from cycle 5:
- Brevo remains the one platform with strong, consistent documented evidence.
- Klaviyo, Make.com, Zapier, n8n, and Mailchimp remain PROHIBITED claims; HubSpot hands-on
  experience is also PROHIBITED (not just a "live posting" caveat — it's in the claims register's
  §5 "do not claim" list). Both came up again this cycle (see Useme.com candidate below).
- German proficiency remains an unresolved CONFLICT — no live posting this cycle tested it either
  way (sixth cycle running).
- TRNC payment-routing caveats from `evidence/payment-routing.md` carried through unchanged for
  every Upwork/Freelancer.com opportunity, and a *new* unresolved payment question surfaced this
  cycle for Useme.com (see below).

Checked `db/email_marketing_system.db` first — 36 opportunities on file from cycles 1-5. Nothing
below duplicates an existing URL.

## Headline

**No new P0 or P1 opportunities this cycle. 2 new candidates fully checked and rejected. All
three of cycle 5's open items were followed up on and closed out** (one unresolved by design —
the rate still won't render — two fully resolved). Not recommending an application package.

## Cycle 5 follow-ups

### (a) Newsletter Specialist for Campaigns / Brevo — rate still unconfirmed
Re-scraped the listing
(https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/)
specifically to check whether the hourly rate renders this time. **It still does not.** Everything
else is essentially unchanged from cycle 5: last viewed by client 4 days ago (was 3 days), 1,973
hours logged (was 1,972), still 20-50 proposals, still 0 interviewing, still $65K total
spent/34 hires/15 active for the client. This remains the strongest-looking lead on file, and it
remains **not a clean recommendation** — the rate is the one fact that would make or break it, and
it is still not visible without an Upwork login this session doesn't have. No change to its score
or P1 tier; a note was appended to its DB row (id 31) recording this re-check rather than
re-scoring it on no new information.

### (b) PeoplePerHour pages 5-7 — swept, category now fully covered
Scraped pages 5, 6, and 7 of the email-marketing category listing. Structural finding worth
recording: **the `?page=` parameter only paginates the "Past Projects" (closed) archive section**
— the "currently open" section at the top of the category is identical across all three pages,
and shows only 2 open listings in total right now: a $10 "Gmail account" setup task (Google
Workspace admin work, not email marketing) and the UK Kajabi listing already on file from cycle 4
(duplicate, not re-logged). The archive entries on pages 5-7 (6-9 months old) are Mailchimp,
Klaviyo, HubSpot, and Wix-automation work — none Brevo, none open, none scorable. **The page sweep
cycle 4/5 called for is now complete.** There is no deeper page of open listings waiting to be
found; this category simply has very few open jobs at any given time, and re-checking page 1
periodically will show everything that's actually live.

### (c) Reddit r/forhire — blocked for a sixth consecutive cycle
Tried once more (`firecrawl_scrape` against an r/forhire search URL this time, not just an
individual thread). Same result: *"Firecrawl can't scrape this site because it is currently not
supported."* **Recommendation: drop this source from the rotation**, or replace it with a
different access method (a logged-in account, a different tool, or a manual check), if the owner
wants it covered at all. Six consecutive cycles with zero scorable results from a source that
costs a tool call each time is no longer worth the cost without a different approach.

## P0 (0–7 day payment) — none found

## P1 (8–30 day payment) — none found this cycle (unchanged carryover from cycle 5, see above)

## New candidates checked this cycle (2 — both rejected)

| Opportunity | Source | Client | Reason rejected |
|---|---|---|---|
| Part-time B2B content & email marketer (remote, ~15h/week) | Useme.com (new source) | Oliver Törnroth, Marketing Manager, Zoined (Finnish B2B SaaS) | Platform mismatch (Mailchimp + HubSpot, both PROHIBITED hands-on claims per the claims register — documented experience is Brevo only); scope is mostly content/blog/LinkedIn work, not email-marketing-specialist work; unresolved Polish student/school-ID payment-settlement requirement on this platform; 25 competing offers within days of posting. |
| [Remote] Email Marketing Specialist, Freelance (listing data corrupted) | remotejobs.dedyn.io (aggregator) | Unverifiable — employer/brand name replaced with placeholder text throughout the scrape | Listing content is templated/corrupted: "reputed company" literally substituted for the employer name, brand, and most tool references; page inconsistently labels the role both "Freelance" and "Full-time." Not a reliable, scorable listing regardless of underlying fit. Logged as SUSPICIOUS for the audit trail; flagging the aggregator's data quality. |

### Screened and rejected on sight (search-result text only, no full scrape)

- **"Upload HTML Email to Brevo"** (Freelancer.com, $10-30 fixed) — "log into my existing Brevo
  account, create the campaign" — a trivial single-send task, the same pattern as the near-
  identical listing rejected on sight in cycle 5. Not worth a scrape call.

## Source coverage this cycle

- **Upwork**: re-scraped the one carried-over P1 listing (see follow-up (a) above); fresh
  Brevo-specific and generic searches surfaced only listings already on file from cycles 1-5. No
  new candidate found.
- **PeoplePerHour**: pages 5-7 scraped, completing the sweep — see follow-up (b) above. No new
  scorable listing; category coverage is now effectively complete going forward (only 2 jobs open
  at any time, re-check page 1 in future cycles rather than paging deeper).
- **Freelancer.com**: search resurfaced only already-logged listings plus one trivial task
  screened on sight (see above). Continues the pattern of this platform's Brevo listings being
  either stale/closed or too low-value to be worth full scraping.
- **Contra**: same structural limitation as every prior cycle — results are "hire a Brevo/Klaviyo/
  Yotpo freelancer" directory pages and freelancer self-profiles, never client job postings. No
  scorable listing data exposed on Contra's public pages; this is now 6 cycles of the same finding.
- **Reddit r/forhire**: tried once more, blocked again — see follow-up (c) above. Recommend
  dropping or replacing this source.
- **German-market search**: re-ran the same German-language query per the master prompt's
  working-level-German instruction. Sixth consecutive cycle with no live German-market
  email-marketing-specialist opening found — results remain freelancer-for-hire directories, not
  open roles. The German-proficiency claims-register conflict remains untested in practice.
- **Direct business prospecting**: out of scope for this workstream per the recurring instruction
  (same as cycles 3-5) — not touched.
- **Useme.com** (new source tried this cycle): a Polish/European freelance marketplace. The
  email-marketing category is dominated by closed Klaviyo/GetResponse/Mailchimp/Mailerlite/
  Edrone/Snov.io listings — no Brevo listing, open or closed, found anywhere in the category. The
  one open listing was fully scraped and rejected (see table above). Also surfaced a
  platform-specific payment wrinkle worth flagging: this listing's Polish-language terms
  reference a student/school-ID requirement for payment settlement, which is unresolved for a
  non-Polish-resident freelancer — an additional, separate question from the existing
  unresolved TRNC payment-routing questions in `evidence/payment-routing.md`.
- **EmailJobs.io** (new source tried this cycle): its "Freelance Email Marketing Specialist" page
  is pure SEO/navigation content with zero actual listings. Its "Remote Email Marketing Jobs"
  page does list real postings, but every one is a salaried full-time/contract role with a named
  company and salary band (Vanta, Houzz, Scribd, etc.) — not freelance/project work. Structurally
  not a fit for this project; likely not worth revisiting unless the site adds a genuine freelance
  section.

## System health

- Sources touched: 8 (Upwork, PeoplePerHour, Freelancer.com, Contra, Reddit-attempted,
  German-market direct search, Useme.com [new], EmailJobs.io [new]). A ninth entry
  (remotejobs.dedyn.io) was logged as a data-quality flag rather than a source to keep using.
- Opportunities found and logged as full rows: 2 new (0 collisions with the existing 36 on file).
  1 additional candidate was screened and rejected on sight from search-result text without a
  full scrape or DB row (documented above, not counted toward the 2).
- 0 reached P0/P1 this cycle as *new* findings; the one carried-over P1 from cycle 5 was
  re-checked and remains unchanged (still discounted, still not a clean recommendation).
- No automation failures beyond the confirmed Reddit scrape restriction (now 6 cycles running,
  recommend dropping) and Contra's continued lack of per-listing verification data (both expected,
  both documented in the DB's `sources` table `last_error`/`terms_notes` fields). One new
  data-quality issue identified (remotejobs.dedyn.io's templated/corrupted listing content).

## Recommended next 3 actions

1. **Decide whether to drop Reddit r/forhire from the rotation** — six consecutive cycles of
   `firecrawl_scrape` refusing reddit.com with zero scorable results. If the owner wants this
   source covered, it needs a different method (a different tool, a logged-in approach, or a
   manual check) rather than a seventh identical attempt.
2. **Check the Newsletter Specialist for Campaigns / Brevo rate directly on Upwork** when
   convenient (requires a login this session doesn't have) — this is still the best lead on file
   across 6 cycles, and the rate is the only thing standing between it and a real decision on
   whether to prepare a package.
3. **Deprioritize PeoplePerHour's deeper page sweep going forward** — the structural finding this
   cycle (only 2 jobs open at any time, "pages" only page through a closed archive) means future
   cycles should just re-check page 1 rather than working through pages 2-7 again; redirect that
   effort toward source rotation (e.g. following up on whether Useme.com or other European
   marketplaces turn up a Brevo-specific listing over time) instead.
