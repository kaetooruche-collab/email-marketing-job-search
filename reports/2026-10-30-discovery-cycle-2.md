# Discovery Cycle 2 — 2026-10-30 (broader pass)

Follow-up to cycle 1. Added: PeoplePerHour category page (page 1 of 7), German-market search terms, "lifecycle marketing" / "email deliverability consultant" search terms, payment-routing research. Attempted and failed: Freelancer.com job detail scrape (page too large), Reddit individual thread fetch (blocked for both `firecrawl_scrape` and `WebFetch`).

## Result: still no clean P0/P1 win, but the picture is clearer

**0 P0, 0 new P1.** Three more Brevo/email-marketing-adjacent listings found on PeoplePerHour — all rejected with concrete reasons (see table). The Underdog Sales lead from cycle 1 remains the strongest candidate on file; its status needs your Upwork login to confirm (you said you'd check).

| Opportunity | Client | Budget | Reason rejected |
|---|---|---|---|
| HTML Email Design (Brevo-compatible) | Unnamed, PeoplePerHour | $133 fixed | Stale (14 days), 56 competing proposals |
| UK Kajabi expert: automations & tagging | BlemishPro | $200 fixed (phased) | Wrong platform (Kajabi, not Brevo); 37 proposals; UK-hours requirement |
| Marketing & Publishing Assistant (mentions Brevo) | UK local-magazine network | $11/hr | Freshest lead found (1hr old, 7 proposals) but role is mostly telephone sales + general marketing/admin; Brevo is 1 of 6 skill areas; rate too low for the breadth asked; requires UK-hours phone availability |

German-market search surfaced mostly full-time/salaried roles and a Facebook group post ("Hiring German Speaking Email Marketing Expert" — German e-commerce activewear brand) that wasn't independently verifiable this pass (Facebook post, no scrape access). Worth a manual look if you want — your German working-level copywriting is a genuine differentiator most competing freelancers won't have.

## Payment routing — resolved as far as research alone can take it

Wrote up `evidence/payment-routing.md`. Short version: Upwork's "Direct to Local Bank" lists "Cyprus (EUR)" but that's almost certainly the Republic of Cyprus banking system, not TRNC — different, unconnected network. Payoneer is confirmed to work in Turkey (TRNC's banking ties run through Turkey). I can't verify further without knowing which payment rail you actually use for your HIBARR pay — **tell me that and this resolves in one message**, since the same rail will very likely work for freelance client payments too.

## Known gaps carried forward (not run this cycle)

- PeoplePerHour pages 2–7 of 7 (135 results total; only ~20 reviewed)
- Freelancer.com (scrape failed on size; would need pagination/targeted scraping)
- Contra
- Reddit r/forhire individual threads (both scrape tools refuse reddit.com directly — the UK Brevo/FreeAgent/Riskbase lead from cycle 1 is still unconfirmed)
- Direct business prospecting (master prompt §4.3/§12) — not started
- LinkedIn, Facebook groups, Discord/Slack communities — not searchable without login in this session

These are now folded into the recurring scheduled scan (see below) rather than done as one-off manual passes.

## Recurring scan now set up

See the scheduled task created this session — daily discovery cycle covering the gaps above, updating the same DB and reports folder, committing and pushing to this branch automatically. It will **not** draft outreach, submit proposals, or take any action requiring your approval (master prompt §11.3) — discovery, verification, scoring, and reporting only.
