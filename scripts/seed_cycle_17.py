#!/usr/bin/env python3
"""Discovery cycle 17 (2026-11-27): regular run following cycle 16 (2026-11-26). Picks up cycle
16's open items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once more --
still open, hourly rate STILL does not render (12TH consecutive cycle), no job-specific 'Hires'
field appears on this listing at all (none has ever rendered for it across cycles). Interviewing
unchanged at 2, invites 0/0. Last viewed by client '3 days ago' (vs '2 days ago' last cycle --
ordinary noise). Client totals: $69K spent (flat), 36 hires (flat), 15 active (flat), hours ticked
up 2,026->2,030 (routine). No clear Hires/closure signal and not gone -- noted on the DB row only,
not re-flagged, per the owner's standing instruction. (b) Brevo CRM and Email Setup (id 40)
rechecked with the cycle-16 methodology fix applied explicitly: the job's own Activity-on-this-job
panel was checked directly and shows NO job-specific 'Hires' line at all (only Proposals/Last
viewed/Interviewing/Invites) -- so, as in all prior cycles, there is no direct hire signal on this
specific listing. Still open. Rate still $10-28/hr. Interviewing STILL at 4 -- now a 6TH
consecutive cycle (12,13,14,15,16,17) with no further climb and no hire signal. Invites-sent/
unanswered unchanged at 2/0. The 'About the client' account-level figures ($15 total spent, 1
hire, 0 active) are unchanged from cycle 16 -- a third consecutive cycle of total stability.
Tier not revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted again (no paid
scrapecreators Alexandria provider used without the owner's go-ahead, open since cycle 7) --
failed identically, the 12TH consecutive cycle blocked on the free method. (d) PeoplePerHour page
1 re-check only -- no genuinely new in-scope listing this cycle: the 'Markerters wanted...' posting
logged last cycle (id 71) is still the same listing, now 12 days old/26 proposals (unchanged); the
recurring out-of-scope items persist in substance (Dubai B2B cold-email lead-gen now 5 days/24
proposals, up from 4 days/24; the outreach-manager role requiring Instantly.ai/Meta Ads now 3
days/33 proposals; the VO-artist B2B lead-gen listing now showing 16 hours/31 proposals in this
relevance-sorted pull, essentially flat) -- all read but not logged, consistent with the project's
scope standard. (e) Contra (17TH consecutive cycle, same id-19 card plus the same two recurring
non-Brevo listings, no new genuine lead), the German-market search (17th consecutive cycle -- the
freiguide.de-mirrored Kleinanzeigen.de 'BREVO Newsletter einrichten' ad was checked again: still
already removed on Kleinanzeigen.de directly ('Die gewuenschte Anzeige ist nicht mehr verfuegbar'),
now the FOURTH consecutive cycle (14,15,16,17) this exact dead-mirror pattern has occurred -- per
the owner's instruction this stays CONFIRMED STRUCTURAL and is not re-described), and freelance.de
(11th consecutive cycle confirming no reachable client-posting section, only directory/hire pages)
were all checked again, kept brief as instructed. Fresh Brevo-specific and generic searches across
Upwork, Freelancer.com, and Guru.com surfaced 2 new-to-file candidates this cycle, both on Upwork:
'Email Deliverability Specialist for 3 Companies' (REJECTED-tier escalated to P1 -- see below, a
genuinely clean match with low current competition) and 'B2B Content Creator - LinkedIn & Email
Marketing (Long-Term Freelance)' (REJECTED -- skill mismatch, the role is primarily LinkedIn
content/Canva graphic design work with only a minor Brevo-or-similar email component, and pay is
low for the described ongoing scope). Freelancer.com's fresh searches surfaced only already-on-file
listings (several as country-subdomain mirrors of URLs already in the DB -- vn./fr./br. variants of
the same slugs) plus one closed, extremely-low-pay ($2-8/hr) repost from the same client behind the
already-logged id-36 listing -- pure noise, not logged. Guru.com's fresh search surfaced only the
same listing already on file (id 70) plus one unrelated teaching/cold-email role out of scope, not
logged. 1 new P1 opportunity this cycle (flagged to the owner per the task's own instruction, not
yet actioned); 0 new P0. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-27-discovery-cycle-17.md for the full narrative."""
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
        "Re-scraped the Newsletter Specialist for Campaigns / Brevo listing (id 31) once more. "
        "Still open. Rate still does not render (12th consecutive cycle); no job-specific Hires "
        "field has ever appeared on this listing. Interviewing unchanged at 2, invites 0/0. Client "
        "totals flat ($69K/36 hires/15 active), hours rose 2,026->2,030. Also re-checked the "
        "PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email Setup' listing (id 40) with the cycle-16 "
        "methodology fix applied explicitly: the job's own Activity panel shows no job-specific "
        "Hires line at all. Still at Interviewing=4, now a 6TH consecutive cycle with no further "
        "climb; account-level client figures ($15 spent/1 hire/0 active) unchanged for a third "
        "consecutive cycle. Tier not revised on either. Fresh Brevo-specific and generic searches "
        "surfaced 2 new-to-file Upwork URLs this cycle: 'Email Deliverability Specialist for 3 "
        "Companies' ($10-28/hr, small-but-real client, 0 Interviewing/1 unanswered invite despite "
        "20-50 proposals, no Hires field) -- escalated to P1 and flagged to the owner as this "
        "cycle's one clean, currently-open, well-matched candidate; and 'B2B Content Creator - "
        "LinkedIn & Email Marketing' (ShelfPerfect, Singapore) -- REJECTED, the role is primarily "
        "LinkedIn content/Canva graphic design work with only a minor Brevo-or-similar component, "
        "skill mismatch plus low pay ($180-250/month) for the described ongoing scope.",
        discovery_count=2, qualified_count=1,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 12 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 12th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- still awaiting "
        "the owner's go-ahead from cycle 7. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-16's finding. No genuinely new in-scope listing this "
        "cycle: the 'Markerters wanted for sale of products email campaigns' posting logged last "
        "cycle (id 71) is still the same listing, now 12 days old/26 proposals, unchanged. "
        "Recurring out-of-scope postings persist in substance: 'Cold Email Marketing Specialist' "
        "(Dubai) now 5 days/24 proposals (up from 4 days/24); 'I need an outreach marketing "
        "professional' (Instantly.ai/Meta Ads, PROHIBITED) now 3 days/33 proposals; "
        "'B2B Lead Generation & Email Outreach for Established VO Artist' now showing 16 hours/31 "
        "proposals in this pull (essentially flat vs cycle 16's 2 days/30) -- all read but not "
        "logged, no Brevo or email-marketing-platform skill involved.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced no new-to-file LIVE Freelancer.com "
        "projects this cycle -- several hits were country-subdomain mirrors (vn., fr., br.) of "
        "URLs already on file under the plain www. domain (same slugs, same projects), plus two "
        "freelancer user-portfolio pages (not job listings), plus one CLOSED, extremely-low-pay "
        "($2-8/hr) repost from the same client behind the already-logged id-36 'Brevo and Hubspot "
        "Client Engagement Assistant' listing ('...-40583685', posted 4 months ago, Closed) -- pure "
        "search noise, not logged.",
        discovery_count=0, qualified_count=0,
    )
    guru_id = get_or_create_source(
        conn, "Guru.com", "https://www.guru.com/jobs/brevo-crm-automation-b2b-cold-email/2121953",
        "firecrawl_search + firecrawl_scrape of individual job listing pages, no login",
        "Fresh Brevo-specific search surfaced only the same listing already on file (id 70, "
        "unchanged tier) plus one unrelated 'Teach B2B Sales & Cold Email' listing (a teaching "
        "role, not email-platform specialist work) -- out of scope, not logged. Kept on the source "
        "list for future cycles.",
        discovery_count=0, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "17th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered the same 'Email Marketing Specialist - Dual "
        "Campaigns for Parents & School Leaders' card already on file (id 19, $25-40/hr), plus the "
        "same two recurring non-Brevo, non-email-platform listings ('Marketing Assistant for "
        "Launch Campaign', 'Prepping Digital Assets Before Launching Campaigns') -- still never a "
        "genuine NEW client email-marketing posting across 17 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 17th consecutive cycle with no live, actionable "
        "German-market email-marketing-specialist opening. The same freiguide.de-mirrored "
        "Kleinanzeigen.de classified titled 'BREVO Newsletter einrichten' surfaced again; checking "
        "the original Kleinanzeigen.de URL directly again returned 'Die gewuenschte Anzeige ist "
        "nicht mehr verfuegbar' (ad no longer available), with the category listing page showing "
        "only unrelated Dresden-area service ads. This is now the FOURTH consecutive cycle (14, 15, "
        "16, 17) this exact dead-mirror pattern has occurred -- per the owner's instruction this "
        "remains CONFIRMED STRUCTURAL and is not re-described as a fresh finding. German-"
        "proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Not re-run this cycle; cycle 16's finding (every listing on the English page 1 now shows "
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
        "posting. Surfaced only the same freelancer-directory page (Brevo-Freelancer finden) plus "
        "Fiverr/Upwork hire-page noise -- no client project listing at all. 11th consecutive cycle "
        "confirming no client project-posting section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle, consistent with cycles 13-16's treatment; "
        "prior cycles' finding (general tutorial/comparison content, no live candidate) assumed "
        "unchanged.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Deliverability Specialist for 3 Companies",
            client_name="Small company (2-9 people), Sales & Marketing industry, Park Ridge, "
                         "United States (Upwork; member since Jun 22, 2020, $2.5K total spent, 9 "
                         "hires, 5 active, 75 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Deliverability-Specialist-for-Companies_~022118751105880279253/",
            posted_at="Duration '1-3 months', ongoing project; last viewed by client 6 days before "
                      "this cycle's discovery; exact posting date not shown",
            description="Improve email deliverability and domain reputation for three companies: "
                        "review current email practices, identify issues, implement fixes to "
                        "increase inbox placement and reduce spam complaints, assess each "
                        "company's setup, recommend improvements, and help maintain strong email "
                        "performance over time. Requires experience handling multiple accounts.",
            required_skills="Email Marketing, Email Deliverability, Email Support, Email "
                             "Communication -- generic deliverability/domain-reputation audit "
                             "work across multiple accounts, the project's single strongest "
                             "documented skill area. No specific platform (Brevo or otherwise) "
                             "named, so no PROHIBITED-tool conflict.",
            budget_amount=19.0, budget_currency="USD", budget_type="hourly ($10.00-$28.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents, per "
                              "evidence/payment-routing.md)",
            client_history="Small but established and genuinely active client: member since "
                            "2020 (5+ years), $2.5K total spent, 9 hires, 5 active contracts right "
                            "now, 75 hours logged -- a real, ongoing Sales & Marketing small "
                            "business, no trust concern.",
            verification_status="VERIFIED",
            priority_tier="P1",
            rejection_reason=None,
            est_days_to_accessible_payment=18,
            score_probability_win=9, score_time_to_payment=13, score_skill_match=14,
            score_payment_certainty=8, score_compensation=6, score_client_credibility=7,
            score_repeat_potential=4, score_total=61,
            score_rationale="This cycle's cleanest candidate: pure deliverability/domain-"
                            "reputation audit work across multiple accounts -- exactly the "
                            "project's best-documented skill area -- for a small but genuinely "
                            "established and currently active client (5 active contracts right "
                            "now, 5+ years on the platform). Unlike this cycle's and prior "
                            "cycles' rejected deliverability leads, the hiring funnel here is NOT "
                            "yet advanced: Interviewing is at 0 (not climbing), only 1 invite sent "
                            "and unanswered, and the job's own Activity panel shows no 'Hires' "
                            "field at all -- this listing is not functionally closed. Discounts "
                            "applied honestly rather than rounded away: 20-50 proposals is still "
                            "real competition even with 0 currently interviewing; last viewed by "
                            "client 6 days ago is mildly stale (not fresh, not dead); the rate "
                            "range ($10-28/hr) is modest, not premium; and the usual TRNC "
                            "payment-routing caveat applies uniformly to every Upwork opportunity "
                            "in this project and has not been independently resolved. Flagged to "
                            "the owner per the task's own instruction as a clean, currently-open, "
                            "well-matched P1 candidate -- not yet actioned, no application "
                            "package prepared without explicit owner go-ahead.",
            status="researched",
            notes="New-to-file Upwork URL this cycle, surfaced by a fresh Brevo/deliverability "
                  "search. Flagged in the cycle-17 report as the one opportunity worth a possible "
                  "application package, pending the owner's explicit go-ahead per master prompt "
                  "section 11.3 -- no proposal drafted, nothing submitted, no contact made.",
        ),
        dict(
            source_id=upwork_id,
            title="B2B Content Creator – LinkedIn & Email Marketing (Long-Term Freelance)",
            client_name="ShelfPerfect, a Singapore-based retail technology company (small company, "
                         "2-9 people; Upwork member since May 9, 2024, $951 total spent, 5 hires, "
                         "1 active)",
            url="https://www.upwork.com/freelance-jobs/apply/B2B-Content-Creator-LinkedIn-Email-Marketing-Long-Term-Freelance_~022122900918117561327/",
            posted_at="Posted November 17, 2026; last viewed by client last week",
            description="Ongoing monthly content role: 4 B2B LinkedIn posts (written copy plus "
                        "branded Canva graphics/carousels) and 2 email marketing campaigns per "
                        "month (copy, design, scheduling in Brevo or a similar platform), plus "
                        "content planning and basic monthly performance reporting. Application "
                        "requires a 2-3 minute self-recorded portfolio video walking through a "
                        "LinkedIn post and an email campaign the applicant personally created.",
            required_skills="Proven B2B LinkedIn content and email marketing campaign experience, "
                             "strong copywriting AND graphic design skills, proficiency with "
                             "Canva, experience with Brevo/Mailchimp/similar platforms (Brevo is "
                             "acceptable so no PROHIBITED-tool conflict on the platform itself, "
                             "but the LinkedIn-content/Canva-graphic-design core of the role is "
                             "not evidenced in the claims register, which documents Brevo "
                             "deliverability/segmentation/lifecycle work, not social content "
                             "design).",
            budget_amount=215.0, budget_currency="USD",
            budget_type="fixed price, monthly retainer ($180.00-$250.00/month for all 6 monthly "
                         "deliverables)",
            payment_platform="Upwork (fixed-price monthly; not independently tested for TRNC "
                              "residents)",
            client_history="Small but real, credible client: member since 2024, $951 total spent, "
                            "5 hires, 1 active contract -- modest but genuine track record, no "
                            "major trust concern.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="The email-marketing component alone would be a reasonable fit (Brevo "
                              "accepted, no PROHIBITED tool), but it is a minor part of a role "
                              "whose core ask is B2B LinkedIn content writing plus hands-on Canva "
                              "graphic design (branded carousels, LinkedIn visuals) -- neither "
                              "documented in the claims register, which supports Brevo platform "
                              "depth, not social-content design work. The application itself "
                              "requires a self-recorded portfolio video demonstrating prior "
                              "LinkedIn-graphic and email-newsletter design work, which cannot be "
                              "credibly produced without that history. Combined with a low fixed "
                              "monthly rate ($180-250) for six recurring monthly deliverables "
                              "across two disciplines, this is a skill-mismatch-plus-compensation "
                              "reject.",
            est_days_to_accessible_payment=None,
            score_probability_win=4, score_time_to_payment=10, score_skill_match=5,
            score_payment_certainty=6, score_compensation=3, score_client_credibility=5,
            score_repeat_potential=3, score_total=36,
            score_rationale="Low competition (Interviewing:1, 10-15 proposals) and a credible "
                            "small client are outweighed by a core skill mismatch -- LinkedIn "
                            "content writing and Canva graphic design are not in evidence -- and "
                            "compensation that is thin for the described six-deliverable monthly "
                            "scope.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: a "
                  "role where the Brevo/email component is real but minor, dominated by an "
                  "unevidenced LinkedIn-content/graphic-design skill requirement.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-16. Per the owner's standing
    # instruction, recorded without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 17 (2026-11-27) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (12th consecutive "
              "cycle); no job-specific Hires field has ever appeared on this listing's Activity "
              "panel across any cycle. Interviewing unchanged at 2, invites 0/0. Last viewed by "
              "client '3 days ago' (vs '2 days ago' in cycle 16 -- ordinary noise). Active "
              "contracts held at 15, total spent flat at $69K, 36 hires on file, hours rose again "
              "2,026->2,030 -- ordinary continued activity on this buyer's other contracts. Not "
              "gone, not closed, nothing new to flag."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead -- the one
    # lead the owner asked to keep tracking closely, now checked with the cycle-16 Hires-field fix.
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 17 (2026-11-27) re-check, with the listing's own Activity-on-this-job "
              "panel checked explicitly for a job-specific Hires field (per the cycle-16 "
              "methodology fix): no such field appears at all (only Proposals/Last viewed/"
              "Interviewing/Invites render) -- no direct hire signal on this specific listing. "
              "Still open. Rate still $10-28/hr. Interviewing STILL at 4 -- now a 6TH consecutive "
              "cycle (12,13,14,15,16,17) with no further climb. Invites-sent/unanswered unchanged "
              "at 2/0. The 'About the client' account-level figures ($15 total spent, 1 hire, 0 "
              "active) are unchanged from cycle 16 -- a third consecutive cycle of total "
              "stability on both the listing and its buyer account. Noted, not treated as "
              "closure. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 11, len(opportunities), 1,
         "Cycle 17, the regular run following cycle 16 (2026-11-26). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (12th cycle), no Hires field has ever appeared, "
         "nothing new, noted only. (b) Brevo CRM and Email Setup (id 40) rechecked with the "
         "job's own Activity panel checked explicitly for a Hires field as the cycle-16 "
         "methodology fix instructed -- none appears; STILL stalled at Interviewing=4 for a 6TH "
         "consecutive cycle, account-level figures unchanged for a third consecutive cycle; not "
         "closed, tier not revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted again "
         "-- blocked identically (12th consecutive cycle); the paid scrapecreators Alexandria "
         "provider was deliberately NOT used again pending the owner's go-ahead from cycle 7. "
         "(d) PeoplePerHour page 1 re-checked only -- no genuinely new in-scope listing this "
         "cycle; the 'Markerters wanted...' posting logged last cycle is unchanged; recurring "
         "out-of-scope postings persist in substance. (e) Contra (17th consecutive cycle, no new "
         "genuine lead), the German-market search (17th consecutive cycle -- the freiguide.de/"
         "Kleinanzeigen.de dead-mirror pattern recurred for a FOURTH time, remains CONFIRMED "
         "STRUCTURAL per the owner's instruction and is not re-described), and freelance.de "
         "(11th consecutive cycle confirming no reachable client-posting section) were checked "
         "again briefly per instruction. Useme.com not re-run this cycle, prior finding assumed "
         "unchanged. Fresh Brevo/generic searches across Upwork, Freelancer.com, and Guru.com "
         "found 2 new-to-file candidates this cycle, both on Upwork: 'Email Deliverability "
         "Specialist for 3 Companies' -- escalated to P1 and flagged to the owner as this cycle's "
         "one clean, currently-open, well-matched opportunity (strong deliverability skill match, "
         "credible small-but-active client, Interviewing at 0 with no Hires field rendering -- "
         "not functionally closed), not yet actioned pending owner go-ahead per master prompt "
         "section 11.3; and 'B2B Content Creator - LinkedIn & Email Marketing' (ShelfPerfect) -- "
         "REJECTED on skill mismatch (LinkedIn content/Canva graphic design, not Brevo platform "
         "depth) plus low pay for scope. Freelancer.com's searches surfaced only already-on-file "
         "listings (country-subdomain mirrors of existing URLs) plus one closed, extremely-low-"
         "pay repost from an already-logged client, not logged. Guru.com surfaced only the "
         "already-on-file listing plus one unrelated teaching role, not logged. Direct business "
         "prospecting (master prompt section 4.3/12) was not run this cycle, per the standing "
         "scope instruction. 1 new P1 opportunity flagged this cycle; 0 new P0."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 17 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
