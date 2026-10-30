# Email Marketing Opportunity Discovery & Revenue Acquisition System

Status: **early build, first live discovery cycle complete.** This is not a finished product — see "What's not built yet" below before assuming more exists than does.

## What's here

- `evidence/claims-register.md` — central source of truth for every factual claim about Kaeto's background (HIBARR metrics, education, tools), each tagged VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / CONFLICT / PROHIBITED, traced to the 3 source documents. **Read this before using any number or claim in a CV, proposal, or outreach message.** Flags one unresolved conflict: location (Northern Cyprus per all 3 CVs vs. Türkiye per the system prompt).
- `db/schema.sql` + `db/email_marketing_system.db` — SQLite persistence for opportunities, sources, contacts, evidence claims, applications, automation runs (master prompt §14, minimal first pass).
- `scripts/init_and_seed.py` — idempotent script that builds the DB and loads discovery-cycle results. Re-run safe.
- `reports/2026-10-30-discovery-cycle-1.md` — first live discovery cycle: 6 real opportunities found and individually qualified/rejected with reasons, 0 reached P0, 1 reached P1 with a major caveat (likely already filled).
- `applications/` — empty; no application package has been prepared yet because no opportunity cleared qualification cleanly this cycle.

## What's not built yet

Per the master prompt's own scope (§6 payment-first qualification, §7 contact research, §9 CV engine, §15 dashboard, §16 automation), the following are **not implemented**:

- Contact/decision-maker research engine (no opportunity qualified cleanly enough to research a contact for)
- CV tailoring/generation pipeline (nothing to tailor to yet)
- Outreach/proposal drafting and the owner-approval queue (§11.3 — nothing drafted, nothing sent)
- Dashboard/UI (file-based reports + SQLite only, for now)
- Recurring scheduled automation (this was one manual run; a recurring scheduled task can be set up on request)
- Payment/contract/invoice tracking tables and workflow (schema has placeholders; nothing populated — no contract exists yet)
- Direct business prospecting pass (§4.3/§12 — not started)

## Why so little landed this cycle

The master prompt specifies two narrow revenue horizons (P0: 0-7 days to accessible payment, P1: 8-30 days) and a strict payment-first qualification test. Running real searches against that bar — not fabricated listings — surfaced 6 live postings, and every one either failed a hard requirement (language, budget too low to be worth the time, speculative/unfunded), was stale/likely filled, or required tools not in Kaeto's verified skill set (Klaviyo, Make.com, Zapier). That's an honest first-cycle outcome, not a failure of the search — see the report for the reasoning on each one.

## Next steps (awaiting your direction)

1. Resolve the Türkiye vs. Northern Cyprus location conflict (payment-routing depends on it).
2. Confirm whether the Underdog Sales Brevo job is actually still open (requires an Upwork login I don't have).
3. Say whether to: set up a recurring scheduled discovery cycle, run a second broader pass (PeoplePerHour/Freelancer.com/direct prospecting), or start building the CV-tailoring and contact-research pieces now even with zero cleanly-qualified opportunities on hand.
