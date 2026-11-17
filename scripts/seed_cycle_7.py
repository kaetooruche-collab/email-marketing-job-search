#!/usr/bin/env python3
"""Discovery cycle 7 (2026-11-17): regular run following cycle 6 (2026-11-16). Picks up cycle 6's
three open items: (a) re-check the Newsletter Specialist for Campaigns / Brevo Upwork rate one
more time (per instruction, after this it should stop being re-scraped every cycle unless
something changes); (b) re-check PeoplePerHour page 1 only (page-sweep is complete per cycle 6);
(c) one more Reddit r/forhire attempt using a genuinely new method (scrapecreators
reddit/subreddit-posts via Alexandria, instead of direct firecrawl_scrape, which has failed for
6 consecutive cycles). Also runs fresh Brevo-specific and generic searches, re-checks
Freelancer.com/Contra/German-market, and tries two new angles/sources this cycle: the
scrapecreators Reddit provider, and freelance.de (German freelance marketplace). Appends to the
same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-17-discovery-cycle-7.md for the full narrative."""
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
        "Re-scraped the Newsletter Specialist for Campaigns / Brevo listing one more time. "
        "Hourly rate still does not render (2 consecutive cycles now failing to render it -- per "
        "instruction, stopping routine re-scrapes of this listing going forward unless something "
        "materially changes). Notable change this time: 'Interviewing' jumped from 0 to 3 "
        "(client is now actively engaging candidates), last viewed by client moved from '4 days "
        "ago' to 'yesterday', client totals ticked up ($68K spent vs $65K, 35 hires vs 34, 16 "
        "active vs 15). Proposals still 20-50, hours still 1,973. Fresh Brevo/generic searches "
        "surfaced only listings already on file, one newly-seen but already-CLOSED Freelancer.com "
        "listing (logged below), and several off-platform/off-tool postings (MailWizz, Klaviyo, "
        "cold-email/outbound) that don't fit the evidenced skill set -- screened out, not logged.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6 -- "
        "?page= only paginates the closed archive, confirmed structurally not worth re-sweeping)",
        "Re-checked page 1 only per cycle 6's recommendation. Identical to cycle 6: exactly 2 "
        "open listings -- 'Gmail account' ($10, Google Workspace admin setup, not email "
        "marketing) and the already-logged UK Kajabi listing (duplicate, not re-logged). No new "
        "open listing. Confirms the category genuinely refreshes slowly; page-1-only re-checks "
        "remain sufficient going forward.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Search resurfaced mostly listings already on file, plus one newly-seen URL ('Brevo "
        "Promotional Automation Workflow Build', Madrid-based client) that turned out to be "
        "already CLOSED/awarded (posted/awarded ~2 months ago, 40 competing bids, awarded to "
        "another freelancer for EUR0) -- logged for the audit trail as a stale/closed reject, "
        "not a live candidate.",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages",
        "Same structural limitation persists for a 7th cycle: search surfaced a community post "
        "tagged 'Brevo' and 'Email Automation' ('Email Marketing Expert with deep expertise in "
        "SMTP setup...') but on scrape this is a freelancer's own self-promotion/portfolio post "
        "(by Sohit Sharma, showcasing his own service), not a client hiring post -- no budget, "
        "no client, no application mechanism. Confirms Contra's public pages still expose no "
        "genuine client job postings, only directory/hire pages and freelancer self-promotion.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 6 cycles); this cycle also tried the scrapecreators "
        "reddit/subreddit-posts Alexandria provider as a genuinely new access method",
        "firecrawl_scrape still refuses reddit.com directly (consistent with 6 prior cycles). "
        "NEW THIS CYCLE: tried the scrapecreators 'reddit/subreddit-posts' structured-data "
        "provider via Alexandria instead -- this WORKED (returned 25 real, current r/forhire "
        "posts with full post data, something no prior cycle achieved). This breaks the "
        "'structurally unscrapable' framing: Reddit r/forhire IS accessible via this provider, "
        "at a small Firecrawl-credit cost per call. However, none of the 25 most recent posts "
        "(the subreddit's last ~13 hours of activity) mentioned email marketing, Brevo, or "
        "newsletters -- so this attempt produced a working method but zero scorable candidates "
        "this cycle. Recommend the owner decide whether to adopt scrapecreators as the standing "
        "method for this source going forward (it has a real per-call cost, unlike the free "
        "failed scrapes) now that an access path exists.",
        last_error=None,
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the same German-language query -- seventh consecutive cycle with no live "
        "German-market email-marketing-specialist opening surfaced; results remain freelancer-"
        "for-hire directories and agency service pages, not open roles. The German-proficiency "
        "claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page",
        "Re-checked the category page. Still exactly one open listing -- the same Oliver "
        "Törnroth/Zoined posting logged and rejected in cycle 6 (now showing 25 days left "
        "instead of 30, same posting, not re-logged). Category remains dominated by closed "
        "Klaviyo/Mailchimp/GetResponse/MailerLite/Edrone/Snov.io listings; still zero Brevo "
        "listings found, open or closed, across two cycles of checking.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages (new source this cycle)",
        "New German freelance-marketplace source tried this cycle, as part of the German-market "
        "rotation. Same structural limitation as Contra: search surfaced only 'find a Brevo/"
        "Newsletter freelancer' directory pages (freelancer-for-hire listings), not client job "
        "postings. No scorable listing found; likely not worth a dedicated full scrape pass "
        "unless a future query surfaces an actual project/Projekt listing page rather than a "
        "directory page.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle",
        "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms (new "
        "search angle this cycle)",
        "Tried a new search angle combining the health/wellness niche (the chosen first "
        "freelance niche per the claims register) with Brevo-specific terms. Surfaced one real "
        "posting -- 'Email & SMS Production Specialist' at Dr. Berg Nutritionals ($32-40/hr, "
        "fully remote) -- but it is a salaried FULL-TIME W2 role (not freelance/project work, "
        "out of this workstream's scope) and explicitly runs on Klaviyo (PROHIBITED hands-on "
        "claim per the claims register). Rejected on both scope and platform grounds; not logged "
        "as an opportunity row since it was never a freelance candidate. Otherwise this angle "
        "surfaced general email-marketing-platform blog content (EmailToolTester, Coachful.co), "
        "not client postings.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=freelancer_id,
            title="Brevo Promotional Automation Workflow Build (closed before discovery)",
            client_name="Individual client, Madrid, Spain (Freelancer.com, 0 prior reviews, "
                         "payment method verified)",
            url="https://www.freelancer.com/projects/email-marketing/brevo-promotional-automation-workflow",
            posted_at="Posted ~2 months before discovery (2026-09ish); status 'Completed', "
                      "awarded ~2 months ago",
            description="Full Brevo (Sendinblue) automation workflow build from a client-supplied "
                        "plan: welcome series rolling into newsletters, timed product-launch "
                        "announcements, sales/discount pushes, segments/tags, dynamic content, "
                        "A/B splits, resend-to-non-openers. Budget EUR 30-250, paid on delivery.",
            required_skills="Brevo (Sendinblue) automation/workflow building, segmentation, "
                             "A/B testing, deliverability troubleshooting.",
            budget_amount=250, budget_currency="EUR", budget_type="fixed (paid on delivery)",
            payment_platform="Freelancer.com (Milestone/escrow; TRNC payment-routing caveats per "
                              "evidence/payment-routing.md apply to any eventual payout)",
            client_history="Madrid-based individual client, 0.0 rating / 0 reviews, payment "
                            "method verified, member since Sep 15, 2026 -- thin history.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed and awarded (to another freelancer, for EUR0, "
                              "~2 months before this cycle's discovery) -- fails the payment-"
                              "horizon test outright since there is no live opportunity to apply "
                              "to. Logged purely for audit-trail completeness since this was a "
                              "URL not previously on file; not a scoring call on fit (the scope "
                              "itself, Brevo automation building, is a reasonable skill match in "
                              "the abstract).",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Surfaced by a fresh Brevo-specific search this cycle; turned out to already be "
                  "closed/awarded. No action needed; logged so it isn't re-surfaced and re-"
                  "checked in a future cycle.",
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

    # Update the still-open P1 lead from cycles 5-6 with this cycle's re-check. Rate still does
    # not render, but the activity signal (Interviewing: 0 -> 3) is a real change worth recording,
    # even though it doesn't change the tier/score (no new confirmable fact about the rate).
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 7 (2026-11-17) re-check: hourly rate still does not render in the "
              "public scrape (2nd consecutive cycle failing to render it) -- per the owner's "
              "standing instruction, this is the last routine re-scrape of this listing; future "
              "cycles will note it as 'unchanged, rate still unconfirmed, needs a human with "
              "Upwork login' without spending a fresh scrape unless something material changes. "
              "One thing DID change this time: Interviewing went from 0 to 3, last-viewed-by-"
              "client moved from '4 days ago' to 'yesterday', and client totals ticked up "
              "($68K/35 hires/16 active vs $65K/34/15). This reads as the client actively moving "
              "toward a hire -- if anything this makes the window to act narrower, not wider. "
              "Still not applying without the rate; still flagged for the owner to check directly "
              "on Upwork if they want to move on it before it's filled."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 9, len(opportunities), 0,
         "Cycle 7, the regular run following cycle 6 (2026-11-16). Followed up on all three of "
         "cycle 6's open items: (a) Newsletter Specialist for Campaigns / Brevo rate re-checked "
         "one final time -- still does not render; per instruction, routine re-scraping of this "
         "listing stops here unless something material changes (note: Interviewing did jump "
         "0->3 this cycle, recorded on the row, tier/score unchanged). (b) PeoplePerHour page 1 "
         "re-checked only (sweep already complete) -- identical 2 open listings, no new "
         "candidate. (c) Reddit r/forhire tried once more with a genuinely new method "
         "(scrapecreators reddit/subreddit-posts via Alexandria instead of firecrawl_scrape) -- "
         "this WORKED technically for the first time in 7 cycles, returning real post data, but "
         "zero of the 25 most recent r/forhire posts were email-marketing/Brevo-relevant. Two "
         "new angles tried: freelance.de (new German marketplace source -- same directory-only "
         "pattern as Contra, no client postings exposed) and a health/wellness-niche + Brevo "
         "search angle (surfaced one full-time Klaviyo-based role, out of scope on both counts, "
         "not logged as an opportunity). One new URL found and logged (Freelancer.com Brevo "
         "Promotional Automation Workflow Build) but it was already closed/awarded before "
         "discovery. 0 new P0/P1 opportunities this cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 7 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
