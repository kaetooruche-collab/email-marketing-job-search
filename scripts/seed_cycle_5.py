#!/usr/bin/env python3
"""Discovery cycle 5 (2026-11-15): single consolidated run covering the backlog of 14 queued
daily firings (2026-11-02 through 2026-11-15), reflecting the live market as of 2026-11-15 --
NOT 14 separate cycles. Brevo-focused + generic email marketing freelancer search, rotating
through cycle 4's gap notes (Freelancer.com individual listings, PeoplePerHour pages 2-4,
Reddit r/forhire individual-thread re-check, Contra re-check, German-market search per master
prompt owner's working-level German). Appends to the same DB. Safe to re-run (INSERT OR IGNORE
on url). See reports/2026-11-15-discovery-cycle-5.md for the full narrative."""
import sqlite3
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "db" / "email_marketing_system.db"
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()


def get_or_create_source(conn, name, url, access_method, terms_notes, last_error=None,
                          discovery_count=0, qualified_count=0):
    row = conn.execute("SELECT id FROM sources WHERE name = ?", (name,)).fetchone()
    if row:
        conn.execute(
            "UPDATE sources SET last_scan_at = ?, last_error = ?, "
            "discovery_count = discovery_count + ?, qualified_count = qualified_count + ? WHERE id = ?",
            (NOW, last_error, discovery_count, qualified_count, row[0]),
        )
        return row[0]
    cur = conn.execute(
        """INSERT INTO sources
        (name, url, access_method, terms_notes, last_scan_at, last_error, discovery_count, qualified_count)
        VALUES (?,?,?,?,?,?,?,?)""",
        (name, url, access_method, terms_notes, NOW, last_error, discovery_count, qualified_count),
    )
    return cur.lastrowid


def main():
    conn = sqlite3.connect(DB_PATH)

    upwork_id = get_or_create_source(
        conn, "Upwork (public job pages via web search)", "https://www.upwork.com",
        "firecrawl_search + firecrawl_scrape of public job detail pages, no login",
        "Full proposal submission requires an Upwork account and login.",
        discovery_count=5, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_scrape of category listing pages 2-4 this cycle (page 1 covered in cycle 4)",
        "Pages 2, 3 and 4 of the category listing scraped cleanly this cycle (119 results total, "
        "page size ~20) -- no new Brevo- or email-marketing-specific listing found beyond the "
        "UK Kajabi job already on file from cycle 4; these pages are dominated by unrelated gigs "
        "(VA, translation, social media, legal, etc). Pages 5-7 not reached this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_scrape of individual project page (category pages too large to scrape in one call)",
        "6 individual listings checked this cycle (Brevo-specific plus Brevo+Hubspot admin-assistant "
        "variants); all Closed, ranging ~3 months to >1 year old, at very low rates (EUR 2-6/hr to "
        "USD 10-30 fixed) -- continues the pattern from cycles 3-4 of stale/closed, low-rate "
        "Brevo listings on this platform.",
        discovery_count=3, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/freelancer pages",
        "No new distinct per-job listing surfaced this cycle -- search results are dominated by "
        "Contra's 'hire a freelancer' category pages (e.g. Klaviyo freelancers, Mailchimp "
        "freelancers), not individual job postings. Contra continues to expose no scorable "
        "listing data from its public pages.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_search only; firecrawl_scrape refuses reddit.com directly",
        "Confirmed blocked for a FIFTH consecutive cycle: firecrawl_scrape returns "
        "'Firecrawl can't scrape this site because it is currently not supported' for reddit.com "
        "individual threads. Search surfaced several title matches (Brevo/email marketing hiring "
        "posts) but every one is from an old post ID (2024-2025 era) with no way to confirm "
        "current status, posted date, or still-open state without the thread itself. Structural "
        "platform restriction, not a one-off -- recommend the owner decide whether this source is "
        "worth continuing to check at all.",
        last_error="firecrawl_scrape: 'currently not supported' for reddit.com",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Searched 'E-Mail Marketing Freiberufler gesucht Brevo/Newsletter deutschsprachig' per "
        "master prompt's German-leverage instruction. Results are almost entirely freelancer "
        "profile directories (Malt.com, freelance.de, freelancermap.de, junico.de) rather than "
        "live job postings -- these list freelancers FOR HIRE, not open roles, so nothing scorable "
        "there. The one actual job posting surfaced (jobgether.com, German web-designer-with-"
        "copywriting role) hard-requires Klaviyo (PROHIBITED per claims register) and is a web "
        "design role, not an email-marketing-specialist role -- rejected on sight, not logged as "
        "a full row. No live German-market email-marketing-specialist opening found this cycle.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Brevo Expert for Email Campaigns",
            client_name="Individual client, Pennington, United States",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Expert-for-Email-Campaigns_~022118445381149116629/",
            posted_at="Not shown explicitly; last viewed by client 2 weeks ago",
            description="Import a contact list into Brevo and create a 3-email marketing campaign: "
                        "list setup, campaign prep, launch-readiness. <1 month, <30 hrs/week, Expert level.",
            required_skills="Brevo, email marketing, marketing automation.",
            budget_amount=48, budget_currency="USD", budget_type="hourly ($20-$48/hr range, Expert)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Nov 3, 2020. $6.4K total spent, 25 hires, 6 active, 417 hours "
                            "logged. Individual client, established and credible.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already shows Hires: 1 and Interviewing: 1, with last-viewed-by-client "
                              "2 weeks ago -- the standard pattern this project has seen for a role that "
                              "has effectively already been filled or is well into selection, even though "
                              "it has not been formally closed. 20-50 competing proposals on top of that. "
                              "Skill fit (Brevo campaign setup) is otherwise reasonable, but the fill-risk "
                              "signal is too strong to justify a bid.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Brevo Admin Automation Setup",
            client_name="Individual client, Stuart, United States",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Admin-Automation-Setup_~022111101520252426613/",
            posted_at="Not shown explicitly; last viewed by client 5 weeks ago",
            description="Build the technical framework for Brevo automation flows using blank templates "
                        "(no copywriting) -- structure only, content to be added by an in-house email "
                        "department later. <1 month, Intermediate.",
            required_skills="Mail Server Implementation, DNS, Microsoft Exchange Server, Linux System "
                             "Administration -- notably NOT email copywriting/campaign skills.",
            budget_amount=15, budget_currency="USD", budget_type="hourly ($15/hr)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Apr 4, 2019. $9.8K total spent, 12 hires, 5 active, 290 hours.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard skill mismatch -- the listed required skills (mail server/DNS/Exchange/"
                              "Linux sysadmin) describe backend infrastructure automation work, explicitly "
                              "NOT content or campaign work ('no email copywriting is needed'). This is "
                              "outside the documented strength (segmentation/lifecycle/deliverability "
                              "content work), not a sysadmin role. Also already Hires: 1, last viewed 5 "
                              "weeks ago -- stale and likely filled on top of the skill mismatch.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Newsletter Specialist for Campaigns / Brevo",
            client_name="Individual client, Fairfax, United States",
            url="https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/",
            posted_at="Not shown explicitly; last viewed by client 3 days ago (fresh)",
            description="Ongoing (6+ months) part-time role to improve email delivery rate and "
                        "strengthen newsletter campaigns in Brevo: list management, campaign performance "
                        "optimization, process review, engagement improvement.",
            required_skills="Email marketing, internet marketing, social media marketing, Facebook. "
                             "Platform explicitly stated as Brevo in the body text.",
            budget_amount=None, budget_currency="USD",
            budget_type="hourly (exact rate not shown in this scrape -- client has an established "
                         "hourly history but no $ range rendered on this listing)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Jan 21, 2026. $65K total spent, 34 hires, 15 active, 1,972 "
                            "hours logged -- a very established, highly active buyer, the strongest "
                            "client-credibility signal found across all 5 cycles of this project to date.",
            verification_status="VERIFIED",
            priority_tier="P1",
            rejection_reason=None,
            est_days_to_accessible_payment=20,
            score_probability_win=11, score_time_to_payment=14, score_skill_match=13,
            score_payment_certainty=8, score_compensation=5, score_client_credibility=9,
            score_repeat_potential=4, score_total=64,
            score_rationale="Best lead found across all 5 discovery cycles to date, but still "
                             "discounted, not a clean go. Strengths: direct Brevo deliverability/"
                             "newsletter-optimization scope matches the one platform with strong "
                             "documented evidence; zero hires and zero interviewing so far despite "
                             "20-50 proposals; client last reviewed applicants only 3 days ago (fresh, "
                             "not stale); client credibility is the strongest seen in this project "
                             "($65K spent, 34 hires, 1,972 hours). Discounts: exact hourly rate is not "
                             "shown in the scrape -- cannot confirm compensation is viable until opened "
                             "directly on Upwork; 20-50 competing proposals is still real competition; "
                             "TRNC payment-routing remains UNVERIFIED for Upwork per "
                             "evidence/payment-routing.md, same caveat applied to every Upwork "
                             "opportunity in this project. Not recommending an application package yet "
                             "-- flagging for the owner to confirm the actual rate first (requires an "
                             "Upwork login this session does not have).",
            status="researched",
            notes="Flagged in cycle-5 summary as the one lead worth a second look, with the explicit "
                  "caveat that the undisclosed rate and TRNC payment-routing uncertainty keep it short "
                  "of a clean recommendation.",
        ),
        dict(
            source_id=upwork_id,
            title="Brevo to Hubspot Leads Automation",
            client_name="Newton Highlands, United States (Media & Entertainment, mid-sized company)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Hubspot-Leads-Automation_~022117683489625785888/",
            posted_at="Posted November 3, 2026; last viewed by client 2 weeks ago",
            description="Build a weekly-run automation syncing a Brevo engagement segment with Hubspot "
                        "subscription lists (check/add/subscribe/unsubscribe logic across both systems), "
                        "plus a pre-run report. $200 fixed price, Intermediate.",
            required_skills="HubSpot, Marketing Automation, Brevo, Airtable -- API/integration logic, "
                             "not campaign content work.",
            budget_amount=200, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Member since Dec 9, 2017. $4.3K total spent, 4 hires, 3 active, 388 hours.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already shows Hires: 1 with 50+ proposals and last viewed 2 weeks ago -- "
                              "very likely filled. Scope is also a technical two-system sync/automation "
                              "build (conditional logic across Brevo and Hubspot), closer to an "
                              "integration-engineering task than documented email-lifecycle/content work.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="B2B CRM Specialist - Brevo",
            client_name="Manchester, United Kingdom (small email/CRM consultancy, 2-9 people)",
            url="https://www.upwork.com/freelance-jobs/apply/B2B-CRM-Specialist-Brevo_~022120459603978401864/",
            posted_at="Not shown explicitly; last viewed by client 4 days ago (fresh)",
            description="Hands-on Email & CRM Consultant role at a specialist email/CRM consultancy: "
                        "planning/building/testing campaigns and journeys, segmentation, briefing an "
                        "in-house designer, performance review, client calls. One-month paid trial, "
                        "then ongoing. UK-hours availability required.",
            required_skills="Explicitly requires '3+ years of hands-on experience in email marketing, "
                             "CRM or lifecycle marketing' plus hands-on experience with at least one of "
                             "Klaviyo, Brevo, HubSpot or Mailchimp.",
            budget_amount=25, budget_currency="USD", budget_type="hourly ($20-$25/hr range)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Feb 16, 2023. $4.1K total spent, 5 hires, 2 active, 139 hours. "
                            "Small, specialist agency -- credible but modest scale.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard experience-threshold mismatch -- explicitly requires 3+ years of "
                              "hands-on email marketing/CRM experience. Kaeto's claims register puts "
                              "total professional email-marketing tenure at under one year (HIBARR, "
                              "Jan 2026-present), and the project's own job-search filter excludes "
                              "opportunities requiring more than ~2 years of experience. Also already "
                              "has 3 candidates interviewing, which independently lowers the odds even "
                              "before the experience gate is considered.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Email Marketing Specialist",
            client_name="Recruitment agency buyer (unnamed)",
            url="https://www.freelancer.com/projects/internet-marketing/brevo-email-marketing-specialist",
            posted_at="Posted over 1 year ago",
            description="Brevo-based email marketing to increase brand awareness for a recruitment "
                        "agency: campaign content, strategy, performance tracking.",
            required_skills="Brevo, copywriting, design, recruitment-industry familiarity (plus).",
            budget_amount=6, budget_currency="EUR", budget_type="hourly (EUR 2-6/hr range)",
            payment_platform="Freelancer.com escrow",
            client_history="34 proposals already; 'Active 1 yr ago' -- long closed.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed, over a year old, and the EUR 2-6/hr rate is far below any "
                              "sustainable freelance rate even if it were still open.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Email Deliverability Warmup Specialist",
            client_name="Casselberry, United States (established buyer, 10 prior reviews)",
            url="https://www.freelancer.com/projects/ab-testing/brevo-email-deliverability-warmup",
            posted_at="Posted 3 months before discovery",
            description="Design and execute a Brevo-specific subdomain warmup plan (4-6 week ramp "
                        "schedule, metric monitoring, final inbox-placement report) for a new subdomain "
                        "on Brevo's shared sending infrastructure.",
            required_skills="Brevo-specific deliverability/warmup experience (explicitly not general "
                             "warmup or dedicated-IP experience).",
            budget_amount=30, budget_currency="USD", budget_type="fixed ($10-30 USD, 20 bids averaging $29)",
            payment_platform="Freelancer.com escrow",
            client_history="5.0 rating, 10 reviews, payment method verified, member since 2012 -- "
                            "credible, established buyer.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed, and the $10-30 fixed budget is too low for the actual scope "
                              "requested (a full multi-week warmup plan with ongoing monitoring and a "
                              "final report) even though the client itself is credible. Deliverability "
                              "work is a genuine documented strength, but this specific listing's "
                              "economics don't work and it's no longer open regardless.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo and Hubspot Client Engagement Assistant",
            client_name="Buyer, Daerah Istimewa Yogyakarta, Indonesia",
            url="https://www.freelancer.com/projects/customer-service/brevo-hubspot-client-engagement",
            posted_at="Posted 2026-07-13 (4 months before discovery)",
            description="Ongoing ~5 hrs/week role: send/schedule pre-written Brevo email campaigns, log "
                        "and follow up on replies in HubSpot within 24 hours, keep a shared contact "
                        "sheet in sync, occasional WhatsApp calls.",
            required_skills="Comfort moving between Brevo, HubSpot, Google Docs and WhatsApp -- a "
                             "client-engagement/VA role, not email-marketing strategy or content work.",
            budget_amount=25, budget_currency="USD", budget_type="hourly ($15-25/hr range, 9 bids "
                         "averaging $19/hr)",
            payment_platform="Freelancer.com escrow",
            client_history="0.0 rating, 0 reviews, brand-new account (member since the posting date "
                            "itself) -- no credibility signal.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed, brand-new unverifiable client, and the scope is a client-"
                              "engagement/follow-up VA role (reply-chasing, CRM bookkeeping, WhatsApp "
                              "calls) rather than email-marketing strategy, content, or deliverability "
                              "work -- a scope mismatch independent of the staleness/credibility issues.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
    ]

    for o in opportunities:
        o.update(discovered_at=NOW, updated_at=NOW)
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
        ("discovery_scan", NOW, NOW, 6, len(opportunities), 1,
         "Single consolidated cycle covering a 14-firing backlog (2026-11-02 through 2026-11-15), "
         "run once against the live 2026-11-15 market per the owner's instruction, not run 14 times. "
         "Reddit r/forhire individual threads confirmed blocked for a FIFTH consecutive cycle "
         "(firecrawl_scrape: 'currently not supported'). PeoplePerHour pages 2-4 scraped (119 "
         "results total), no new Brevo/email-marketing-specific listing beyond what cycle 4 already "
         "logged; pages 5-7 not reached. Contra surfaced no new scorable listing. German-market "
         "search surfaced only freelancer-directory pages and one Klaviyo-requiring web-design "
         "role (rejected on sight, not logged as a full row) -- no live German-market email-"
         "marketing-specialist opening found. One P1 lead found and scored (Newsletter Specialist "
         "for Campaigns / Brevo, Upwork, score 64/100) -- flagged as the best lead across all 5 "
         "cycles but still discounted, not a clean recommendation, pending the actual hourly rate "
         "and the still-unresolved TRNC payment-routing question."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 5 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
