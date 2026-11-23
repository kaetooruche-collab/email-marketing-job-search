#!/usr/bin/env python3
"""Discovery cycle 13 (2026-11-23): regular run following cycle 12 (2026-11-22). Picks up cycle
12's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, hourly rate still does not render (8th consecutive cycle),
and this cycle is essentially flat versus cycle 12: Interviewing unchanged at 2, client totals
ticked up only marginally (1,985 hours vs 1,983 -- ordinary usage noise, same $68K/36 hires/16
active). No job-specific "Hires" signal and nothing indicating the listing is gone or closed, so
per the owner's standing instruction this is noted on the DB row only, not re-flagged. (b)
re-checked the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- the one
lead that showed real movement across cycles 9-11 (Interviewing climbing 2->3->4) and then stalled
at 4 in cycle 12. This cycle: still stalled at 4, a 2nd consecutive cycle with no further climb and
no hire appearing. Rate unchanged ($10-28/hr), client still 1 hire/1 active, invites-sent/unanswered
unchanged at 2/0. Stated plainly per instruction: it has NOT moved again -- not up, no hire, not
closed. Tier not revised. (c) one more Reddit r/forhire direct firecrawl_scrape attempt (no paid
scrapecreators Alexandria provider used without the owner's go-ahead, open since cycle 7) -- failed
identically again, the 8th consecutive cycle blocked on the free method. (d) PeoplePerHour page 1
re-check only -- no genuinely new live candidate matching scope: the current-listings section held
one new posting ("Cold Email Marketing Specialist", Dubai B2B cold-email/lead-gen for a tax
consultancy, $131 fixed) that is out of scope (cold-outreach lead generation, not Brevo/email-
marketing-platform work, no documented skill match) and "Gmail account" (unchanged, out of scope).
"UK Kajabi expert" (id 8) moved from current to the Past Projects section (unchanged scope, still on
file). "Help with Brevo" (id 46) unchanged in Past Projects. 8th cycle running with nothing new from
this source. Also runs fresh Brevo-specific and generic searches across Upwork and Freelancer.com,
plus checks on Contra, the German-market search angle, freelance.de, and Useme.com (brief per
instruction, since these three keep confirming the same structural dead end -- 13th consecutive
cycle for Contra and the German-market search, 7th for freelance.de). Found 2 new-to-file URLs this
cycle: (1) "Brevo Expert for Creative Email Mailings" (Upwork, open) -- REJECTED on compensation
($7.00/hr, well below a viable rate once TRNC payment-routing friction and Upwork's service fee are
applied) and on competition (client already interviewing 4 candidates out of 15-20 proposals, 4
invites already sent -- an active, advanced-stage listing). (2) "Upload completed emails to brevo
right now -- 2" (Freelancer.com) -- REJECTED/closed: already awarded to another freelancer for $0
USD before this cycle's discovery; trivial $10-30 budget for 8 HTML-email uploads, logged for audit-
trail completeness only. Two further search hits (a real-estate cold-email mail-merge job closed
over a year ago, and a Mailchimp/Klaviyo-required campaign-setup job closed 5 months ago, both
stale and not independently actionable) and a years-stale Reddit post surfaced by search were not
logged as DB rows, consistent with the project's standard of only logging independently verified,
live-at-discovery candidates; noted in the report narrative only. 0 new P0/P1 opportunities this
cycle. Not recommending an application package. Appends to the same DB. Safe to re-run (INSERT OR
IGNORE on url). See reports/2026-11-23-discovery-cycle-13.md for the full narrative."""
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
        "quiet status check. Still open. Rate still does not render (8th consecutive cycle). "
        "Essentially flat versus cycle 12: Interviewing unchanged at 2, client totals ticked up "
        "only marginally (1,985 hours vs 1,983 -- ordinary usage noise; $68K spent/36 hires/16 "
        "active all unchanged). Last viewed by client: '3 days ago' (vs '2 days ago' cycle 12, "
        "ordinary noise). Also re-checked the PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email "
        "Setup' listing (id 40), the one lead that showed real movement (Interviewing 2->3->4 "
        "across cycles 9-11) before stalling at 4 in cycle 12: this cycle it is STILL at 4, a 2nd "
        "consecutive cycle with no further climb and no hire. Rate unchanged $10-28/hr, client "
        "still 1 hire/1 active, invites-sent/unanswered unchanged at 2/0. Tier not revised. Fresh "
        "Brevo-specific and generic searches (including the general Upwork email-marketing "
        "category listing, sorted newest) surfaced 1 new-to-file Brevo-specific Upwork URL this "
        "cycle: 'Brevo Expert for Creative Email Mailings' -- REJECTED on compensation ($7.00/hr) "
        "and competition (client already interviewing 4 of 15-20 proposals, 4 invites already "
        "sent). The newest general-category postings were Klaviyo/cold-email/lead-gen/B2B-sales "
        "roles, none naming Brevo and none a close match once read in full.",
        discovery_count=1, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 13 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 8th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- that decision "
        "is still the owner's to make, not yet given. A generic web search surfaced only a years-"
        "stale Reddit thread ('Hiring Email Marketing Specialist for E-commerce Business (Brevo)', "
        "a 2024-era post ID) which could not be independently verified as live since Reddit remains "
        "unscrapeable -- not logged as a DB row. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-12's finding. No genuinely new live candidate matching "
        "scope: the current-listings section held one new posting this cycle, 'Cold Email "
        "Marketing Specialist' (Dubai B2B tax-consultancy lead generation, $131 fixed, 16 "
        "proposals, 19 hours old) -- out of scope, this is cold-outreach/lead-gen work, not Brevo "
        "or any documented email-marketing-platform skill, so not logged -- plus 'Gmail account' "
        "(unchanged, out of scope). 'UK Kajabi expert' (id 8, unchanged scope) moved from the "
        "current-listings section into Past Projects since last cycle, consistent with its posting "
        "age. 'Help with Brevo' (id 46, already rejected as stale) remains unchanged in Past "
        "Projects. 8th cycle running with no genuinely new, in-scope, live candidate from this "
        "source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific searches surfaced 1 new-to-file URL this cycle: 'Upload completed "
        "emails to brevo right now -- 2' -- already CLOSED/awarded (to another freelancer, for $0 "
        "USD) before this cycle's discovery; trivial $10-30 budget for uploading 8 completed HTML "
        "emails into an existing Brevo automation, 25 competing proposals. Logged for audit-trail "
        "completeness only; REJECTED as closed and as too thin a scope to have been worth pursuing "
        "even if open. Two further search hits were stale and not independently actionable, so not "
        "logged as DB rows: 'Automated Email Offer System Setup' (a real-estate cold-email "
        "mail-merge job, closed over a year ago, Brevo mentioned only in one bidder's own comment, "
        "not the client's requirement) and 'Email Marketing Campaign Setup' / project 40554712 "
        "(closed 5 months ago, requires Mailchimp or Klaviyo -- both PROHIBITED per the claims "
        "register -- and names no Brevo requirement at all).",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "13th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered real featured-job cards, including the same "
        "'Email Marketing Specialist - Dual Campaigns for Parents & School Leaders' card already "
        "on file (id 19, $25-40/hr) -- still never a genuine NEW client email-marketing posting "
        "across 13 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query ('Brevo E-Mail Marketing Freiberufler Projekt gesucht') "
        "-- 13th consecutive cycle with no live German-market email-marketing-specialist opening "
        "surfaced; results remain Brevo's own German marketing/help-center pages, Upwork's Brevo "
        "hire-page, and freelance.de directory/profile pages, not client project postings. German-"
        "proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-12: same Oliver "
        "Tornroth/Zoined posting (now 19 days left, down from 20 in cycle 12), still the only open "
        "listing, still zero live Brevo listings. Rest of the category remains closed Klaviyo/"
        "Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend listings, same as prior cycles. "
        "Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a dedicated search ('Newsletter freelance.de Brevo Auftrag') aimed specifically at "
        "a client project/Auftrag posting. Surfaced only freelancer profile/directory pages "
        "(individuals advertising their own Brevo/Newsletter/E-Mail-Marketing skills), no client "
        "project listing at all. 7th consecutive cycle confirming no client project-posting "
        "section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle; prior cycles' finding (general tutorial/"
        "comparison content, no live candidate) assumed unchanged, consistent with cycle 12's "
        "treatment.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Brevo Expert for Creative Email Mailings",
            client_name="Individual client, San Miguel de Allende, Mexico (Upwork; member since "
                         "May 31, 2018, $1.5K total spent, 12 hires/8 active, 77 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-Expert-for-Creative-Email-Mailings_~022124226272023245807/",
            posted_at="Recent (exact post date not shown; last viewed by client 2 days before this "
                      "cycle's discovery)",
            description="Design visually appealing, creative Brevo email mailings with engaging "
                        "headings intended to capture attention and drive reader engagement. "
                        "Less than 30 hrs/week, 1-3 month, ongoing project, intermediate "
                        "experience level.",
            required_skills="Email Marketing; Email Communication; Microsoft Outlook; HTML; "
                             "creative email design/copy.",
            budget_amount=7.0, budget_currency="USD", budget_type="hourly ($7.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Long-standing individual client (member since 2018), $1.5K total "
                            "spent, 12 hires/8 active, 77 hours logged -- a real, active hirer, "
                            "but a small-budget one.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="$7.00/hr fails the project's compensation bar outright -- well below "
                              "a viable rate once Upwork's service fee and TRNC payment-routing "
                              "friction (per evidence/payment-routing.md, no rail is yet confirmed "
                              "to clear cleanly for a TRNC-registered account) are factored in. "
                              "Separately, the listing is already at an advanced stage -- "
                              "Interviewing: 4, with 4 invites already sent by the client out of "
                              "15-20 total proposals -- so even disregarding rate, competitive "
                              "timing is poor. Brevo itself is a genuine, in-scope platform match "
                              "(no claims-register conflict here), so this is a clean compensation/"
                              "competition reject, not a skill-mismatch reject.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="open",
            notes="New-to-file Upwork URL this cycle, surfaced by a Brevo-specific search. Logged "
                  "for audit-trail completeness.",
        ),
        dict(
            source_id=freelancer_id,
            title="Upload completed emails to brevo right now -- 2",
            client_name="Individual client, New York, United States (Freelancer.com; 4.9 rating, "
                         "346 reviews, payment method verified, member since Jan 1, 2008)",
            url="https://www.freelancer.com/projects/email-marketing/upload-completed-emails-brevo-right",
            posted_at="Posted about 2 months before this cycle's discovery; already completed/"
                      "awarded",
            description="Upload 8 already-completed HTML emails into the client's existing Brevo "
                        "account and wire them into one automation.",
            required_skills="Brevo platform familiarity; HTML email import/template handling; "
                             "basic automation configuration.",
            budget_amount=20, budget_currency="USD", budget_type="fixed ($10-30 USD, paid on "
                          "delivery; 25 bidders averaging $25 USD; awarded for $0 USD)",
            payment_platform="Freelancer.com (fixed-price; not independently tested for TRNC "
                              "residents)",
            client_history="Long-standing, highly-rated client (member since 2008, 4.9/346 "
                            "reviews, payment verified) with several other small jobs posted -- "
                            "credible buyer, but this specific listing was already closed.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already CLOSED and awarded (to another freelancer, for $0 USD) before "
                              "this cycle's discovery -- no longer an actionable opportunity "
                              "regardless of fit. Separately, even had it still been open, the "
                              "$10-30 budget for 8 HTML-email uploads against 25 competing bidders "
                              "is too thin a scope to pursue as a standalone engagement.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com URL this cycle, surfaced by a Brevo-specific search. "
                  "Logged for audit-trail completeness only, per the project's standard of logging "
                  "independently verified new-to-file URLs even when already closed.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-12. Per the owner's standing
    # instruction (flagged already, their call to act on), this is recorded without being
    # surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 13 (2026-11-23) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (8th consecutive "
              "cycle). Essentially flat versus cycle 12: Interviewing unchanged at 2, client "
              "totals ticked up only marginally (1,985 hours vs 1,983 -- ordinary usage noise; "
              "$68K spent/36 hires/16 active all unchanged). Last viewed by client: '3 days ago' "
              "(vs '2 days ago' in cycle 12 -- ordinary noise). No job-specific 'Hires' field and "
              "no signal the listing is gone or closed. Noted; no fresh flag raised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead -- the one
    # lead the owner asked to keep tracking closely given its prior rising-interviewing trend.
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 13 (2026-11-23) re-check: still open. Rate still $10-28/hr. Client still "
              "1 hire/1 active (no new hires). Interviewing STILL at 4 -- a 2nd consecutive cycle "
              "with no further climb beyond cycle 12's stall, and still no hire appearing. "
              "Invites-sent/unanswered unchanged at 2/0. Stated plainly, since this is the lead "
              "being tracked most closely: it has NOT moved again this cycle -- not up, no hire, "
              "not closed. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 9, len(opportunities), 0,
         "Cycle 13, the regular run following cycle 12 (2026-11-22). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (8th cycle), essentially flat vs cycle 12 -- not "
         "re-flagged per the owner's standing instruction. (b) Brevo CRM and Email Setup (id 40), "
         "the lead with the strongest prior movement, rechecked closely as instructed -- STILL "
         "stalled at Interviewing=4 for a 2nd consecutive cycle, no hire, not closed, tier not "
         "revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted again, still blocked "
         "(8th consecutive cycle); the paid scrapecreators Alexandria provider was deliberately "
         "NOT used again pending the owner's go-ahead from cycle 7. (d) PeoplePerHour page 1 "
         "re-checked only -- no genuinely new in-scope live candidate (8th cycle running; one new "
         "posting found was out-of-scope cold-email/lead-gen work, not logged). Fresh Brevo/"
         "generic searches across Upwork and Freelancer.com found 2 new URLs this cycle: a "
         "Brevo-specific Upwork listing REJECTED on compensation ($7/hr) and competition (already "
         "4 interviewing), and a Freelancer.com listing REJECTED as already closed/awarded before "
         "discovery. Contra (13th consecutive cycle with no genuine NEW client email-marketing "
         "posting), the dedicated German-market search (13th consecutive cycle with nothing "
         "live), and freelance.de (7th consecutive cycle confirming no reachable client-posting "
         "section) were checked again briefly per instruction. Direct business prospecting "
         "(master prompt section 4.3/12) was not run this cycle, per the standing scope "
         "instruction. 0 new P0/P1 opportunities this cycle; no application package "
         "recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 13 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
