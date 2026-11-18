#!/usr/bin/env python3
"""Discovery cycle 8 (2026-11-18): regular run following cycle 7 (2026-11-17). Picks up cycle 7's
three open items: (a) a final quiet re-check of the Newsletter Specialist for Campaigns / Brevo
Upwork rate -- nothing materially new, per the owner's standing instruction this is noted, not
re-flagged; (b) one more Reddit r/forhire attempt via direct firecrawl_scrape only (no paid
Alexandria provider used without the owner's go-ahead) -- still blocked, as expected; (c)
PeoplePerHour page 1 re-check only (sweep already complete) -- identical to cycles 6-7. Also runs
fresh Brevo-specific and generic searches, re-checks Freelancer.com/Contra/German-market/
freelance.de/Useme.com. Found and logged 3 new URLs: one genuine Brevo skill match that scores
below the P1 bar (PAYMENT_TIMELINE_UNCERTAIN, not rounded up), one tool/scope-mismatch reject, and
one already-closed Useme.com listing. Appends to the same DB. Safe to re-run (INSERT OR IGNORE on
url). See reports/2026-11-18-discovery-cycle-8.md for the full narrative."""
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
        "status check (not a re-flag, per the owner's standing instruction). Rate still does not "
        "render (3rd consecutive cycle); Interviewing still 3 (no further movement since cycle 7); "
        "client totals flat ($68K/35 hires/16 active, same as cycle 7; hours up slightly 1,973->"
        "1,976, routine usage not a signal). Fresh Brevo/generic searches surfaced two new URLs: "
        "'Brevo CRM and Email Setup' (genuine skill match, but client account only 8 days old with "
        "1 hire -- scored PAYMENT_TIMELINE_UNCERTAIN, not rounded up to P1) and 'B2B Cold Email & "
        "Lead Generation Specialist (Instantly/Apollo/Brevo)' (rejected -- cold-outreach tooling "
        "scope, not email marketing, requires unevidenced/PROHIBITED tools).",
        discovery_count=2, qualified_count=0,
    )
    pph_id = get_or_create_source(
        conn, "PeoplePerHour", "https://www.peopleperhour.com/freelance-jobs/digital-marketing/email-marketing",
        "firecrawl_scrape of category listing page 1 only (page sweep completed cycle 6)",
        "Re-checked page 1 only, per cycles 6-7's finding. Identical again: exactly 2 open "
        "listings -- 'Gmail account' ($10, Google Workspace admin, not email marketing) and the "
        "already-logged UK Kajabi listing (duplicate). No new open listing, 3rd cycle running.",
        discovery_count=0, qualified_count=0,
    )
    freelancer_id = get_or_create_source(
        conn, "Freelancer.com", "https://www.freelancer.com/jobs/email-marketing",
        "firecrawl_search of individual project listings",
        "Fresh Brevo-specific search this cycle surfaced only listings already on file (including "
        "the one closed listing logged in cycle 7). No new URL found this cycle.",
        discovery_count=0, qualified_count=0,
    )
    contra_id = get_or_create_source(
        conn, "Contra", "https://contra.com/featured-jobs/freelance-marketing-jobs",
        "firecrawl_search of Contra listings/community posts/freelancer pages",
        "8th consecutive cycle with the same structural limitation: search surfaces only the "
        "/hire/brevo-freelancers directory page and freelancer self-promotion/profile content, "
        "never a genuine client job posting.",
        discovery_count=0, qualified_count=0,
    )
    reddit_id = get_or_create_source(
        conn, "Reddit r/forhire", "https://www.reddit.com/r/forhire",
        "firecrawl_scrape (blocked, 8 cycles on the free method); scrapecreators Alexandria "
        "provider works but was NOT used this cycle pending the owner's go-ahead from cycle 7",
        "Tried direct firecrawl_scrape again this cycle, as instructed, against both the "
        "subreddit listing page and an individual thread URL surfaced by web search. Both failed "
        "identically: 'Firecrawl can't scrape this site because it is currently not supported.' "
        "Same result as 7 of the last 8 cycles. Per instruction, did NOT fall back to the paid "
        "scrapecreators Alexandria provider this cycle -- that decision is still the owner's to "
        "make, not yet given. No cost incurred, no new data gained, as expected.",
        last_error="Firecrawl can't scrape this site because it is currently not supported.",
        discovery_count=0, qualified_count=0,
    )
    german_id = get_or_create_source(
        conn, "German-market search (direct, no single platform)",
        "https://www.google.com (web search for German-language email marketing freelance work)",
        "firecrawl_search for German-language freelance email marketing terms",
        "Re-ran the German-language query -- eighth consecutive cycle with no live German-market "
        "email-marketing-specialist opening surfaced; results remain tutorials, platform blog "
        "content, and one German agency's own service page (web-labels.de, selling Brevo/Klaviyo "
        "services to clients, not hiring). German-proficiency claims-register conflict remains "
        "untested in practice.",
        discovery_count=0, qualified_count=0,
    )
    freelancede_id = get_or_create_source(
        conn, "freelance.de", "https://www.freelance.de/Brevo-Freelancer",
        "firecrawl_search of category/directory pages and a dedicated 'Projekt gesucht' query "
        "aimed at finding an actual client posting",
        "Tried both a directory-style query and a query specifically aimed at finding a genuine "
        "client project posting rather than a freelancer directory. Still only surfaced "
        "/Brevo-Freelancer and /Newsletter-Freelancer directory pages -- same structural "
        "limitation as cycle 7, now confirmed across two cycles. No client project-posting "
        "section found for this platform; likely not worth a further dedicated pass unless a "
        "future query surfaces an actual Projekt/Auftrag listing.",
        discovery_count=0, qualified_count=0,
    )
    useme_id = get_or_create_source(
        conn, "Useme.com", "https://useme.com/en/jobs/category/marketing,37/email-marketing,116/",
        "firecrawl_scrape of category listing page (English page 1 + Polish page 2 this cycle)",
        "Re-checked page 1 (English) -- unchanged from cycle 7, same Oliver Tornroth/Zoined "
        "posting (now 24 days left instead of 25), still the only open listing, still zero live "
        "Brevo listings. Also checked Polish page 2 this cycle (new angle), which surfaced one "
        "Brevo-specific URL not previously on file ('ROZBUDOWA AUTOMATYZACJI BREVO') -- turned "
        "out to be posted 2025-12-30 with a 30-day listing window, expired ~11 months before this "
        "cycle's discovery, 7 proposals already on record. Logged as closed/rejected for the "
        "audit trail. Category remains dominated by closed Klaviyo/Mailchimp/GetResponse/"
        "MailerLite/Edrone/Snov.io/Omnisend/SendGrid listings.",
        discovery_count=1, qualified_count=0,
    )

    opportunities = [
        dict(
            source_id=upwork_id,
            title="Brevo CRM and Email Setup",
            client_name="Individual/small business client, Washington, United States (Upwork, "
                         "member since Nov 10, 2026 -- 8 days old, 1 hire, 1 active contract, "
                         "payment method not independently verifiable from the public scrape)",
            url="https://www.upwork.com/freelance-jobs/apply/Brevo-CRM-and-Email-Setup_~022122535830947990577/",
            posted_at="Scraped 2026-11-18; exact posted date not shown, client account itself "
                      "only 8 days old at discovery",
            description="Setting up Brevo CRM and email system for onboarding, retention, and "
                        "e-commerce customer journeys: configuring workflows, building email "
                        "sequences, supporting customer communication across lifecycle stages. "
                        "Requires communicating to a developer what events need to be integrated "
                        "into Brevo (custom-built app/website, no native integration).",
            required_skills="Brevo workflow/automation configuration, email sequence building, "
                             "lifecycle-stage segmentation, ability to spec integration events "
                             "for a developer. Auto-tagged skills (Microsoft Dynamics CRM, Zoho "
                             "CRM, Email Support) appear to be Upwork's suggested tags, not "
                             "stated requirements in the job text itself.",
            budget_amount=19, budget_currency="USD", budget_type="hourly ($10.00-$28.00/hr)",
            payment_platform="Upwork (hourly contract, weekly billing once hired; TRNC "
                              "payment-routing caveats per evidence/payment-routing.md apply)",
            client_history="Member since Nov 10, 2026 (8 days old at discovery). United States "
                            "(Washington). 1 hire, 1 active contract -- effectively no track "
                            "record to assess trust/payment follow-through against.",
            verification_status="VERIFIED",
            priority_tier="PAYMENT_TIMELINE_UNCERTAIN",
            rejection_reason=None,
            est_days_to_accessible_payment=14,
            score_probability_win=6, score_time_to_payment=14, score_skill_match=12,
            score_payment_certainty=6, score_compensation=5, score_client_credibility=2,
            score_repeat_potential=2, score_total=47,
            score_rationale="Genuine Brevo skill match -- lifecycle/workflow email-sequence "
                            "configuration is exactly the documented HIBARR scope, and no "
                            "PROHIBITED tool is required (the Dynamics/Zoho CRM tags read as "
                            "Upwork's auto-suggested tags, not stated requirements). What keeps "
                            "this below the P1 bar: the client account is only 8 days old with "
                            "exactly 1 hire/1 active contract -- essentially no track record on a "
                            "platform where unfunded milestones and client disappearance are known "
                            "failure modes -- combined with 20-50 competing proposals and 2 active "
                            "interviews against that thin-history, low-budget client. Scored and "
                            "logged honestly rather than rounded up; not recommending a proposal on "
                            "this alone. Would be worth a second look if the client's history "
                            "develops (more hires, reviews) in a future cycle, assuming the role is "
                            "still open.",
            status="researched",
            notes="Surfaced by a fresh Brevo-specific Upwork search this cycle. A real candidate, "
                  "not a reject, but the client-credibility and competition signals are genuinely "
                  "weak, not a close call being talked down.",
        ),
        dict(
            source_id=upwork_id,
            title="B2B Cold Email & Lead Generation Specialist (Instantly / Apollo / Brevo)",
            client_name="Sales & Marketing agency, Karachi, Pakistan (Upwork, member since Jul "
                         "11, 2018, $3.5K total spent, 351 hires, 17 active, mid-sized company "
                         "10-99 people)",
            url="https://www.upwork.com/freelance-jobs/apply/B2B-Cold-Email-Lead-Generation-Specialist-Instantly-Apollo-Brevo_~022122083849773630505/",
            posted_at="Scraped 2026-11-18; last viewed by client 'yesterday', 1 hire/3 "
                      "interviewing/3 invites sent already recorded against this posting",
            description="B2B cold email and lead-generation specialist role: Apollo.io/LinkedIn "
                        "Sales Navigator prospect-list building and verification, multi-step cold "
                        "email sequences and A/B tests inside Instantly, Lemlist, or Brevo, "
                        "SPF/DKIM/DMARC domain-health and warm-up management, and daily "
                        "open/reply/bounce metric reporting in Google Sheets.",
            required_skills="Hands-on Instantly, Lemlist, Apollo.io, HubSpot, or ActiveCampaign; "
                             "cold-outreach deliverability engineering (SPF/DKIM/DMARC, domain "
                             "warm-up); B2B prospect-list sourcing and verification.",
            budget_amount=7.5, budget_currency="USD", budget_type="hourly ($5.00-$10.00/hr)",
            payment_platform="Upwork (hourly contract; TRNC payment-routing caveats apply)",
            client_history="Member since Jul 11, 2018. Pakistan (Karachi). $3.5K total spent, "
                            "351 hires, 17 active -- high hire volume relative to spend suggests "
                            "many small/short engagements, consistent with a lead-gen agency "
                            "staffing model rather than a single substantial project.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Despite 'Brevo' in the title, the actual scope is B2B cold-outreach "
                              "infrastructure (Apollo/Instantly/Lemlist sequence building, domain "
                              "warm-up, SPF/DKIM/DMARC), not email-marketing-specialist work. None "
                              "of Instantly, Lemlist, or Apollo appear anywhere in the claims "
                              "register (re-checked for updates this cycle -- none found); "
                              "HubSpot and ActiveCampaign are explicitly PROHIBITED hands-on "
                              "claims. A different job family wearing an email-marketing label. "
                              "Entry-level $5-10/hr is also well below a reasonable rate for the "
                              "stated scope.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Surfaced by the same Brevo-specific search that found the CRM/Email Setup "
                  "candidate above -- screened on full scrape, rejected on tool/scope grounds, "
                  "same pattern as cycle 7's Klaviyo/cold-outbound rejects.",
        ),
        dict(
            source_id=useme_id,
            title="ROZBUDOWA AUTOMATYZACJI BREVO (closed before discovery)",
            client_name="Individual client 'MT', Poland (Useme.com, anonymized handle)",
            url="https://useme.com/pl/jobs/rozbudowa-automatyzacji-brevo,128480/",
            posted_at="Posted 2025-12-30; stated listing window 30 days (expired ~2026-01-29, "
                      "roughly 11 months before this cycle's discovery)",
            description="Expand and organize an existing partial Brevo (formerly Sendinblue) "
                        "implementation on a PrestaShop-based online store -- automations and "
                        "abandoned-cart flow already partially built -- into a full "
                        "revenue-generating email sales tool for the existing customer base.",
            required_skills="Brevo automation/workflow building, PrestaShop e-commerce "
                             "integration, abandoned-cart and lifecycle sequence design.",
            budget_amount=None, budget_currency=None, budget_type="negotiable (budżet: do negocjacji)",
            payment_platform="Useme.com (escrow/invoicing; not independently tested for TRNC "
                              "residents, same unresolved question raised for this platform in "
                              "cycle 6)",
            client_history="Individual client 'MT', no further profile detail surfaced on the "
                            "public listing page.",
            verification_status="VERIFIED",
            priority_tier="REJECTED",
            rejection_reason="Already closed -- posted 2025-12-30 with a stated 30-day listing "
                              "window (expired roughly 11 months before this cycle's discovery), "
                              "with 7 proposals already submitted against it between late 2025 "
                              "and January 2026. No live opportunity exists; fails the "
                              "payment-horizon test outright. Logged purely for audit-trail "
                              "completeness since this was a URL not previously on file -- the "
                              "scope itself (Brevo automation build-out) would otherwise have been "
                              "a reasonable skill match.",
            est_days_to_accessible_payment=None,
            score_probability_win=None, score_time_to_payment=None, score_skill_match=None,
            score_payment_certainty=None, score_compensation=None, score_client_credibility=None,
            score_repeat_potential=None, score_total=None, score_rationale=None,
            status="closed",
            notes="Surfaced via a new angle this cycle (checking Useme.com's Polish-language page "
                  "2 rather than only the English page 1). Confirms the category's listings "
                  "cycle through fairly quickly and page 2+ mostly holds long-closed postings, "
                  "same structural pattern as PeoplePerHour's archive pagination.",
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

    # Update the still-open P1 lead from cycles 5-7 with this cycle's quiet re-check. Per the
    # owner's standing instruction (flagged twice already, their call to act on), this is recorded
    # without being surfaced as a fresh "needs attention" item.
    newsletter_url = "https://www.upwork.com/freelance-jobs/apply/Newsletter-Specialist-for-Campaigns-Brevo_~022120509588989804149/"
    existing_note_row = conn.execute(
        "SELECT notes FROM opportunities WHERE url = ?", (newsletter_url,)
    ).fetchone()
    if existing_note_row:
        appended_note = (
            (existing_note_row[0] or "")
            + " | Cycle 8 (2026-11-18) quiet re-check (per owner's standing instruction, not "
              "re-flagged): hourly rate still does not render (3rd consecutive cycle). "
              "Interviewing unchanged at 3 (no further movement since cycle 7's 0->3 jump). "
              "Last viewed by client: 'yesterday' (consistent with ongoing activity). Client "
              "totals flat: $68K spent/35 hires/16 active (same as cycle 7); hours ticked up "
              "1,973->1,976 (routine usage, not a signal). Nothing materially new; no action "
              "taken, no fresh flag raised."
        )
        conn.execute(
            "UPDATE opportunities SET notes = ?, updated_at = ? WHERE url = ?",
            (appended_note, NOW, newsletter_url),
        )

    conn.execute("""INSERT INTO automation_runs
        (run_type, started_at, finished_at, sources_scanned, opportunities_found, opportunities_qualified, errors)
        VALUES (?,?,?,?,?,?,?)""",
        ("discovery_scan", NOW, NOW, 8, len(opportunities), 0,
         "Cycle 8, the regular run following cycle 7 (2026-11-17). Followed up on all three of "
         "cycle 7's open items: (a) Newsletter Specialist for Campaigns / Brevo rechecked once "
         "quietly -- nothing materially new, not re-flagged per the owner's standing instruction. "
         "(b) Reddit r/forhire: direct firecrawl_scrape attempted again (subreddit page + an "
         "individual thread URL), still blocked both times; the paid scrapecreators Alexandria "
         "provider was deliberately NOT used again pending the owner's go-ahead from cycle 7. "
         "(c) PeoplePerHour page 1 re-checked only (sweep already complete) -- identical to "
         "cycles 6-7, no new candidate. Fresh Brevo/generic searches plus a new Useme.com "
         "Polish-page-2 angle found 3 new URLs: 'Brevo CRM and Email Setup' (genuine skill match, "
         "scored honestly at 47/100 -- PAYMENT_TIMELINE_UNCERTAIN due to an 8-day-old client "
         "account and heavy competition, not rounded up to P1), 'B2B Cold Email & Lead "
         "Generation Specialist' (rejected -- cold-outreach tooling scope, unevidenced/PROHIBITED "
         "tools), and a Useme.com Brevo/PrestaShop listing (rejected -- closed ~11 months before "
         "discovery). Direct business prospecting (master prompt section 4.3/12) was not run this "
         "cycle and the reasoning was written up explicitly: its method ends in drafting "
         "outreach, which is out of scope for this cycle's no-drafting instruction, so it "
         "continues as the separate manual workstream it has been since cycle 3. 0 new P0/P1 "
         "opportunities this cycle; no application package recommended."))

    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    print(f"Cycle 8 seeded. {n} total opportunities on file.")
    conn.close()


if __name__ == "__main__":
    main()
