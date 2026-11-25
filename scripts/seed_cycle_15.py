#!/usr/bin/env python3
"""Discovery cycle 15 (2026-11-25): regular run following cycle 14 (2026-11-24). Picks up cycle
14's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, hourly rate still does not render (10th consecutive cycle).
Interviewing unchanged at 2, invites 0/0. The client's active-contracts count, which dipped
16->15 last cycle, has now HELD at 15 (not dropped further) while total spent is flat at $69K and
hours rose again (2,002->2,020, ongoing growth on this high-volume buyer's OTHER contracts) --
this stability confirms last cycle's dip was unrelated to this specific listing, not a delayed
closure signal. Per the owner's standing instruction, noted on the DB row only, not re-flagged.
(b) re-checked the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- still
stalled at Interviewing=4, now a 4TH consecutive cycle (12, 13, 14, 15) with no further climb and
no hire on this specific listing. One new but ambiguous account-level signal this cycle: the
client's "active" contract count dropped from 1 to 0 (their one all-time hire no longer shows as
active) while total spent stays flat at $15 -- by the same logic applied to id 31's account-level
dip last cycle, this reads as that hire's OTHER contract concluding, not a hire/closure signal on
THIS listing (which still shows no "Hires" field, Interviewing unchanged, invites unchanged).
Noted, not re-flagged; tier not revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted
again against the subreddit listing page (no paid scrapecreators Alexandria provider used without
the owner's go-ahead, open since cycle 7) -- failed identically, the 10th consecutive cycle blocked
on the free method. (d) PeoplePerHour page 1 re-check only -- the current-listings section now
shows one genuinely new-to-page posting ("B2B Lead Generation & Email Outreach for Established VO
Artist", $138, 27 proposals) alongside the same three recurring out-of-scope postings (the Dubai
B2B cold-email lead-gen role now aged to 3 days/22 proposals, "Find 75 Property Owners for Free
Listings" unchanged, "Gmail account" unchanged) -- the new item is pure lead-generation/outreach
work with no Brevo or email-marketing-platform skill involved, so it was read but not logged,
consistent with the project's scope standard. 10th cycle running with nothing new and in-scope
from this source. (e) Contra, the German-market search, and freelance.de -- all three checked
again, kept brief as instructed. Contra: 15th consecutive cycle, same id-19 card plus two other
recurring non-Brevo listings, no new genuine client email-marketing lead. German-market search:
15th consecutive cycle with nothing live and actionable -- a second, different freiguide.de-
mirrored Kleinanzeigen.de "BREVO Newsletter einrichten" classified surfaced (a different ad ID
than cycle 14's), and checking the original Kleinanzeigen.de URL directly again showed it already
removed ("Die gewuenschte Anzeige ist nicht mehr verfuegbar") -- this is now the SECOND time this
exact dead-mirror pattern has repeated, suggesting freiguide.de's index structurally lags behind
Kleinanzeigen.de's live removals rather than this being a one-off; a separate German Kleinanzeigen
hit found this cycle ("Biete: E-Mail-Marketing einrichten...") is a freelancer's OWN service ad
(competitor, not a client request), so not actionable either. freelance.de: 9th consecutive cycle
confirming no reachable client-posting section, only freelancer directory pages. Fresh Brevo-
specific and generic searches across Upwork and Freelancer.com found 2 new-to-file Upwork URLs
this cycle, both REJECTED: "Email Deliverability Specialist" (genuine Brevo/SPF/DKIM/DMARC
deliverability work -- the project's single strongest documented skill area -- from an established,
high-spend Australian client, but 50+ competing proposals with the client already Interviewing 3
candidates and invites already sent, so rejected on competition/probability-of-win grounds, not
scope) and "Email Marketing & Campaign Automation Specialist" ($25 fixed price from a brand-new,
zero-track-record Indian client requiring experience across Instantly/Smartlead/Lemlist/Apollo/
Brevo/Mailchimp -- several of which are PROHIBITED/unevidenced per the claims register -- rejected
on compensation, prohibited-tool-stack requirement, and low client credibility). A third
new-to-file Upwork hit, "Mail Merge & Personalized Email Outreach Specialist" (mentions BREVO once
in passing but the core scope is Word/Excel mail-merge cold-outreach for an honors-recognition
solicitation org, posted ~2.5 months ago with 50+ proposals/8 interviewing/9 invites all answered),
was read but not logged as a DB row -- too stale and scope-mismatched to carry audit-trail value,
consistent with cycle 14's treatment of similarly stale hits. Useme.com (English page 1) rechecked:
unchanged, same Oliver Toernroth/Zoined posting (17 days left, down from 18), still zero live Brevo
listings. 0 new P0/P1 opportunities this cycle. Not recommending an application package. Appends to
the same DB. Safe to re-run (INSERT OR IGNORE on url). See reports/2026-11-25-discovery-cycle-15.md
for the full narrative."""
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
        "quiet status check. Still open. Rate still does not render (10th consecutive cycle). "
        "Interviewing unchanged at 2, invites 0/0. Active contracts HELD at 15 (did not drop "
        "further from last cycle's 16->15 dip), total spent flat at $69K, hours rose 2,002->2,020 "
        "-- confirms last cycle's dip was unrelated to this listing. Noted only, not re-flagged. "
        "Also re-checked the PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email Setup' listing (id "
        "40): still at Interviewing=4, now a 4TH consecutive cycle with no further climb and no "
        "hire on this listing. New ambiguous signal: client's active-contract count dropped 1->0 "
        "(their sole hire no longer active), read the same way as id 31's account-level dip -- "
        "not a closure signal on this specific job. Tier not revised. Fresh Brevo-specific and "
        "generic searches surfaced 2 new-to-file Upwork URLs this cycle, both REJECTED (see "
        "opportunities below), plus one further hit ('Mail Merge & Personalized Email Outreach "
        "Specialist', mentions Brevo in passing but ~2.5 months stale with 50+ proposals/8 "
        "interviewing/9 invites already answered) read but not logged as too stale and "
        "scope-mismatched for audit-trail value.",
        discovery_count=2, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 10 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 10th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- still awaiting "
        "the owner's go-ahead from cycle 7. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-14's finding. One genuinely new-to-page posting this "
        "cycle: 'B2B Lead Generation & Email Outreach for Established VO Artist' ($138, 27 "
        "proposals) -- read but not logged, pure lead-generation/outreach work with no Brevo or "
        "email-marketing-platform skill involved, out of scope. The same three recurring "
        "out-of-scope postings persist ('Cold Email Marketing Specialist', Dubai B2B "
        "tax-consultancy lead generation, now aged to 3 days/22 proposals; 'Find 75 Property "
        "Owners for Free Listings', unchanged; 'Gmail account', unchanged). 10th cycle running "
        "with no genuinely new, in-scope, live candidate from this source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced no new-to-file Freelancer.com URLs "
        "this cycle -- every Brevo-specific hit returned (e.g. 'Brevo Email Marketing Specialist' "
        "at EUR2-6/hr) was already on file from a prior cycle.",
        discovery_count=0, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "15th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered the same 'Email Marketing Specialist - Dual "
        "Campaigns for Parents & School Leaders' card already on file (id 19, $25-40/hr), plus two "
        "other recurring non-Brevo, non-email-platform listings ('Marketing Assistant for Launch "
        "Campaign', 'Prepping Digital Assets Before Launching Campaigns') -- still never a genuine "
        "NEW client email-marketing posting across 15 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 15th consecutive cycle with no live, actionable "
        "German-market email-marketing-specialist opening. A second, different freiguide.de-"
        "mirrored Kleinanzeigen.de classified titled 'BREVO Newsletter einrichten' surfaced this "
        "cycle (a different ad ID than cycle 14's find); checking the original Kleinanzeigen.de "
        "URL directly again showed it already removed ('Die gewuenschte Anzeige ist nicht mehr "
        "verfuegbar'). This is now the SECOND time this exact dead-mirror pattern has repeated, "
        "suggesting freiguide.de's index structurally lags behind Kleinanzeigen.de's live removals "
        "rather than being a one-off coincidence. A separate Kleinanzeigen hit this cycle, 'Biete: "
        "E-Mail-Marketing einrichten - Newsletter endlich starten', is a freelancer's OWN service "
        "ad (a competitor advertising their skills, not a client request), so not actionable "
        "either. German-proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-14: same Oliver "
        "Tornroth/Zoined posting (now 17 days left, down from 18 in cycle 14), still the only open "
        "listing, still zero live Brevo listings. Rest of category remains closed Klaviyo/"
        "Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend listings, same as prior cycles. "
        "Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried the same dedicated search again, aimed specifically at a client project/Auftrag "
        "posting. Surfaced only freelancer profile/directory pages (Brevo-Freelancer finden, "
        "Newsletter-Freelancer finden, Newsletter-kampagnen-Freelancer finden) plus a Fiverr gig "
        "directory, no client project listing at all. 9th consecutive cycle confirming no client "
        "project-posting section is reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle, consistent with cycle 13-14's treatment; "
        "prior cycles' finding (general tutorial/comparison content, no live candidate) assumed "
        "unchanged.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Deliverability Specialist",
            client_name="Travel & hospitality small company (2-9 people), Sydney, Australia "
                         "(Upwork; member since Jul 26, 2012, $68K total spent, 61 hires, 10 "
                         "active, 2,443 hours -- long-established, high-spend client)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Deliverability-Specialist_~022120688264949218210/",
            posted_at="Duration tag 'Less than 1 month', last viewed by client 3 days before "
                      "this cycle's discovery; exact posting date not shown",
            description="Fix email deliverability issues for the client's Google Workspace and "
                        "Brevo setup: review and improve SPF, DKIM, and DMARC configurations, "
                        "resolve spam issues with Yahoo and Outlook, diagnose problems, recommend "
                        "fixes, and confirm successful implementation.",
            required_skills="Email Marketing, Email Communication, Email Deliverability, Email "
                             "Support; explicit Google Workspace + Brevo authentication/"
                             "deliverability troubleshooting (SPF/DKIM/DMARC) -- this is the "
                             "single most strongly documented skill area in the claims register.",
            budget_amount=23.5, budget_currency="USD", budget_type="hourly ($12.00-$35.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents, per "
                              "evidence/payment-routing.md)",
            client_history="Established client: member since 2012, $68K total spent, 61 hires, "
                            "10 active contracts, 2,443 hours logged -- strong track record and "
                            "credibility, no trust concern.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Genuine skill match (Brevo deliverability/SPF/DKIM/DMARC is exactly "
                              "the project's strongest, most consistently documented claim), and "
                              "a credible, established client -- but rejected on competition and "
                              "probability-of-win grounds, per the owner's standing instruction "
                              "against rounding up marginal matches: 50+ competing proposals, the "
                              "client already Interviewing 3 candidates, and 3 invites already "
                              "sent (2 still unanswered) show the hiring funnel is well advanced "
                              "before this cycle's discovery even ran. Submitting a fresh proposal "
                              "now would be a late, low-probability bid into an already-saturated, "
                              "already-progressing pipeline, not a clean P0/P1 candidate.",
            est_days_to_accessible_payment=None,
            score_probability_win=2, score_time_to_payment=4, score_skill_match=5,
            score_payment_certainty=3, score_compensation=3, score_client_credibility=5,
            score_repeat_potential=2, score_total=24,
            score_rationale="Strong skill and client-credibility scores dragged down by a very "
                            "low probability-of-win score (50+ proposals, 3 already interviewing, "
                            "invites already out) -- the deciding factor for the reject.",
            status="open",
            notes="New-to-file Upwork URL this cycle, surfaced by a Brevo-specific search. Logged "
                  "for audit-trail completeness; closest skill match of this cycle's new finds, "
                  "rejected purely on competition timing, not scope or compensation.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing & Campaign Automation Specialist",
            client_name="Individual/small business client, India (Upwork; member since Nov 6, "
                         "2026 -- 19 days old at discovery, no total-spent or hires figures shown, "
                         "i.e. zero verified track record)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Campaign-Automation-Specialist_~022119718210708323417/",
            posted_at="Posted November 9, 2026 (16 days before this cycle's discovery)",
            description="Client currently uses Zoho for email operations but faces deliverability "
                        "issues; wants a specialist to evaluate the setup, recommend a new "
                        "platform, configure infrastructure, build bulk campaigns and automated "
                        "multi-step outreach sequences with non-responder-only follow-ups, "
                        "ensure SPF/DKIM/DMARC authentication, set up tracking/reporting, and "
                        "advise on warm-up and domain reputation.",
            required_skills="Explicitly names Instantly, Smartlead, Lemlist, Apollo, Brevo, "
                             "Mailchimp 'or similar platforms', and wants the freelancer to "
                             "recommend the right platform rather than just operate Brevo alone.",
            budget_amount=25.0, budget_currency="USD", budget_type="fixed price ($25.00, ongoing "
                           "project)",
            payment_platform="Upwork (fixed-price; not independently tested for TRNC residents)",
            client_history="Brand-new client account (member since Nov 6, 2026, 19 days old at "
                            "discovery), no total-spent or hires data displayed at all -- no "
                            "track record to assess trust or payment follow-through against.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Three independent reject grounds: (1) compensation -- $25.00 fixed "
                              "price for a scope that includes platform evaluation, infrastructure "
                              "setup, multi-step automated sequences, authentication "
                              "configuration, and reporting is not a viable rate under any "
                              "reading, before TRNC payment-routing friction is even considered; "
                              "(2) required tool stack -- the posting explicitly wants experience "
                              "with Instantly, Smartlead, Lemlist, and Apollo as well as Brevo and "
                              "Mailchimp, and wants the freelancer to recommend across that whole "
                              "stack; Instantly, Lemlist, Apollo, and Mailchimp are all "
                              "PROHIBITED/unevidenced per evidence/claims-register.md, so a Brevo-"
                              "only skill set does not cover what this role is actually asking "
                              "for; (3) client credibility -- brand-new account (19 days old) "
                              "with zero verified spend or hire history on the platform.",
            est_days_to_accessible_payment=None,
            score_probability_win=2, score_time_to_payment=5, score_skill_match=2,
            score_payment_certainty=2, score_compensation=1, score_client_credibility=2,
            score_repeat_potential=2, score_total=16,
            score_rationale="Low across almost every axis: compensation and skill-match scores "
                            "are the worst of this cycle's candidates (prohibited-tool requirement "
                            "plus a token fixed price), with no redeeming client-credibility "
                            "signal to offset them.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness as a "
                  "clean compensation + prohibited-tool-stack + credibility reject, not a close "
                  "call.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-14. Per the owner's standing
    # instruction (flagged already, their call to act on), this is recorded without being
    # surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 15 (2026-11-25) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (10th consecutive "
              "cycle). Interviewing unchanged at 2, invites 0/0. Active contracts HELD at 15 "
              "(did not drop further from last cycle's 16->15 dip) while total spent stayed flat "
              "at $69K and hours rose again (2,002->2,020) -- this stability confirms last "
              "cycle's dip was unrelated to this specific listing, not a delayed closure signal. "
              "Last viewed by client: 'yesterday' (vs '4 days ago' in cycle 14 -- ordinary "
              "recency noise). Noted; no fresh flag raised."
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
            + " | Cycle 15 (2026-11-25) re-check: still open. Rate still $10-28/hr. Interviewing "
              "STILL at 4 -- now a 4TH consecutive cycle with no further climb beyond cycle 12's "
              "stall, and still no hire appearing on this specific listing. Invites-sent/"
              "unanswered unchanged at 2/0. One new but ambiguous account-level signal: the "
              "client's 'active' contract count dropped from 1 to 0 (their sole all-time hire no "
              "longer shows as active), with total spent still flat at $15 -- read the same way "
              "as id 31's account-level active-contracts dip last cycle, this most plausibly "
              "reflects that hire's OTHER contract concluding, not a hire/closure signal on THIS "
              "job (no job-specific 'Hires' field appeared, Interviewing/invites unchanged). "
              "Noted, not treated as closure. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 8, len(opportunities), 0,
         "Cycle 15, the regular run following cycle 14 (2026-11-24). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (10th cycle); the active-contracts dip noted last "
         "cycle has HELD at 15 rather than dropping further, confirming it was unrelated to this "
         "listing, so noted only, not re-flagged, per the owner's standing instruction. (b) Brevo "
         "CRM and Email Setup (id 40), the lead with the strongest prior movement, rechecked "
         "closely as instructed -- STILL stalled at Interviewing=4 for a 4TH consecutive cycle, no "
         "hire on this listing, not closed, tier not revised; a new account-level active-hires "
         "dip (1->0) was noted but not treated as a closure signal, by the same reasoning applied "
         "to id 31 last cycle. (c) Reddit r/forhire: direct firecrawl_scrape attempted again -- "
         "blocked identically (10th consecutive cycle); the paid scrapecreators Alexandria "
         "provider was deliberately NOT used again pending the owner's go-ahead from cycle 7. (d) "
         "PeoplePerHour page 1 re-checked only -- one genuinely new-to-page lead-generation/"
         "outreach posting found but out of scope (no Brevo/platform skill involved), so not "
         "logged; 10th cycle running with no genuinely new in-scope live candidate. (e) Contra "
         "(15th consecutive cycle, same id-19 card, no new genuine lead), the German-market search "
         "(15th consecutive cycle -- a second, different freiguide.de/Kleinanzeigen.de Brevo "
         "classified surfaced and was again already removed by check time, now a repeated pattern "
         "rather than a one-off; a separate hit was a freelancer's own competing service ad, not a "
         "client request), and freelance.de (9th consecutive cycle confirming no reachable "
         "client-posting section) were checked again briefly per instruction. Fresh Brevo/generic "
         "searches across Upwork and Freelancer.com found 2 new-to-file Upwork URLs this cycle, "
         "both REJECTED: 'Email Deliverability Specialist' (genuine Brevo/deliverability skill "
         "match from a credible established client, but 50+ proposals and the client already "
         "Interviewing 3 candidates made this a late, low-probability bid -- rejected on "
         "competition timing, not scope) and 'Email Marketing & Campaign Automation Specialist' "
         "($25 fixed price, brand-new zero-track-record client, requires several PROHIBITED/"
         "unevidenced tools alongside Brevo -- rejected on compensation, prohibited-tool-stack, "
         "and credibility). A third hit ('Mail Merge & Personalized Email Outreach Specialist', "
         "~2.5 months stale, 50+ proposals/8 interviewing/9 invites all answered, core scope is "
         "Word/Excel mail-merge cold outreach with only a passing Brevo mention) was read but not "
         "logged, consistent with the project's audit-trail standard for stale/scope-mismatched "
         "hits. Direct business prospecting (master prompt section 4.3/12) was not run this "
         "cycle, per the standing scope instruction. 0 new P0/P1 opportunities this cycle; no "
         "application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 15 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
