# Handoff prompt — direct-prospecting batch 2+ (for another LLM/agent session)

Paste the block below into a fresh LLM or coding-agent session to continue building the
medical/healthcare/wellness direct-prospecting list toward the 50-100 target, using the
same method established in `evidence/direct-prospecting-playbook.md` and
`evidence/prospects-medical-wellness.md` (batch 1: 4 prospects, 2 sent — Claire Cesta,
Susan Spear).

---

```
You are continuing a direct-client-prospecting research task for Kaeto Oruche, a freelance email marketing specialist (MPharm graduate, pharmacy background, builds lifecycle/welcome email sequences for small health & wellness businesses). The goal: build a list of 50-100 INDIVIDUALLY VERIFIED prospects in the medical/healthcare/wellness niche, each with a real, observed email-marketing gap, a confirmed contact channel, and a drafted first-touch message. This is NOT a mass-scrape job — quality and verification standard matter more than speed. Research backs this: personalized, narrow-target cold email converts at roughly 1 per 24 sends, versus 1 per 150-500 for generic/templated blasts. The 50-100 target itself comes from published guidance that this style of outreach performs best in batches of 30-80, not thousands.

4 prospects are already done in batch 1 — do not duplicate these names/businesses: Claire Cesta (Claire Cesta Integrative Medicine, Cary NC), Martina Pignatone (nutritionaltherapymartina.com), Susan Spear (Nutritious Insight, Phoenix AZ), ANNAZUR Organic Spa (Jacksonville FL, logged as weak-signal, not pursued). Claire and Susan have already been emailed; do not re-contact them.

## Target profile
Small/independent, solo-or-near-solo health & wellness operators where the owner is the decision-maker and can say yes fast: nutrition/functional medicine, naturopathy, holistic health coaching, acupuncture, chiropractic, therapy/counseling practices, med spas, dental/wellness clinics, midwifery/doula practices, physical therapy. NOT hospital systems, NOT large multi-location practices, NOT anything requiring enterprise procurement.

## Qualifying signal — need at least ONE of these, directly observed on the live site, never assumed:
- Has a website/social presence collecting attention but no visible newsletter or follow-up sequence
- Runs webinars/events with no visible registration-to-attendance email flow
- Sells products with no visible abandoned-cart or post-purchase sequence
- Has a lead magnet (free guide, quiz, etc.) with no visible nurture after opt-in
- Has real audience-building content (podcast appearances, a published book, YouTube, blog) with no way for that audience to join a list

## Verification discipline — this is the most important part
1. Actually scrape/read the site — homepage AND at minimum the About, Contact, and any FAQ/footer pages — before concluding anything. A prior pass on this project initially wrote "no public email found" for a prospect after only checking the homepage, then found a real email later on a deeper FAQ page. Don't make that mistake: check thoroughly before writing "unconfirmed."
2. NEVER invent or guess a contact email (no guessing info@ or hello@ patterns). Only use an email you can see written on the page or in a working mailto: link. If you can't find one, write the contact channel as "UNCONFIRMED" and do not draft a message for it yet.
3. Confirm the business is actually solo/small (look for "my practice," absence of a team/staff page, a single named owner) — not an assumption from the business name alone.
4. The "gap" must be something you directly observed on their current live site, described specifically (not "they could use more marketing").

## Writing the first-touch message — rules derived from tested research, not generic advice
- Open with ONE specific, true detail about them — but pull it from something ADJACENT to their own sales/marketing copy (their About-page personal story, a podcast appearance, a teaching role, a book) — NEVER restate their own services/specialties list back at them. Restating their own marketing copy reads as a templated mail-merge trick to anyone paying attention, and defeats the purpose of personalizing at all.
- NEVER claim a depth of engagement you can't back up if questioned (e.g. do not claim "I listened to your whole podcast episode" or "I read your book" if you only saw the title/description — say "I saw you appeared on X" or "I noticed you published Y" instead; this is both an honesty issue and a credibility-risk issue if the business owner replies with a follow-up question you can't answer).
- Then name the specific observed gap — frame it as an untapped opportunity, not a criticism of what they built.
- Propose ONE primary fix only (typically: a short 2-3 email welcome/nurture sequence) — never a multi-service menu, never a full "audit" pitch.
- State plainly that this doesn't touch client records/health information — only the marketing side (removes a real trust concern specific to health-adjacent businesses).
- Identity line: "I'm an MPharm graduate who moved into building email marketing systems for health and wellness businesses." Do NOT say "pharmacist," "licensed pharmacist," or "pharmacy student" — he graduated and is not registered/licensed as a pharmacist. Do NOT name his past employer under any circumstance.
- Pricing: $175 flat fee for a 2-3 email sequence, no retainer, is the baseline — this has been independently checked against market rates ($50-250/email is typical freelance pricing for this scope) and happens to also land near what several prospects in this niche charge for their own one-hour session, which is a coincidence worth knowing about but should NEVER be stated in the message itself (pointing out that the price matches their own rate reads as a manipulative anchoring tactic to anyone numerate). For roughly half the batch, omit price entirely from the first message and instead end on a soft question like "Would you be interested in seeing a sample?" — this tests whether a no-price variant converts better; keep track of which approach was used for each prospect.
- NEVER ask about budget, team size, or "who handles your email marketing" in a first-touch message — this is a known anti-pattern that converts a specific-opportunity message into a sales-qualification script, and for most of these targets (solo operators) a "team" framing is itself a mismatch that reveals low research depth.
- Keep the message under ~150 words. Research on this specific point: emails between 50-125 words get meaningfully higher reply rates than longer ones.
- End with a low-pressure close ("No worries if it's not useful right now" or similar) — lowers the social cost of the business owner replying at all, which counterintuitively raises response rates.
- Do NOT draft free-trial or free-audit offers (ruled out entirely for this project) and do NOT send anything yourself — Kaeto sends every message personally; your job is research and drafting only.

## Output format — follow this exact structure per prospect, matching the existing file evidence/prospects-medical-wellness.md in the repo kaetooruche-collab/email-marketing-job-search (branch claude/blissful-turing-awwbgt) if you have access to it, otherwise produce it as a new markdown file for Kaeto to merge in himself:

### N. [Name] — [Business name] ([City, State/Country if known])
- **Site:** [URL]
- **What they do:** [1-2 sentences, their actual specialty/credentials]
- **Observed gap:** [specific, from direct observation]
- **Decision-maker:** [name] (solo practice / confirm how you know)
- **Contact channel:** [confirmed email, with the exact quoted text/location where you found it — OR "UNCONFIRMED — [where you looked and what's missing]"]
- **Confidence:** PARTIALLY VERIFIED / VERIFIED — [why]

**Draft opening message (price variant: [with $175 / no-price]):**
> [message]

## Pacing
Work in batches of roughly 10-15 newly verified prospects per session rather than trying to produce all 50-100 at once — depth per prospect matters more than raw count, and rushing increases the risk of guessed contact info or shallow "gaps" that don't hold up. Stop and report back after each batch rather than silently continuing to 50-100 in one pass.
```
