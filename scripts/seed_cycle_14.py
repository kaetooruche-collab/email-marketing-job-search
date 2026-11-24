#!/usr/bin/env python3
"""Discovery cycle 14 (2026-11-24): regular run following cycle 13 (2026-11-23). Picks up cycle
13's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, hourly rate still does not render (9th consecutive cycle).
Interviewing unchanged at 2, invites 0/0. One real but ambiguous signal: the client's active-
contracts count dropped 16->15 while total spend ticked up ($68K->$69K) and hours jumped
(1,985->2,002) -- a genuine account-level change, but no job-specific "Hires" field confirms this
particular listing closed, so per the owner's standing instruction this is noted on the DB row
only, not re-flagged. (b) re-checked the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup"
listing (id 40) -- the one lead that showed real movement across cycles 9-11 (Interviewing
climbing 2->3->4) and then stalled at 4 in cycles 12-13. This cycle: still stalled at 4, now a 3RD
consecutive cycle with no further climb and no hire appearing. Rate unchanged ($10-28/hr), client
still 1 hire/1 active, invites-sent/unanswered unchanged at 2/0. Tier not revised. (c) Reddit
r/forhire: direct firecrawl_scrape attempted again against the subreddit listing page (no paid
scrapecreators Alexandria provider used without the owner's go-ahead, open since cycle 7) -- failed
identically, the 9th consecutive cycle blocked on the free method. This cycle also tried a specific
individual post URL surfaced by a generic web search ("[HIRING] Help me set up a Brevo email
campaign") -- failed with the identical "not supported" error, confirming the block is platform-
wide, not just the listing-page URL pattern. Not logged (could not be verified as live). (d)
PeoplePerHour page 1 re-check only -- no genuinely new live candidate matching scope: the same two
out-of-scope postings persist (Dubai B2B cold-email lead-gen "Cold Email Marketing Specialist", now
aged to 2 days/22 proposals; "Gmail account", unchanged) plus a new but equally out-of-scope
lead-gen posting ("Find 75 Property Owners for Free Listings", $131, UK holiday-house listing
outreach, no email-marketing-platform skill). 9th cycle running with nothing new and in-scope from
this source. Also runs fresh Brevo-specific and generic searches across Upwork and Freelancer.com
(all Upwork hits already on file from prior cycles), plus checks on Contra (14th consecutive cycle,
same id-19 card, no new lead), the German-market search angle (14th consecutive cycle -- surfaced a
genuine Brevo-specific German classified via a freiguide.de/Kleinanzeigen.de mirror, but the
original ad was already removed by the time it was checked, so not actionable and not logged), and
freelance.de (8th consecutive cycle confirming no reachable client-posting section, only freelancer
directory pages). Found 1 new-to-file URL this cycle: "Virtual Assistant: Phones & Newsletters"
(Freelancer.com, open, $8-15/hr) -- REJECTED on scope (a general admin/VA/phone-support role where
"prepare Brevo newsletters" is one incidental duty among unrelated tasks, not an email-marketing-
specialist engagement) and on compensation (well below a viable rate, 29 competing proposals mostly
from general VAs). Three further hits were read in full but not logged as DB rows, consistent with
the project's standard of only logging independently verified, live-and-actionable new-to-file URLs:
a ~2-year-old closed "Email Marketing Expert Needed: Domain Setup & Brevo Configuration" listing
(genuine Brevo requirement but too stale to carry audit-trail value), the unverifiable Reddit thread
noted above, and an already-awarded "WordPress Developer Needed Replace Zapier with Brevo API" job
that is explicitly out of scope (developer/API work, and the client's own posting explicitly
excludes candidates who have "only worked with Brevo email campaigns"). 0 new P0/P1 opportunities
this cycle. Not recommending an application package. Appends to the same DB. Safe to re-run (INSERT
OR IGNORE on url). See reports/2026-11-24-discovery-cycle-14.md for the full narrative."""
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
        "quiet status check. Still open. Rate still does not render (9th consecutive cycle). "
        "Interviewing unchanged at 2, invites 0/0. One real but ambiguous account-level signal: "
        "active contracts dropped 16->15 while total spend ($68K->$69K) and hours (1,985->2,002) "
        "both rose -- no job-specific 'Hires' field confirms this listing itself closed, so noted "
        "only per the owner's standing instruction. Also re-checked the PAYMENT_TIMELINE_UNCERTAIN "
        "'Brevo CRM and Email Setup' listing (id 40): still at Interviewing=4, now a 3rd "
        "consecutive cycle with no further climb and no hire. Rate unchanged $10-28/hr, client "
        "still 1 hire/1 active, invites-sent/unanswered unchanged at 2/0. Tier not revised. Fresh "
        "Brevo-specific and generic searches surfaced zero new-to-file Upwork URLs this cycle -- "
        "every result returned (Email Marketing Manager, Manage email campaigns, CRM and Mail "
        "Marketing Manager, Brevo Sendinblue Email Designer, B2B Cold Email & Lead Generation "
        "Specialist) was already on file from a prior cycle.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 9 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 9th consecutive cycle failing on the free method. This cycle additionally "
        "tried a specific individual post URL surfaced by a generic web search ('[HIRING] Help me "
        "set up a Brevo email campaign') to see if a single-post URL fared differently from the "
        "listing-page pattern tried in earlier cycles -- it failed with the identical error, "
        "confirming the block is platform-wide. Per instruction, did NOT fall back to the paid "
        "scrapecreators Alexandria provider this cycle -- that decision is still the owner's to "
        "make, not yet given. The post could not be independently verified as live or stale, so "
        "not logged as a DB row. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-13's finding. No genuinely new live candidate matching "
        "scope: the current-listings section held the same two out-of-scope postings as cycle 13 "
        "('Cold Email Marketing Specialist', Dubai B2B tax-consultancy lead generation, now aged to "
        "2 days/22 proposals -- out of scope, cold-outreach lead-gen, not Brevo/email-marketing-"
        "platform work; 'Gmail account', unchanged, out of scope) plus one new but equally "
        "out-of-scope posting, 'Find 75 Property Owners for Free Listings' ($131, UK holiday-house "
        "listing outreach/lead-gen, no email-marketing-platform skill involved). 9th cycle running "
        "with no genuinely new, in-scope, live candidate from this source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced 1 new-to-file URL this cycle: 'Virtual "
        "Assistant: Phones & Newsletters' -- OPEN, $8-15/hr, 29 proposals, posted 3 days before "
        "discovery; REJECTED on scope (a general front-desk/admin VA role -- phones, interview "
        "scheduling, applicant records, spreadsheets -- where 'prepare Brevo newsletters' is one "
        "incidental recurring duty, not an email-marketing-specialist engagement) and on "
        "compensation ($8-15/hr well below a viable rate once TRNC payment-routing friction and "
        "platform fees are applied). Three further hits were read but not logged as DB rows, "
        "consistent with the project's standard of logging only independently verified, live-and-"
        "actionable (or recently-closed) new-to-file URLs: 'Email Marketing Expert Needed: Domain "
        "Setup & Brevo Configuration' (project 38898157, a genuine client-stated Brevo requirement "
        "but closed almost 2 years ago -- too stale for audit-trail value), and 'WordPress "
        "Developer Needed Replace Zapier with Brevo API' (already awarded/closed, and genuinely "
        "out of scope regardless -- backend developer/API work, with the client's own posting "
        "explicitly excluding candidates who have 'only worked with Brevo email campaigns').",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "14th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered real featured-job cards, including the same "
        "'Email Marketing Specialist - Dual Campaigns for Parents & School Leaders' card already "
        "on file (id 19, $25-40/hr) -- still never a genuine NEW client email-marketing posting "
        "across 14 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 14th consecutive cycle with no live, actionable "
        "German-market email-marketing-specialist opening. This cycle surfaced, for the first "
        "time, a genuine Brevo-specific German request: 'BREVO Newsletter einrichten', a private "
        "individual's classified ad, mirrored on a third-party aggregator (freiguide.de) from the "
        "original Kleinanzeigen.de posting. Checking the original Kleinanzeigen.de URL directly "
        "showed the ad has already been removed ('Die gewuenschte Anzeige ist nicht mehr "
        "verfuegbar') with no budget or client-credibility information ever available, so it was "
        "not independently actionable and was not logged. German-proficiency claims-register "
        "conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-13: same Oliver "
        "Tornroth/Zoined posting (now 18 days left, down from 19 in cycle 13), still the only open "
        "listing, still zero live Brevo listings. Rest of the category remains closed Klaviyo/"
        "Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend listings, same as prior cycles. "
        "Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a dedicated search ('freelance.de Newsletter Brevo Auftrag gesucht Projekt') aimed "
        "specifically at a client project/Auftrag posting. Surfaced only freelancer profile/"
        "directory pages (individuals advertising their own Brevo/Newsletter skills), no client "
        "project listing at all. 8th consecutive cycle confirming no client project-posting "
        "section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle; prior cycles' finding (general tutorial/"
        "comparison content, no live candidate) assumed unchanged, consistent with cycle 13's "
        "treatment.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=freelancer_id,
            title="Virtual Assistant: Phones & Newsletters",
            client_name="Individual/small business client, Matawan, United States "
                         "(Freelancer.com; 0.0 rating, 0 reviews, member since Nov 21, 2026 -- "
                         "brand-new account at discovery)",
            url="https://www.freelancer.com/projects/administrative-support/virtual-assistant-phones-newsletters",
            posted_at="Posted 3 days before this cycle's discovery; ends in 6 days from discovery",
            description="General front-line communication and admin role: answer incoming calls, "
                        "respond to general business/office questions by email or chat, schedule "
                        "interviews, keep applicant records current, prepare Brevo newsletters, "
                        "update spreadsheets, and handle back-office work inside the client's "
                        "'Apps Base 44' environment.",
            required_skills="Phone/customer communication, email/chat response, interview "
                             "scheduling, applicant record-keeping, Excel/Google Sheets, basic "
                             "Brevo newsletter preparation (one of several unrelated admin "
                             "duties, not the core scope).",
            budget_amount=11.5, budget_currency="USD", budget_type="hourly ($8.00-$15.00/hr)",
            payment_platform="Freelancer.com (hourly; not independently tested for TRNC "
                              "residents)",
            client_history="Brand-new client account (member since Nov 21, 2026, 3 days old at "
                            "discovery), 0.0 rating, 0 reviews -- no track record to assess trust "
                            "or payment follow-through against.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Scope mismatch: this is a general front-desk/admin virtual-assistant "
                              "role -- answering phones, scheduling interviews, maintaining "
                              "applicant records -- where 'prepare Brevo newsletters' is one "
                              "incidental recurring duty bolted onto unrelated admin work, not an "
                              "email-marketing-specialist engagement. The documented Brevo skill "
                              "set (deliverability, segmentation, lifecycle automation, campaign "
                              "performance) is not what this role is asking for. Separately, "
                              "$8.00-$15.00/hr is well below a viable rate once TRNC "
                              "payment-routing friction (per evidence/payment-routing.md) and "
                              "platform fees are factored in, and 29 competing proposals (mostly "
                              "experienced general VAs bidding $8-12/hr) confirm this is being "
                              "priced and bid as a commodity admin role. Clean scope-mismatch and "
                              "compensation reject, not a close call.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="open",
            notes="New-to-file Freelancer.com URL this cycle, surfaced by a Brevo-specific search. "
                  "Logged for audit-trail completeness; a genuine Brevo mention but not in-scope "
                  "email-marketing work.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-13. Per the owner's standing
    # instruction (flagged already, their call to act on), this is recorded without being
    # surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 14 (2026-11-24) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (9th consecutive "
              "cycle). Interviewing unchanged at 2, invites 0/0. One real but ambiguous "
              "account-level signal: active contracts dropped 16->15 while total spend "
              "($68K->$69K) and hours (1,985->2,002) both rose -- no job-specific 'Hires' field "
              "confirms this listing itself closed, so this is noted only, not treated as a "
              "closure signal. Last viewed by client: '4 days ago' (vs '3 days ago' in cycle "
              "13). Noted; no fresh flag raised."
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
            + " | Cycle 14 (2026-11-24) re-check: still open. Rate still $10-28/hr. Client still "
              "1 hire/1 active (no new hires). Interviewing STILL at 4 -- now a 3RD consecutive "
              "cycle with no further climb beyond cycle 12's stall, and still no hire appearing. "
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
         "Cycle 14, the regular run following cycle 13 (2026-11-23). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (9th cycle); one real but ambiguous account-level "
         "signal (active contracts 16->15) with no job-specific closure signal, so noted only, "
         "not re-flagged, per the owner's standing instruction. (b) Brevo CRM and Email Setup "
         "(id 40), the lead with the strongest prior movement, rechecked closely as instructed -- "
         "STILL stalled at Interviewing=4 for a 3RD consecutive cycle, no hire, not closed, tier "
         "not revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted again against both "
         "the subreddit listing page and a specific individual post URL -- both blocked "
         "identically (9th consecutive cycle); the paid scrapecreators Alexandria provider was "
         "deliberately NOT used again pending the owner's go-ahead from cycle 7. (d) PeoplePerHour "
         "page 1 re-checked only -- no genuinely new in-scope live candidate (9th cycle running). "
         "Fresh Brevo/generic searches across Upwork and Freelancer.com found 1 new-to-file URL "
         "this cycle, a Freelancer.com general-VA listing REJECTED on scope mismatch and "
         "compensation (Brevo newsletter prep was one incidental duty, not the role's core scope). "
         "Three further hits (a ~2-year-stale closed Brevo domain-setup job, an unverifiable "
         "Reddit thread, and an already-awarded WordPress/Zapier-replacement dev job explicitly "
         "excluding Brevo-email-campaign-only candidates) were read but not logged, consistent "
         "with the project's audit-trail standard. Contra (14th consecutive cycle with no genuine "
         "NEW client email-marketing posting), the dedicated German-market search (14th "
         "consecutive cycle -- a genuine but already-dead Brevo-specific German classified "
         "surfaced via a freiguide.de/Kleinanzeigen.de mirror), and freelance.de (8th consecutive "
         "cycle confirming no reachable client-posting section) were checked again briefly per "
         "instruction. Direct business prospecting (master prompt section 4.3/12) was not run "
         "this cycle, per the standing scope instruction. 0 new P0/P1 opportunities this cycle; "
         "no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 14 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
