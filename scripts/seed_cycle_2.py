#!/usr/bin/env python3
"""Discovery cycle 2 (2026-10-30): broader pass — PeoplePerHour, German-market search,
lifecycle/deliverability search terms. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url)."""
import sqlite3
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "email_marketing_system.db"
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""INSERT OR IGNORE INTO sources
        (name, url, access_method, terms_notes, last_scan_at, last_error, discovery_count, qualified_count)
        VALUES (?,?,?,?,?,?,?,?)""",
        ("PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
         "firecrawl_scrape of public category listing page (page 1 of 7, 135 total results)",
         "Only page 1 scraped this cycle; pages 2-7 not yet reviewed.",
         NOW, None, 20, 0))

    source_id = conn.execute("SELECT id FROM sources WHERE name = 'PeoplePerHour'").fetchone()[0]

    opportunities = [
        dict(
            title="HTLM Email Design (Brevo-compatible templates)",
            client_name="Unnamed (PeoplePerHour)",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing/htlm-email-design-4527048",
            posted_at="2026-10-16 (14 days before discovery)",
            description="Responsive HTML email templates matching brand identity, must render reliably in Brevo across devices/clients.",
            required_skills="HTML email design, Brevo rendering compatibility",
            budget_amount=133, budget_currency="USD", budget_type="fixed",
            payment_platform="PeoplePerHour escrow",
            client_history="Not captured (no client spend/history panel scraped this pass).",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Stale (posted 14 days ago) with 56 competing proposals already — functionally oversubscribed; probability of winning too low to justify a proposal.",
            status="closed",
        ),
        dict(
            title="UK Kajabi expert: email automations, tagging & lead capture",
            client_name="BlemishPro (UK membership site for blemish-removal practitioners)",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing/uk-kajabi-expert-email-automations-tagging-lead-capture-4528018",
            posted_at="2026-10-23 (7 days before discovery)",
            description="3-phase fixed-price project: event-triggered tagging/lead capture automation in Kajabi (urgent, "
                        "must be live before Nov 26 event), member tagging cleanup, win-back + nurture sequences. "
                        "~270 contacts, 110 active members.",
            required_skills="Kajabi platform expertise (not Brevo), UK working hours",
            budget_amount=200, budget_currency="USD", budget_type="fixed (phased)",
            payment_platform="PeoplePerHour escrow",
            client_history="Not captured.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Platform mismatch — requires Kajabi, not Brevo (not in evidence register); already 37 "
                              "competing proposals at 7 days old; requires UK working hours.",
            status="closed",
        ),
        dict(
            title="Marketing & Publishing Assistant, Sales-Minded (includes Brevo)",
            client_name="Unnamed UK local-magazine/community-website network",
            url="https://www.peopleperhour.com/freelance-jobs/business/administration-assistance/marketing-publishing-assistant-sales-minded-4528991",
            posted_at="~1 hour before discovery (very fresh)",
            description="Hybrid part-time role (10 rising to 20 hrs/week): Facebook marketing, Brevo email marketing "
                        "and automation, WordPress updates, Canva/magazine design, AND telephone sales/lead follow-up. "
                        "Requires phone interview with clear audio equipment, UK business hours availability.",
            required_skills="Broad marketing generalist + telephone sales (Brevo is one of six listed skill areas)",
            budget_amount=11, budget_currency="USD", budget_type="hourly",
            payment_platform="PeoplePerHour escrow",
            client_history="Not captured.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Genuinely fresh (1 hr old, only 7 proposals) and does mention Brevo, but the role is "
                              "mostly telephone sales + general marketing/admin, not email marketing specialism; "
                              "$11/hr is below a sane rate for the breadth asked; requires UK-hours phone availability "
                              "with specific audio equipment. Noting it rather than silently dropping it, since it's "
                              "the freshest Brevo-mentioning lead found this cycle, but it is a poor positioning fit.",
            status="closed",
        ),
    ]

    for o in opportunities:
        o.update(source_id=source_id, discovered_at=NOW, updated_at=NOW,
                  score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
                  score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
                  score_repeat_potential=None, score_total=None, score_rationale=None,
                  est_days_to_accessible_payment=None, notes=None)
        conn.execute("""INSERT OR IGNORE INTO opportunities
            (source_id, title, client_name, url, discovered_at, posted_at, description, required_skills,
             budget_amount, budget_currency, budget_type, payment_platform, client_history,
             verification_status, priority_tier, rejection_reason, est_days_to_accessible_payment,
             score_probability_win, score_time_to_payment, score_skill_match, score_payment_certainty,
             score_compensation, score_client_credibility, score_repeat_potential, score_total, score_rationale,
             status, notes, updated_at)
            VALUES (:source_id, :title, :client_name, :url, :discovered_at, :posted_at, :description, :required_skills,
             :budget_amount, :budget_currency, :budget_type, :payment_platform, :client_history,
             :verification_status, :priority_tier, :rejection_reason, :est_days_to_accessible_payment,
             :score_probability_win, :score_time_to_payment, :score_skill_match, :score_payment_certainty,
             :score_compensation, :score_client_credibility, :score_repeat_potential, :score_total, :score_rationale,
             :status, :notes, :updated_at)""", o)

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 1, 3, 0,
         "Freelancer.com job page scrape failed (result too large, 94K+ chars); Reddit thread still unreachable via "
         "WebFetch ('unable to fetch from www.reddit.com'); PeoplePerHour pages 2-7 (of 7) not yet reviewed; "
         "Contra and direct-business-prospecting (master prompt §4.3/§12) not run this cycle, deferred to recurring scans."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 2 seeded. {n} total opportunities on file.")
    conn.close()

if __name__ == "__main__":
    main()
