#!/usr/bin/env python3
"""Discovery cycle 16 (2026-11-26): regular run following cycle 15 (2026-11-25). Picks up cycle
15's open items: (a) one more quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork listing (id 31) -- still open, hourly rate still does not render (11th consecutive cycle).
Interviewing unchanged at 2, invites 0/0. Last viewed by client "2 days ago" (ordinary recency
noise vs "yesterday" last cycle). Account-level figures this cycle: $69K total spent (flat),
36 hires, 15 active (unchanged from cycle 15's settled value), hours rose again 2,020->2,026 --
consistent with ongoing work on this buyer's many other contracts, no new ambiguity. Noted on the
DB row only, not re-flagged, per the owner's standing instruction. (b) re-checked the
PAYMENT_TIMELINE_UNCERTAIN "Brevo CRM and Email Setup" listing (id 40) -- still at Interviewing=4,
now a 5TH consecutive cycle (12,13,14,15,16) with no further climb and no hire on this specific
listing. Invites-sent/unanswered unchanged at 2/0. The account-level active-hires figure that
dropped 1->0 last cycle HELD at 0 this cycle (no further change), total spent still flat at $15 --
this stability is itself informative: nothing on this listing or its buyer account has moved in
either direction for two consecutive cycles now. Noted, not re-flagged; tier not revised. (c)
Reddit r/forhire: direct firecrawl_scrape attempted again (no paid scrapecreators Alexandria
provider used without the owner's go-ahead, open since cycle 7) -- failed identically, the 11th
consecutive cycle blocked on the free method. (d) PeoplePerHour page 1 re-check only -- found one
genuinely new, in-scope listing this cycle ("Markerters wanted for sale of products email
campaigns", $175, 26 proposals) and logged it as a full DB row (REJECTED on compensation +
zero-track-record client + undefined multi-niche scope), breaking several cycles of in-scope
PeoplePerHour finds being nil; the recurring out-of-scope items persist unchanged in substance
(Dubai B2B cold-email lead-gen now 4 days/24 proposals, the VO-artist B2B lead-gen listing now 2
days/30 proposals, plus a new out-of-scope lead-gen/ads role requiring Instantly.ai and Meta
Ads -- all read but not logged, consistent with the project's scope standard). (e) Contra (16th
consecutive cycle, same id-19 card plus the same two recurring non-Brevo listings, no new genuine
lead), the German-market search (16th consecutive cycle -- the freiguide.de-mirrored
Kleinanzeigen.de "BREVO Newsletter einrichten" ad was checked again: still already removed on
Kleinanzeigen.de directly ("Die gewuenschte Anzeige ist nicht mehr verfuegbar"), now the THIRD
consecutive cycle this exact dead-mirror pattern has occurred -- per the owner's instruction this
is now called CONFIRMED STRUCTURAL rather than described as a fresh finding), and freelance.de
(10th consecutive cycle confirming no reachable client-posting section, only directory pages) were
all checked again, kept brief as instructed. Useme.com (English page 1): a notable change this
cycle -- every listing on the category page now shows status "Finished" (20 closed jobs spanning
Mailchimp/GetResponse/Klaviyo/MailerLite/Edrone/Snov.io), and the long-running Oliver Tornroth/
Zoined posting that had persisted as the sole open listing across cycles 7-15 is no longer present
at all -- ordinary listing turnover, not a system failure, but the first time in 9 cycles this
specific listing has changed state; no live Brevo listing either way. Fresh Brevo-specific and
generic searches across Upwork, Freelancer.com, and (new this cycle) Guru.com surfaced 6
new-to-file candidates, all REJECTED: five Upwork listings in the deliverability/email-marketing-
specialist space (two already showing a "Hires" field, i.e. functionally closed/filled; one
requiring GoHighLevel, an unevidenced platform; one from a zero-track-record agency with no budget
disclosed; one requiring Shopify e-commerce revenue-growth experience not in the claims register,
with heavy competition) and one new-to-project source, Guru.com, surfacing a Brevo CRM automation
job whose Phase 2 earning path requires the freelancer's own cold-email sending infrastructure
(10+ inboxes) -- unevidenced and not something the project can credibly claim. Freelancer.com's
own search surfaced only already-on-file Brevo listings plus one decade-old cancelled project
(pure search noise, not logged). 0 new P0/P1 opportunities this cycle; no application package
recommended. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on url). See
reports/2026-11-26-discovery-cycle-16.md for the full narrative."""
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
        "quiet status check. Still open. Rate still does not render (11th consecutive cycle). "
        "Interviewing unchanged at 2, invites 0/0. Active contracts held at 15, total spent flat "
        "at $69K, hours rose again 2,020->2,026 -- ordinary continued activity on this buyer's "
        "other contracts, nothing new to flag. Also re-checked the PAYMENT_TIMELINE_UNCERTAIN "
        "'Brevo CRM and Email Setup' listing (id 40): still at Interviewing=4, now a 5TH "
        "consecutive cycle with no further climb and no hire on this listing. The account-level "
        "active-hires figure that dropped 1->0 last cycle HELD at 0 this cycle (no further "
        "movement either way), total spent still flat at $15. Tier not revised. Fresh "
        "Brevo-specific and generic searches surfaced 5 new-to-file Upwork URLs this cycle, all "
        "REJECTED (see opportunities below): two already show a job-specific 'Hires' field "
        "(functionally closed/filled despite still being publicly listed), one requires "
        "GoHighLevel (unevidenced platform) and is also already at Hires:2, one is from a "
        "zero-track-record new agency with no budget disclosed, and one requires Shopify "
        "e-commerce revenue-growth experience not in the claims register under heavy competition "
        "(50+ proposals, 4 interviewing, 7 invites sent). A further hit ('Cold Email "
        "Deliverability Specialist Needed') was found already removed ('This job is no longer "
        "available') and a separate hit ('Marketing Email Outreach Infrastructure') was read but "
        "not logged -- cold-email domain-warming infrastructure work, not a platform-operation "
        "skill match, consistent with the project's treatment of cold-outreach-infrastructure "
        "roles as out of scope.",
        discovery_count=5, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 11 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Direct firecrawl_scrape attempted again this cycle against the subreddit listing page, as "
        "instructed. Failed identically: 'Firecrawl can't scrape this site because it is currently "
        "not supported.' 11th consecutive cycle failing on the free method. Per instruction, did "
        "NOT fall back to the paid scrapecreators Alexandria provider this cycle -- still awaiting "
        "the owner's go-ahead from cycle 7. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-15's finding. One genuinely new, in-scope listing "
        "this cycle: 'Markerters wanted for sale of products email campaigns' ($175, 26 proposals, "
        "0%-rating/0-projects-completed client) -- logged as a full DB row and REJECTED (budget, "
        "zero client track record, undefined multi-niche scope), the first in-scope PeoplePerHour "
        "find logged in many cycles. The same recurring out-of-scope postings persist in substance "
        "('Cold Email Marketing Specialist', the Dubai B2B tax-consultancy cold-outreach role, now "
        "aged to 4 days/24 proposals; 'B2B Lead Generation & Email Outreach for Established VO "
        "Artist', now 2 days/30 proposals), joined by a new out-of-scope listing this cycle ('I "
        "need an outreach marketing professional', requiring Instantly.ai and Meta Ads) -- all "
        "read but not logged, no Brevo or email-marketing-platform skill involved.",
        discovery_count=1, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific and generic searches surfaced no new-to-file LIVE Freelancer.com "
        "URLs this cycle -- every Brevo-specific hit returned was already on file from a prior "
        "cycle, plus one decade-old, long-since-cancelled project ('Mailing to 400000 emails', "
        "posted ~10 years ago, Cancelled) that surfaced as pure search noise and was not logged.",
        discovery_count=0, qualified_count=0,
    )
    guru_id = get_or_create_source(
        conn, "Guru.com", "https://www.guru.com/jobs/brevo-crm-automation-b2b-cold-email/2121953",
        "firecrawl_search + firecrawl_scrape of individual job listing pages, no login",
        "New source touched for the first time this cycle, surfaced by a Brevo-specific search. "
        "One listing found and logged: 'Brevo CRM Automation + B2B Cold Email Lead Generation' -- "
        "Phase 1 is genuine Brevo CRM/automation setup work ($100 fixed fee), but Phase 2's "
        "performance-pay earning path explicitly requires the freelancer's own cold-email sending "
        "infrastructure (10+ inboxes) and the application itself gates on answering cold-email "
        "infrastructure questions -- unevidenced per the claims register. REJECTED on compensation "
        "and the unevidenced Phase 2 requirement. Worth keeping on the source list for future "
        "cycles given it is a live, Brevo-relevant freelance marketplace not previously checked.",
        discovery_count=1, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages; firecrawl_scrape "
        "of the featured-jobs landing page",
        "16th consecutive cycle with the same structural limitation. A direct scrape of the "
        "featured-jobs landing page again rendered the same 'Email Marketing Specialist - Dual "
        "Campaigns for Parents & School Leaders' card already on file (id 19, $25-40/hr), plus the "
        "same two recurring non-Brevo, non-email-platform listings ('Marketing Assistant for "
        "Launch Campaign', 'Prepping Digital Assets Before Launching Campaigns') -- still never a "
        "genuine NEW client email-marketing posting across 16 cycles.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- 16th consecutive cycle with no live, actionable "
        "German-market email-marketing-specialist opening. The same freiguide.de-mirrored "
        "Kleinanzeigen.de classified titled 'BREVO Newsletter einrichten' surfaced again; checking "
        "the original Kleinanzeigen.de URL directly (https://www.kleinanzeigen.de/s-anzeige/"
        "brevo-newsletter-einrichten/2736294866-298-3833) again returned 'Die gewuenschte Anzeige "
        "ist nicht mehr verfuegbar' (ad no longer available), with the category listing page "
        "showing only unrelated Dresden-area service ads. This is now the THIRD consecutive cycle "
        "this exact dead-mirror pattern has occurred (cycles 14, 15, 16) -- per the owner's "
        "instruction this is now treated as CONFIRMED STRUCTURAL (freiguide.de's index "
        "structurally lags behind Kleinanzeigen.de's live removals) rather than being re-described "
        "as a fresh finding each cycle. German-proficiency claims-register conflict remains "
        "untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 only this cycle)",
        "Re-checked page 1 (English) only this cycle. Notable change: every one of the 20 listed "
        "jobs now shows status 'Finished' (spanning Mailchimp, GetResponse, Klaviyo, MailerLite, "
        "Edrone, Snov.io work) -- the long-running Oliver Tornroth/Zoined posting that had been "
        "the sole open listing across cycles 7-15 (last seen with 17 days left in cycle 15) is no "
        "longer present on the page at all. Read as ordinary listing turnover/expiry, not a "
        "scraping failure -- the page rendered correctly and shows real (closed) job data -- but "
        "it is the first state change on this specific listing in 9 cycles. Still zero live Brevo "
        "listings either way. Polish page 2 not re-checked this cycle.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried the same dedicated search again, aimed specifically at a client project/Auftrag "
        "posting. Surfaced only freelancer profile/directory pages (Brevo-Freelancer finden, plus "
        "a freelancerteam.de referral-tool hit and a Fiverr gig directory), no client project "
        "listing at all. 10th consecutive cycle confirming no client project-posting section is "
        "reachable for this platform via search.",
        discovery_count=0, qualified_count=0,
    )
    indeed_health_id = get_or_create_source(
        conn, "Indeed / general search, health-wellness + Brevo angle", "https://www.indeed.com",
        "firecrawl_search combining the health/wellness niche with Brevo-specific terms",
        "Not re-run as a dedicated search this cycle, consistent with cycles 13-15's treatment; "
        "prior cycles' finding (general tutorial/comparison content, no live candidate) assumed "
        "unchanged.",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Deliverability Specialist for CRM",
            client_name="Individual/small client, San Agustin de Guadalix, Spain (Upwork; member "
                         "since Jun 11, 2023, $300 total spent, 3 hires, 1 active)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Deliverability-Specialist-for-CRM_~022120888823289404355/",
            posted_at="Duration tag 'Less than 1 month', one-time project; last viewed by client "
                      "6 days before this cycle's discovery; exact posting date not shown",
            description="Review and improve email deliverability within the client's own CRM: "
                        "analyze current processes and email performance, identify inbox-placement "
                        "issues, and implement fixes. Spanish speaking is a plus.",
            required_skills="Email Marketing, Email Communication, Customer Relationship "
                             "Management, Email Support -- generic deliverability troubleshooting, "
                             "no specific platform named.",
            budget_amount=19.0, budget_currency="USD", budget_type="hourly ($10.00-$28.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents, per "
                              "evidence/payment-routing.md)",
            client_history="Small but real, verified client: member since 2023, $300 total spent, "
                            "3 hires, 1 active contract.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="The job's own activity data shows 'Hires: 1' already recorded "
                              "against this specific listing, with Interviewing now at 0 and only "
                              "1 invite sent (unanswered) -- this listing is functionally closed/"
                              "filled even though it remains publicly viewable. A fresh proposal "
                              "now would be applying to a job that has already been awarded.",
            est_days_to_accessible_payment=None,
            score_probability_win=1, score_time_to_payment=5, score_skill_match=8,
            score_payment_certainty=6, score_compensation=4, score_client_credibility=4,
            score_repeat_potential=1, score_total=29,
            score_rationale="Decent generic deliverability skill match and a real small client, "
                            "but the job-specific Hires:1 field is decisive -- this is a closed "
                            "listing, not an open one, regardless of the other scores.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: a "
                  "listing that looks open on first glance but whose own activity panel shows it "
                  "already filled.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Deliverability & Domain Reputation Expert",
            client_name="Established client, Vestaburg, United States (Upwork; member since Jan "
                         "23, 2018, $218K total spent, 228 hires, 44 active, 14,962 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Deliverability-Domain-Reputation-Expert_~022120479753175742536/",
            posted_at="Duration '1-3 months', ongoing project; last viewed by client last week; "
                      "exact posting date not shown",
            description="Audit email and domain reputation, identify issues, and implement fixes "
                        "to improve deliverability, with hands-on technical review, reputation "
                        "remediation, and team guidance on best practices.",
            required_skills="Email Marketing, Email Deliverability, Email Support, Email "
                             "Communication -- squarely the project's strongest documented skill "
                             "area (deliverability/SPF/DKIM/DMARC-adjacent audit work), no "
                             "specific platform named.",
            budget_amount=29.0, budget_currency="USD", budget_type="hourly ($8.00-$50.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Extremely well-established client: member since 2018, $218K total "
                            "spent, 228 hires, 44 active contracts, 14,962 hours logged -- very "
                            "high credibility, no trust concern whatsoever.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="The strongest skill match of this cycle's new finds (pure "
                              "deliverability/domain-reputation audit work, the project's best-"
                              "documented area) and an exceptionally credible client -- but, per "
                              "the owner's standing instruction against rounding up marginal "
                              "matches on competition alone, the hiring funnel is already far "
                              "advanced: 50+ proposals, 9 candidates already Interviewing, and 9 "
                              "invites already sent (1 still unanswered). A fresh proposal now "
                              "would be a very late, low-probability bid.",
            est_days_to_accessible_payment=None,
            score_probability_win=2, score_time_to_payment=5, score_skill_match=13,
            score_payment_certainty=9, score_compensation=6, score_client_credibility=10,
            score_repeat_potential=3, score_total=48,
            score_rationale="Near-ceiling skill match and client-credibility scores, dragged down "
                            "entirely by probability-of-win -- the same pattern as cycle 15's "
                            "'Email Deliverability Specialist' reject, repeated with an even "
                            "stronger funnel already in place (9 interviewing vs 3).",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: the "
                  "cycle's best skill match, rejected purely on competition timing.",
        ),
        dict(
            source_id=upwork_id,
            title="Senior Email Marketing & Deliverability Expert",
            client_name="Mid-sized education company (10-99 people), Hong Kong (Upwork; member "
                         "since Aug 30, 2022, $346K total spent, 106 hires, 24 active, 8,841 "
                         "hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Senior-Email-Marketing-Deliverability-Expert_~022109576004451987288/",
            posted_at="Duration '1-3 months', ongoing project; last viewed by client 2 weeks "
                      "before this cycle's discovery",
            description="Investigate and improve email performance for an established online "
                        "education business sending a large volume of emails through "
                        "GoHighLevel; review setup, identify root causes (not assumed to be "
                        "deliverability alone), and recommend fixes, starting with a smaller paid "
                        "project before a more extensive engagement.",
            required_skills="Email Deliverability, Email Marketing Tools, Email Marketing "
                             "Services; explicitly names GoHighLevel, with experience on that "
                             "platform called out as an advantage.",
            budget_amount=85.0, budget_currency="USD", budget_type="hourly ($50.00-$120.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Very well-established client: member since 2022, $346K total spent, "
                            "106 hires, 24 active contracts, 8,841 hours -- high credibility.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Two independent reject grounds: (1) the job's own activity panel "
                              "already shows 'Hires: 2' with 6 still Interviewing -- this listing "
                              "is functionally filled even though visible; (2) the platform named, "
                              "GoHighLevel, is not in the claims register at all (Brevo is the "
                              "project's only evidenced platform), so even absent the closure "
                              "signal this would be a platform-mismatch reject under the owner's "
                              "rule against claiming unevidenced tools.",
            est_days_to_accessible_payment=None,
            score_probability_win=1, score_time_to_payment=4, score_skill_match=6,
            score_payment_certainty=8, score_compensation=7, score_client_credibility=9,
            score_repeat_potential=2, score_total=37,
            score_rationale="High rate and strong client credibility, but a double reject: "
                            "already hired on this specific listing, and the named platform "
                            "(GoHighLevel) has no evidentiary support in the claims register.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: "
                  "closed-in-practice listing plus an unevidenced-platform requirement.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist | Domain Safety & Deliverability Experience "
                  "Required",
            client_name="Finish Green, a business solutions agency, New Kent, United States "
                         "(Upwork; member since Sep 10, 2026 -- brand new, no total-spent or "
                         "hires figures shown at all)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist-Domain-Safety-Deliverability-Experience-Required_~022110770815249119975/",
            posted_at="Duration '1-3 months', ongoing project; last viewed by client 4 weeks "
                      "before this cycle's discovery",
            description="Agency seeking an email marketing specialist for client projects: set up "
                        "email marketing systems, configure SPF/DKIM/DMARC/DNS records, ensure "
                        "domain authentication and safe sending, set up campaigns/automations, "
                        "manage contact lists, monitor deliverability/bounce/spam complaints, "
                        "troubleshoot issues. Fluent English required.",
            required_skills="Email Deliverability, Email Marketing Strategy, Email Marketing "
                             "Tools, Email Campaign Setup, Email Marketing Services -- no specific "
                             "platform named, generic deliverability/authentication skills "
                             "requested (good overlap with the project's strongest documented "
                             "area).",
            budget_amount=None, budget_currency="USD", budget_type="hourly (not disclosed in the "
                           "public listing)",
            payment_platform="Upwork (hourly, rate not shown; not independently tested for TRNC "
                              "residents)",
            client_history="Brand-new agency account (member since Sep 10, 2026, ~2.5 months old "
                            "at discovery), no total-spent or hires data displayed at all -- zero "
                            "verified track record.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Genuine skill-area overlap (SPF/DKIM/DMARC, domain reputation, "
                              "deliverability monitoring -- no prohibited tool required), but "
                              "three compounding concerns: no budget disclosed at all (fails the "
                              "compensation/payment-horizon test outright, since it cannot be "
                              "evaluated), zero client track record (brand-new agency, no spend or "
                              "hire history to assess reliability against), and the hiring funnel "
                              "is already at 5 Interviewing with 1 invite sent.",
            est_days_to_accessible_payment=None,
            score_probability_win=3, score_time_to_payment=5, score_skill_match=11,
            score_payment_certainty=3, score_compensation=2, score_client_credibility=2,
            score_repeat_potential=2, score_total=28,
            score_rationale="Good skill overlap offset by an undisclosed rate and a zero-history "
                            "client -- the compensation and credibility axes carry too much "
                            "uncertainty to qualify despite the otherwise reasonable fit.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: a "
                  "skill-area match let down by missing compensation data and no client history.",
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist",
            client_name="Livable Hair, small e-commerce company (2-9 people), Foothills, Canada "
                         "(Upwork; member since Oct 24, 2024, $15K total spent, 11 hires, 8 "
                         "active, 436 hours)",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist_~022123606161787904455/",
            posted_at="Duration '1-3 months', ongoing project; last viewed by client 2 days "
                      "before this cycle's discovery",
            description="Senior email marketing strategist for an e-commerce brand launch: own "
                        "strategy and execution, write campaign copy, build and optimize "
                        "automated flows (welcome, abandoned checkout, post-purchase, win-back), "
                        "segment audiences, test and report on revenue/conversions.",
            required_skills="Email Marketing, Internet Marketing, Email Communication, Marketing "
                             "Strategy; requires 'proven experience growing email revenue for "
                             "e-commerce brands' and 'experience with Shopify and email marketing "
                             "platforms' -- Shopify/e-commerce revenue track record is not in the "
                             "claims register, and no specific email platform (Brevo or "
                             "otherwise) is named.",
            budget_amount=70.0, budget_currency="USD", budget_type="hourly ($20.00-$120.00/hr)",
            payment_platform="Upwork (hourly; not independently tested for TRNC residents)",
            client_history="Established small client: member since 2024, $15K total spent, 11 "
                            "hires, 8 active contracts, 436 hours -- credible, no trust concern.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="No Brevo or other named platform (so no PROHIBITED-tool conflict), "
                              "but the role explicitly wants proven e-commerce email-revenue "
                              "growth and Shopify experience, neither of which the claims register "
                              "supports -- HIBARR experience is B2B financial-advisory email "
                              "marketing, not e-commerce flow revenue attribution. Combined with "
                              "heavy competition (50+ proposals, 4 already Interviewing, 7 invites "
                              "sent with 3 unanswered), this is a skill-mismatch-plus-competition "
                              "reject.",
            est_days_to_accessible_payment=None,
            score_probability_win=2, score_time_to_payment=5, score_skill_match=5,
            score_payment_certainty=7, score_compensation=6, score_client_credibility=6,
            score_repeat_potential=2, score_total=33,
            score_rationale="A credible client and a reasonable rate are offset by a weak skill "
                            "match -- the role wants e-commerce/Shopify revenue-growth experience "
                            "the project does not have evidence for -- and an already-advanced "
                            "competitive funnel.",
            status="open",
            notes="New-to-file Upwork URL this cycle. Logged for audit-trail completeness: "
                  "skill-mismatch (Shopify/e-commerce revenue growth) plus competition reject.",
        ),
        dict(
            source_id=guru_id,
            title="Brevo CRM Automation + B2B Cold Email Lead Generation",
            client_name="Individual/small consulting client, United States (Guru.com; no visible "
                         "spend or hire history in the public listing)",
            url="https://www.guru.com/jobs/brevo-crm-automation-b2b-cold-email/2121953",
            posted_at="Exact posting date not shown in the public scrape; nearby similar listings "
                      "on the same category page are dated November 8-20, 2026, suggesting a "
                      "recent posting",
            description="Phase 1 ($100 fixed fee): integrate Calendly Free and Acuity Scheduling "
                        "Paid with Brevo Free without paid middleware, upload and automate ~20 "
                        "lead-nurturing emails plus ~10 pre-meeting and ~20 post-meeting follow-up "
                        "emails, set up CRM pipeline stages/segmentation/triggers, test "
                        "everything. Phase 2 ($1,000 per 20 attended B2B appointments, "
                        "performance-based): use the freelancer's OWN cold-email platforms, "
                        "prospecting tools, and sending infrastructure (client explicitly asks "
                        "whether the applicant has '10+ email inboxes') to generate and book "
                        "qualified B2B sales appointments.",
            required_skills="Brevo, CRM Automation, Webhook Integration, Marketing Automation "
                             "(Phase 1 -- genuine overlap with the project's strongest documented "
                             "platform); Cold Email Marketing, Customer Acquisition, Lead "
                             "Generation, and owned cold-email sending infrastructure (Phase 2 -- "
                             "not in the claims register, and the application itself requires "
                             "confirming interest in and capability for both phases).",
            budget_amount=100.0, budget_currency="USD", budget_type="fixed price (Phase 1, "
                           "$100.00) plus uncapped performance pay (Phase 2, contingent on "
                           "unevidenced capability)",
            payment_platform="Guru.com (fixed-price escrow; not previously used by this project, "
                              "not independently tested for TRNC residents)",
            client_history="No total-spent, hires, or rating data visible in the public listing -- "
                            "zero verified track record on this specific marketplace.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Phase 1 is a genuine Brevo CRM/automation task the project's "
                              "documented skills cover well, but $100 fixed for that scope "
                              "(integrations, 40+ templated/triggered emails, pipeline setup, "
                              "testing) is low pay for the work described. More decisively, the "
                              "client wants a freelancer who can execute both phases and the "
                              "application itself requires answering detailed questions about "
                              "owned cold-email sending infrastructure and B2B appointment-setting "
                              "track record -- capabilities not in evidence per "
                              "evidence/claims-register.md. Taking Phase 1 alone while being "
                              "unable to credibly answer the Phase 2 screening questions is not a "
                              "clean path in. Client credibility on this new-to-project platform "
                              "is also unverified.",
            est_days_to_accessible_payment=None,
            score_probability_win=4, score_time_to_payment=10, score_skill_match=6,
            score_payment_certainty=3, score_compensation=2, score_client_credibility=3,
            score_repeat_potential=2, score_total=30,
            score_rationale="A real Brevo-skill overlap in Phase 1 is outweighed by low fixed "
                            "pay for that scope and a Phase 2 requirement (owned cold-email "
                            "infrastructure) the project cannot credibly claim, on a marketplace "
                            "whose client credibility and payment protection are both unverified "
                            "for this project.",
            status="open",
            notes="First listing logged from Guru.com, a source newly added this cycle. Kept on "
                  "the source list for future cycles as a live, Brevo-relevant marketplace not "
                  "previously checked.",
        ),
        dict(
            source_id=pph_id,
            title="Markerters wanted for sale of products email campaigns thank u",
            client_name="Individual client (Steve K.), Australia (PeoplePerHour; 0% rating, 0 "
                         "projects completed, 0 freelancers worked with -- brand-new buyer "
                         "account, last active 26 Nov 2026)",
            url="https://www.peopleperhour.com/freelance-jobs/marketing-branding-sales/direct-marketers/markerters-wanted-for-sale-of-products-email-campaigns-than-4531119",
            posted_at="Posted approximately 11 days before this cycle's discovery; 26 proposals "
                      "at time of discovery",
            description="Seeking an experienced email marketing specialist to develop and manage "
                        "campaigns across several landing pages and websites spanning beauty and "
                        "wellness, real estate investment, business coaching, and consumer "
                        "products (including mopeds). Scope may include campaign strategy, "
                        "persuasive copywriting, audience segmentation, email automation, and "
                        "performance tracking. Clarification-board Q&A shows the client has not "
                        "yet decided whether the sites already have an email platform and "
                        "subscriber lists, or whether setup from scratch is also in scope.",
            required_skills="Email marketing strategy, copywriting, segmentation, automation, "
                             "performance tracking -- no specific platform named, so no "
                             "PROHIBITED-tool conflict, but the scope spans four unrelated "
                             "business verticals for one buyer with no track record.",
            budget_amount=175.0, budget_currency="USD", budget_type="fixed price ($175.00, scope "
                           "and ongoing-vs-one-time status undefined pending clarification)",
            payment_platform="PeoplePerHour (escrow exists, but not independently tested for TRNC "
                              "residents)",
            client_history="Brand-new buyer account: 0% rating, 0 projects completed, 0 "
                            "freelancers worked with -- no track record at all to assess "
                            "reliability or payment follow-through against.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="No prohibited-tool conflict and a nominally in-scope skill ask, but "
                              "three compounding problems: (1) compensation -- $175 for ongoing "
                              "multi-website, multi-vertical campaign management (beauty/wellness, "
                              "real estate investment, business coaching, consumer products) is "
                              "not viable for the scope described; (2) client credibility -- a "
                              "zero-history buyer account with no completed projects or ratings; "
                              "(3) scope clarity -- even the client's own clarification-board "
                              "answers show the basic setup-vs-existing-platform question is still "
                              "unresolved, meaning the real scope could be far larger than the "
                              "posted budget implies.",
            est_days_to_accessible_payment=None,
            score_probability_win=3, score_time_to_payment=8, score_skill_match=7,
            score_payment_certainty=2, score_compensation=2, score_client_credibility=1,
            score_repeat_potential=2, score_total=25,
            score_rationale="A nominally in-scope, no-prohibited-tool listing let down by the "
                            "weakest client-credibility score of the cycle (zero track record) "
                            "and compensation that does not match the described multi-vertical "
                            "scope.",
            status="open",
            notes="New-to-file PeoplePerHour URL this cycle, the first in-scope listing logged "
                  "from this source in several cycles.",
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

    # Quiet re-check note on the still-open P1 lead from cycles 5-15. Per the owner's standing
    # instruction, recorded without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 16 (2026-11-26) quiet re-check (per owner's standing instruction, not "
              "re-flagged): still open. Hourly rate still does not render (11th consecutive "
              "cycle). Interviewing unchanged at 2, invites 0/0. Last viewed by client '2 days "
              "ago' (ordinary recency noise). Active contracts held at 15 (unchanged from cycle "
              "15's settled value), total spent flat at $69K, 36 hires on file, hours rose again "
              "2,020->2,026 -- ordinary continued activity on this buyer's other contracts. "
              "Nothing new to flag."
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
            + " | Cycle 16 (2026-11-26) re-check: still open. Rate still $10-28/hr. Interviewing "
              "STILL at 4 -- now a 5TH consecutive cycle (12,13,14,15,16) with no further climb "
              "and still no hire appearing on this specific listing. Invites-sent/unanswered "
              "unchanged at 2/0. The account-level active-hires figure that dropped 1->0 last "
              "cycle HELD at 0 this cycle (no further movement), total spent still flat at $15 -- "
              "two consecutive cycles of total stability on both the listing and its buyer "
              "account. Noted, not treated as closure. Tier not revised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note2, NOW, brevo_crm_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 11, len(opportunities), 0,
         "Cycle 16, the regular run following cycle 15 (2026-11-25). Followed up on all open "
         "items: (a) Newsletter Specialist for Campaigns / Brevo (id 31) rechecked once quietly -- "
         "still open, rate still unconfirmed (11th cycle), nothing new, noted only. (b) Brevo CRM "
         "and Email Setup (id 40) rechecked closely as instructed -- STILL stalled at "
         "Interviewing=4 for a 5TH consecutive cycle, and the account-level active-hires dip noted "
         "last cycle has now HELD at 0 for a second cycle, i.e. total stability rather than fresh "
         "movement; not closed, tier not revised. (c) Reddit r/forhire: direct firecrawl_scrape "
         "attempted again -- blocked identically (11th consecutive cycle); the paid scrapecreators "
         "Alexandria provider was deliberately NOT used again pending the owner's go-ahead from "
         "cycle 7. (d) PeoplePerHour page 1 re-checked only -- found and logged one genuinely new, "
         "in-scope listing this cycle (REJECTED on compensation/credibility/scope-clarity), the "
         "first in several cycles; recurring out-of-scope postings persist, joined by one new "
         "out-of-scope lead-gen/ads role. (e) Contra (16th consecutive cycle, no new genuine "
         "lead), the German-market search (16th consecutive cycle -- the freiguide.de/"
         "Kleinanzeigen.de dead-mirror pattern recurred for a THIRD time and is now treated as "
         "CONFIRMED STRUCTURAL per the owner's instruction, rather than re-described as new), and "
         "freelance.de (10th consecutive cycle confirming no reachable client-posting section) "
         "were checked again briefly per instruction. Useme.com showed a notable change: the "
         "long-running sole-open Oliver Tornroth/Zoined listing (open since cycle 7) is gone, "
         "every listing on the page now reads Finished -- ordinary turnover, no live Brevo "
         "listing either way. Fresh Brevo/generic searches across Upwork, Freelancer.com, and a "
         "newly-touched source (Guru.com) found 6 new-to-file candidates this cycle, 5 on Upwork "
         "and 1 on Guru.com plus 1 on PeoplePerHour (7 total), ALL REJECTED: two Upwork listings "
         "already show a job-specific Hires field (functionally closed/filled despite being "
         "publicly visible), one requires GoHighLevel (an unevidenced platform) and is also "
         "already hired, one is from a zero-track-record new agency with no budget disclosed, one "
         "requires Shopify e-commerce revenue-growth experience not in the claims register under "
         "heavy competition, the new Guru.com listing's genuine Brevo Phase-1 work is undercut by "
         "low fixed pay and a Phase-2 requirement for owned cold-email sending infrastructure the "
         "project cannot credibly claim, and the PeoplePerHour listing combines low budget with a "
         "zero-history client and an unresolved scope question. A further Upwork hit ('Cold Email "
         "Deliverability Specialist Needed') was found already removed from the platform, and "
         "another ('Marketing Email Outreach Infrastructure') was read but not logged as "
         "cold-email domain-warming infrastructure work, out of scope. Freelancer.com's search "
         "surfaced only already-on-file listings plus one decade-old cancelled project (pure "
         "search noise, not logged). Direct business prospecting (master prompt section 4.3/12) "
         "was not run this cycle, per the standing scope instruction. 0 new P0/P1 opportunities "
         "this cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 16 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
