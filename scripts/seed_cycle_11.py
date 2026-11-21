#!/usr/bin/env python3
"""Discovery cycle 11 (2026-11-21): regular run following cycle 10 (2026-11-20). Picks up cycle
10's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, rate still does not render (6th consecutive cycle), but for
the first time in several cycles there is small movement: Interviewing dropped 3->2, and client
totals ticked up slightly ($68K spent/36 hires [was 35]/16 active/1,983 hours [was 1,980]) -- noted
on the DB row, not re-flagged as "needs attention" per the owner's standing instruction, since the
job-specific status gives no "Hires: 1"-style signal that it has actually closed. (b) re-checked
the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- still open, same thin
1-hire client history, but Interviewing progressed further, 3->4 (continuing cycle 10's 2->3 move);
invites-sent/unanswered unchanged at 2/0. Tier not revised. (c) one more Reddit r/forhire direct
firecrawl_scrape attempt (no paid Alexandria provider used without the owner's go-ahead) -- failed
identically again, the 6th consecutive cycle blocked on the free method. (d) PeoplePerHour page 1
re-check only -- no genuinely new live candidate; the only two current-section listings were
out-of-scope (Gmail account setup) or already on file (UK Kajabi, id 8), and "Help with Brevo" is
unchanged in the Past Projects section (still 6 proposals, already rejected as stale, id 46). Also
runs fresh Brevo-specific and generic searches across Upwork and Freelancer.com, plus checks on
Contra, German-market search, freelance.de and Useme.com. Found and logged 5 new URLs this cycle
(3 Upwork, 2 Freelancer.com), all REJECTED: a $15 fixed academic Brevo/DNS job duplicate-posted by
the same already-1-hire Pakistani client as cycle 10's id 47, a UK prize-competition business
Growth Marketing role requiring unevidenced Meta/Facebook paid-ads management and AI content
tooling alongside Brevo, a Dublin-agency Email Marketing Specialist role where Brevo is only one of
five optional ESPs and structured A/B testing is a firm requirement (the unresolved CONFLICT), and
two long-stale/already-closed Freelancer.com postings (one "In Progress" since ~1 year ago, one
formally awarded 10 months ago). 0 new P0/P1 opportunities. Contra (11th consecutive cycle with no
genuine client posting, and this cycle not even a directory page surfaced), the dedicated
German-market search angle (11th consecutive cycle with nothing live), and freelance.de (5th
consecutive cycle confirming no reachable client-project-posting section) are flagged in the report
as candidates the owner may want to consider deprioritizing in favor of a new source. Appends to
the same DB. Safe to re-run (INSERT OR IGNORE on url). See reports/2026-11-21-discovery-cycle-11.md
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
        "quiet status check. Still open. Rate still does not render (6th consecutive cycle). "
        "Interviewing dropped 3->2 (first movement in several cycles); client totals ticked up "
        "slightly ($68K spent, 36 hires [was 35], 16 active, 1,983 hours [was 1,980]). Last viewed "
        "by client: 'yesterday' (vs '3 days ago' cycle 10). Also re-checked the "
        "PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email Setup' listing (id 40): still open, client "
        "still 1 hire/1 active, Interviewing progressed further 3->4 (continuing cycle 10's 2->3 "
        "move), invites-sent/unanswered unchanged at 2/0. Tier not revised. Fresh Brevo-specific "
        "and generic searches surfaced 3 new-to-file URLs this cycle, all REJECTED: a $15 "
        "fixed-price academic Brevo/DNS subdomain job that is a duplicate posting by the same "
        "already-'1 hire, 1 active' Karachi, Pakistan client as cycle 10's id 47 (same FYP scope, "
        "different listing title/URL), a UK prize-competition business's Growth Marketing role "
        "naming Brevo as the preferred ESP but requiring Meta/Facebook paid-advertising campaign "
        "management and AI-tool content creation (both unevidenced), and a Dublin, Ireland agency's "
        "Email Marketing Specialist role where Brevo is only one of five optional named ESPs "
        "(Klaviyo/Mailchimp/ActiveCampaign/HubSpot/Brevo) and structured A/B testing is a firm "
        "requirement, testing the unresolved A/B-testing CONFLICT directly.",
        discovery_count=3, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 11 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 6th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- that decision "
        "is still the owner's to make, not yet given. No cost incurred, no new data gained, as "
        "expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-10's finding. No genuinely new live candidate: the "
        "two current-section listings this cycle were 'Gmail account' (Google Workspace account "
        "setup, out of email-marketing scope) and 'UK Kajabi expert' (already on file, id 8, "
        "unchanged). 'Help with Brevo' (id 46, already rejected as stale) reappeared again under "
        "the Past Projects section, still showing 6 proposals and '2 months ago', no material "
        "change. 6th cycle running with no genuinely new, live candidate from this source.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced 2 new-to-file URLs this cycle, both "
        "REJECTED as long-closed/stale: 'Email Marketing Management for Local Business' (posted "
        "about 1 year ago, status 'In Progress', deadline already passed Sept 2025) and 'Brevo "
        "Workflow Automation Expert Needed -- 2' (freelancer.com.co mirror; status 'Terminado' "
        "[Finished], posted 10 months ago, already formally awarded to another freelancer, also "
        "tagged Make.com). Other search hits matched URLs already on file (cycles 3-10) or were "
        "freelancer self-promotion/portfolio pages, not genuine new client postings.",
        discovery_count=2, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "11th consecutive cycle with the same structural limitation. This cycle a direct scrape of "
        "the featured-jobs landing page returned only Contra's own generic marketing/landing-page "
        "content (hero copy, trusted-by logos, nav links) with no job-posting anchors at all -- not "
        "even the directory-style /hire/brevo-freelancers link that search surfaced in prior "
        "cycles. A separate web search still surfaced /hire/brevo-freelancers and "
        "/hire/constantcontact-freelancers-style directory pages, never a genuine client job "
        "posting.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query ('Brevo E-Mail Marketing Freiberufler Projekt gesucht') "
        "-- 11th consecutive cycle with no live German-market email-marketing-specialist opening "
        "surfaced; results remain Brevo's own German marketing pages, freelance.de directory/"
        "profile pages, and Contra's directory page, not client project postings. "
        "German-proficiency claims-register conflict remains untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-10: same Oliver "
        "Tornroth/Zoined posting (now 21 days left, down from 22 in cycle 10, 23 in cycle 9), still "
        "the only open listing, still zero live Brevo listings. Rest of the category remains "
        "closed Klaviyo/Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend listings, same as "
        "prior cycles. Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a site-scoped query ('site:freelance.de Brevo E-Mail-Marketing Auftrag') aimed "
        "specifically at a client project/Auftrag posting. Surfaced only freelancer profile/"
        "directory pages (individuals advertising their own Brevo/E-Mail-Marketing skills, e.g. "
        "the 'Newsletter-Freelancer-in-Dresden' directory page), no client project listing at all. "
        "5th consecutive cycle confirming no client project-posting section is reachable for this "
        "platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle; prior cycles' finding (general tutorial/"
        "comparison content, no live candidate) assumed unchanged. Covered this cycle instead by "
        "the broader generic email-marketing search pass, which also surfaced only job-board "
        "landing/aggregator pages (Indeed, LinkedIn, ZipRecruiter, Toptal, Arc.dev), not individual "
        "live postings.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Infrastructure & Domain Configuration Specialist (duplicate posting by "
                  "the same already-hired academic FYP client as id 47)",
            client_name="Individual client, Karachi, Pakistan (Upwork; member since Oct 24, 2026; "
                         "1 hire, 1 active)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Infrastructure-Domain-Configuration-Specialist_~022114233614615365717/",
            posted_at="Posted October 25, 2026",
            description="University Final Year Project in Cybersecurity: configure a Brevo "
                        "subdomain of a university-provided domain with SPF/DKIM/DMARC so the "
                        "main university domain does not appear in a normal Gmail inbox sender "
                        "view. Near-identical scope and wording to the 'Fix Brevo/Mailgun' listing "
                        "(id 47) from the same client, posted under a different title in the "
                        "Network & System Administration category instead of Digital Marketing.",
            required_skills="Brevo configuration, DNS management, SPF/DKIM/DMARC, email "
                             "deliverability, Gmail headers and sender authentication, subdomain "
                             "configuration.",
            budget_amount=15, budget_currency="USD", budget_type="fixed-price; Expert level, "
                          "one-time project",
            payment_platform="Upwork (fixed-price; not independently tested for TRNC residents)",
            client_history="Member since Oct 24, 2026 (under 1 month old at discovery). Pakistan. "
                            "1 hire, 1 active -- the same client already logged under id 47.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Same client as cycle 10's id 47 ('Fix Brevo/Mailgun'), which already "
                              "shows '1 hire, 1 active' -- this is a duplicate posting of "
                              "effectively the same academic FYP scope under a different title and "
                              "category, not a second independent opportunity. Even taken alone: "
                              "$15 fixed-price, a one-time university student project, not a "
                              "sustainable freelance relationship, and 7 interviewing / 11 invites "
                              "sent / 2 unanswered shows the client already deep into its hiring "
                              "funnel for this scope.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle (different URL from id 47, same client/scope "
                  "duplicate). Logged for audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="Growth Marketing Specialist -- Email, Meta Ads & AI Marketing (Brevo named, but "
                  "unevidenced paid-ads/AI-content skills required)",
            client_name="WTF Giveaways, United Kingdom (Upwork; member since Nov 1, 2026 -- 3 "
                         "weeks old at discovery; no spend/hire history shown)",
            url="https://www.upwork.com/freelance-jobs/apply/Growth-Marketing-Specialist-Email-Meta-Ads-Marketing_~022117279678077084233/",
            posted_at="Posted November 2, 2026",
            description="Growth marketing role for a UK online prize-competition business: email "
                        "marketing and customer segmentation using Brevo (creating AI-assisted "
                        "campaign emails, lifecycle/reactivation flows), plus Meta/Facebook "
                        "advertising strategy and campaign management, plus AI-powered content "
                        "creation (ChatGPT/Claude, Canva), plus weekly marketing planning/"
                        "reporting. Contract-to-hire potential, paid trial before ongoing "
                        "commitment.",
            required_skills="Proven email marketing experience, preferably Brevo; customer "
                             "segmentation/lifecycle marketing; Meta/Facebook advertising campaign "
                             "management (essential, not optional); AI-tool content creation; "
                             "marketing copywriting; commercial/sales focus; UK GDPR/PECR "
                             "awareness and prize-competition advertising-rules knowledge "
                             "(desirable).",
            budget_amount=1000, budget_currency="USD", budget_type="fixed-price ($1,000); "
                          "contract-to-hire, initially 10-15 hrs/week",
            payment_platform="Upwork (fixed-price; not independently tested for TRNC residents)",
            client_history="Member since Nov 1, 2026 (3 weeks old at discovery). United Kingdom. "
                            "No total-spent, hires, or hours shown -- no track record yet.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Brevo is named as the preferred email platform (a genuine partial "
                              "match), but the role's essential qualifications require hands-on "
                              "Meta/Facebook paid-advertising campaign management -- paid ads are "
                              "explicitly listed in the claims register as 'none demonstrated, "
                              "don't claim.' The application itself requires submitting 'examples "
                              "of Meta campaigns you've managed and their results,' which cannot be "
                              "honestly supplied. Separately, the role also expects UK prize-"
                              "competition/GDPR/PECR regulatory familiarity and AI-content-tool "
                              "production at a volume beyond a narrow email-marketing scope -- a "
                              "multi-skill role, not a close match once the paid-ads requirement is "
                              "accounted for.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Decent budget and a genuine Brevo component, "
                  "but a clean reject on the unevidenced paid-ads requirement. Logged for "
                  "audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist (Automations, Campaigns & Revenue Growth) -- Brevo "
                  "only one of five optional ESPs, A/B testing required",
            client_name="Travel/booking-based business, Dublin, Ireland (Upwork; member since Jun "
                         "29, 2026; 1 hire, 0 active)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist_~022109978878252474269/",
            posted_at="Last viewed by client last week (relative to discovery)",
            description="Email marketing specialist role to grow revenue through campaigns, "
                        "customer journeys, and automated lifecycle flows (welcome, abandoned "
                        "booking, re-engagement, post-booking follow-up) for a booking-based "
                        "business. Segmentation, copywriting, A/B testing, analytics/reporting.",
            required_skills="Email marketing strategy and campaign management; automated flows/"
                             "customer journeys; segmentation and personalization; A/B testing and "
                             "performance optimization; experience with Klaviyo, Mailchimp, "
                             "ActiveCampaign, HubSpot, Brevo, 'or similar' (client's choice, not "
                             "firmly Brevo).",
            budget_amount=15, budget_currency="USD", budget_type="hourly ($10.00-$20.00/hr); 30+ "
                          "hrs/week, 6+ months, ongoing",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Member since Jun 29, 2026. Ireland (Dublin). 1 hire, 0 active -- a "
                            "thin but real track record.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Brevo is listed as only one of five acceptable ESPs (Klaviyo, "
                              "Mailchimp, ActiveCampaign, HubSpot, or Brevo) -- the client has not "
                              "committed to Brevo specifically, consistent with the project's "
                              "'Brevo keyword != platform match' discipline. Separately, A/B "
                              "testing and performance optimization is listed as a required skill, "
                              "not optional -- this directly tests the unresolved A/B-testing "
                              "CONFLICT in the claims register (a documented CV claim vs. an "
                              "internal ruling that it has not actually been implemented). 20-50 "
                              "competing proposals already on record.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Clean reject on the Brevo-optional + "
                  "A/B-testing-conflict combination. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=freelancer_id,
            title="Email Marketing Management for Local Business (stale -- posted ~1 year ago, "
                  "already In Progress)",
            client_name="Individual local-business owner, country not shown (Freelancer.com)",
            url="https://www.freelancer.com/projects/email-marketing/email-marketing-management-for-local",
            posted_at="Posted about 1 year before this cycle's discovery; stated deadline Sept 31, "
                      "2025 (already long past)",
            description="Take over an existing Brevo-based local-business email marketing "
                        "operation: keep using Brevo, keep the Tuesday/Thursday send schedule and "
                        "existing contact list, rotate through an existing content calendar and "
                        "templates, use AI for content from a supplied photo library.",
            required_skills="Familiarity with or ability to learn Brevo, Google Drive, and AI "
                             "content tools.",
            budget_amount=5, budget_currency="USD", budget_type="hourly ($2-8 USD/hr)",
            payment_platform="Freelancer.com (hourly; not independently tested for TRNC residents)",
            client_history="Not independently assessable from this scrape beyond the listing "
                            "itself.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Listing status is 'In Progress' and was posted roughly a year before "
                              "this cycle's discovery, with a stated deadline (Sept 31, 2025) that "
                              "has already long passed and 23 proposals already on record -- this "
                              "work has already been awarded and completed or abandoned, not a "
                              "live opportunity. Also a very low hourly rate ($2-8/hr) that would "
                              "not clear a reasonable compensation bar even if open.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com URL this cycle. Genuine Brevo scope, but a year-old "
                  "already-in-progress listing. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Workflow Automation Expert Needed -- 2 (already awarded 10 months ago)",
            client_name="Individual client, Modi'in-Maccabim-Re'ut, Israel (Freelancer.com/.com.co "
                         "mirror; 5.0 rating, 66 reviews, payment method verified; member since "
                         "Oct 15, 2014)",
            url="https://www.freelancer.com.co/projects/email-marketing/Brevo-Workflow-Automation-Expert-Needed",
            posted_at="Posted 10 months before this cycle's discovery; status 'Terminado' "
                      "(Finished/Closed)",
            description="Set up and optimize Brevo workflow automations for membership and "
                        "non-membership customer interactions, to enhance customer experience. "
                        "Also tagged under the Make.com category.",
            required_skills="Proven Brevo experience; workflow-automation design; customer-"
                             "experience strategy.",
            budget_amount=20, budget_currency="USD", budget_type="fixed ($10-30 USD, paid on "
                          "delivery)",
            payment_platform="Freelancer.com (fixed-price; not independently tested for TRNC "
                              "residents)",
            client_history="Member since Oct 15, 2014 (11+ years). Israel. 5.0 rating across 66 "
                            "reviews, payment method verified -- an established, credible buyer, "
                            "but this specific listing is long closed.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed and formally awarded 10 months before this cycle's "
                              "discovery (status 'Terminado'/Finished, 4 proposals, one explicitly "
                              "marked 'Adjudicado a' [awarded to] another freelancer) -- not a live "
                              "opportunity by a wide margin. Also tagged under the Make.com "
                              "category alongside Email Marketing, suggesting middleware tooling "
                              "may have been part of the actual scope.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com (.com.co mirror) URL this cycle. A credible long-"
                  "tenured client, but a listing closed 10 months ago. Logged for audit-trail "
                  "completeness.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-10. Per the owner's standing
    # instruction (flagged already, their call to act on), this is recorded without being
    # surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 11 (2026-11-21) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (6th consecutive "
              "cycle). Interviewing dropped 3->2 -- the first movement after 3 flat cycles, "
              "though no job-specific 'Hires' field appears on this listing to confirm whether it "
              "has actually closed. Proposals still 20-50. Last viewed by client: 'yesterday' (vs "
              "'3 days ago' in cycle 10). Client totals ticked up slightly: $68K spent (same), 36 "
              "hires (was 35), 16 active (same), 1,983 hours (was 1,980) -- small but real "
              "movement after cycle 10's fully-flat snapshot. Noted; no fresh flag raised."
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
            + " | Cycle 11 (2026-11-21) re-check: still open. Rate still $10-28/hr. Client still "
              "1 hire/1 active (no new hires). Interviewing progressed further, 3->4 (continuing "
              "cycle 10's 2->3 move) -- the second consecutive cycle of upward movement on this "
              "signal. Invites-sent/unanswered unchanged at 2/0. Proposals still 20-50. Tier not "
              "revised: the client is still thin on track record (1 hire total), but this is now "
              "two cycles running of modest outbound-activity growth, worth watching."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 9, len(opportunities), 0,
         "Cycle 11, the regular run following cycle 10 (2026-11-20). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (6th cycle), Interviewing dropped 3->2 (first "
         "movement after 3 flat cycles), client totals ticked up slightly -- not re-flagged per "
         "the owner's standing instruction. (b) Brevo CRM and Email Setup (id 40) rechecked -- "
         "still open, Interviewing progressed further 3->4, tier not revised. (c) Reddit "
         "r/forhire: direct firecrawl_scrape attempted again, still blocked (6th consecutive "
         "cycle); the paid scrapecreators Alexandria provider was deliberately NOT used again "
         "pending the owner's go-ahead from cycle 7. (d) PeoplePerHour page 1 re-checked only -- "
         "no genuinely new live candidate (6th cycle running). Fresh Brevo/generic searches across "
         "Upwork and Freelancer.com found 5 new URLs total (3 Upwork, 2 Freelancer.com), all "
         "REJECTED: a duplicate posting by an already-1-hire academic client, a UK growth-"
         "marketing role requiring unevidenced paid-ads/Meta-advertising skills, a Dublin agency "
         "role where Brevo is optional and A/B testing is required (the unresolved conflict), and "
         "two long-closed/stale Freelancer.com listings. Contra (11th consecutive cycle with "
         "nothing, and this cycle not even a directory page), the dedicated German-market search "
         "(11th consecutive cycle with nothing live), and freelance.de (5th consecutive cycle "
         "confirming no reachable client-posting section) are flagged in the report as candidates "
         "for possible deprioritization in favor of a new source. Direct business prospecting "
         "(master prompt section 4.3/12) was not run this cycle, per the standing scope "
         "instruction. 0 new P0/P1 opportunities this cycle; no application package "
         "recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 11 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
