#!/usr/bin/env python3
"""Initialize the SQLite DB from schema.sql and seed it with discovery cycle 1 results
(2026-10-30, live web search — see reports/2026-10-30-discovery-cycle-1.md for full narrative).
Safe to re-run: uses INSERT OR IGNORE keyed on opportunities.url.
"""
import sqlite3
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "email_marketing_system.db"
SCHEMA_PATH = ROOT / "db" / "schema.sql"

NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_PATH.read_text())

    conn.execute("""INSERT OR IGNORE INTO sources
        (name, url, access_method, terms_notes, last_scan_at, last_error, discovery_count, qualified_count)
        VALUES (?,?,?,?,?,?,?,?)""",
        ("Upwork (public job pages via web search)", "https://www.upwork.com",
         "firecrawl_search + firecrawl_scrape of public job detail pages, no login",
         "Full proposal submission requires an Upwork account and login; this session can read public listings but cannot submit a proposal.",
         NOW, None, 8, 1))
    conn.execute("""INSERT OR IGNORE INTO sources
        (name, url, access_method, terms_notes, last_scan_at, last_error, discovery_count, qualified_count)
        VALUES (?,?,?,?,?,?,?,?)""",
        ("Reddit r/forhire", "https://www.reddit.com/r/forhire",
         "firecrawl_search only; firecrawl_scrape refuses reddit.com directly",
         "Could not open individual Reddit threads this cycle to confirm recency/status; titles only.",
         NOW, "firecrawl_scrape: 'we do not support this site' for reddit.com", 10, 0))

    source_id = conn.execute("SELECT id FROM sources WHERE name LIKE 'Upwork%'").fetchone()[0]

    opportunities = [
        dict(
            title="Brevo deliverability and list cleanup specialist",
            client_name="Underdog Sales (B2B cold-calling training company)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-deliverability-and-list-cleanup-specialist_~022115757776792063959/",
            posted_at="2026-10-29",
            description="SPF/DKIM/DMARC audit across all senders, Google Postmaster Tools setup, placement-drop diagnosis, "
                        "rebuild engagement segments (Apple MPP-aware), run sunset using 3 pre-written re-engagement emails "
                        "and automate it, pre-send checklist/SOP for client's assistant. Explicitly excludes copywriting/design.",
            required_skills="Hands-on Brevo (segments, automations), Google Postmaster Tools, Make or Zapier",
            budget_amount=350, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow (milestones: $150 then $200)",
            client_history="Member since 2025-11-01, Paphos, Cyprus (CYP). $2.5K total spent, 9 hires, 6 active, 16 hrs logged.",
            verification_status="VERIFIED",
            priority_tier="P1",
            rejection_reason=None,
            est_days_to_accessible_payment=18,
            score_probability_win=6, score_time_to_payment=20, score_skill_match=13,
            score_payment_certainty=13, score_compensation=8, score_client_credibility=9, score_repeat_potential=4,
            score_total=73,
            score_rationale="Best skill match found this cycle (deliverability/list hygiene/MPP-aware segmentation is exactly "
                             "the documented HIBARR work). Credible, established buyer with real spend history. BUT: listing "
                             "activity panel shows 'Hires: 1' already recorded against this posting despite being posted "
                             "yesterday, plus 15-20 competing proposals — strong signal the role may already be filled. "
                             "Also requires Make/Zapier, which is not in the evidence register (PROHIBITED claim). Probability "
                             "score discounted heavily for likely-filled status; skill/payment/client scores are what they'd "
                             "be if still genuinely open.",
            status="researched",
        ),
        dict(
            title="Brevo (Sendinblue) Email Designer — Master Email Template",
            client_name="Audinc (custom hearing protection / in-ear monitors, Belgium)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Sendinblue-Email-Designer-needed-build-responsive-Master-Email-Template_~022088205773409866641/",
            posted_at=None,
            description="Build one modular master HTML/drag-and-drop email template inside Brevo covering a 4-step B2C "
                        "post-visit automation (welcome/status, 6-week follow-up, 6-month care/upsell, 12-month check-in). "
                        "Fast turnaround requested (2-4 days).",
            required_skills="Proven Brevo/Sendinblue template design, 100% mobile-responsive HTML, brand matching",
            budget_amount=None, budget_currency=None, budget_type="hourly (rate not fixed, 'Not Sure')",
            payment_platform="Upwork escrow",
            client_history="Member since 2026-08-06, Essen, Belgium. $60 total spent, 1 hire, 0 active — thin history.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Stale (client last viewed applicants 2 weeks ago), heavy competition (20-50 proposals already), "
                              "low-spend/thin-history client, and core ask is HTML/visual template design rather than the "
                              "lifecycle/deliverability work that is the strongest documented skill match.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None, score_repeat_potential=None,
            score_total=None,
            score_rationale=None,
            status="closed",
        ),
        dict(
            title="Setup Brevo to hide main domain, show only subdomain in email header",
            client_name="Unnamed (web/dev-oriented client)",
            url="https://www.upwork.com/freelance-jobs/apply/Setup-Brevo-hide-main-domain-and-show-only-subdomain-email-header_~022112561399388302760/",
            posted_at="2026-10-20",
            description="DNS/domain authentication task: set up subdomain as authenticated sending domain in Brevo "
                        "(SPF/DKIM/DMARC), remove Brevo branding/via-tag, configure Mail-From to show only subdomain, "
                        "test in Gmail. Client will provide DNS access.",
            required_skills="Brevo domain auth, DNS (Cloudflare), some PHP/WordPress context",
            budget_amount=15, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Member since 2026-10-18, Lahore, Pakistan. No spend history yet.",
            verification_status="PARTIALLY_VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Budget ($15 fixed) does not clear a sane effective hourly rate for DNS/authentication work; "
                              "stale (last viewed 6 days ago, 2 already interviewing); scope leans sysadmin/DNS rather than "
                              "email marketing strategy; brand-new client with no payment track record.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None, score_repeat_potential=None,
            score_total=None,
            score_rationale=None,
            status="closed",
        ),
        dict(
            title="E-commerce Email Marketing Specialist (freelance network)",
            client_name="EcomGrowth (agency launching Nov 2026, Ireland)",
            url="https://www.upwork.com/freelance-jobs/apply/commerce-Email-Marketing-Specialist_~022115407762934403380/",
            posted_at=None,
            description="Recruiting into a freelancer 'network' for a not-yet-launched agency; no specific funded project, "
                        "scope/fee/timeline explicitly 'negotiated per project as they arise'; work 'not guaranteed'.",
            required_skills="Strong Klaviyo + Shopify integration experience, DTC/beauty vertical preferred",
            budget_amount=None, budget_currency=None, budget_type="contract-to-hire, hourly, no fixed scope",
            payment_platform="Upwork (if/when a project materializes)",
            client_history="Agency itself is pre-launch (Nov 2026); no track record to evaluate.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Fails the payment-horizon test per master prompt §2.1/§6: no funded project, no budget, no "
                              "timeline — speculative business development, not a P0/P1 opportunity. Also a skill mismatch "
                              "(requires Klaviyo+Shopify; documented experience is Brevo).",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None, score_repeat_potential=None,
            score_total=None,
            score_rationale=None,
            status="closed",
        ),
        dict(
            title="E-mail marketing specialist — real estate agency (Russian/English required)",
            client_name="Ola Estate (Portugal real estate, serves Russian-speaking clients)",
            url="https://www.upwork.com/freelance-jobs/apply/mail-marketing-specialist_~022113649596673008747/",
            posted_at="2026-10-29",
            description="Build email marketing infrastructure from scratch for a real-estate agency (property seller "
                        "acquisition focus), 3-6 month engagement, <30 hrs/week.",
            required_skills="MUST be fluent in both Russian and English (explicitly stated as a hard requirement)",
            budget_amount=None, budget_currency=None, budget_type="hourly",
            payment_platform="Upwork escrow",
            client_history="Not captured this pass.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard language requirement (fluent Russian) not met — candidate's languages are English "
                              "(fluent), German (working), Turkish (basic). Disqualifying, not a close call.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None, score_repeat_potential=None,
            score_total=None,
            score_rationale=None,
            status="closed",
        ),
        dict(
            title="List Building & Email Marketing Specialist Needed",
            client_name="Unnamed (US-based, New York)",
            url="https://www.upwork.com/freelance-jobs/apply/List-Building-Email-Marketing-Specialist-Needed_~022110410615994973421/",
            posted_at=None,
            description="Prospect list research/building plus email campaigns for lead gen; outreach and response-rate "
                        "optimization.",
            required_skills="Lead generation + email marketing + outreach tracking",
            budget_amount=23.5, budget_currency="USD", budget_type="hourly ($12-$35/hr range)",
            payment_platform="Upwork escrow",
            client_history="Member since 2026-08-07, New York. $755 total spent, 58 hires, 18 active — very high hire "
                            "volume relative to spend (avg ~$13/hire), suggests short/cheap gigs, not sustained relationships.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already has 1 hire recorded and was last viewed by client 2 weeks ago — functionally stale/"
                              "filled. Scope also leans more cold-outreach/list-building than lifecycle email marketing.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None, score_repeat_potential=None,
            score_total=None,
            score_rationale=None,
            status="closed",
        ),
    ]

    for o in opportunities:
        conn.execute("""INSERT OR IGNORE INTO opportunities
            (source_id, title, client_name, url, discovered_at, posted_at, description, required_skills,
             budget_amount, budget_currency, budget_type, payment_platform, client_history,
             verification_status, priority_tier, rejection_reason, est_days_to_accessible_payment,
             score_probability_win, score_time_to_payment, score_skill_match, score_payment_certainty,
             score_compensation, score_client_credibility, score_repeat_potential, score_total, score_rationale,
             status, updated_at)
            VALUES (:source_id, :title, :client_name, :url, :discovered_at, :posted_at, :description, :required_skills,
             :budget_amount, :budget_currency, :budget_type, :payment_platform, :client_history,
             :verification_status, :priority_tier, :rejection_reason, :est_days_to_accessible_payment,
             :score_probability_win, :score_time_to_payment, :score_skill_match, :score_payment_certainty,
             :score_compensation, :score_client_credibility, :score_repeat_potential, :score_total, :score_rationale,
             :status, :updated_at)""",
            {**o, "source_id": source_id, "discovered_at": NOW, "updated_at": NOW})

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 2, 6, 1,
         "reddit.com individual threads not scrapable by firecrawl_scrape this session (search snippets only)"))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"DB initialized at {DB_PATH}. {n} opportunities on file.")
    conn.close()

if __name__ == "__main__":
    main()
