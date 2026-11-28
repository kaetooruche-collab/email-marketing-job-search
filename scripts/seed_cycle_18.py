#!/usr/bin/env python3
"""Discovery cycle 18 (2026-11-28): regular run following cycle 17 (2026-11-27). Picks up cycle
17's open items. (OWNER'S PENDING DECISION, IMPORTANT) 'Email Deliverability Specialist for 3
Companies' (id 72) rechecked per the task's explicit instruction -- NO application package was
prepared, that decision remains the owner's. Still open: Interviewing still 0, 1 invite sent still
unanswered, no job-specific Hires field has ever appeared, client account unchanged ($2.5K/9
hires/5 active), hours ticked 75->76 (routine). Last viewed by client 'last week' (same recency as
cycle 17's '6 days ago', just a coarser bucket). Nothing makes the owner's pending decision moot --
the listing is exactly as open and exactly as under-the-radar as when flagged. (a) Newsletter
Specialist for Campaigns / Brevo (id 31) rechecked once more -- still open, hourly rate STILL does
not render (13TH consecutive cycle), no job-specific Hires field has ever appeared. Interviewing
unchanged at 2, invites 0/0. Last viewed '4 days ago' (vs '3 days ago' last cycle -- ordinary
noise). Client totals: $69K spent (flat), 36 hires (flat), 15 active (flat), hours rose again
2,030->2,039 (routine). Noted on the DB row only, not re-flagged, per the owner's standing
instruction. (b) Brevo CRM and Email Setup (id 40) rechecked with the job's own Activity panel
checked directly: no job-specific Hires line appears. Interviewing STILL at 4 -- now a 7TH
consecutive cycle (12-18) with no further climb. Invites-sent/unanswered unchanged at 2/0. ONE
REAL CHANGE: the 'About the client' account-level figures moved from '$15 spent/1 hire/0 active'
(stable cycles 15-17) to '$15 spent/2 hires/1 active' -- the first account-level movement in three
cycles. Read plainly, not over-read: total spend still flat at $15, and since Interviewing on THIS
job stayed flat at 4 with no job-specific Hires field appearing, the new hire most plausibly
belongs to a different job this same buyer posted, not this one. Tier not revised. (c) Reddit
r/forhire: direct firecrawl_scrape attempted again (no paid scrapecreators Alexandria provider
used without the owner's go-ahead, open since cycle 7) -- failed identically, the 13TH consecutive
cycle blocked on the free method. (d) PeoplePerHour page 1 re-check only -- no genuinely new
in-scope listing this cycle: the 'Markerters wanted...' posting logged in cycle 16 (id 71) is still
the same listing, now 13 days old/26 proposals (flat vs cycle 17's 12 days/26); the recurring
out-of-scope items persist in substance (Dubai B2B cold-email lead-gen now 6 days/24 proposals, up
from 5 days/24; the Instantly.ai/Meta-Ads outreach-manager role now 4 days/34 proposals, up from 3
days/33; the VO-artist B2B lead-gen listing now 2 days/32 proposals, up from 2 days/31) -- all read
but not logged. (e) Contra (18TH consecutive cycle, same id-19 card plus the same two recurring
non-Brevo listings, no new genuine lead), the German-market search (18th consecutive cycle -- this
time the usual freiguide.de/Kleinanzeigen.de dead-mirror did NOT recur; instead a direct
Kleinanzeigen.de listing surfaced, 'Biete: E-Mail-Marketing einrichten - Newsletter endlich
starten' (Duesseldorf, EUR850) -- on inspection this is a FREELANCER'S OWN service-offer ad (Nina
Mamsch offering Brevo/ActiveCampaign setup), not a client job posting at all, and it is itself
shown as 'Geloescht'/'Reserviert' (deleted/reserved) on the page -- still zero actionable German-
market opportunities, just a different non-result this time), and freelance.de (12th consecutive
cycle confirming no reachable client-posting section, only portfolio/privacy-policy mentions of
Brevo) were all checked again, kept brief as instructed. Fresh Brevo-specific and generic searches
across Upwork, Freelancer.com, and Guru.com found 3 new-to-file candidates this cycle, all on
Upwork: 'Email Marketing Specialist for Black Friday' (REJECTED -- stale last-viewed-by-client
'4 weeks ago' despite an active Interviewing:4/5-invites-sent funnel, read as likely already
quietly filled per this project's established methodology) and 'Email marketing Developer'
(REJECTED -- explicit 'Hires: 1' field renders, confirming this job IS filled, plus it separately
requires PROHIBITED tools Klaviyo/Omnisend) are logged below; 'Marketing Email Outreach
Infrastructure' (cold-email domain-warming/authentication setup, not email-marketing-platform
work, further disqualified by 50+ proposals/2-weeks-stale/Expert-level-required) was read but not
logged as a scope mismatch. Freelancer.com's fresh searches surfaced only already-on-file listings
(ids 34, 27, 57), no new URL. Guru.com surfaced only the already-on-file listing (id 70). 0 new P0,
0 new P1 this cycle; the owner's pending-decision candidate from cycle 17 remains unactioned per
instruction. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-28-discovery-cycle-18.md for the full narrative."""
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
        "Re-scraped the owner's pending-decision listing ('Email Deliverability Specialist for 3 "
        "Companies', id 72) -- still open, Interviewing still 0, no Hires field, nothing makes the "
        "owner's cycle-17 decision moot. Also re-scraped the Newsletter Specialist listing (id 31, "
        "13th consecutive cycle rate-does-not-render) and the Brevo CRM and Email Setup listing "
        "(id 40, 7th consecutive cycle at Interviewing=4, but first account-level hire/active "
        "movement in 3 cycles). Fresh Brevo-specific and generic searches surfaced 3 new-to-file "
        "Upwork URLs this cycle: 'Email Marketing Specialist for Black Friday' (REJECTED -- stale "
        "last-viewed 4 weeks ago despite active interview funnel, read as likely quietly filled); "
        "'Email marketing Developer' (REJECTED -- explicit Hires:1 field renders, confirmed "
        "filled, plus PROHIBITED tools Klaviyo/Omnisend required); 'Marketing Email Outreach "
        "Infrastructure' (read but not logged -- cold-email domain-warming infra work, not "
        "email-marketing-platform work, further disqualified by 50+ proposals/2-weeks-stale).",
        discovery_count=2, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 13 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 13th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- still awaiting "
        "the owner's go-ahead from cycle 7. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-17's finding. No genuinely new in-scope listing this "
        "cycle: the 'Markerters wanted for sale of products email campaigns' posting logged in "
        "cycle 16 (id 71) is still the same listing, now 13 days old/26 proposals, flat vs cycle "
        "17's 12 days/26. Recurring out-of-scope postings persist in substance: 'Cold Email "
        "Marketing Specialist' (Dubai) now 6 days/24 proposals (up from 5 days/24); 'I need an "
        "outreach marketing professional' (Instantly.ai/Meta Ads, PROHIBITED) now 4 days/34 "
        "proposals (up from 3 days/33); 'B2B Lead Generation & Email Outreach for Established VO "
        "Artist' now 2 days/32 proposals (up from 2 days/31) -- all read but not logged, no Brevo "
        "or email-marketing-platform skill involved.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced no new-to-file Freelancer.com projects "
        "this cycle -- all hits matched listings already on file under their existing slugs (ids "
        "34, 27, 57).",
        discovery_count=0, qualified_count=0,
    )
    guru_id = get_or_create_source(
        conn, "Guru.com", "https://www.guru.com/jobs/brevo-crm-automation-b2b-cold-email/2121953",
        "firecrawl_search + firecrawl_scrape of individual job listing pages, no login",
        "Fresh Brevo-specific search surfaced only the same listing already on file (id 70, "
        "unchanged tier). Kept on the source list for future cycles.",
        discovery_count=0, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "18th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered the same 'Email Marketing Specialist - Dual "
        "Campaigns for Parents & School Leaders' card already on file (id 19, $25-40/hr), plus the "
        "same two recurring non-Brevo, non-email-platform listings ('Marketing Assistant for "
        "Launch Campaign', 'Prepping Digital Assets Before Launching Campaigns') -- still never a "
        "genuine NEW client email-marketing posting across 18 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 18th consecutive cycle with no live, actionable "
        "German-market email-marketing-specialist opening. This cycle the usual freiguide.de-"
        "mirrored Kleinanzeigen.de dead-mirror did NOT recur; instead a direct Kleinanzeigen.de "
        "listing surfaced, 'Biete: E-Mail-Marketing einrichten - Newsletter endlich starten' "
        "(Duesseldorf, EUR850) -- on inspection this is a FREELANCER'S OWN service-offer ad (Nina "
        "Mamsch offering Brevo/ActiveCampaign setup with SPF/DKIM/DMARC and double opt-in), not a "
        "client job posting, and it is itself shown as 'Geloescht'/'Reserviert' (deleted/reserved) "
        "on the page. Net result unchanged: zero actionable German-market opportunities, now an "
        "18th consecutive cycle, just a different non-result than the usual dead mirror this time. "
        "German-proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Not re-run this cycle; cycle 16's finding (every listing on the English page 1 shows "
        "status 'Finished', long-running Oliver Tornroth/Zoined posting gone) assumed unchanged, "
        "consistent with the project's treatment of lower-priority sources between active-change "
        "cycles. No live Brevo listing assumed.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried the same dedicated search again, aimed specifically at a client project/Auftrag "
        "posting. Surfaced only freelancer-portfolio and privacy-policy pages mentioning Brevo in "
        "passing -- no client project listing at all. 12th consecutive cycle confirming no client "
        "project-posting section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle, consistent with cycles 13-17's treatment; "
        "prior cycles' finding (general tutorial/comparison content, no live candidate) assumed "
        "unchanged.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist for Black Friday",
            client_name="Qatar-based client, member since Apr 6, 2026; no total-spent/hires/"
                         "active figures shown on the public page (no visible track record)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist-for-Black-Friday_~022115451632556166784/",
            posted_at="Duration '1-3 months'; last viewed by client 4 weeks before this cycle's "
                      "discovery; exact posting date not shown",
            description="Support a Black Friday email campaign: improve list segmentation, warm "
                        "up inactive contacts, and create sales emails to drive conversions. "
                        "Recommend a campaign structure and help increase engagement/sales during "
                        "the holiday season. Experience with Black Friday campaigns important.",
            required_skills="Email Marketing -- generic list segmentation/re-engagement/holiday "
                             "sales-email work, no PROHIBITED-tool conflict on skills alone.",
            budget_amount=18.5, budget_currency="USD", budget_type="hourly ($12.00-$25.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents, per "
                              "evidence/payment-routing.md)",
            client_history="No total-spent/hires/active figures render on the public page at "
                            "all -- an essentially blank track record on this metric, separate "
                            "from the staleness issue that actually drives the rejection.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Skill match is acceptable on its face, but the hiring-funnel "
                              "signals point to a job that has most likely already been filled "
                              "through the invite/interview channel: Interviewing is at 4 and 5 "
                              "invites have been sent with 0 unanswered (every invite has been "
                              "engaged), yet the client last viewed applicants FOUR WEEKS ago. "
                              "Per this project's established methodology (checking closure "
                              "signals beyond raw proposal counts), an active interview funnel "
                              "paired with a month-stale last-viewed date reads as quietly filled "
                              "with the public page not yet reflecting it. Applying now would "
                              "likely mean competing for a slot that no longer exists. Discounted "
                              "honestly rather than rounded up to a candidate.",
            est_days_to_accessible_payment=None,
            score_probability_win=3, score_time_to_payment=11, score_skill_match=10,
            score_payment_certainty=6, score_compensation=7, score_client_credibility=4,
            score_repeat_potential=3, score_total=44,
            score_rationale="Decent nominal skill fit and rate, but the staleness-vs-active-"
                            "funnel combination (Interviewing:4/Invites:5 answered, yet last "
                            "viewed 4 weeks ago) is treated as a likely-already-filled signal, "
                            "not a live opportunity. No client track record shown to offset the "
                            "doubt. Rejected rather than discounted into a marginal candidate.",
            status="open",
            notes="New-to-file Upwork URL this cycle, surfaced by a fresh generic Upwork search. "
                  "Logged for audit-trail completeness as a clear example of the "
                  "stale-last-viewed-despite-active-funnel rejection pattern.",
        ),
        dict(
            source_id=upwork_id,
            title="Email marketing Developer",
            client_name="Established Melbourne, Australia retail-technology agency (small "
                         "company, 2-9 people; Upwork member since Dec 10, 2023; $67K total "
                         "spent, 86 hires, 19 active, 2,625 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-marketing-Developer_~022121353793000016945/",
            posted_at="Duration '3-6 months'; last viewed by client last week",
            description="Convert Figma email designs into responsive HTML emails; build and "
                        "configure email automations/campaigns; set up email and SMS "
                        "integrations; configure segmentation/triggers; integrate with "
                        "WooCommerce and Shopify; troubleshoot deliverability.",
            required_skills="Strong HTML/CSS email development, FunnelKit, Omnisend, and Klaviyo "
                             "experience, WordPress/WooCommerce, SMTP/DNS configuration -- "
                             "Omnisend and Klaviyo are both PROHIBITED per the claims register "
                             "(not evidenced in any of the 3 source documents).",
            budget_amount=12.5, budget_currency="USD", budget_type="hourly ($5.00-$20.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Genuinely established and credible: member since Dec 2023, $67K "
                            "total spent, 86 hires, 19 active contracts, 2,625 hours logged -- a "
                            "real, busy agency, no trust concern on the client side.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Double disqualifier, stated plainly. (1) The listing's own Activity "
                              "panel shows an explicit 'Hires: 1' field rendering -- the job is "
                              "already filled, confirmed directly rather than inferred from "
                              "proposal/interviewing counts. (2) Independently, and even had it "
                              "still been open, the role requires Klaviyo and Omnisend "
                              "experience, both PROHIBITED per the claims register -- this "
                              "project's documented platform depth is Brevo, not either of "
                              "those. Rejected on both grounds.",
            est_days_to_accessible_payment=None,
            score_probability_win=1, score_time_to_payment=8, score_skill_match=3,
            score_payment_certainty=5, score_compensation=4, score_client_credibility=7,
            score_repeat_potential=2, score_total=30,
            score_rationale="Already hired (explicit Hires:1 field, the first such field this "
                            "project has seen actually render with a non-zero value) plus a hard "
                            "PROHIBITED-tool requirement (Klaviyo, Omnisend). A clean, "
                            "unambiguous reject on two independent grounds; the credible client "
                            "account does not offset either disqualifier.",
            status="closed",
            notes="New-to-file Upwork URL this cycle, surfaced by a fresh generic Upwork search. "
                  "Logged for audit-trail completeness: useful direct confirmation that Upwork's "
                  "job-specific 'Hires' field does render when a hire has genuinely happened, "
                  "strengthening confidence in the absence-of-the-field reasoning already applied "
                  "to ids 31, 40, and 72 across many cycles.",
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

    # Owner's pending-decision listing from cycle 17 -- rechecked, NOT actioned, per instruction.
    deliverability_url = "https://www.upwork.com/freelance-jobs/apply/Email-Deliverability-Specialist-for-Companies_~022118751105880279253/"
    existing_note_row0 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (deliverability_url,)
    ).fetchone()
    if existing_note_row0:
        appended_note0 = (
            (existing_note_row0[0] or "")
            + " | Cycle 18 (2026-11-28) re-check per the task's explicit instruction: NO "
              "application package, draft, or proposal prepared -- that decision remains the "
              "owner's, not actioned. Still open. Interviewing still 0 (unchanged). Invites "
              "sent/unanswered still 1/0 (unchanged). No job-specific Hires field has ever "
              "appeared. Last viewed by client 'last week' (same recency as cycle 17's '6 days "
              "ago', a coarser bucket, not a fresh signal). Client account unchanged: $2.5K "
              "spent, 9 hires, 5 active; hours rose 75->76 (routine). Nothing about this cycle's "
              "check makes the owner's pending decision moot -- the listing is exactly as open "
              "and exactly as under-the-radar as when flagged in cycle 17."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note0, NOW, deliverability_url),
        )

    # Quiet re-check note on the still-open lead from cycles 5-17. Per the owner's standing
    # instruction, recorded without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 18 (2026-11-28) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (13th consecutive "
              "cycle); no job-specific Hires field has ever appeared on this listing's Activity "
              "panel across any cycle. Interviewing unchanged at 2, invites 0/0. Last viewed by "
              "client '4 days ago' (vs '3 days ago' in cycle 17 -- ordinary noise). Active "
              "contracts held at 15, total spent flat at $69K, 36 hires on file, hours rose again "
              "2,030->2,039 -- ordinary continued activity on this buyer's other contracts. Not "
              "gone, not closed, nothing new to flag."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead -- the one
    # lead the owner asked to keep tracking closely. First account-level movement in 3 cycles.
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 18 (2026-11-28) re-check, with the listing's own Activity-on-this-job "
              "panel checked directly: no job-specific Hires field appears (only Proposals/Last "
              "viewed/Interviewing/Invites render). Still open. Rate still $10-28/hr. Interviewing "
              "STILL at 4 -- now a 7TH consecutive cycle (12-18) with no further climb. "
              "Invites-sent/unanswered unchanged at 2/0. ONE REAL CHANGE: the 'About the client' "
              "account-level figures moved from '$15 spent/1 hire/0 active' (stable cycles 15-17) "
              "to '$15 spent/2 hires/1 active' -- the first account-level movement in three "
              "cycles. Read plainly, not over-read: total spend is still flat at $15, and since "
              "Interviewing on THIS job stayed flat at 4 with no job-specific Hires field "
              "appearing, the new hire most plausibly belongs to a different job this same buyer "
              "posted, not this one. Noted; not treated as closure or advancement on this "
              "specific listing. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 10, len(opportunities), 0,
         "Cycle 18, the regular run following cycle 17 (2026-11-27). Followed up on all open "
         "items: owner's pending-decision listing ('Email Deliverability Specialist for 3 "
         "Companies', id 72) rechecked per explicit instruction -- NOT actioned, still open, "
         "still unfilled, nothing makes the decision moot. (a) Newsletter Specialist for "
         "Campaigns / Brevo (id 31) rechecked once quietly -- still open, rate still unconfirmed "
         "(13th cycle), no Hires field has ever appeared, nothing new, noted only. (b) Brevo CRM "
         "and Email Setup (id 40) rechecked with the job's own Activity panel checked directly -- "
         "none appears; STILL stalled at Interviewing=4 for a 7TH consecutive cycle, but the "
         "buyer account showed its first movement in three cycles (1->2 hires, 0->1 active), read "
         "as most likely unrelated to this specific job; tier not revised. (c) Reddit r/forhire: "
         "direct firecrawl_scrape attempted again -- blocked identically (13th consecutive "
         "cycle); the paid scrapecreators Alexandria provider was deliberately NOT used again "
         "pending the owner's go-ahead from cycle 7. (d) PeoplePerHour page 1 re-checked only -- "
         "no genuinely new in-scope listing this cycle; the 'Markerters wanted...' posting logged "
         "in cycle 16 is unchanged in substance; recurring out-of-scope postings persist. (e) "
         "Contra (18th consecutive cycle, no new genuine lead), the German-market search (18th "
         "consecutive cycle -- the usual dead-mirror pattern did not recur; a different "
         "non-actionable result turned up instead, a freelancer's own deleted/reserved service "
         "ad), and freelance.de (12th consecutive cycle confirming no reachable client-posting "
         "section) were checked again briefly per instruction. Useme.com not re-run this cycle, "
         "prior finding assumed unchanged. Fresh Brevo/generic searches across Upwork, "
         "Freelancer.com, and Guru.com found 3 new-to-file candidates this cycle, all on Upwork: "
         "'Email Marketing Specialist for Black Friday' -- REJECTED, stale last-viewed (4 weeks) "
         "despite an active interview funnel, read as likely already quietly filled; 'Email "
         "marketing Developer' -- REJECTED, explicit Hires:1 field confirms already filled, plus "
         "PROHIBITED tools (Klaviyo, Omnisend) required; 'Marketing Email Outreach "
         "Infrastructure' -- read but not logged, cold-email domain-warming infra work rather "
         "than email-marketing-platform work, further disqualified by high competition and "
         "staleness. Freelancer.com's searches surfaced only already-on-file listings, not "
         "logged. Guru.com surfaced only the already-on-file listing, not logged. Direct "
         "business prospecting (master prompt section 4.3/12) was not run this cycle, per the "
         "standing scope instruction. 0 new P0, 0 new P1 this cycle; the owner's pending-decision "
         "candidate from cycle 17 remains unactioned per instruction."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 18 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
