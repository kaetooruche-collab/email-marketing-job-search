#!/usr/bin/env python3
"""Discovery cycle 4 (2026-11-01): Brevo-focused + generic email marketing freelancer search,
rotating through cycle 3's gap notes (Freelancer.com individual listings instead of category pages,
Reddit r/forhire individual-thread re-check, Contra re-check) plus Upwork/PeoplePerHour generic
"email marketing specialist" terms and a re-check of the cycle-3 discounted P1 lead. Appends to the
same DB. Safe to re-run (INSERT OR IGNORE on url). See reports/2026-11-01-discovery-cycle-4.md for
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
        "Full proposal submission requires an Upwork account and login.",
        discovery_count=5, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-email-marketing-jobs",
        "firecrawl_search + firecrawl_scrape of individual job pages and the category listing page",
        "Category listing page IS scrapable here (unlike Upwork's), gives posted-date/proposal-count for "
        "many jobs at once; individual pages add full description + clarification board history.",
        discovery_count=2, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_scrape of individual project page (category pages too large to scrape in one call)",
        "Confirmed again this cycle: individual project pages scrape fine; every Brevo-specific listing "
        "found this cycle was already 'Closed' (posted 1 month to ~2 years ago) with 14-138 proposals at "
        "very low day-rate bids (EUR 12-30/hr typical) -- this platform is now showing a consistent pattern "
        "of stale/closed Brevo listings across 3 consecutive cycles checked here.",
        discovery_count=3, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/freelancer pages",
        "No new distinct per-job listing surfaced this cycle beyond the one already logged and rejected "
        "in cycle 3 (unverifiable, no posted date/applicant/client data). Contra continues to expose no "
        "scorable listing data from its public pages.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_search only; firecrawl_scrape refuses reddit.com directly",
        "Confirmed blocked for a FOURTH consecutive cycle: firecrawl_scrape returns "
        "'we do not support this site' for reddit.com. Structural platform restriction, not a one-off.",
        last_error="firecrawl_scrape: 'we do not support this site' for reddit.com",
        discovery_count=0, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist",
            client_name="Unnamed, Canada",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist_~022098500703821937253/",
            posted_at="Not shown explicitly; last viewed by client 3 weeks ago",
            description="Generic email marketing specialist role: manage email lists, create content, "
                        "support outreach to attract new subscribers, improve open/click-through rates, "
                        "maintain consistent email presence. Part-time, 6+ months, contract-to-hire.",
            required_skills="Email marketing, audience growth, campaign performance. No specific platform named.",
            budget_amount=35, budget_currency="USD", budget_type="hourly ($12-$35/hr range, Intermediate)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Oct 31, 2018, Canada. No spend/hires figures shown in this scrape.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Oversaturated and stale for an unscored client -- 20-50 proposals already, "
                              "5 interviewing, and the client last reviewed applicants 3 weeks ago (long gap "
                              "suggesting slow or stalled hiring). No named platform to differentiate on, and "
                              "the listing explicitly wants 'improve open and click-through rates' as a "
                              "deliverable -- the claims register flags open/click rates as restricted "
                              "(below benchmark), so this would require volunteering a weak metric as a "
                              "headline promise. Competition too high and signal too stale to justify a bid.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Email Marketing Specialist Needed",
            client_name="Unnamed, United Kingdom",
            url="https://www.upwork.com/freelance-jobs/apply/Email-Marketing-Specialist-Needed_~022115246019939602740/",
            posted_at="Not shown; client joined Oct 27, 2026 (5 days before discovery), last viewed yesterday",
            description="Manage and improve email marketing: create campaigns, improve open/click-through "
                        "rates, grow email list. 1-3 months. No named platform.",
            required_skills="Email marketing (generic, no platform named).",
            budget_amount=15, budget_currency="USD", budget_type="hourly ($8-$15/hr range, Intermediate)",
            payment_platform="Upwork (hourly)",
            client_history="Member since Oct 27, 2026 (brand new account, 5 days old at discovery) -- no "
                            "spend history, no prior hires shown. Cannot assess credibility.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Brand-new, unverifiable client (account 5 days old, zero spend history) paired "
                              "with a low $8-15/hr rate and already 20-50 competing proposals despite the "
                              "account's youth -- high risk, low compensation, no credibility signal to offset "
                              "either. Same pattern as prior-cycle low-budget rejects.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Ads marketing, digital skills, email marketing",
            client_name="Unnamed, India",
            url="https://www.upwork.com/freelance-jobs/apply/Ads-marketing-digital-skills-email-marketing_~022105571537136376264/",
            posted_at="2026-10-01 (1 month before discovery); last viewed by client 4 weeks ago",
            description="Vague scope: 'We have to start the digital marketing like email marketing, ads "
                        "marketing etc.' $1,000 fixed price, Intermediate, contract-to-hire.",
            required_skills="Email marketing plus paid ads marketing (broad, undefined).",
            budget_amount=1000, budget_currency="USD", budget_type="fixed",
            payment_platform="Upwork escrow",
            client_history="Member since Sep 30, 2026 (joined 1 day before posting this job) -- brand new, "
                            "no spend history.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Stale (client has not reviewed applicants in 4 weeks despite the job staying "
                              "open -- a sign of an inactive or abandoned posting) and scope bundles paid ads "
                              "marketing, which is explicitly not demonstrated per the claims register ('paid "
                              "ads... none demonstrated, don't claim'). Brand-new, unverifiable client compounds "
                              "the risk.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=upwork_id,
            title="Growth Strategist - eCommerce & Digital Marketing Agency",
            client_name="RiseUp (UK-based AI-first digital growth agency)",
            url="https://www.upwork.com/freelance-jobs/apply/Growth-Strategist-eCommerce-Digital-Marketing-Agency_~022114017138989643896/",
            posted_at="Not captured in this pass (found via search, not individually dated).",
            description="Senior/Expert freelance growth strategist role supporting an agency's eCommerce "
                        "client portfolio across Google Ads, Microsoft Ads, Meta, TikTok, international SEO "
                        "and Shopify, plus general digital strategy. UK hours only.",
            required_skills="Broad multi-channel paid ads (Google/Microsoft/Meta/TikTok), SEO, Shopify, "
                             "agency-side strategic ownership -- Senior/Expert bar.",
            budget_amount=None, budget_currency="USD", budget_type="hourly (unspecified in this pass)",
            payment_platform="Upwork",
            client_history="Not captured in this pass.",
            verification_status="UNVERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard skill mismatch -- this is a multi-channel paid-ads/SEO/Shopify growth "
                              "strategist role at a Senior/Expert bar, not an email-marketing-specific "
                              "position. Paid ads, SEO and Shopify are all explicitly flagged in the claims "
                              "register as 'none demonstrated, don't claim.' Not a fit regardless of other "
                              "factors; not worth a full scrape for competition/budget detail.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=pph_id,
            title="Freelance Marketing Campaign Coordinator",
            client_name="Maria Nata (small company, UK/German markets)",
            url="https://www.peopleperhour.com/freelance-jobs/marketing-branding-sales/direct-marketers/freelance-marketing-campaign-coordinator-4529078",
            posted_at="2 days before discovery (fresh).",
            description="Own monthly Mailchimp campaigns (plan/build/schedule/send, segmentation, reporting), "
                        "quarterly seasonal product-launch plans for UK and German markets, audience growth "
                        "ideas, reporting. $47/hr, junior/intermediate welcome.",
            required_skills="Practical Mailchimp experience (explicitly required); German language skills "
                             "'an advantage, not essential'; UK/Europe based, UK business hours.",
            budget_amount=47, budget_currency="USD", budget_type="hourly",
            payment_platform="PeoplePerHour escrow",
            client_history="Small company, UK, fresh posting with 15 proposals already -- credibility not "
                            "independently verified from this scrape.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Hard skill mismatch -- the listing explicitly requires 'practical Mailchimp "
                              "experience,' and Mailchimp is on the claims register's PROHIBITED list "
                              "(documented platform experience is Brevo, not Mailchimp). German is only "
                              "'an advantage, not essential' here so the unresolved German-proficiency "
                              "conflict doesn't even need to be invoked -- the Mailchimp requirement alone "
                              "disqualifies this one.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=pph_id,
            title="Bravo email marketing,",
            client_name="Nigel R., United Kingdom",
            url="https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing/bravo-email-marketing-4397109",
            posted_at="Clarification-board entry dated 28 Jun 2025 -- job is at least ~16 months old at "
                      "discovery, i.e. significantly predates every other listing checked this cycle and last.",
            description="Brevo email automation strategy: professional templates, segmentation workflows, "
                        "nurturing campaigns, WordPress landing pages for lead capture, third-party list-sync "
                        "integration, reporting dashboards, plus SEO and social-media follow-on work.",
            required_skills="Brevo automation, WordPress landing-page build, third-party integration, SEO, "
                             "social media -- Expert level, broader than core documented strength.",
            budget_amount=128, budget_currency="GBP", budget_type="fixed (per PPH price field)",
            payment_platform="PeoplePerHour escrow",
            client_history="Buyer Nigel R.: 100% rating (51), 55 projects completed, 50 freelancers worked "
                            "with, 16% award rate, last project 29 Oct 2026 -- an established, credible buyer, "
                            "but that doesn't rescue this specific listing's age.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Extremely stale -- a clarification-board question dated 28 Jun 2025 puts this "
                              "listing at roughly 16 months old, far beyond any other listing treated as live "
                              "in this or prior cycles. Already ~29 proposals. Scope also bundles WordPress "
                              "landing-page build, SEO and social media on top of Brevo, going beyond the "
                              "documented lifecycle/segmentation strength.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Email Marketing Expert Needed: Domain Setup & Brevo Configuration",
            client_name="Buyer in Secunderabad, India",
            url="https://www.freelancer.com/projects/email-marketing/email-marketing-expert-needed-domain",
            posted_at="Posted almost 2 years before discovery.",
            description="Domain setup (SPF/DKIM/DMARC), Brevo account configuration, email warm-up and "
                         "domain-reputation management, monitoring/reporting via Google Postmaster/MXToolbox.",
            required_skills="Domain/DNS authentication, Brevo configuration, deliverability/reputation "
                             "management, email warm-up.",
            budget_amount=250, budget_currency="USD", budget_type="fixed ($30-$250, paid on delivery)",
            payment_platform="Freelancer.com escrow",
            client_history="5.0 rating (11 reviews), payment method verified, member since Dec 12, 2008 -- "
                            "credible long-term buyer, but moot given project status.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed, posted almost 2 years before this discovery cycle -- long filled. 14 "
                              "proposals already recorded at the time it closed, averaging $159 USD bid. "
                              "Nothing to apply to.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Email Sales Strategist Needed",
            client_name="Buyer in Canada",
            url="https://www.freelancer.com/projects/email-marketing/brevo-email-sales-strategist-needed",
            posted_at="Posted about 1 month before discovery.",
            description="Brevo-based welcome/nurture/sales email sequence for a service-based B2C business, "
                         "with A/B testing, dynamic content, revenue-attribution tracking inside Brevo.",
            required_skills="Brevo workflow automation, A/B testing, revenue-attribution reporting, proven "
                             "B2C sales results through Brevo.",
            budget_amount=250, budget_currency="CAD", budget_type="fixed ($30-$250, paid on delivery)",
            payment_platform="Freelancer.com escrow",
            client_history="Not independently scored -- moot given project status below.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed (32 proposals already, client active as recently as 8 hours before this "
                              "scrape, so already deep in selection or decided). Budget ($30-250 CAD fixed) is "
                              "also far too low for the requested scope (3-5 fully designed templates plus full "
                              "workflow automation and revenue attribution) even if it were still open. The "
                              "A/B-testing deliverable also runs into the claims register's unresolved "
                              "A/B-testing conflict, which would need to be worked around in any proposal.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
        ),
        dict(
            source_id=freelancer_id,
            title="Brevo Email Automation Expert Needed",
            client_name="Buyer in Leiden, Netherlands",
            url="https://www.freelancer.com/projects/email-marketing/brevo-email-automation-expert-needed",
            posted_at="Posted 6 months before discovery (last activity 4 months ago).",
            description="Brevo + WooCommerce automation flows: abandoned cart, welcome-with-discount, review "
                         "request, post-purchase follow-up. Client states 3-4 prior freelancers already failed "
                         "to deliver this.",
            required_skills="Brevo automation, WooCommerce integration, PHP/WordPress-level technical trigger "
                             "work, MySQL.",
            budget_amount=18, budget_currency="EUR", budget_type="hourly (EUR 12-18/hr range)",
            payment_platform="Freelancer.com escrow",
            client_history="0.0 rating (0 reviews), payment method verified, member since Jan 16, 2026 -- "
                            "thin, unproven buyer history.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Closed, 138 competing proposals averaging EUR 16/hr -- a saturated race-to-the-"
                              "bottom rate well below a sustainable freelance rate, and the scope requires "
                              "WooCommerce/PHP/MySQL technical integration depth that is outside the "
                              "documented strength (segmentation/lifecycle/deliverability, not e-commerce "
                              "platform engineering). Client's own description (3-4 prior freelancers already "
                              "failed) is also a credibility/scope-clarity red flag independent of staleness.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes=None,
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

    # Re-check note on the cycle-3 discounted P1 lead (same URL, id 10 in the DB) -- update notes/history
    # without changing its score, since the fill-risk signal is unchanged (Hires: 1, Interviewing: 4) but
    # the client's logged hours grew (635 -> 667 since cycle 3), confirming it's still an active account.
    conn.execute(
        """UPDATE opportunities SET notes = notes || ' | Cycle-4 re-check (2026-11-01): still shows '
           || 'Hires: 1, Interviewing: 4, proposals 15-20, last viewed by client 2 weeks ago -- fill-risk '
           || 'signal unchanged from cycle 3. Client hours logged grew 635 -> 667, confirming the account '
           || 'is still active. Still not recommended without owner confirmation the role is genuinely open.',
           updated_at = ?
           WHERE url = 'https://www.upwork.com/freelance-jobs/apply/Brevo-Email-Marketing-Manager-Subscription-App-engagement-Lifecycle_~022107889186699907933/'""",
        (NOW,),
    )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 5, len(opportunities), 0,
         "Reddit r/forhire individual threads still blocked for a FOURTH consecutive cycle "
         "(firecrawl_scrape: 'we do not support this site'). Contra surfaced no new distinct, scorable "
         "listing beyond the one already logged in cycle 3. All 3 Freelancer.com Brevo-specific listings "
         "found this cycle were already Closed (posted 1 month to ~2 years ago). Re-checked the cycle-3 "
         "discounted P1 (Brevo Email Marketing Manager, language-learning app): fill-risk signal unchanged "
         "(Hires: 1, Interviewing: 4), client still active (hours 635 -> 667). German-proficiency conflict "
         "in the claims register remains unresolved; no live job this cycle required German as a hard "
         "requirement (one PeoplePerHour listing had German as 'an advantage, not essential' but was "
         "rejected on a Mailchimp hard-requirement before German mattered)."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 4 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
