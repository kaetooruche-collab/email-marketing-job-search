#!/usr/bin/env python3
"""Discovery cycle 10 (2026-11-20): regular run following cycle 9 (2026-11-19). Picks up cycle 9's
open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo Upwork
listing (id 31) -- still open, rate still does not render (5th consecutive cycle), Interviewing
flat at 3 for the 3rd cycle running, and for the first time every client metric ($68K/35 hires/16
active/1,980 hours) is fully unchanged from the prior cycle; per the owner's standing instruction
this is noted on the DB row, not re-flagged as 'needs attention' again; (b) re-checked the
PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- still open, same thin
1-hire client history, but Interviewing ticked up 2->3 and invites-sent appeared for the first time
(2 sent, 0 answered), the first outbound-activity signal since discovery; tier not revised. (c) one
more Reddit r/forhire direct firecrawl_scrape attempt (no paid Alexandria provider used without the
owner's go-ahead) -- failed identically again, the 5th consecutive cycle blocked on the free
method. (d) PeoplePerHour page 1 re-check only -- one new-to-file URL found ("Help with Brevo"),
rejected as a stale "Past Projects"-section listing. Also runs fresh Brevo-specific and generic
searches across Upwork, Freelancer.com, Contra, Useme.com, German-market search and freelance.de.
Found and logged 8 new URLs this cycle (1 PeoplePerHour, 5 Upwork, 2 Freelancer.com), all REJECTED
for a mix of reasons (already-hired/filled, extreme competition, required PROHIBITED tools,
experience-filter mismatch, brand-new low-credibility clients, already-closed). 0 new P0/P1
opportunities. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-20-discovery-cycle-10.md for the full narrative."""
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
        "quiet status check (not a re-flag, per the owner's standing instruction). Still open. Rate "
        "still does not render (5th consecutive cycle). Interviewing flat at 3 (3rd cycle "
        "unchanged). Last viewed by client: '3 days ago' (vs '2 days ago' cycle 9 -- ordinary "
        "noise). Client totals fully flat for the first time: $68K/35 hires/16 active/1,980 hours, "
        "identical to cycle 9. Also re-checked the PAYMENT_TIMELINE_UNCERTAIN 'Brevo CRM and Email "
        "Setup' listing (id 40): still open, client still 1 hire/1 active, but Interviewing moved "
        "2->3 and invites-sent appeared for the first time (2 sent, 0 answered) -- the first "
        "outbound-activity signal since discovery; tier not revised. Fresh Brevo-specific and "
        "generic searches surfaced 5 new-to-file URLs this cycle, all REJECTED: a Brevo/Mailgun DNS "
        "job that already shows 1 hire (effectively filled), a cold-email list-management job "
        "naming Apollo (PROHIBITED) as an acceptable tool alongside Brevo with heavy existing "
        "competition, an Email Marketing Manager role requiring 2-4 years experience and "
        "Lemlist/Instantly/Apollo/Expandi outreach tools (all PROHIBITED), a $500 fixed WordPress + "
        "newsletter launch job with 50+ proposals against a brand-new 8-day-old client, and a "
        "German-agency CRM/Email Marketing Manager role with a genuine Brevo scope but explicit "
        "required hands-on experience in Mailchimp, HubSpot, and Zapier/Make.com/N8N (all "
        "PROHIBITED) -- the same multi-tool disqualifier pattern as cycle 9's Softgile listing.",
        discovery_count=5, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 10 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 5th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- that decision "
        "is still the owner's to make, not yet given. No cost incurred, no new data gained, as "
        "expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-9's finding. One new-to-file URL surfaced this cycle "
        "('Help with Brevo', id 7 duplicate -- 'HTLM Email Design' -- reappeared again, confirmed "
        "duplicate, no action). 'Help with Brevo' is listed under the category page's 'Past "
        "Projects' section rather than the current/latest listings at the top, posted roughly 2 "
        "months before discovery with 6 proposals already on record -- logged and REJECTED as "
        "stale. 5th cycle running with no genuinely new, live candidate from this source.",
        discovery_count=1, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced 2 new-to-file URLs this cycle, both "
        "REJECTED: a Squarespace-to-Brevo signup integration with 229 competing proposals already "
        "on record and closing within 1 day of discovery (an extreme, unwinnable competition "
        "signal), and an already-closed 'Urgent: Social Media & Email Marketing Expert' listing "
        "requiring 2+ years' experience, a social-media-management portfolio, and naming "
        "Mailchimp/Klaviyo as acceptable tools alongside Brevo. Other search hits matched URLs "
        "already on file (cycles 3-9) or were freelancer self-promotion/portfolio pages, not "
        "genuine new client postings.",
        discovery_count=2, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages",
        "10th consecutive cycle with the same structural limitation: search surfaces only "
        "/hire/brevo-freelancers, /hire/constantcontact-freelancers and related directory pages, "
        "plus freelancer self-promotion/community posts -- never a genuine client job posting.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 10th consecutive cycle with no live German-market "
        "email-marketing-specialist opening surfaced; results remain freelancer profile/portfolio "
        "pages (freelance.de), Fiverr gig listings, and the Brevo careers page, not client project "
        "postings. German-proficiency claims-register conflict remains untested in practice. "
        "(Separately, a genuine German-market client project was found via Upwork this cycle, not "
        "via this search angle -- see the CRM and E-Mail Marketing Manager listing logged under "
        "Upwork, rejected on required-tools grounds.)",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Unchanged from cycles 7-9: same Oliver "
        "Tornroth/Zoined posting (now 22 days left, down from 23 in cycle 9, 24 in cycle 8, 25 in "
        "cycle 7), still the only open listing, still zero live Brevo listings. Rest of the "
        "category remains closed Klaviyo/Mailchimp/GetResponse/MailerLite/Edrone/Snov.io/Omnisend "
        "listings, same as prior cycles. Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried a site-scoped query aimed specifically at a client project/Auftrag posting "
        "mentioning Brevo or newsletter work. Surfaced only freelancer profile pages (individuals "
        "advertising their own Brevo/E-Mail-Marketing skills), no client project listing at all. "
        "4th consecutive cycle confirming no client project-posting section is reachable for this "
        "platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle; prior cycles' finding (general tutorial/"
        "comparison content, no live candidate) assumed unchanged. Covered this cycle instead by "
        "the broader generic email-marketing search pass, which also surfaced only job-board "
        "landing/aggregator pages, not individual live postings.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=pph_id,
            title="Help with Brevo (stale -- listed in PeoplePerHour's 'Past Projects' section)",
            client_name="Mick O., United Kingdom (PeoplePerHour; 91% positive, 14 reviews; 13 "
                         "projects completed, 12 freelancers worked with, 54% projects awarded; "
                         "last project 30 Sep 2026)",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing/help-with-brevo-4523834",
            posted_at="Roughly 2 months before this cycle's discovery; appears under the category "
                      "page's 'Past Projects' section, not the current/latest listings",
            description="Small company just starting to use Brevo for direct mail campaigns; needs "
                        "ad hoc ongoing help managing hard bounces and sanitizing the database, "
                        "plus rolling out more campaigns later. Also mentions wanting 'Google maps "
                        "scraper activities' later -- outside stated email-marketing scope.",
            required_skills="Brevo hands-on experience (list hygiene, bounce management). Entry "
                            "experience level stated by the client.",
            budget_amount=10, budget_currency="EUR", budget_type="fixed/starting bid, ongoing "
                          "ad hoc support (amount shown is a placeholder, not a real scope budget)",
            payment_platform="PeoplePerHour (not independently tested for TRNC residents)",
            client_history="91% positive feedback across 14 reviews; 13 projects completed, 54% "
                            "award rate; last project 30 Sep 2026 -- an established, credible small "
                            "buyer, but no recent activity visible since then.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Listed under PeoplePerHour's 'Past Projects' section (not the "
                              "current/latest section at the top of the category page), posted "
                              "roughly 2 months before this cycle's discovery with 6 proposals "
                              "already on record and no visible client activity since 30 Sep 2026 "
                              "-- reads as stale/likely filled rather than live. Separately, the "
                              "stated budget is a nominal placeholder for ongoing ad hoc work, not "
                              "a real scope budget, and the later mention of 'Google maps scraper "
                              "activities' is outside stated email-marketing scope. Does not clear "
                              "the payment-horizon test with any confidence.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file PeoplePerHour URL this cycle, found on page 1 per the established "
                  "page-1-only finding. Genuine Brevo scope but stale; logged for audit-trail "
                  "completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="Fix Brevo/Mailgun -- Brevo Email Setup Expert for Cybersecurity University FYP "
                  "(already has 1 hire)",
            client_name="Individual client, Karachi, Pakistan (Upwork; member since Oct 24, 2026)",
            url="https://www.upwork.com/freelance-jobs/apply/Fix-Brevo-Mailgun-Hide-Main-Domain-from-From-Mailed-Signed_~022114221303104013111/",
            posted_at="Last viewed by client 3 weeks before this cycle's discovery",
            description="University Final Year Project in Cybersecurity: configure a Brevo "
                        "subdomain with correct SPF/DKIM/DMARC so the university's main domain does "
                        "not appear in the sender details visible in a normal Gmail inbox view.",
            required_skills="Brevo email configuration, DNS management, SPF/DKIM/DMARC, email "
                             "deliverability troubleshooting, Gmail header/authentication knowledge.",
            budget_amount=None, budget_currency="USD", budget_type="hourly (rate did not render in "
                          "the public scrape); <1 month, Expert level, one-time project",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Member since Oct 24, 2026 (under 1 month old). Pakistan. 1 hire, 1 "
                            "active contract.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="The job listing itself already shows 'Hires: 1' alongside the "
                              "client's '1 hire, 1 active' summary -- a contract on this exact "
                              "posting has already started, so it is effectively filled even though "
                              "the public listing is still reachable. Separately, this is a "
                              "narrow, one-time academic student project (a university FYP), not a "
                              "sustainable paid freelance relationship, and the hourly rate never "
                              "rendered in the public scrape.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Genuine Brevo/deliverability scope, but "
                  "already hired and academic in nature. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="Manage email campaigns (cold-email list management; Apollo named as an "
                  "acceptable tool)",
            client_name="Individual client, Santa Monica, United States (Upwork; member since May "
                         "20, 2018; $19K total spent, 153 hires, 40 active, 278 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Manage-email-campaigns_~022123500863490613702/",
            posted_at="Last viewed by client yesterday (relative to discovery)",
            description="Manage email drip campaigns through Apollo, Brevo, Insightly or Gmass "
                        "against a list of 25,000 email addresses; copy already written, client "
                        "wants high deliverability maintained.",
            required_skills="Email deliverability management, drip-campaign execution in any of "
                             "Apollo, Brevo, Insightly or Gmass (client's choice of platform, not "
                             "firmly Brevo).",
            budget_amount=None, budget_currency="USD", budget_type="hourly (rate not shown in this "
                          "scrape); 30+ hrs/week, 6+ months, ongoing",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Member since May 20, 2018 (7+ years). $19K total spent, 153 hires, 40 "
                            "active, 278 hours -- an established, high-volume individual buyer.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Apollo is listed as one of four acceptable tools alongside Brevo, and "
                              "Apollo is an explicitly PROHIBITED unevidenced-tool claim per the "
                              "claims register -- the client has not committed to Brevo "
                              "specifically. Separately, this reads as cold-email list management "
                              "against a 25,000-address list (deliverability/inbox-placement "
                              "work, not lifecycle/newsletter marketing in the project's chosen "
                              "niche), and the activity signals (6 interviewing, 25 invites sent, "
                              "17 unanswered) show the client is already deep into its hiring "
                              "funnel.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Rejected on tool-requirement and competition "
                  "grounds, not staleness. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing Manager (Slovenia agency; 2-4 yrs experience + PROHIBITED "
                  "outreach tools required)",
            client_name="Digital marketing agency, Ljubljana, Slovenia (Upwork; member since Aug 9, "
                         "2022; $8.1K total spent, 69 hires, 22 active, 115 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Manager_~022110822432147080458/",
            posted_at="Last viewed by client 3 days before this cycle's discovery",
            description="Production-led email/retention/lifecycle role for a B2B/SaaS/fintech "
                        "agency: building Figma layouts into Customer.io, HubSpot or Brevo, "
                        "lifecycle automation, structured A/B testing, deliverability monitoring, "
                        "and B2B outreach support via Lemlist/Instantly/Apollo/Expandi.",
            required_skills="2-4 years building/running email programs; hands-on with at least one "
                             "of Customer.io, HubSpot, Brevo or Klaviyo; Figma-to-HTML/CSS email "
                             "production; A/B testing; nice-to-have Lemlist/Instantly/Apollo/"
                             "Expandi, GA4/GTM, SPF/DKIM/DMARC understanding.",
            budget_amount=13.5, budget_currency="USD", budget_type="hourly ($12.00-$15.00/hr); "
                          "30-40 hrs/week, 3-6 months, contract-to-hire",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Member since Aug 9, 2022. Slovenia. $8.1K total spent, 69 hires, 22 "
                            "active, 115 hours -- an established, credible agency buyer.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Requires 2-4 years of hands-on email-program experience, exceeding "
                              "both Kaeto's actual tenure (~10 months at HIBARR) and this project's "
                              "own ~2-year job-search filter. Requires production-build skill "
                              "(Figma layout to HTML/CSS email) that is not an evidenced claim. "
                              "Requires running and reporting structured A/B tests -- A/B testing "
                              "is an explicit CONFLICT in the claims register (ruled not "
                              "implemented, contradicting a CV claim), so this role would test the "
                              "unresolved conflict directly. 'Nice to have' B2B outreach tools "
                              "(Lemlist, Instantly, Apollo, Expandi) are all PROHIBITED/unevidenced. "
                              "A clean multi-reason reject.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Credible client, but multiple hard "
                  "disqualifiers (experience floor, unevidenced production skill, A/B testing "
                  "conflict, prohibited outreach tools). Logged for audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="WordPress & Email Newsletter Setup + Ongoing Monthly Operator (B2B Executive "
                  "Advisory; 50+ proposals vs. a brand-new client)",
            client_name="Independent executive compensation advisory firm, United States (Upwork; "
                         "member since Nov 12, 2026 -- 8 days old at discovery; no spend/hire "
                         "history shown)",
            url="https://www.upwork.com/freelance-jobs/apply/WordPress-Email-Newsletter-Setup-Ongoing-Monthly-Operator-B2B-Executive-Advisory_~022121245436846671612/",
            posted_at="Posted November 13, 2026 (7 days before this cycle's discovery)",
            description="One-time technical launch of a monthly executive briefing newsletter for "
                        "biotech compensation-committee directors: set up an ESP (Kit, Brevo, or "
                        "Mailchimp -- client open to recommendation), configure SPF/DKIM/DMARC, "
                        "build a WordPress landing page and signup forms, build two email "
                        "templates and an automated welcome email. Possible 3-5 hrs/month ongoing "
                        "afterward.",
            required_skills="Email platform setup and domain authentication (SPF/DKIM/DMARC), "
                             "WordPress landing-page and form-building, responsive email template "
                             "design.",
            budget_amount=500, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork (fixed-price milestone; not independently tested for TRNC "
                              "residents)",
            client_history="Member since Nov 12, 2026 (8 days old at discovery). United States. No "
                            "total-spent, hires, or hours shown -- no track record at all.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="50+ proposals already on record against a client account only 8 "
                              "days old with zero spending or hiring history -- a severe "
                              "competition signal stacked on a severe credibility/payment-risk "
                              "signal. Brevo is only one of three ESPs the client would accept "
                              "(Kit or Mailchimp equally acceptable), not a confirmed requirement, "
                              "and the core deliverable (a WordPress landing page with signup "
                              "forms) rests on a skill that is not an evidenced Kaeto claim.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle. Rejected on competition + client-credibility "
                  "+ skill-match grounds. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=upwork_id,
            title="CRM and E-Mail Marketing Manager (Germany agency; genuine Brevo scope, but "
                  "Mailchimp/HubSpot/Zapier-Make-N8N all required)",
            client_name="Online marketing agency, Idstein, Germany (Upwork; member since Oct 28, "
                         "2018; $45K total spent, 31 hires, 7 active, 1,626 hours; mid-sized "
                         "company, 10-99 people)",
            url="https://www.upwork.com/freelance-jobs/apply/CRM-and-Mail-Marketing-Manager_~022112112419886693499/",
            posted_at="Last viewed by client yesterday (relative to discovery)",
            description="CRM and e-mail marketing manager role for a German agency's external "
                        "client portfolio: develop/implement/manage campaigns across Brevo, Active "
                        "Campaign, Mailchimp, Clevereach, and HubSpot; A/B testing and "
                        "optimization; middleware integration via Zapier, Make.com or N8N; social "
                        "media-to-CRM connection; WhatsApp/push/SMS/chat configuration.",
            required_skills="Hands-on experience with Brevo, Active Campaign, Mailchimp, "
                             "Clevereach, and HubSpot (stated as a set, not alternatives); "
                             "segmentation/automation/data analysis; A/B testing; middleware "
                             "(Zapier, Make.com, or N8N) -- stated as a required technical skill.",
            budget_amount=25, budget_currency="USD", budget_type="hourly ($20.00-$30.00/hr); <30 "
                          "hrs/week, 6+ months",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Member since Oct 28, 2018 (7+ years). Germany. $45K total spent, 31 "
                            "hires, 7 active, 1,626 hours, mid-sized company -- a well-established, "
                            "credible agency buyer, the strongest client-credibility profile found "
                            "this cycle.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="A genuine, credible client with a real Brevo scope -- but the stated "
                              "qualifications explicitly require hands-on experience across "
                              "Mailchimp and HubSpot (both named directly, not as alternatives), "
                              "plus middleware experience in Zapier, Make.com, or N8N, listed under "
                              "'Technical Skills' as a required capability, not a nice-to-have. "
                              "Every one of these is an explicitly PROHIBITED unevidenced-tool "
                              "claim per the claims register; Brevo is only one of five named "
                              "platforms here, not the primary one. The same multi-tool "
                              "disqualifier pattern flagged in cycle 9's Softgile listing. Note: "
                              "English is the stated working-communication language here (not "
                              "German), so this listing does not actually test the unresolved "
                              "German-proficiency CONFLICT either way, despite being a genuine "
                              "German-market employer.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Upwork URL this cycle, found via a Brevo-specific search (not the "
                  "dedicated German-market search angle, which again found nothing -- see source "
                  "notes). The best-credentialed client found this cycle, but a clean multi-tool "
                  "reject. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=freelancer_id,
            title="Squarespace-Brevo Signup Integration (229 competing proposals, closes in 1 day)",
            client_name="Individual client, Melbourne, Australia (Freelancer.com; payment method "
                         "verified; 0.0 rating, 0 reviews; member since May 5, 2021)",
            url="https://www.freelancer.com/projects/api/squarespace-brevo-signup-integration",
            posted_at="Posted 6 days before this cycle's discovery; listing ends in 1 day",
            description="Connect a custom Squarespace signup form (email address only) to a single "
                        "Brevo mailing list in real time, via the Brevo API, a Squarespace code "
                        "injection, or a lightweight intermediary such as Zapier.",
            required_skills="Brevo API integration, Squarespace code injection/JavaScript, "
                             "optionally Zapier.",
            budget_amount=37.5, budget_currency="AUD", budget_type="hourly ($25-50 AUD/hour)",
            payment_platform="Freelancer.com (hourly; not independently tested for TRNC residents)",
            client_history="Member since May 5, 2021 (4+ years). Australia (Melbourne). 0.0 "
                            "rating, 0 reviews despite the long tenure -- payment method verified "
                            "but no completed-job track record visible.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="229 proposals already on record (average bid $34 AUD/hr) with the "
                              "listing closing within 1 day of this cycle's discovery -- an "
                              "extreme, effectively unwinnable competition signal regardless of "
                              "skill match. Also closer to a lightweight API/developer integration "
                              "task than an email-marketing strategy role.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com URL this cycle. Genuine Brevo scope, rejected purely "
                  "on competition volume and closing window. Logged for audit-trail completeness.",
        ),
        dict(
            source_id=freelancer_id,
            title="Urgent: Social Media & Email Marketing Expert (closed before discovery; "
                  "Mailchimp/Klaviyo also named)",
            client_name="Digital agency, Mohali, India (Freelancer.com; 0.0 rating, 0 reviews; "
                         "member since Jul 4, 2024)",
            url="https://www.freelancer.com/projects/email-marketing/urgent-social-media-email-marketing",
            posted_at="Posted 15 days before this cycle's discovery; closed",
            description="Combined social media marketing (Instagram/Facebook content, captions, "
                        "Canva/Photoshop creatives, Meta ad campaigns) and email marketing "
                        "(newsletters, offers, welcome/win-back flows using Mailchimp, Brevo, "
                        "Klaviyo or similar) for a digital agency's local-services clients.",
            required_skills="2+ years in SMM and email marketing; portfolio with BOTH social media "
                             "AND email campaign samples (mandatory); Mailchimp, Brevo, Klaviyo or "
                             "similar; Canva/Photoshop.",
            budget_amount=25000, budget_currency="INR", budget_type="fixed (INR12,500-37,500)",
            payment_platform="Freelancer.com (fixed-price, paid on delivery; not independently "
                              "tested for TRNC residents)",
            client_history="Member since Jul 4, 2024. India (Mohali). 0.0 rating, 0 reviews -- "
                            "unestablished account.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed -- posted 15 days before this cycle's discovery, 29 "
                              "proposals already on record. Would also have failed on scope even "
                              "if open: requires 2+ years' experience (exceeds this project's "
                              "~2-year job-search filter) and a mandatory social-media-management "
                              "portfolio Kaeto does not have, and names Mailchimp and Klaviyo as "
                              "acceptable tools alongside Brevo -- both explicitly PROHIBITED "
                              "unevidenced-tool claims. A multi-reason reject.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="New-to-file Freelancer.com URL this cycle. Already closed plus a multi-reason "
                  "scope mismatch. Logged for audit-trail completeness.",
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

    # Update the still-open P1 lead from cycles 5-9 with this cycle's quiet re-check. Per the
    # owner's standing instruction (flagged twice already, their call to act on), this is recorded
    # without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 10 (2026-11-20) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (5th consecutive "
              "cycle). Interviewing flat at 3 (3rd consecutive cycle with no movement, since "
              "cycle 7's 0->3 jump). Proposals still 20-50. Last viewed by client: '3 days ago' "
              "(vs '2 days ago' in cycle 9 -- ordinary noise). Client totals fully flat for the "
              "first time: $68K spent/35 hires/16 active/1,980 hours, identical to cycle 9 with "
              "zero movement on any metric. Nothing materially new; no action taken, no fresh "
              "flag raised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    # Quiet re-check note on the PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" lead from
    # cycle 8, re-checked again this cycle since it was re-scraped for completeness.
    brevo_crm_url = "https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/"
    existing_note_row2 = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (brevo_crm_url,)
    ).fetchone()
    if existing_note_row2:
        appended_note2 = (
            (existing_note_row2[0] or "")
            + " | Cycle 10 (2026-11-20) re-check: still open. Hourly rate now renders clearly "
              "($10-28/hr, consistent with the figure already on file). Client still 1 hire/1 "
              "active (no new hires). Interviewing moved 2->3, and invites-sent appeared for the "
              "first time (2 sent, 0 answered) -- the first sign of outbound client activity "
              "since discovery. Proposals still 20-50. Slightly more active than cycle 9's "
              "snapshot, but not enough to revise the tier: the client is still only ~10 days "
              "old with the same thin 1-hire history. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 9, len(opportunities), 0,
         "Cycle 10, the regular run following cycle 9 (2026-11-19). Followed up on all four "
         "carried-over open items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) "
         "rechecked once quietly -- still open, rate still unconfirmed (5th cycle), interviewing "
         "flat at 3 (3rd cycle unchanged), all client metrics fully flat for the first time -- not "
         "re-flagged per the owner's standing instruction. (b) Brevo CRM and Email Setup (id 40) "
         "rechecked -- still open, interviewing ticked up 2->3 with invites-sent appearing for the "
         "first time, tier not revised. (c) Reddit r/forhire: direct firecrawl_scrape attempted "
         "again, still blocked (5th consecutive cycle); the paid scrapecreators Alexandria "
         "provider was deliberately NOT used again pending the owner's go-ahead from cycle 7. (d) "
         "PeoplePerHour page 1 re-checked only -- one new-to-file URL found and rejected as stale. "
         "Fresh Brevo/generic searches across Upwork, Freelancer.com, Contra, Useme.com, "
         "German-market search and freelance.de found 8 new URLs total (1 PeoplePerHour, 5 "
         "Upwork, 2 Freelancer.com), all REJECTED for a mix of reasons: already-hired/filled, "
         "extreme proposal competition, required PROHIBITED tools (Apollo, Mailchimp, HubSpot, "
         "Klaviyo, Zapier/Make.com/N8N, Lemlist/Instantly/Expandi), an experience-floor mismatch "
         "(2-4 years vs ~10 months), a brand-new low-credibility client, and an already-closed "
         "listing. One listing (CRM and E-Mail Marketing Manager, Germany) was the most credible "
         "client found this cycle but still a clean multi-tool reject. Direct business "
         "prospecting (master prompt section 4.3/12) was not run this cycle, per the standing "
         "scope instruction. 0 new P0/P1 opportunities this cycle; no application package "
         "recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 10 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
