#!/usr/bin/env python3
"""Discovery cycle 6 (2026-11-16): regular daily run following cycle 5's consolidated catch-up
(2026-11-15). Picks up cycle 5's three open items: (a) re-check the undisclosed hourly rate on
the Newsletter Specialist for Campaigns / Brevo Upwork listing, (b) PeoplePerHour pages 5-7,
(c) one more Reddit r/forhire attempt. Also runs fresh Brevo-specific and generic searches and
continues rotating through source gaps (Freelancer.com, Contra, German-market), and tries two
new sources (Useme.com, EmailJobs.io). Appends to the same DB. Safe to re-run (INSERT OR IGNORE
on url). See reports/2026-11-16-discovery-cycle-6.md for the full narrative."""
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
        "Re-scraped the Newsletter Specialist for Campaigns / Brevo listing (cycle 5's flagged "
        "open item) to check whether the hourly rate renders -- it still does not. Everything "
        "else on the listing is unchanged except small counter drift (last-viewed 4 days ago vs "
        "3, 1,973 hours vs 1,972, still 20-50 proposals, still 0 interviewing). Fresh Brevo/"
        "generic searches surfaced only listings already on file; no new candidate found.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing pages 5-7 this cycle (pages 1-4 covered cycles 4-5)",
        "Pages 5, 6 and 7 scraped, completing the page sweep cycle 5 recommended. Structural "
        "finding: the ?page= parameter only paginates the 'Past Projects' (closed) archive "
        "section -- the 'currently open' section at the top of the category (just 2 listings: "
        "'Gmail account' $10 Google Workspace setup, not email-marketing work; and the already-"
        "logged UK Kajabi listing) is IDENTICAL on pages 5, 6 and 7. There is no deeper page of "
        "open listings to find -- the category genuinely has only 2 open jobs right now. Pages "
        "5-7's archive entries (6-9 months old) are Mailchimp/Klaviyo/HubSpot/Wix-automation "
        "work, none Brevo, none open. Page sweep is now complete; no further PeoplePerHour page "
        "scraping is likely to find anything beyond what re-checking page 1 (the live/open "
        "section) would show.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Search resurfaced only listings already on file (closed, same as cycles 3-5), plus one "
        "new trivial $10-30 'Upload HTML Email to Brevo' task (log-in-and-click-send, no "
        "copywriting/strategy) -- screened and rejected on sight, same pattern as the near-"
        "identical 'Upload completed emails to brevo right now' task rejected on sight in cycle 5.",
        discovery_count=0, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/freelancer pages",
        "Same structural limitation persists: results are entirely 'hire a Brevo/Klaviyo/Yotpo "
        "freelancer' directory pages and freelancer self-profiles, not client job postings. No "
        "scorable listing surfaced, continuing the pattern from every prior cycle.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_search only; firecrawl_scrape refuses reddit.com directly",
        "Confirmed blocked for a SIXTH consecutive cycle: firecrawl_scrape returns "
        "\"Firecrawl can't scrape this site because it is currently not supported\" for "
        "reddit.com, now including search-results URLs, not just individual threads. "
        "Recommendation given in this cycle's report: drop this source from the rotation (or "
        "replace it with a different access method) unless the owner wants to keep paying the "
        "cost of a call that has not produced one scorable listing in six tries.",
        last_error="firecrawl_scrape: 'currently not supported' for reddit.com",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran 'E-Mail Marketing Freelancer gesucht Brevo Newsletter deutschsprachig Job' -- "
        "sixth consecutive cycle with no live German-market email-marketing-specialist opening "
        "surfaced. Results remain freelancer-for-hire directory pages, not open roles. The "
        "German-proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page + individual job page (new source this cycle)",
        "New source tried this cycle (Polish/European freelance marketplace with escrow-style "
        "invoicing). The email-marketing category is dominated by closed listings requiring "
        "Klaviyo, GetResponse, Mailchimp, Mailerlite, Edrone, or Snov.io -- no Brevo listing "
        "found, open or closed. One open listing (Zoined, Mailchimp/HubSpot-based "
        "content+email role) was fully scraped and rejected -- see opportunities table. Useme "
        "also carries a platform-specific quirk worth flagging: at least this listing's terms "
        "reference a Polish student/school-ID requirement for payment settlement, which may "
        "affect whether a non-Polish-resident freelancer can even be paid through it -- untested, "
        "and on top of the existing unresolved TRNC payment-routing question for any other rail.",
        discovery_count=1, qualified_count=0,
    )
    emailjobs_id = get_or_create_source(
        conn, "EmailJobs.io", "https://www.emailjobs.io/remote-email-marketing-jobs",
        "firecrawl_scrape of category/landing pages (new source this cycle)",
        "New source tried this cycle. The site's 'Freelance Email Marketing Specialist' page is "
        "pure SEO/navigation content with zero actual listings. Its 'Remote Email Marketing "
        "Jobs' page does list real postings, but every one is a salaried full-time or contract "
        "W2-style role with a company and salary band (Vanta, Houzz, Scribd, etc.), not a "
        "freelance/project listing -- structurally not a fit for this project's freelance-"
        "opportunity scope. No scorable candidate found; likely not worth revisiting unless the "
        "site adds a genuine freelance-listings section.",
        discovery_count=0, qualified_count=0,
    )
    remotejobs_agg_id = get_or_create_source(
        conn, "remotejobs.dedyn.io (aggregator, data-quality flag)",
        "https://us.remotejobs.dedyn.io",
        "firecrawl_scrape of individual job page, reached via general web search",
        "Surfaced one nominally 'freelance' Email Marketing Specialist listing via search, but "
        "the scraped content is templated/corrupted: the employer name, brand name and nearly "
        "every platform/tool reference are literally replaced with the placeholder string "
        "'reputed company' throughout the posting, and the page inconsistently labels the role "
        "both 'Freelance' (title) and 'Full-time' (metadata/structured data). Logged as "
        "SUSPICIOUS and rejected -- client identity, actual platform requirement, and genuine "
        "scope cannot be verified from this page. Flagging the source itself as unreliable.",
        last_error="Listing content templated/corrupted -- placeholder text in place of real employer/brand/tool names",
        discovery_count=1, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=useme_id,
            title="Part-time B2B content & email marketer (remote, ~15h/week)",
            client_name="Oliver Törnroth, Marketing Manager, Zoined (Finnish B2B analytics SaaS "
                         "for retail/hospitality)",
            url="https://useme.com/en/jobs/part-time-b2b-content-email-marketer-remote-15h-week-excellent-english,147376/",
            posted_at="Published 4 days before discovery (2026-11-16); listing expires in 30 days",
            description="Part-time (~15 hrs/week) role mixing B2B email campaigns (Mailchimp/"
                        "HubSpot) to targeted segments, LinkedIn post writing/scheduling, and "
                        "turning recorded expert conversations into blog posts. Budget ~EUR "
                        "1,400/month, includes a short paid trial task.",
            required_skills="Mailchimp and HubSpot ('or quick to learn them'), B2B/SaaS content "
                             "and email copywriting, LinkedIn posting, blog writing, strong "
                             "written English.",
            budget_amount=1400, budget_currency="EUR",
            budget_type="monthly retainer (~15 hrs/week, roughly EUR 21-23/hr effective)",
            payment_platform="Useme.com (Polish freelancer-invoicing platform; client deposits "
                              "before work starts per the site's own model)",
            client_history="Individual poster (marketing manager at Zoined); no prior useme.com "
                            "track record visible on this listing; 25 competing offers already "
                            "sent within days of posting.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Platform mismatch: the role explicitly runs on Mailchimp and "
                              "HubSpot, both PROHIBITED hands-on claims per the claims register "
                              "(documented experience is Brevo only) -- 'or quick to learn them' "
                              "does not change that the client wants demonstrated comfort with "
                              "tools not evidenced. Scope is also mixed content/social/blog work "
                              "more than email-marketing-specialist work. Separately, the "
                              "listing's Polish-language terms reference a student/school-ID "
                              "requirement for payment settlement on Useme, which is unresolved "
                              "for a non-Polish-resident freelancer and adds a payment-routing "
                              "question on top of the already-unresolved TRNC rail questions in "
                              "evidence/payment-routing.md. 25 competing offers within days adds "
                              "real competition on top of both issues.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="First candidate logged from a new source (Useme.com) tried this cycle. "
                  "Rejected on platform-claim and scope grounds independent of the payment-"
                  "routing question, but the Polish student-ID payment clause is worth keeping "
                  "in mind if Useme.com listings come up again.",
        ),
        dict(
            source_id=remotejobs_agg_id,
            title="[Remote] Email Marketing Specialist, Freelance (listing data corrupted)",
            client_name="Unverifiable -- employer name replaced with placeholder text throughout "
                         "the scraped page",
            url="https://us.remotejobs.dedyn.io/job/remote-email-marketing-specialist-freelance-82670292",
            posted_at="Posted Nov 15, 2026 per page metadata",
            description="Nominally an eyewear-brand freelance Email Marketing Specialist role "
                        "(email+SMS campaigns, flows, segmentation), but the scraped content "
                        "substitutes the literal placeholder string 'reputed company' for the "
                        "employer name, brand name, and most tool/platform references throughout "
                        "the body text -- the page cannot be read as a reliable source of fact.",
            required_skills="Unverifiable (platform/tool names also redacted to placeholder text "
                             "in the scrape).",
            budget_amount=None, budget_currency=None, budget_type="unknown",
            payment_platform="Unknown",
            client_history="Unverifiable.",
            verification_status="SUSPICIOUS",
            priority_tier="REJECTED",
            rejection_reason="Listing content is templated/corrupted on this aggregator -- cannot "
                              "verify client identity, the actual email platform required, or "
                              "genuine scope from this page, and the page inconsistently labels "
                              "the role both 'Freelance' (title) and 'Full-time' (metadata). Not "
                              "a reliable, scorable listing regardless of underlying fit.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Logged for audit-trail transparency and to flag this aggregator's data "
                  "quality; not recommended as a source to prioritize going forward unless this "
                  "proves to be a one-off scrape glitch rather than a systemic template issue.",
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

    # Update the still-open P1 lead from cycle 5 with this cycle's re-check, without changing its
    # score/tier -- the rate still does not render, so nothing has actually changed to re-score.
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?",
        ("https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/",),
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 6 (2026-11-16) re-check: hourly rate still does not render in the public "
              "scrape. Listing otherwise unchanged (last viewed by client 4 days ago vs 3 days "
              "in cycle 5; 1,973 hours logged vs 1,972; still 20-50 proposals, still 0 "
              "interviewing). Not applying; still flagged for the owner to check the rate "
              "directly on Upwork before any package is prepared."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW,
             "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 8, len(opportunities), 0,
         "Cycle 6, the regular daily run following cycle 5's 14-firing consolidated catch-up. "
         "Followed up on all three of cycle 5's open items: (a) Newsletter Specialist for "
         "Campaigns / Brevo rate re-checked -- still does not render, not applying; (b) "
         "PeoplePerHour pages 5-7 completed -- structural finding that only 2 jobs are "
         "currently open in the whole category and the page parameter only paginates the closed "
         "archive, so the page sweep is now complete; (c) Reddit r/forhire tried once more -- "
         "blocked for a sixth consecutive cycle, recommending the source be dropped or replaced. "
         "Two new sources tried (Useme.com, EmailJobs.io); Useme produced one scorable candidate "
         "(rejected on platform-claim/scope/payment-clause grounds), EmailJobs.io produced "
         "nothing freelance-relevant. One aggregator listing (remotejobs.dedyn.io) logged as "
         "SUSPICIOUS/REJECTED due to template-corrupted content. 0 new P0/P1 opportunities this "
         "cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 6 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
