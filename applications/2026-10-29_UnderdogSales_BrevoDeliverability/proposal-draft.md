# Proposal draft — Brevo deliverability and list cleanup specialist (Underdog Sales)

**Status: DRAFT, NOT SUBMITTED.** You submit this yourself from your logged-in Upwork account — I can't submit on your behalf. Confirm the listing is actually still open first (its activity panel showed "Hires: 1" recorded against it the day after posting).

**Job:** https://www.upwork.com/freelance-jobs/apply/Brevo-deliverability-and-list-cleanup-specialist_~022115757776792063959/
**Budget:** $350 fixed, 2 milestones ($150 / $200)

## Honest fit check before you send this

- **Strong, evidenced match:** list hygiene, bounce-rate reduction, engagement-based segmentation, Apple Mail Privacy Protection-aware engagement scoring, re-engagement/sunset sequences. These are directly documented in your HIBARR work.
- **Not evidenced, disclosed below rather than hidden:** hands-on SPF/DKIM/DMARC record auditing specifically, and Google Postmaster Tools. Your CVs say "deliverability optimization" and "sender reputation monitoring" generally, not protocol-level DNS auth work by name. I wrote the proposal to be honest about this rather than claim specialist DNS experience you haven't documented.
- **Make/Zapier:** the job's requirements line mentions it, but re-reading the actual scope, the two paid milestones ($150 audit/diagnosis, $200 segments/sunset/SOP) don't require it — the Make/Zapier-dependent piece ("Make scenarios sending Zoom attendance and Stripe purchases into Brevo") is explicitly called out as **optional, quoted separately**. The proposal below addresses this directly instead of pretending the gap doesn't exist.

## Proposal text

> The last deliverability problem I fixed was at HIBARR, where I owned email marketing end to end: list hygiene and sender-reputation work took bounce rates down 10% and spam complaints to 0.019% across 245 campaigns and 90K+ sends. More relevant to your brief — I built engagement segmentation that's Apple MPP-aware from the ground up: a five-tier engagement ladder driven by click recency only, because I'd already learned the hard way that counting opens as a signal post-MPP just tells you who has an iPhone, not who's engaged. That's exactly the "two broken segments" problem you're describing.
>
> I also designed and ran a three-tier re-engagement sequence for a cohort of lapsed leads (ten-day window, segmented by engagement tier, each email with a distinct job) before handing them to sales — which maps closely to the sunset automation you want built from your three existing re-engagement emails.
>
> Two things I want to be upfront about rather than have you find out mid-project: I haven't personally run an SPF/DKIM/DMARC audit end-to-end before, though I understand the mechanics and have worked adjacent to authentication issues through sender-reputation monitoring — I'd treat milestone 1 as exactly that: find the cause, document it clearly, fix it. And I haven't used Make or Zapier hands-on. Looking at your scope again, the two paid milestones don't actually seem to need it (you've called the Make/Zoom/Stripe piece optional and separately quoted) — so I don't think that's a blocker for the $350 scope, but happy to talk through it if I'm misreading.
>
> If that's a reasonable trade for someone who's actually run the segmentation/sunset/list-hygiene side of this at scale, I'd like to take milestone 1 first — audit, Postmaster setup, placement diagnosis — so you can see the work before committing to milestone 2.

## Before sending
1. Confirm the job is still open (your Upwork login).
2. Adjust tone/length to taste — this is a draft, not a template to send verbatim.
3. If you want, I can also draft the Postmaster/SPF-DKIM-DMARC audit checklist in advance so milestone 1 can start fast if you're hired.
