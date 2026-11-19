#!/usr/bin/env python3
"""Discovery cycle 9 (2026-11-19): regular run following cycle 8 (2026-11-18). Picks up cycle 8's
open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo Upwork
listing -- still open, rate still does not render (4th consecutive cycle), Interviewing flat at 3
for the 2nd cycle running; per the owner's standing instruction this is noted on the DB row, not
re-flagged as 'needs attention' again; (b) one more Reddit r/forhire direct firecrawl_scrape
attempt (no paid Alexandria provider used without the owner's go-ahead) -- still blocked, as
expected; (c) PeoplePerHour page 1 re-check only -- no new candidate. Also runs fresh Brevo-
specific and generic searches across Upwork, Freelancer.com, Contra, Useme.com, German-market
search and freelance.de. Found and logged 3 new URLs, all via Freelancer.com, all closed/stale
(1-2+ years old) -- none clear the payment-horizon test. 0 new P0/P1 opportunities. Appends to the
same DB. Safe to re-run (INSERT OR IGNORE on url). See reports/2026-11-19-discovery-cycle-9.md for
the full narrative."""
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
        "Re-scraped the Newsletter Specialist for Campaigns / Brevo listing once more as a quiet "
        "status check (not a re-flag, per the owner's standing instruction -- flagged twice "
        "already). Still open. Rate still does not render (4th consecutive cycle). Proposals "
        "still 20-50; Interviewing flat at 3 (no movement since cycle 7's 0->3 jump, 2nd "
        "consecutive cycle unchanged). Last viewed by client: '2 days ago' (vs 'yesterday' in "
        "cycle 8 -- ordinary noise, not a signal). Client totals flat ($68K/35 hires/16 active, "
        "same as cycles 7-8); hours ticked up 1,976->1,980 (routine usage). Also re-checked the "
        "PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email Setup' listing from cycle 8: still open, "
        "client still 1 hire/1 active (no new hires), interviewing steady at 2 -- essentially "
        "unchanged, tier not revised. Fresh Brevo/generic searches surfaced no new Upwork URL "
        "this cycle; all Brevo-tagged results matched URLs already on file.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 9 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, "
        "as instructed. Failed identically: 'Firecrawl can't scrape this site because it is "
        "currently not supported.' Same result as 8 of the last 9 cycles. A web search also "
        "surfaced one old r/forhire thread (a Brevo e-commerce email marketing listing) via its "
        "search index, but the URL itself could not be scraped for the same reason, so no "
        "verifiable detail (posted date, status, client) could be obtained -- not logged as an "
        "opportunity. Per instruction, did NOT fall back to the paid scrapecreators Alexandria "
        "provider this cycle -- that decision is still the owner's to make, not yet given. No "
        "cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-8's finding. Category now shows 115 results (vs "
        "135 in cycle 8) with a different relevance-sorted mix of listings, but still zero new "
        "Brevo/email-marketing freelance candidates. The 'Marketing & Publishing Assistant "
        "Sales-Minded' listing (already on file, id 9) reappeared on page 1 -- confirmed "
        "duplicate, no action needed. 4th cycle running with no new candidate from this source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific search this cycle surfaced 3 URLs not previously on file, all "
        "already closed at discovery (1-2+ years old, 22-26 proposals each): 'Brevo Advanced "
        "Automation Expert' (closed ~2 yrs ago), 'Email Marketing Specialist' / Softgile (closed "
        "~1 yr ago, also requires 3+ years experience and Mailchimp/Creatio -- would have failed "
        "on scope even if open), and 'Email Designer Needed' (closed ~2 yrs ago -- 'Brevo' here "
        "turned out to be the client's own product/brand name, not the Brevo ESP platform, a "
        "keyword false-positive worth flagging for future search quality). All three logged for "
        "audit-trail completeness since the URLs were not previously on file; none clear the "
        "payment-horizon test.",
        discovery_count=3, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages",
        "9th consecutive cycle with the same structural limitation: search surfaces only "
        "/hire/brevo-freelancers, /hire/email-marketers and related directory pages, plus "
        "freelancer self-promotion/profile content and 'how to start a freelance career' blog "
        "posts -- never a genuine client job posting.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- ninth consecutive cycle with no live German-market "
        "email-marketing-specialist opening surfaced; results remain tutorials, platform blog "
        "content, and review/comparison sites. German-proficiency claims-register conflict "
        "remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-8: same Oliver "
        "Tornroth/Zoined posting (now 23 days left, down from 24 in cycle 8 and 25 in cycle 7), "
        "still the only open listing, still zero live Brevo listings. Rest of the category "
        "remains closed Klaviyo/Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend "
        "listings, same as prior cycles. Polish page 2 not re-checked this cycle (checked cycle "
        "8, one closed Brevo listing already logged).",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a site-scoped query aimed specifically at a client project/Auftrag posting "
        "mentioning Brevo or newsletter work. Surfaced only one irrelevant freelance.de blog "
        "post (customer-retention marketing advice, no job listing at all). 3rd consecutive "
        "cycle confirming no client project-posting section is reachable for this platform via "
        "search; not worth a further dedicated pass without a different access method.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Re-ran the health/wellness + Brevo combined search angle. Surfaced the same general "
        "tutorial/comparison content as cycle 7 plus one Facebook group post (a Brevo/Sendinblue "
        "'project-based, no experience required' listing) -- Facebook, like Reddit, returns "
        "'Firecrawl can't scrape this site because it is currently not supported' on direct "
        "scrape, so no verifiable client/budget/posted-date detail could be obtained and it was "
        "not logged as an opportunity. No new freelance candidate found via this angle this "
        "cycle.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=freelancer_id,
            title="Brevo Advanced Automation Expert (closed before discovery)",
            client_name="Individual client, Jupiter, United States (Freelancer.com; payment "
                         "method verified; member since Sep 4, 2015; 0.0 rating, 0 reviews)",
            url="https://www.freelancer.com/projects/internet-marketing/brevo-advanced-automation-expert",
            posted_at="Posted about 2 years ago; closed, active 2 yrs ago",
            description="Patient-doctor matching automation in Brevo: API trigger 'Doctor_Matched' "
                        "needs to route emails to doctor_email (not the default patient email_id); "
                        "contact-attribute mapping and event-data routing issue.",
            required_skills="Brevo automation configuration, contact-attribute mapping, API "
                             "trigger/event data routing.",
            budget_amount=140, budget_currency="USD", budget_type="fixed ($30-250 USD)",
            payment_platform="Freelancer.com (fixed-price, paid on delivery; not independently "
                              "tested for TRNC residents)",
            client_history="Member since Sep 4, 2015. United States (Jupiter). 0.0 rating, 0 "
                            "reviews on this account despite the long tenure -- no completed-job "
                            "track record visible on the public page.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed -- posted about 2 years before this cycle's "
                              "discovery, with 24 proposals already on record (average bid "
                              "$151). No live opportunity exists; fails the payment-horizon test "
                              "outright. The scope itself (Brevo automation/routing "
                              "troubleshooting) would otherwise have been a reasonable skill "
                              "match. Logged for audit-trail completeness since this URL was not "
                              "previously on file.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Surfaced by a fresh Brevo-specific Freelancer.com search this cycle. Confirms "
                  "the pattern seen on this source since cycle 3: most search hits for "
                  "'Brevo'+'freelance' on this platform are long-closed listings, not live work.",
        ),
        dict(
            source_id=freelancer_id,
            title="Email Marketing Specialist (Softgile) (closed before discovery)",
            client_name="Softgile (tech company), Bielany Wroclawskie, Ukraine (Freelancer.com; "
                         "member since Jun 25, 2025; 0.0 rating, 0 reviews)",
            url="https://www.freelancer.com/projects/email-marketing/email-marketing-specialist-39546138",
            posted_at="Posted over 1 year ago; closed, active 1 yr ago",
            description="End-to-end CRM/lifecycle email marketing campaigns: planning, "
                        "segmentation, hypothesis development, execution, performance analysis, "
                        "A/B testing. Tools named: Mailchimp, Brevo, Creatio.",
            required_skills="3+ years of email marketing/CRM/lifecycle marketing experience; "
                             "hands-on Mailchimp, Brevo, Creatio; A/B testing; marketing "
                             "automation tools generally.",
            budget_amount=20, budget_currency="USD", budget_type="hourly ($15-25 USD/hr)",
            payment_platform="Freelancer.com (hourly; not independently tested for TRNC residents)",
            client_history="Member since Jun 25, 2025. Ukraine. 0.0 rating, 0 reviews -- new, "
                            "unestablished account.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed -- posted over 1 year before this cycle's discovery, "
                              "26 proposals already on record. Would also have failed on scope "
                              "even if open: stated requirement of 3+ years of experience exceeds "
                              "the project's ~2-year job-search filter (claims register), and "
                              "Mailchimp is an explicitly PROHIBITED unevidenced-tool claim (Brevo "
                              "is only one of three named tools, not the primary one). Logged for "
                              "audit-trail completeness.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Second of three new-to-file Freelancer.com URLs this cycle, all stale. "
                  "Multi-reason reject (staleness + experience filter + unevidenced tools), "
                  "logged in full for the audit trail.",
        ),
        dict(
            source_id=freelancer_id,
            title="Email Designer Needed (closed before discovery; 'Brevo' = client's own brand, "
                  "not the platform)",
            client_name="Individual client, Abu Dhabi, United Arab Emirates (Freelancer.com; "
                         "payment method verified; 5.0 rating, 4 reviews; member since Dec 11, "
                         "2023)",
            url="https://www.freelancer.com/projects/email-marketing/email-designer-needed",
            posted_at="Posted over 2 years ago; closed, active 2 yrs ago",
            description="Design a series of promotional and automated (post-purchase, order "
                        "confirmation) emails for 'our brand, Brevo', compatible with Gmail, "
                        "Outlook and Yahoo Mail.",
            required_skills="Email design (HTML), cross-client compatibility testing. No Brevo "
                             "(the ESP platform) skill actually required -- 'Brevo' here is the "
                             "client's own product/brand name, confirmed by context (several "
                             "bidders' proposals also read it as a brand, not a tool).",
            budget_amount=48, budget_currency="USD", budget_type="fixed ($10-30 USD)",
            payment_platform="Freelancer.com (fixed-price, paid on delivery; not independently "
                              "tested for TRNC residents)",
            client_history="Member since Dec 11, 2023. United Arab Emirates (Abu Dhabi). 5.0 "
                            "rating across 4 reviews, payment method verified -- a credible, "
                            "established small account.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed -- posted over 2 years before this cycle's "
                              "discovery, 22 proposals already on record. Separately, this is a "
                              "keyword false-positive for this project's Brevo-platform search: "
                              "'Brevo' in the listing is the client's own brand/product name "
                              "(an email-marketing or SaaS brand being promoted), not a request "
                              "for skill with the Brevo ESP platform -- there is no actual "
                              "platform-skill match here even setting staleness aside. Logged "
                              "for audit-trail completeness and flagged as a search-quality note "
                              "for future cycles.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Third of three new-to-file Freelancer.com URLs this cycle. Notable mainly as "
                  "a search-noise example: 'Brevo' search hits are not always about the Brevo "
                  "platform. Worth remembering when scoring future 'Brevo'-keyword hits on any "
                  "source, not just Freelancer.com.",
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

    # Update the still-open P1 lead from cycles 5-8 with this cycle's quiet re-check. Per the
    # owner's standing instruction (flagged twice already, their call to act on), this is recorded
    # without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 9 (2026-11-19) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (4th consecutive "
              "cycle). Interviewing flat at 3 (2nd consecutive cycle with no movement). "
              "Proposals still 20-50. Last viewed by client: '2 days ago' (vs 'yesterday' in "
              "cycle 8 -- ordinary noise). Client totals flat: $68K spent/35 hires/16 active "
              "(same as cycles 7-8); hours ticked up 1,976->1,980 (routine usage). Nothing "
              "materially new; no action taken, no fresh flag raised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Quiet re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead from
    # cycle 8, since it was also re-scraped this cycle (not required by the owner's standing
    # instruction, but checked for completeness as the second-best lead on file).
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 9 (2026-11-19) re-check: still open, client still 1 hire/1 active (no "
              "new hires since cycle 8), interviewing steady at 2, proposals still 20-50. "
              "Essentially unchanged; tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 8, len(opportunities), 0,
         "Cycle 9, the regular run following cycle 8 (2026-11-18). Followed up on all three "
         "carried-over open items: (a) Newsletter Specialist for Campaigns / Brevo rechecked once "
         "quietly -- still open, rate still unconfirmed (4th cycle), interviewing flat at 3 (2nd "
         "cycle unchanged) -- not re-flagged per the owner's standing instruction (flagged twice "
         "already). (b) Reddit r/forhire: direct firecrawl_scrape attempted again, still blocked; "
         "the paid scrapecreators Alexandria provider was deliberately NOT used again pending the "
         "owner's go-ahead from cycle 7. (c) PeoplePerHour page 1 re-checked only -- no new "
         "candidate, 4th cycle running. Fresh Brevo/generic searches across Upwork, "
         "Freelancer.com, Contra, Useme.com, German-market and freelance.de found 3 new URLs, "
         "all via Freelancer.com, all already closed (1-2+ years stale) and none clearing the "
         "payment-horizon test; one also surfaced a useful search-quality finding ('Brevo' as a "
         "client's own brand name, not the ESP platform). Direct business prospecting (master "
         "prompt section 4.3/12) was not run this cycle, same reasoning as cycle 8: its method "
         "ends in drafting outreach, out of scope for this cycle's no-drafting instruction. 0 new "
         "P0/P1 opportunities this cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 9 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
