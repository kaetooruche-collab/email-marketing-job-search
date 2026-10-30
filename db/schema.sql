-- Email Marketing Revenue Acquisition System — persistent schema (SQLite)
-- Minimal first pass covering master-prompt §14 core entities.
-- Extend with contacts/applications/contracts/payments tables as those workflows come online.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS sources (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,                 -- e.g. "Upwork", "Reddit r/forhire"
    url TEXT,
    access_method TEXT,                 -- "firecrawl_search/scrape (public page, no login)"
    terms_notes TEXT,
    last_scan_at TEXT,
    last_error TEXT,
    discovery_count INTEGER DEFAULT 0,
    qualified_count INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY,
    source_id INTEGER REFERENCES sources(id),
    title TEXT NOT NULL,
    client_name TEXT,
    url TEXT UNIQUE,
    discovered_at TEXT NOT NULL,
    posted_at TEXT,                     -- as stated by the listing, if known
    description TEXT,
    required_skills TEXT,
    budget_amount REAL,
    budget_currency TEXT,
    budget_type TEXT,                   -- fixed | hourly | unknown
    payment_platform TEXT,              -- e.g. "Upwork escrow"
    client_history TEXT,                -- member since, total spent, hires, etc as free text
    verification_status TEXT CHECK(verification_status IN
        ('VERIFIED','PARTIALLY_VERIFIED','UNVERIFIED','SUSPICIOUS','REJECTED')) NOT NULL,
    priority_tier TEXT CHECK(priority_tier IN ('P0','P1','PAYMENT_TIMELINE_UNCERTAIN','REJECTED')) NOT NULL,
    rejection_reason TEXT,
    est_days_to_accessible_payment INTEGER,
    score_probability_win INTEGER,      -- /20
    score_time_to_payment INTEGER,      -- /25
    score_skill_match INTEGER,          -- /15
    score_payment_certainty INTEGER,    -- /15
    score_compensation INTEGER,         -- /10
    score_client_credibility INTEGER,   -- /10
    score_repeat_potential INTEGER,     -- /5
    score_total INTEGER,                -- /100
    score_rationale TEXT,
    status TEXT DEFAULT 'new',          -- new | researched | package_ready | applied | responded | won | lost | closed
    notes TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    opportunity_id INTEGER REFERENCES opportunities(id),
    name TEXT,
    role TEXT,
    email TEXT,
    email_verification_status TEXT CHECK(email_verification_status IN
        ('VERIFIED_DELIVERABLE','DOMAIN_VERIFIED_MAILBOX_UNCONFIRMED','PUBLICLY_LISTED_NOT_VERIFIED',
         'GUESSED_PATTERN','INVALID','UNKNOWN')),
    other_channel TEXT,                 -- linkedin url, form, etc.
    source_url TEXT,
    confidence TEXT,
    notes TEXT,
    discovered_at TEXT
);

CREATE TABLE IF NOT EXISTS evidence_claims (
    id INTEGER PRIMARY KEY,
    claim TEXT NOT NULL,
    source_doc TEXT,
    verification_status TEXT CHECK(verification_status IN
        ('VERIFIED','PARTIALLY_VERIFIED','UNVERIFIED','CONFLICT','PROHIBITED')) NOT NULL,
    permitted_wording TEXT,
    limitations TEXT,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY,
    opportunity_id INTEGER REFERENCES opportunities(id),
    channel TEXT,                       -- upwork proposal | email | linkedin | etc
    cv_version_id INTEGER,
    documents_prepared TEXT,            -- json/free text list
    proposed_price REAL,
    status TEXT DEFAULT 'draft',        -- draft | awaiting_approval | approved | submitted | responded | rejected
    drafted_at TEXT,
    approved_at TEXT,
    submitted_at TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS automation_runs (
    id INTEGER PRIMARY KEY,
    run_type TEXT,                      -- discovery_scan | verification | contact_research | report
    started_at TEXT,
    finished_at TEXT,
    sources_scanned INTEGER,
    opportunities_found INTEGER,
    opportunities_qualified INTEGER,
    errors TEXT
);
