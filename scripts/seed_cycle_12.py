#!/usr/bin/env python3
"""Discovery cycle 12 (2026-11-22): regular run following cycle 11 (2026-11-21). Picks up cycle
11's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, rate still does not render (7th consecutive cycle), and this
cycle is fully flat versus cycle 11: Interviewing unchanged at 2 (no further movement after cycle
11's 3->2 drop), client totals identical ($68K spent/36 hires/16 active/1,983 hours, all unchanged
from cycle 11). No job-specific "Hires" signal and nothing indicating the listing is gone/closed,
so per the owner's standing instruction this is noted on the DB row only, not re-flagged. (b)
re-checked the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- still
open, same thin 1-hire/1-active client history, rate unchanged ($10-28/hr), invites-sent/unanswered
unchanged at 2/0. Interviewing is flat at 4 this cycle -- the two-cycle rising trend (2->3->4 across
cycles 9-11) has stalled, with no further climb and no hire appearing. Stated clearly per
instruction: this reads as stalled, not progressing further and not closed/filled. Tier not
revised. (c) one more Reddit r/forhire direct firecrawl_scrape attempt (no paid Alexandria
provider used without the owner's go-ahead, open since cycle 7) -- failed identically again, the
7th consecutive cycle blocked on the free method. (d) PeoplePerHour page 1 re-check only -- no
genuinely new live candidate; the two current-section listings were again out-of-scope (Gmail
account setup) or already on file (UK Kajabi, id 8, now 37 proposals), and "Help with Brevo" (id
46) is unchanged in the Past Projects section. 7th cycle running with nothing new from this source.
Also runs fresh Brevo-specific and generic searches across Upwork and Freelancer.com, plus checks
on Contra, the German-market search angle, freelance.de, and Useme.com (brief per instruction,
since these three keep confirming the same structural dead end -- 12th consecutive cycle for
Contra and the German-market search, 6th for freelance.de). Found and logged 1 new URL this cycle
(Freelancer.com), REJECTED: a WordPress/Stripe/Brevo event-registration-automation integration job
that is fundamentally a WordPress-development and payment-webhook integration task (419 competing
proposals, almost all from web developers quoting WordPress/PHP/Stripe experience), not a close
skill match once the actual technical scope is read in full -- Brevo is one piece of the
integration, not the central skill being hired for. A Facebook-group "Email Marketing Specialist
(Brevo)" posting surfaced in search but could not be scraped (Facebook is not a supported
scrape target) and showed a sub-minimum-wage rate ($5.65/hr) in the visible snippet -- not logged
as a DB row since it could not be independently verified per the project's scraping standard, and
noted in the report narrative only. 0 new P0/P1 opportunities this cycle. Not recommending an
application package. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-22-discovery-cycle-12.md for the full narrative."""
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
            "UPDATE sources SET last_scan_at = ?, last_error = ?, terms_notes = ?, "
            "discovery_count = discovery_count + ?, qualified_count = qualified_count + ? WHERE id = ?",
            (NOW, last_error, terms_notes, discovery_count, qualified_count, row[0]),
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
        "Re-scraped the Newsletter Specialist for Campaigns / Brevo listing (id 31) once more as a "
        "quiet status check. Still open. Rate still does not render (7th consecutive cycle). "
        "Fully flat versus cycle 11: Interviewing unchanged at 2, client totals identical ($68K "
        "spent, 36 hires, 16 active, 1,983 hours -- all the same as cycle 11). Last viewed by "
        "client: '2 days ago' (vs 'yesterday' cycle 11, ordinary noise). Also re-checked the "
        "PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email Setup' listing (id 40): still open, "
        "client still 1 hire/1 active, rate unchanged $10-28/hr, invites-sent/unanswered unchanged "
        "at 2/0. Interviewing flat at 4 -- the two-cycle rising trend (2->3->4 across cycles 9-11) "
        "has stalled this cycle, no further climb and no hire appearing. Tier not revised. Fresh "
        "Brevo-specific and generic searches (including the general Upwork email-marketing "
        "category listing, sorted by newest) surfaced no new-to-file Brevo-specific Upwork URL "
        "this cycle -- the newest postings in the category were cold-email/lead-gen/Klaviyo/Meta "
        "roles, none naming Brevo and none a close match once read in full.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 12 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 7th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- that decision "
        "is still the owner's to make, not yet given. No cost incurred, no new data gained, as "
        "expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-11's finding. No genuinely new live candidate: the "
        "two current-section listings this cycle were again 'Gmail account' (Google Workspace "
        "account setup, out of email-marketing scope) and 'UK Kajabi expert' (already on file, id "
        "8, unchanged scope, now 37 proposals vs prior cycles). 'Help with Brevo' (id 46, already "
        "rejected as stale) reappeared again under the Past Projects section with no material "
        "change (still 6 proposals, still '2 months ago'). 7th cycle running with no genuinely "
        "new, live candidate from this source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings + firecrawl_scrape of the email-marketing "
        "category listing pages 1-2",
        "Fresh Brevo-specific and generic searches, plus a direct scrape of the email-marketing "
        "category listing (pages 1-2), surfaced 1 new-to-file URL this cycle: 'WordPress Event "
        "Registration Integration' (Toronto, Canada client), which names Brevo as one of three "
        "integrated systems (WordPress + Stripe + Brevo) but is fundamentally a web-development/"
        "payment-webhook integration task -- REJECTED. 419 competing proposals, nearly all from "
        "web developers citing WordPress/PHP/Stripe experience, not email-marketing specialists. "
        "Page 2 of the category listing surfaced no further Brevo-specific or close-match "
        "candidates (lead-generation, GoHighLevel, AI-chatbot, and bulk Gmail-setup postings, none "
        "a fit). Other search hits matched URLs already on file (cycles 3-11, including the "
        "freelancer.in mirror of the already-closed id-58 'Brevo Workflow Automation Expert Needed "
        "-- 2' listing) or were freelancer self-promotion/portfolio pages.",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "12th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page this cycle returned actual 'Featured freelance marketing jobs' "
        "cards for the first time in several cycles (e.g. 'Marketing Assistant for Launch "
        "Campaign', 'Social Media Carousel Designer'), but none is an email-marketing or Brevo "
        "role -- still never a genuine client email-marketing posting across 12 cycles. A parallel "
        "web search still surfaced only the /hire/brevo-freelancers directory page, not a client "
        "job posting.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query ('Brevo E-Mail Marketing Freiberufler Projekt gesucht') "
        "-- 12th consecutive cycle with no live German-market email-marketing-specialist opening "
        "surfaced; results remain Brevo's own German marketing/help-center pages and "
        "freelance.de directory/profile pages, not client project postings. German-proficiency "
        "claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-11: same Oliver "
        "Tornroth/Zoined posting (now 20 days left, down from 21 in cycle 11), still the only open "
        "listing, still zero live Brevo listings. Rest of the category remains closed Klaviyo/"
        "Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend listings, same as prior cycles. "
        "Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a site-scoped query ('site:freelance.de Brevo E-Mail-Marketing Auftrag') aimed "
        "specifically at a client project/Auftrag posting. Surfaced only freelancer profile/"
        "directory pages (individuals advertising their own Brevo/E-Mail-Marketing skills), no "
        "client project listing at all. 6th consecutive cycle confirming no client "
        "project-posting section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle; prior cycles' finding (general tutorial/"
        "comparison content, no live candidate) assumed unchanged. Covered this cycle instead by "
        "a health/wellness + Brevo search pass folded into the broader generic sweep, which again "
        "surfaced only job-board aggregator/landing pages (Indeed, ZipRecruiter) and Brevo's own "
        "healthcare-email-marketing blog content, not individual live postings.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=freelancer_id,
            title="WordPress Event Registration Integration (Brevo named, but a WordPress/Stripe "
                  "development task, not an email-marketing-specialist role)",
            client_name="Individual client, Toronto, Canada (Freelancer.com; 5.0 rating, 1 review, "
                         "payment method verified; member since Nov 6, 2025)",
            url="https://www.freelancer.com/projects/stripe/wordpress-event-registration-integration",
            posted_at="Posted 3 days before this cycle's discovery; ends in 4 days (bidding "
                      "deadline, not a posting-age signal)",
            description="Build one complete, repeatable event registration/payment/email-"
                        "communication flow connecting an existing WordPress site, Brevo account, "
                        "and Stripe account: WordPress registration form -> Brevo list/segment "
                        "updates -> Stripe Checkout link -> payment webhook back into Brevo "
                        "(paid/unpaid list logic) -> timed reminder and event-detail emails. "
                        "Requires building/configuring the WordPress form-to-Stripe mapping, "
                        "wiring the Stripe payment webhook into Brevo, styling the Brevo email "
                        "template, and end-to-end testing in both Stripe test and live modes, plus "
                        "handover documentation/Loom walkthrough.",
            required_skills="WordPress form building/configuration; Stripe Checkout and payment-"
                             "webhook integration; Brevo contact-list and automation configuration "
                             "(the email-marketing component); end-to-end technical testing; "
                             "written/video handover documentation.",
            budget_amount=140, budget_currency="CAD", budget_type="fixed ($30-250 CAD, paid on "
                          "delivery; 419 bidders averaging $139 CAD)",
            payment_platform="Freelancer.com (fixed-price; not independently tested for TRNC "
                              "residents)",
            client_history="Member since Nov 6, 2025 (just over a year). Toronto, Canada. 5.0 "
                            "rating from 1 review, payment method verified. Several other recent "
                            "jobs posted (LimeSurvey API, Proton email migration, WordPress "
                            "content, YouTube/Elementor) -- a credible, active buyer, but this "
                            "specific listing's scope is the issue, not the client.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Brevo is a genuine named component, but the actual deliverable is a "
                              "WordPress-development and Stripe-payment-webhook integration task "
                              "-- building/configuring a WordPress registration form, wiring a "
                              "Stripe webhook into Brevo, and end-to-end technical testing across "
                              "two systems beyond Brevo itself. None of this (WordPress form "
                              "development, Stripe API/webhook work) is documented experience per "
                              "the claims register, which lists SQL, scripting, and "
                              "platform-integration work as not demonstrated. All 20 visible "
                              "competing bids (419 total proposals) are from web developers citing "
                              "WordPress/PHP/Stripe portfolios, not email-marketing specialists -- "
                              "confirming this is being hired and judged as a dev integration job, "
                              "not an email-marketing role. Budget is also thin once split against "
                              "that competition ($30-250 CAD fixed, averaging $139 CAD across 419 "
                              "bidders).",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com URL this cycle, surfaced by a direct scrape of the "
                  "email-marketing category listing (Brevo appeared in the listing body, not the "
                  "title). Logged for audit-trail completeness. A Facebook-group 'Email Marketing "
                  "Specialist (Brevo)' posting also surfaced in search this cycle but could not be "
                  "scraped (Facebook is not a supported scrape target) and showed a "
                  "sub-minimum-wage rate ($5.65/hr) in the visible search snippet -- not logged as "
                  "a DB row since it could not be independently verified per the project's "
                  "scraping standard; noted here only.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-11. Per the owner's standing
    # instruction (flagged already, their call to act on), this is recorded without being
    # surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 12 (2026-11-22) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (7th consecutive "
              "cycle). Fully flat versus cycle 11: Interviewing unchanged at 2 (no further "
              "movement after cycle 11's 3->2 drop), client totals identical ($68K spent/36 "
              "hires/16 active/1,983 hours, all unchanged). Last viewed by client: '2 days ago' "
              "(vs 'yesterday' in cycle 11 -- ordinary noise). No job-specific 'Hires' field and "
              "no signal the listing is gone or closed. Noted; no fresh flag raised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead.
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 12 (2026-11-22) re-check: still open. Rate still $10-28/hr. Client still "
              "1 hire/1 active (no new hires). Interviewing flat at 4 -- the two-cycle rising "
              "trend (2->3->4 across cycles 9-11) has stalled this cycle, no further climb. "
              "Invites-sent/unanswered unchanged at 2/0. Proposals still 20-50. Stated clearly: "
              "no hire has appeared and nothing indicates this listing has closed; it is stalled, "
              "not progressing further and not filled. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 9, len(opportunities), 0,
         "Cycle 12, the regular run following cycle 11 (2026-11-21). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (7th cycle), fully flat vs cycle 11 on every signal "
         "(Interviewing, client totals) -- not re-flagged per the owner's standing instruction. "
         "(b) Brevo CRM and Email Setup (id 40) rechecked -- still open, Interviewing flat at 4 "
         "(the 2->3->4 rising trend has stalled, no hire appeared), tier not revised. (c) Reddit "
         "r/forhire: direct firecrawl_scrape attempted again, still blocked (7th consecutive "
         "cycle); the paid scrapecreators Alexandria provider was deliberately NOT used again "
         "pending the owner's go-ahead from cycle 7. (d) PeoplePerHour page 1 re-checked only -- "
         "no genuinely new live candidate (7th cycle running). Fresh Brevo/generic searches across "
         "Upwork and Freelancer.com found 1 new URL (Freelancer.com), REJECTED: a WordPress/"
         "Stripe/Brevo event-registration integration job that is fundamentally a web-development "
         "task (419 competing proposals, nearly all from web developers), not an email-marketing "
         "role, once the full scope was read. Contra (12th consecutive cycle with no genuine "
         "client email-marketing posting), the dedicated German-market search (12th consecutive "
         "cycle with nothing live), and freelance.de (6th consecutive cycle confirming no "
         "reachable client-posting section) were checked again briefly per instruction, since "
         "they keep confirming the same structural dead end. Direct business prospecting (master "
         "prompt section 4.3/12) was not run this cycle, per the standing scope instruction. 0 "
         "new P0/P1 opportunities this cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 12 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
