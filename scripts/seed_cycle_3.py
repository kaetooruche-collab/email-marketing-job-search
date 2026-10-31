#!/usr/bin/env python3
"""Discovery cycle 3 (2026-10-31): Brevo-focused + generic email marketing freelancer search,
rotating through prior gaps (Freelancer.com individual listings, Contra, PeoplePerHour beyond
page 1, Reddit r/forhire individual threads) plus a German-market check. Appends to the same DB.
Safe to re-run (INSERT OR IGNORE on url). See reports/2026-10-31-discovery-cycle-3.md for the
full narrative."""
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
        discovery_count=6, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_search + firecrawl_scrape of individual job pages",
        "Search surfaced listings outside page 1 (not full pagination pass of pages 2-7).",
        discovery_count=2, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_scrape of individual project page (category pages too large to scrape in one call)",
        "Individual project pages ARE scrapable with firecrawl_scrape (resolves prior cycle's "
        "category-page-too-large gap); category/listing pages are not practical to scrape whole.",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search + firecrawl_scrape of featured-jobs landing page",
        "Contra's public featured-jobs page shows only a handful of recurring 'featured' cards with "
        "no posted date, applicant count, or client history, and no distinct per-job URL was exposed "
        "in the scrape — cannot verify staleness/competition/credibility for anything found here.",
        discovery_count=1, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_search only; firecrawl_scrape refuses reddit.com directly",
        "Confirmed blocked for a third consecutive cycle: firecrawl_scrape returns "
        "'we do not support this site' for reddit.com. Structural gap, not one-off.",
        last_error="firecrawl_scrape: 'we do not support this site' for reddit.com",
        discovery_count=3, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Brevo Email Marketing Manager — Subscription App (Re-engagement & Lifecycle)",
            client_name="Consumer language-learning app, USA (Orange, CA)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Email-Marketing-Manager-Subscription-App-engagement-Lifecycle_~022107889186699907933/",
            posted_at="Not shown explicitly; last viewed by client 'last week'",
            description="Own lifecycle/retention email program for a subscription language-learning app: "
                        "build onboarding/re-engagement/win-back/lapsed/renewal automations, run update/feature "
                        "campaigns, segment by lifecycle stage, report on open/click/conversion/churn. "
                        "Contract-to-hire.",
            required_skills="Email marketing with subscription/consumer apps, retention/churn strategy, "
                             "automation platform + segmentation hands-on, data-backed recommendations.",
            budget_amount=10, budget_currency="USD", budget_type="hourly ($5-$10/hr range, Expert level)",
            payment_platform="Upwork (hourly, weekly billing + standard security hold)",
            client_history="Member since Apr 11, 2026, USA. $13K total spent, 47 hires (25 active), 635 hours logged — "
                            "highly credible, active buyer.",
            verification_status="VERIFIED",
            priority_tier="P1",
            rejection_reason=None,
            est_days_to_accessible_payment=14,
            score_probability_win=5, score_time_to_payment=18, score_skill_match=13,
            score_payment_certainty=13, score_compensation=4, score_client_credibility=9, score_repeat_potential=4,
            score_total=66,
            score_rationale="Strongest skill match this cycle — re-engagement/win-back/lifecycle segmentation and "
                             "churn reporting map closely onto the documented HIBARR scope, and the client is highly "
                             "credible (47 hires, $13K spent, 25 active contracts). BUT the listing's activity panel "
                             "already shows 'Hires: 1' plus '4 interviewing' — a strong signal the role is in final "
                             "selection or already filled, same pattern as the Underdog Sales lead discounted in "
                             "cycle 1. Compensation is also unusually low for 'Expert' level ($5-10/hr). Probability-"
                             "of-winning scored low to reflect the fill risk; not recommended for a proposal without "
                             "owner confirmation it's still genuinely open.",
            status="researched",
            notes="Discounted P1, not a clean go — see score_rationale. Flagged in report, not recommended for "
                  "immediate application package without confirming the job is still accepting proposals.",
        ),
        dict(
            source_id=upwork_id,
            title="Brevo CRM, Email Marketing & Lead Automation Setup for Travel Company",
            client_name="South African travel company (Corporate + Private Travel), Durban",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-Email-Marketing-Lead-Automation-Setup-for-Travel-Company_~022105628576495448901/",
            posted_at="Not shown; last viewed by client 3 weeks ago",
            description="Full Brevo CRM build: corporate/private pipelines, WordPress form integration, Meta/"
                        "LinkedIn lead-form integration, email deliverability setup, multiple automated customer "
                        "journeys, lead dashboards, documentation and recorded handover.",
            required_skills="Brevo CRM/pipeline architecture, WordPress integration, Meta + LinkedIn lead-gen "
                             "integration — client explicitly states 'please do not apply if your experience is "
                             "limited to sending newsletters in Brevo.'",
            budget_amount=None, budget_currency="USD", budget_type="fixed (open bid)",
            payment_platform="Upwork escrow",
            client_history="Member since Aug 30, 2026, South Africa. Only $150 total spent, 1 hire/0 active — thin "
                            "history.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard skill mismatch — the client explicitly excludes candidates whose Brevo experience "
                             "is 'limited to sending newsletters,' and wants CRM pipeline architecture plus Meta/"
                             "LinkedIn ad lead-integration and WordPress dev work, none of which is in the evidence "
                             "register (documented strength is segmentation/lifecycle/deliverability, not CRM "
                             "architecture or ads integration). Also already 20-50 competing proposals, 18 "
                             "interviewing, 1 hire already recorded, and thin client spend history ($150).",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Brevo Setup and Training",
            client_name="Unnamed, Canada (Burlington)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Setup-and-Training_~022113468126348158059/",
            posted_at="Not shown explicitly",
            description="Client has a Brevo license and wants help with initial setup and getting the first "
                        "marketing email out — design, structure, campaign creation, response handling, tracking.",
            required_skills="Basic Brevo setup and first-campaign walkthrough.",
            budget_amount=50, budget_currency="USD", budget_type="hourly ($15-$50/hr range)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Apr 14, 2025, Canada. $773 total spent, 2 hires (1 active), 27 hours logged "
                            "— modest but real credibility.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Oversaturated for the scope — 20-50 competing proposals already on a small, simple "
                             "setup/training task. Skill match is fine but probability of winning against that much "
                             "competition for a low-complexity job is too low to justify a proposal.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Fix Brevo Account So Can Send Transactional Emails",
            client_name="Unnamed, USA (Tempe, AZ)",
            url="https://www.upwork.com/freelance-jobs/apply/Fix-Brevo-Account-Can-Send-Transactional-Emails_~022110479308329682186/",
            posted_at="2026-10-14 (17 days before discovery)",
            description="Fix a Brevo account's configuration so it can send transactional emails again — described "
                        "by the client as a simple, one-time coding fix.",
            required_skills="Brevo transactional-email/API configuration.",
            budget_amount=10, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Member since Mar 5, 2016, USA. $15K total spent, 43 hires (11 active), 2,745 hours — "
                            "very credible long-term buyer.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Stale (17 days old, last viewed by client 2 weeks ago) and already shows 'Hires: 1' — "
                             "functionally filled. $10 budget also fails the compensation test outright even if open.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Brevo Email Designer Needed — Quick Email Polish",
            client_name="Unnamed (not scraped — rejected on budget alone)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Email-Designer-Needed-Quick-Email-Polish_~022115823770351866820/",
            posted_at="2026-10-29 (2 days before discovery, per search snippet)",
            description="Email design 'polish' job, per search snippet title/description only.",
            required_skills="Brevo email design.",
            budget_amount=10, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Not scraped.",
            verification_status="UNVERIFIED",
            priority_tier="REJECTED",
            rejection_reason="$10 fixed budget fails the compensation test outright regardless of any other factor — "
                             "same pattern as the $15 Pakistan DNS job rejected in cycle 1. Not worth a full scrape.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Mailchimp to Brevo Migration",
            client_name="Unnamed (not scraped — rejected on staleness alone)",
            url="https://www.upwork.com/freelance-jobs/apply/Mailchimp-Brevo-Migration_~022108186833889589786/",
            posted_at="2026-10-08 (23 days before discovery, per search snippet)",
            description="Platform migration job, per search snippet title/description only.",
            required_skills="Mailchimp and Brevo.",
            budget_amount=140, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Not scraped.",
            verification_status="UNVERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Stale — posted 23+ days before this discovery cycle with no sign of recent activity in "
                             "the search index. Not worth a full scrape given clear staleness disqualifier.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=pph_id,
            title="Email Automation Specialist (Brevo)",
            client_name="Elisha O. (buyer profile), Nigeria",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing/email-automation-specialist-brevo-4399444",
            posted_at="Not shown; job ID (4399444) is well below the 4514550-4528991 range of listings confirmed "
                      "posted Aug-Oct 2026 in this and the prior cycle, implying this is a materially older posting.",
            description="Build Brevo automation flows (welcome series, abandoned cart, post-purchase, winback, "
                        "lead nurturing) for an ecommerce or service business; entry experience level.",
            required_skills="Brevo automation builder, segments/tags/triggers, deliverability troubleshooting.",
            budget_amount=51, budget_currency="GBP", budget_type="fixed (inferred from PPH price field)",
            payment_platform="PeoplePerHour escrow",
            client_history="Buyer profile shown is for a proposal submitter, not confirmed as the job poster's own "
                            "history; could not independently verify client credibility.",
            verification_status="UNVERIFIED",
            priority_tier="REJECTED",
            rejection_reason="No reliable posted date surfaced, and the job ID numbering strongly implies this "
                             "listing significantly predates the Aug-Oct 2026 PeoplePerHour listings confirmed fresh "
                             "in this and the prior cycle — treating as likely stale per the 'don't round up marginal "
                             "matches' rule rather than assuming it's still live on 10 proposals alone.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=pph_id,
            title="Email marketing flows in Brevo for BigCommerce website",
            client_name="Yak E., United Kingdom",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/ecommerce-marketing-managers/email-marketing-flows-in-brevo-for-bigcommerce-website-4514550",
            posted_at="Clarification-board question dated 2026-08-10 — job is at least ~82 days old at discovery.",
            description="Technical Brevo-BigCommerce integration project: order confirmation, dispatch notification, "
                        "review requests, abandoned cart recovery, welcome series, cross-sell flows. Client wants "
                        "someone who 'knows the Brevo-BigCommerce integration inside out.'",
            required_skills="Brevo-BigCommerce technical integration, expert level.",
            budget_amount=100, budget_currency="GBP", budget_type="fixed",
            payment_platform="PeoplePerHour escrow",
            client_history="Buyer side not independently verified from this scrape.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Very stale (~82+ days old, unresolved clarification question from mid-August still "
                             "open), already 42 competing proposals, and the scope is a platform-specific technical "
                             "integration (BigCommerce <-> Brevo) rather than lifecycle/segmentation email marketing "
                             "— outside documented strengths.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Email Marketing for Newsletters",
            client_name="New publication (unnamed), Freelancer.com",
            url="https://www.freelancer.com/projects/email-marketing/brevo-email-marketing-for-newsletters",
            posted_at="Posted 4 months before discovery; job start date stated as 7/17.",
            description="Brevo setup (lists/segments/automations, sender authentication, GDPR/CAN-SPAM compliance), "
                         "one master newsletter template, repeatable content-block system, simple automation flows, "
                         "then ongoing weekly newsletter writing/loading.",
            required_skills="Brevo setup, WordPress, responsive email template design, ongoing newsletter writing.",
            budget_amount=25, budget_currency="USD", budget_type="hourly ($2-$25/hr range)",
            payment_platform="Freelancer.com escrow/Milestone",
            client_history="Not independently scored — moot given project status below.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already awarded and 'In Progress' — project page explicitly shows status 'In Progress', "
                             "posted 4 months ago with 141 proposals, 'Active 4 mos ago'. Filled; nothing to apply to.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Positive finding for source coverage: Freelancer.com INDIVIDUAL project pages scrape fine with "
                  "firecrawl_scrape (unlike the category/listing pages, which are too large) — this resolves part "
                  "of the Freelancer.com gap noted in cycle 2; future cycles should search then scrape individual "
                  "project URLs rather than category pages.",
        ),
        dict(
            source_id=contra_id,
            title="Email Marketing Specialist – Dual Campaigns for Parents & School Leaders",
            client_name="Unnamed, Contra",
            url="https://contra.com/featured-jobs/freelance-marketing-jobs#email-marketing-specialist-dual-campaigns",
            posted_at="Unknown — Contra's public featured-jobs page does not expose a posted date.",
            description="Listed rate and title only: '$25-$40/hr, 20 hrs/wk, Ongoing' for an 'Email Marketer' role, "
                        "surfaced as a recurring 'featured' card on Contra's public marketing-jobs landing page.",
            required_skills="Not stated beyond title/rate.",
            budget_amount=40, budget_currency="USD", budget_type="hourly ($25-$40/hr range)",
            payment_platform="Contra (commission-free; payment rail not detailed)",
            client_history="Not available — Contra's public page exposes no client name, spend history, or "
                           "applicant count for featured cards.",
            verification_status="UNVERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Cannot verify this is a live, currently-open, distinct posting rather than a recurring "
                             "evergreen 'featured' example — Contra's public job board exposes no posted date, "
                             "applicant/competition count, or client credibility signal, and no distinct per-job "
                             "URL was returned by the scrape. Logged for completeness per this cycle's instruction "
                             "to cover the Contra gap, but not scored or qualified given the verification gap — "
                             "would need a logged-in Contra account to check properly.",
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
        ("discovery_scan", NOW, NOW, 5, len(opportunities), 0,
         "Reddit r/forhire individual threads still blocked for a third consecutive cycle "
         "(firecrawl_scrape: 'we do not support this site'); two 'Hiring' titles noted via search snippet only "
         "(Brevo campaign setup walkthrough; UK Brevo/FreeAgent automation — same unconfirmed lead as cycle 1/2) "
         "and could not be scored. Contra's public job board does not expose posted date/applicant "
         "count/client history, so the one Brevo/email listing found there could not be scored, only logged. "
         "German-market search ('deutschsprachig email marketing freelancer gesucht Brevo') surfaced no live job "
         "postings requiring German — mostly agency service pages and marketplace noise — so the unresolved "
         "German-proficiency conflict in the claims register was not triggered either way this cycle."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 3 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
