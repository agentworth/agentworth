#!/usr/bin/env python3
# Generates agentworth's programmatic SEO pages: /roi-for/, /compare/, /glossary/, /use-cases/
# Run from the repo root: python3 generate_seo_pages.py

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://agentworth.cloud"

HEAD_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">"""

STYLE = """<style>
  :root { --signal: #2E9BFF; }
  * { box-sizing: border-box; }
  body { margin: 0; background: #0B0C10; color: #F4F5F7; font-family: 'Plus Jakarta Sans', sans-serif; -webkit-font-smoothing: antialiased; }
  a { color: var(--signal); text-decoration: none; }
  .af-nav a { color: inherit; transition: color 0.2s ease; }
  .af-nav a:hover { color: #F4F5F7; }
  article h2 { font-family:'Outfit',sans-serif; font-weight:600; font-size:24px; margin:40px 0 14px; letter-spacing:-0.01em; }
  article p { font-size:17px; line-height:1.75; color:#C7CBD1; margin:0 0 18px; }
  article ul { margin:0 0 20px; padding-left:22px; }
  article li { font-size:16px; line-height:1.7; color:#C7CBD1; margin-bottom:10px; }
  .af-pill { display:inline-block; font-size:12.5px; color:var(--signal); font-weight:600; letter-spacing:0.04em; text-transform:uppercase; margin-bottom:14px; }
  .af-cta { display:block; margin-top:36px; padding:24px; border-radius:14px; background:linear-gradient(165deg,#15181F,#0F1115); border:1px solid #21242D; }
  .af-cta a { font-weight:600; }
  .af-related { margin-top:40px; padding-top:28px; border-top:1px solid #181B22; }
  .af-related a { display:inline-block; margin:0 10px 10px 0; padding:8px 14px; border-radius:999px; border:1px solid #2A2E38; color:#B6BBC4; font-size:14px; }
  .af-related a:hover { color:#F4F5F7; border-color:#37506B; }
  .af-hublist { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; margin-top:32px; }
  .af-hubcard { padding:20px 22px; border-radius:12px; border:1px solid #21242D; background:#13151A; }
  .af-hubcard h3 { margin:0 0 6px; font-family:'Outfit',sans-serif; font-size:17px; font-weight:600; }
  .af-hubcard p { margin:0; font-size:14px; color:#9BA1AE; }
  @media (max-width: 680px) {
    .af-pad { padding-left: 24px !important; padding-right: 24px !important; }
    .af-hublist { grid-template-columns:1fr !important; }
  }
</style>"""

HEADER = """<header class="af-pad" style="position:sticky; top:0; z-index:50; display:flex; align-items:center; justify-content:space-between; padding:20px 48px; backdrop-filter:blur(12px); background:rgba(11,12,16,0.72); border-bottom:1px solid #1E2129">
  <a href="/"><img src="/logo.png" alt="agentworth" style="height:22px; width:auto; display:block"></a>
  <nav class="af-nav" style="display:flex; align-items:center; gap:36px; font-size:14px; color:#B6BBC4; flex-wrap:wrap">
    <a href="/#how-it-works">How it works</a>
    <a href="/#roi-calculator">ROI calculator</a>
    <a href="/blog/">Blog</a>
    <a href="/#contact" style="padding:10px 20px; border-radius:999px; background:var(--signal); color:#06111F; font-weight:600">Get in touch</a>
  </nav>
</header>"""

def footer():
    return """<footer class="af-pad" style="padding:40px 48px; display:flex; align-items:center; justify-content:space-between; border-top:1px solid #181B22; flex-wrap:wrap; gap:16px; max-width:760px; margin:0 auto">
  <a href="/"><img src="/logo.png" alt="agentworth" style="height:16px; width:auto; display:block; opacity:0.8"></a>
  <span style="font-size:13px; color:#6B7280">&copy; 2026 agentworth. Built for teams who have to answer for their AI.</span>
</footer>"""


ANALYTICS_SCRIPT = '<script defer src="/_vercel/insights/script.js"></script>'

def page_shell(title, meta_desc, canonical_path, body_inner):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{SITE}{canonical_path}">
{HEAD_FONTS}
{STYLE}
</head>
<body>
{HEADER}
{body_inner}
{footer()}
{ANALYTICS_SCRIPT}
</body>
</html>
"""


def content_page(back_href, back_label, eyebrow, h1, subhead, body_html, related_html, title, meta_desc, canonical_path):
    inner = f"""
<article class="af-pad" style="padding:80px 48px 120px; max-width:760px; margin:0 auto">
  <a href="{back_href}" style="font-size:14px; color:#6B7280">&larr; {back_label}</a>
  <div class="af-pill" style="margin-top:28px">{eyebrow}</div>
  <h1 style="font-family:'Outfit',sans-serif; font-weight:600; font-size:clamp(28px,5vw,40px); margin:0 0 18px; letter-spacing:-0.02em">{h1}</h1>
  <p style="font-size:18px; line-height:1.65; color:#9BA1AE; margin:0 0 32px">{subhead}</p>
  {body_html}
  <div class="af-cta">
    <p style="margin:0 0 14px; color:#C7CBD1">Running an AI agent and want a verified number instead of a guess? <a href="/#contact">Tell us about your setup</a> or <a href="/#roi-calculator">try the free ROI calculator</a>.</p>
  </div>
  {related_html}
</article>
"""
    return page_shell(title, meta_desc, canonical_path, inner)


def hub_page(eyebrow, h1, subhead, cards_html, title, meta_desc, canonical_path):
    inner = f"""
<article class="af-pad" style="padding:80px 48px 120px; max-width:900px; margin:0 auto">
  <a href="/" style="font-size:14px; color:#6B7280">&larr; Back home</a>
  <div class="af-pill" style="margin-top:28px">{eyebrow}</div>
  <h1 style="font-family:'Outfit',sans-serif; font-weight:600; font-size:clamp(28px,5vw,40px); margin:0 0 18px; letter-spacing:-0.02em">{h1}</h1>
  <p style="font-size:18px; line-height:1.65; color:#9BA1AE; margin:0 0 8px; max-width:600px">{subhead}</p>
  <div class="af-hublist">
    {cards_html}
  </div>
</article>
"""
    return page_shell(title, meta_desc, canonical_path, inner)


def related_links(items, base):
    links = "".join(f'<a href="{base}{slug}/">{label}</a>' for slug, label in items)
    return f'<div class="af-related">{links}</div>'

def related_links_abs(items):
    # Like related_links, but items are (full_path, label) pairs instead of
    # (slug, label) pairs within a single category, for cross category links.
    links = "".join(f'<a href="{path}">{label}</a>' for path, label in items)
    return f'<div class="af-related">{links}</div>'

# ---------------------------------------------------------------------------
# INDUSTRY PAGES  (/roi-for/<slug>/)
# ---------------------------------------------------------------------------
INDUSTRIES = [
    {
        "name": "Ecommerce", "slug": "ecommerce",
        "agents": "order status, returns, and cart recovery agents",
        "intro": "Support volume in ecommerce swings hard around sales events and holidays, and returns spike every season. A resolution number from last quarter rarely tells you anything useful about this quarter.",
        "bullets": [
            "A simple where is my order question is not the same win as a full return handled end to end, but most dashboards count them the same",
            "Peak season volume makes it impossible to manually sample enough agent conversations to trust the number you report",
            "Refund and chargeback costs need to be subtracted from what the agent saved, or the ROI figure is overstated",
        ],
        "closing": "agentworth ties every conversation to its order type and outcome, so a returns agent's savings are measured against actual refund costs, not just a ticket count, and the number holds up whether volume is flat or five times normal.",
    },
    {
        "name": "Fintech", "slug": "fintech",
        "agents": "account support, fraud triage, and payment dispute agents",
        "intro": "A fintech support agent touches money, which means every resolution carries compliance weight that a generic support metric does not capture.",
        "bullets": [
            "Getting a dispute resolution wrong has a real cost that a simple containment rate hides completely",
            "Regulators and auditors want to see why a case was closed a certain way, not just that it was closed",
            "Fraud triage agents are judged on catching the right cases, not on closing the most cases quickly",
        ],
        "closing": "agentworth logs the reasoning path behind each resolution alongside the dollar outcome, so compliance has a record to point to and finance gets a number that reflects quality, not just speed.",
    },
    {
        "name": "SaaS", "slug": "saas",
        "agents": "onboarding, technical support, and renewal support agents",
        "intro": "SaaS support agents are often judged by ticket deflection alone, which rewards closing tickets fast rather than keeping the account healthy.",
        "bullets": [
            "A deflected ticket that leads to churn next quarter was never actually a win",
            "Technical support resolutions vary wildly in complexity, and a flat cost per ticket hides that",
            "Onboarding agents need to be measured against activation and time to value, not just resolution count",
        ],
        "closing": "agentworth connects resolution data to the outcomes that actually matter for a subscription business, so a support agent's ROI reflects retained revenue, not just a shrinking ticket queue.",
    },
    {
        "name": "Healthcare", "slug": "healthcare",
        "agents": "patient scheduling, benefits navigation, and intake agents",
        "intro": "Healthcare support work touches sensitive information and strict rules, so an ROI case has to survive more scrutiny than it would almost anywhere else.",
        "bullets": [
            "A scheduling agent's value depends on no show reduction and staff time saved, two numbers that rarely live in the same system",
            "Benefits navigation resolutions need a traceable record, since patients and regulators both expect one",
            "Intake agents are only worth what they save once rework and escalations are subtracted",
        ],
        "closing": "agentworth builds the audit trail into the ROI number itself, so a patient facing agent's savings come with the same documentation a compliance review would ask for.",
    },
    {
        "name": "Insurance", "slug": "insurance",
        "agents": "claims intake, policy question, and renewal agents",
        "intro": "Claims work is where an insurance AI agent either earns trust or loses it fast, because a wrong resolution on a claim is expensive in ways a support ticket never is.",
        "bullets": [
            "Claims intake agents need to be measured on accuracy of routing, not just speed of intake",
            "A policy question agent's value looks different depending on whether it prevents an escalation to a licensed adjuster",
            "Renewal agents are often credited with retention they did not actually influence",
        ],
        "closing": "agentworth separates resolutions that genuinely avoided an escalation from ones that would have closed themselves, so the ROI case for a claims agent holds up when an actuary looks at it.",
    },
    {
        "name": "Travel and hospitality", "slug": "travel-and-hospitality",
        "agents": "booking support, itinerary changes, and cancellation agents",
        "intro": "Travel support is seasonal, disruption prone, and full of edge cases, which makes a flat average resolution cost almost meaningless.",
        "bullets": [
            "A cancellation surge from a weather event or an airline outage changes the math entirely for a week at a time",
            "Itinerary change agents save different amounts depending on how close to departure the change happens",
            "Guest satisfaction after an agent interaction matters as much as whether the ticket closed",
        ],
        "closing": "agentworth tracks resolution cost against the actual disruption context, so a spike week does not quietly inflate or deflate the quarterly ROI number you report.",
    },
    {
        "name": "Telecom", "slug": "telecom",
        "agents": "billing support, outage triage, and plan change agents",
        "intro": "Telecom support volume is dominated by a small number of issue types, so most of the ROI story comes down to getting those few categories exactly right.",
        "bullets": [
            "Billing disputes resolved incorrectly tend to come back as a second, angrier ticket",
            "Outage triage agents are valuable for routing speed, not resolution count, during an incident",
            "Plan change agents touch revenue directly, so a wrong recommendation has a cost beyond the support budget",
        ],
        "closing": "agentworth flags repeat contacts automatically, so a billing agent's reported resolution rate reflects issues that actually stayed resolved, not ones that just got closed once.",
    },
    {
        "name": "Logistics and shipping", "slug": "logistics-and-shipping",
        "agents": "delivery status, exception handling, and carrier dispute agents",
        "intro": "A logistics support agent lives or dies on how it handles exceptions, since most routine status questions were never expensive to answer in the first place.",
        "bullets": [
            "The real cost savings are in exception handling, lost packages, delays, and carrier disputes, not simple tracking questions",
            "A single exception resolved badly can trigger a chain of downstream contacts across multiple stakeholders",
            "Carrier dispute outcomes need to be tied to the dollar amount actually recovered, not just the case closed",
        ],
        "closing": "agentworth separates routine status answers from exception resolutions in the ROI calculation, so the number reflects where the agent is actually earning its keep.",
    },
    {
        "name": "Edtech", "slug": "edtech",
        "agents": "student support, enrollment, and technical help desk agents",
        "intro": "Edtech support has sharp seasonal spikes around enrollment and exam periods, and the cost of a bad resolution often shows up later as a withdrawal, not an immediate complaint.",
        "bullets": [
            "Enrollment support agents are better measured against completed enrollments than against tickets closed",
            "Technical help desk resolutions during exam periods carry outsized stakes compared to the rest of the year",
            "Student churn from a poor support experience rarely gets traced back to the interaction that caused it",
        ],
        "closing": "agentworth links resolution data to downstream outcomes like completed enrollments, so an edtech support agent's ROI case accounts for what actually happened after the ticket closed.",
    },
    {
        "name": "Real estate", "slug": "real-estate",
        "agents": "leasing inquiry, maintenance request, and tenant support agents",
        "intro": "Property and leasing support work is high volume but low margin per interaction, so the ROI case depends on getting the cost per resolution genuinely right, not rounding it.",
        "bullets": [
            "Maintenance request agents are valuable for routing speed to the right vendor, not just for logging the request",
            "Leasing inquiry resolutions that do not convert to a tour or application were never worth much",
            "Tenant satisfaction after an automated interaction affects renewal rates more than any single ticket metric shows",
        ],
        "closing": "agentworth ties maintenance and leasing resolutions to the outcomes landlords actually care about, occupied units and resolved work orders, instead of a generic ticket count.",
    },
    {
        "name": "Retail banking", "slug": "retail-banking",
        "agents": "account support, card dispute, and loan inquiry agents",
        "intro": "Retail banking support sits under heavy regulatory attention, so an ROI number that cannot show its work will not survive a compliance review.",
        "bullets": [
            "Card dispute resolutions need a documented reasoning trail, not just a closed status",
            "Account support agents are judged differently depending on whether the resolution avoided a branch visit or a call",
            "Loan inquiry agents are only valuable if they route correctly, a wrong answer here is costly",
        ],
        "closing": "agentworth builds a reviewable record into every resolution, so a retail banking agent's ROI case comes with the documentation a compliance or audit team will actually ask to see.",
    },
    {
        "name": "Marketplaces", "slug": "marketplaces",
        "agents": "buyer and seller support, dispute resolution, and listing help agents",
        "intro": "Marketplace support has to satisfy two sides of every interaction at once, which makes a simple resolution count a poor stand in for whether the agent is actually working.",
        "bullets": [
            "A dispute resolved in a way that drives one side off the platform was not really a win",
            "Seller support and buyer support carry very different cost and churn implications",
            "Listing help agents are valuable for completed listings, not for the number of questions answered",
        ],
        "closing": "agentworth tracks resolutions against both sides of a marketplace transaction, so the ROI number reflects whether the agent kept the marketplace healthy, not just whether tickets got closed.",
    },
]

# ---------------------------------------------------------------------------
# COMPARISON PAGES  (/compare/<slug>/)
# ---------------------------------------------------------------------------
COMPARISONS = [
    {
        "topic": "Spreadsheets", "slug": "spreadsheets",
        "what_it_is": "A spreadsheet pieced together from a few different exports, usually rebuilt by hand every time someone asks for an updated number.",
        "breaks": [
            "Every update depends on someone remembering to pull fresh data from each source and reconcile it correctly",
            "There is no record of why a number changed from one version to the next",
            "The moment the person who built it goes on leave, the process usually breaks",
        ],
        "differs": "agentworth connects directly to the agent platform and recalculates continuously, so the number is always current and every figure can be traced back to a specific resolution instead of a manual export.",
    },
    {
        "topic": "Manual QA sampling", "slug": "manual-qa-sampling",
        "what_it_is": "A reviewer reads a small random sample of agent conversations each week and extrapolates a quality and cost figure from that sample.",
        "breaks": [
            "A small sample can easily miss the exact failure pattern that is costing the most money",
            "Sampling does not scale when volume spikes, which is exactly when quality matters most",
            "The extrapolation from sample to total is itself an estimate, stacked on top of other estimates",
        ],
        "differs": "agentworth reviews every resolution, not a sample, so the ROI number is built from the full population of conversations rather than a guess about what the rest of them probably looked like.",
    },
    {
        "topic": "Generic BI dashboards", "slug": "generic-bi-dashboards",
        "what_it_is": "A business intelligence dashboard that charts ticket volume, response time, and similar operational metrics pulled from the support platform.",
        "breaks": [
            "Operational metrics like response time do not translate into a dollar figure finance can use",
            "A generic dashboard has no concept of what a resolution was actually worth",
            "There is no way to separate what the AI agent did from what a human agent did in the same queue",
        ],
        "differs": "agentworth is built specifically to calculate ROI, not just display activity, so it separates agent driven resolutions from human ones and attaches a verified cost figure to each.",
    },
    {
        "topic": "Building it in house", "slug": "building-it-in-house",
        "what_it_is": "An internal engineering project to pull data from the agent platform's API and build a custom ROI reporting pipeline.",
        "breaks": [
            "It takes real engineering time away from product work, and it is rarely anyone's full time job to maintain",
            "Every time the agent platform changes its API or data model, the internal pipeline needs rework",
            "The resulting report usually lacks the audit trail a finance or compliance review will ask for",
        ],
        "differs": "agentworth is already built and maintained for this exact job, so the same outcome is available without the engineering time, and it comes with the audit trail built in from day one.",
    },
    {
        "topic": "Gut feel and anecdotes", "slug": "gut-feel-and-anecdotes",
        "what_it_is": "A few good examples brought to a leadership meeting to argue that the AI agent is working well.",
        "breaks": [
            "A handful of good examples says nothing about the full population of conversations",
            "Anecdotes are easy to challenge, and a skeptical finance leader usually will challenge them",
            "There is no way to track whether the anecdote still holds true a month later",
        ],
        "differs": "agentworth replaces the anecdote with a number that covers every resolution and can be checked at any time, so the case for the agent does not depend on which examples got picked for the meeting.",
    },
    {
        "topic": "Vanity metrics like tickets closed", "slug": "vanity-metrics",
        "what_it_is": "Reporting raw ticket volume or tickets closed as a stand in for the agent's actual value.",
        "breaks": [
            "A high ticket count says nothing about whether those resolutions were correct or whether the customer came back with the same issue",
            "It rewards closing tickets quickly over closing them well",
            "It cannot be converted into a dollar figure that finance will accept at face value",
        ],
        "differs": "agentworth starts from the outcome of each resolution, not the count of them, so the reported number reflects value delivered instead of activity performed.",
    },
    {
        "topic": "Your agent platform's own native reporting", "slug": "native-reporting",
        "what_it_is": "The built in analytics dashboard that ships with most AI agent platforms, showing engagement and resolution rates.",
        "breaks": [
            "Native reporting is built to show the platform in a good light, not to survive independent scrutiny",
            "It rarely connects resolution activity to an actual cost figure your finance team can use",
            "It has no way to account for the human cost it is supposedly replacing",
        ],
        "differs": "agentworth sits independently of the agent platform and calculates ROI the same way regardless of which platform you run, so the number is not graded by the vendor whose product it is measuring.",
    },
    {
        "topic": "Quarterly audits", "slug": "quarterly-audits",
        "what_it_is": "A periodic manual review, often done once a quarter, to check whether the AI agent program is still paying off.",
        "breaks": [
            "Problems that start in week two of a quarter often are not caught until the quarter ends",
            "A quarterly snapshot cannot show a trend, only a single point in time",
            "Preparing the audit itself takes real staff time that could go elsewhere",
        ],
        "differs": "agentworth calculates the number continuously, so a quarterly review becomes a report you already have instead of a project you have to start from scratch every three months.",
    },
    {
        "topic": "Customer satisfaction scores", "slug": "customer-satisfaction-scores",
        "what_it_is": "A CSAT or NPS style score collected right after a support interaction, used as a quick signal that customers are generally happy with how their issue was handled.",
        "breaks": [
            "A satisfaction score captures the customer's mood in the moment, not whether the resolution actually held or what it cost the business to deliver",
            "Survey response rates are usually low and skewed toward people who had either a very good or a very bad experience, so the score rarely represents the full population of conversations",
            "A satisfied customer can still represent a resolution that lost money, if the agent granted a refund or concession it should not have",
        ],
        "differs": "agentworth calculates ROI from the verified cost and outcome of each resolution rather than from how the customer felt about it afterward, so a feel good survey score and a sound financial number are tracked as two separate things instead of being treated as the same one.",
    },
]

# ---------------------------------------------------------------------------
# GLOSSARY PAGES  (/glossary/<slug>/)
# ---------------------------------------------------------------------------
GLOSSARY = [
    {
        "term": "Cost per resolution", "slug": "cost-per-resolution",
        "definition": "The total cost of handling one support interaction to completion, including the cost of the AI agent itself, divided across the resolutions it actually closed.",
        "matters": "It is the single number most finance teams want to see before they believe an AI agent is paying off, but it only means something if every resolution it is based on was a genuine, verified closure rather than a ticket that bounced back later.",
    },
    {
        "term": "AI agent ROI", "slug": "ai-agent-roi",
        "definition": "The net financial return an AI agent produces, calculated as the value of resolutions it handled minus what the agent itself costs to run.",
        "matters": "A positive resolution rate does not automatically mean positive ROI, since agent cost, rework, and escalations all have to be subtracted before the number means anything to a board.",
    },
    {
        "term": "Containment rate", "slug": "containment-rate",
        "definition": "The share of conversations an AI agent resolves without any human involvement at all.",
        "matters": "A high containment rate looks good on a slide, but it says nothing about whether those contained conversations were actually resolved well, which is why it should never be reported alone.",
    },
    {
        "term": "Resolution rate", "slug": "resolution-rate",
        "definition": "The percentage of conversations that end with the customer's issue actually solved, as opposed to simply closed or abandoned.",
        "matters": "Resolution rate is often confused with containment rate, but a conversation can be contained by the agent and still never actually resolve the person's problem.",
    },
    {
        "term": "Deflection rate", "slug": "deflection-rate",
        "definition": "The percentage of potential support contacts that never reach a human agent at all, often because a bot or help center article answered the question first.",
        "matters": "Deflection is frequently reported as if it were pure savings, but a deflected contact that leads to a frustrated customer coming back through another channel was not actually free.",
    },
    {
        "term": "Agent assist vs full automation", "slug": "agent-assist-vs-full-automation",
        "definition": "Agent assist means the AI supports a human who still makes the final call, while full automation means the AI resolves the interaction entirely on its own.",
        "matters": "These two modes have completely different ROI math, since agent assist still carries the full cost of a human agent's time, just potentially less of it.",
    },
    {
        "term": "Audit trail for AI decisions", "slug": "audit-trail-for-ai-decisions",
        "definition": "A timestamped, reviewable record of why an AI agent reached a particular resolution, kept separately from the resolution outcome itself.",
        "matters": "Without an audit trail, an ROI number is just a claim. With one, finance, compliance, and leadership can check it themselves instead of taking it on faith.",
    },
    {
        "term": "Time to resolution", "slug": "time-to-resolution",
        "definition": "How long it takes, from the first message to the final resolution, for a conversation to be fully closed.",
        "matters": "A fast time to resolution is only a good sign if the resolution actually held, a quick wrong answer is worse than a slower correct one.",
    },
    {
        "term": "Escalation rate", "slug": "escalation-rate",
        "definition": "The percentage of AI agent conversations that get handed off to a human instead of being resolved by the agent alone.",
        "matters": "A rising escalation rate over time can be an early warning sign that the agent is struggling with a new type of issue, well before it shows up in the overall ROI number.",
    },
    {
        "term": "First contact resolution", "slug": "first-contact-resolution",
        "definition": "Whether an issue gets solved on the very first interaction, without the customer needing to come back about the same thing.",
        "matters": "An agent can look efficient on paper while quietly generating repeat contacts, which is why first contact resolution matters as much as raw resolution count.",
    },
    {
        "term": "Cost avoidance vs cost savings", "slug": "cost-avoidance-vs-cost-savings",
        "definition": "Cost savings is money no longer being spent that used to be spent, while cost avoidance is money that was never spent because the agent handled growth that would otherwise have required hiring.",
        "matters": "Finance teams treat these two very differently, and conflating them is one of the most common ways an AI agent ROI claim loses credibility.",
    },
    {
        "term": "Human in the loop", "slug": "human-in-the-loop",
        "definition": "A setup where a human reviews or approves an AI agent's action before it takes effect, rather than the agent acting fully on its own.",
        "matters": "Human in the loop changes the ROI calculation significantly, since the human's time still needs to be counted even though the agent did most of the work.",
    },
    {
        "term": "Hallucination rate", "slug": "hallucination-rate",
        "definition": "How often an AI agent states something false or unsupported as if it were true, within its resolutions.",
        "matters": "A low hallucination rate is a prerequisite for trusting any ROI number that comes out of the same system, since a confidently wrong resolution can cost more than no resolution at all.",
    },
    {
        "term": "Ticket volume normalization", "slug": "ticket-volume-normalization",
        "definition": "Adjusting resolution and cost figures to account for seasonal or event driven swings in support volume, so one quarter can be fairly compared to another.",
        "matters": "Without normalization, a quiet quarter can look like a huge ROI win and a busy quarter can look like a failure, when neither reflects how well the agent actually performed.",
    },
    {
        "term": "Net value per resolution", "slug": "net-value-per-resolution",
        "definition": "The value created by a single resolution after subtracting the agent's share of the platform cost for that interaction.",
        "matters": "This is the number that actually answers the board's question, not the gross cost avoided, but what is left over once the agent's own cost is paid for.",
    },
    {
        "term": "Payback period for AI agents", "slug": "payback-period",
        "definition": "The amount of time it takes for an AI agent's cumulative savings to cover its total cost of deployment and operation.",
        "matters": "A short payback period is a much easier story to tell a board than a abstract ROI percentage, since it answers a concrete question in a concrete unit of time.",
    },
    {
        "term": "Agent uptime vs agent accuracy", "slug": "agent-uptime-vs-agent-accuracy",
        "definition": "Uptime measures whether the agent is running and available, while accuracy measures whether its resolutions are actually correct.",
        "matters": "A platform can report near perfect uptime while accuracy quietly declines, which is why uptime alone is never a safe proxy for whether the agent is doing its job well.",
    },
    {
        "term": "Verified ROI vs estimated ROI", "slug": "verified-roi-vs-estimated-roi",
        "definition": "Estimated ROI is calculated from assumptions typed into a model, while verified ROI is calculated from an audited record of what the agent actually did.",
        "matters": "A free calculator can give you an estimate in thirty seconds, but only a verified number, tied to an audit trail, will survive being challenged by finance or the board.",
    },
    {
        "term": "False escalation", "slug": "false-escalation",
        "definition": "An escalation to a human agent that did not actually need to happen, because the AI agent was capable of resolving the issue correctly but handed it off anyway, often out of caution, a confidence threshold set too conservatively, or a gap in what it was trained to handle.",
        "matters": "A high false escalation rate quietly inflates the human labor cost sitting behind an AI agent program, since every one of these handoffs consumes real staff time that a better tuned agent would not have needed, and it almost never shows up in a plain escalation rate figure, because that number cannot tell a necessary escalation apart from an unnecessary one.",
    },
]

# ---------------------------------------------------------------------------
# USE CASE PAGES  (/use-cases/<slug>/)
# ---------------------------------------------------------------------------
USE_CASES = [
    {
        "name": "AI support agent", "slug": "ai-support-agent",
        "scenario": "A support agent handling inbound customer questions, troubleshooting, and basic account requests across chat and email.",
        "signals": [
            "Resolution rate split between fully automated and escalated conversations",
            "Repeat contact rate, since a resolution that comes back is not really a resolution",
            "Cost per resolution compared against the fully loaded cost of a human agent handling the same volume",
        ],
    },
    {
        "name": "AI sales agent", "slug": "ai-sales-agent",
        "scenario": "An agent qualifying inbound leads, answering product questions, and booking meetings for a sales team.",
        "signals": [
            "Meetings booked and qualified pipeline generated, not just conversations handled",
            "Lead quality compared against leads a human sales development rep would have passed through",
            "Cost per qualified meeting against what a human sales development rep costs to produce the same outcome",
        ],
    },
    {
        "name": "AI ops or triage agent", "slug": "ai-ops-triage-agent",
        "scenario": "An agent that routes incoming requests, flags incidents, and prioritizes work across an operations team.",
        "signals": [
            "Routing accuracy, since a misrouted request costs more time than it saves",
            "Time to the right team, not just time to any response",
            "Reduction in operator hours spent on manual triage",
        ],
    },
    {
        "name": "AI onboarding agent", "slug": "ai-onboarding-agent",
        "scenario": "An agent guiding new users or customers through setup, activation steps, and early product questions.",
        "signals": [
            "Activation rate for users who went through the agent versus those who did not",
            "Time to first value, since a faster activation often predicts retention",
            "Support ticket volume in the first thirty days compared to before the agent was in place",
        ],
    },
    {
        "name": "AI collections agent", "slug": "ai-collections-agent",
        "scenario": "An agent handling payment reminders, payment plan negotiation, and basic account questions for overdue balances.",
        "signals": [
            "Recovery rate compared to the baseline recovery rate before the agent",
            "Customer complaint rate, since an aggressive collections agent can create more cost than it recovers",
            "Cost per dollar recovered against a human collections team handling the same accounts",
        ],
    },
    {
        "name": "AI scheduling agent", "slug": "ai-scheduling-agent",
        "scenario": "An agent booking, rescheduling, and confirming appointments across calendars and systems.",
        "signals": [
            "No show rate before and after the agent took over scheduling",
            "Staff hours saved on manual scheduling and rescheduling calls",
            "Booking completion rate compared to a human scheduler handling the same requests",
        ],
    },
    {
        "name": "AI QA agent", "slug": "ai-qa-agent",
        "scenario": "An agent reviewing support conversations, flagging quality issues, and scoring interactions instead of a human QA team sampling manually.",
        "signals": [
            "Coverage, the percentage of conversations actually reviewed, compared to manual sampling rates",
            "Agreement rate between the AI's scoring and a human reviewer's scoring on the same conversations",
            "Hours of manual QA work no longer required",
        ],
    },
    {
        "name": "AI research agent", "slug": "ai-research-agent",
        "scenario": "An agent gathering information, summarizing documents, or compiling research for an internal team.",
        "signals": [
            "Hours of analyst or researcher time saved per completed research task",
            "Accuracy of the compiled research compared against a human researched baseline",
            "Turnaround time for a research request compared to the prior process",
        ],
    },
    {
        "name": "AI compliance agent", "slug": "ai-compliance-agent",
        "scenario": "An agent reviewing documents, flagging risk, or checking communications against compliance rules.",
        "signals": [
            "Flagged issue accuracy, since a high false positive rate creates its own cost in reviewer time",
            "Coverage compared to a manual compliance review process",
            "Time to flag a genuine issue compared to the prior manual review cadence",
        ],
    },
]

# ---------------------------------------------------------------------------
# COMBINATION PAGES  (/use-cases/<industry>-<agent-type>/)
# Industry crossed with agent type, with content specific to that combination,
# not a copy paste of the separate industry and use case pages.
# ---------------------------------------------------------------------------
COMBINATIONS = [
    {
        "name": "AI compliance agent in insurance", "slug": "insurance-ai-compliance-agent",
        "intro": "A compliance agent that reviews generic documents is one kind of system. A compliance agent reviewing insurance claims and policy language sits inside state insurance regulation and market conduct exam scrutiny, and that changes what actually counts as a good resolution.",
        "bullets": [
            "A flagged issue that would never actually surface in a market conduct exam is not real risk reduction, it is just noise that costs a reviewer time",
            "A missed referral to the special investigations unit on a claim that turns out to be fraudulent costs far more than anything the agent saved that quarter",
            "Policy disclosure reviews have to be checked against each state's specific requirements, not a single generic rule set, or the flag rate does not mean much",
        ],
        "closing": "agentworth ties this combination's resolutions to the kind of findings a market conduct exam or a special investigations unit referral would actually care about, so the ROI case for a compliance agent reviewing insurance claims holds up under the same scrutiny the claims themselves face.",
        "related": [
            ("/roi-for/insurance/", "AI agent ROI for Insurance"),
            ("/use-cases/ai-compliance-agent/", "Proving ROI for an AI compliance agent"),
            ("/glossary/audit-trail-for-ai-decisions/", "Audit trail for AI decisions"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
        ],
    },
]

# ---------------------------------------------------------------------------
# FAQ PAGES  (/faq/<slug>/)
# A specific real question someone would type into Google, answered directly
# in a couple of short paragraphs.
# ---------------------------------------------------------------------------
FAQS = [
    {
        "question": "Does AI agent ROI include the labor cost of reviewing escalations?",
        "slug": "escalation-review-labor-cost",
        "subhead": "Short answer, it should, and a lot of reported numbers quietly leave it out.",
        "body": """
  <h2>Short answer</h2>
  <p>A number is only honest if it does. Every AI agent program that is not fully hands off still needs a human to review the cases the agent could not close, the ones it flagged as uncertain, or a sample of the ones it marked resolved. That reviewer's time is a real cost, and if it never gets subtracted from the agent's gross savings, the reported ROI is overstated.</p>
  <h2>Why this is easy to get wrong</h2>
  <p>Most of the savings story comes from the resolutions the agent handled on its own, so that is where the attention goes. The cost of the human layer sitting behind the agent, reviewing escalations, approving edge cases, or auditing a slice of what the agent closed, tends to live in a different budget line and gets left out of the comparison. An agent that resolves most of its queue automatically but still needs a reviewer checking a third of it is not nearly as cheap as the headline resolution rate makes it look.</p>
  <p>Before trusting a vendor's ROI claim, ask whether the stated cost per resolution already has that reviewer time subtracted, or whether it only counts the cases the agent closed without anyone looking at them. If the answer is the second one, you are looking at gross savings, not net ROI.</p>
""",
        "related": [
            ("/glossary/human-in-the-loop/", "Human in the loop"),
            ("/glossary/cost-avoidance-vs-cost-savings/", "Cost avoidance vs cost savings"),
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/compare/vanity-metrics/", "agentworth vs Vanity metrics like tickets closed"),
        ],
        "meta": "A straight answer on whether AI agent ROI numbers account for the human labor still spent reviewing escalated or flagged cases.",
    },
    {
        "question": "How long does it take to see AI agent ROI?",
        "slug": "time-to-see-ai-agent-roi",
        "subhead": "Long enough that the first few weeks of good looking numbers should not be trusted on their own.",
        "body": """
  <h2>Short answer</h2>
  <p>There is no single timeline that holds for every team, but a reasonable pattern is that a directionally useful number tends to show up within the first couple of months after launch, while a number solid enough to defend in front of a board usually needs a full quarter of data behind it.</p>
  <h2>Why it takes longer than the early numbers suggest</h2>
  <p>An agent tends to look best in its first few weeks, because it is handling the easiest, most common questions first while harder cases are still being routed to humans or tuned by hand. Early containment and resolution numbers from that period are real, but they are not representative of the full mix the agent will eventually carry.</p>
  <p>The other reason a full quarter matters is seasonality and normal volume swings. A support queue that is quiet one month and busy the next will make the same agent look like it is performing very differently from one period to the next, even though nothing about the agent itself changed. A number that only covers a few weeks has not yet had the chance to average that out.</p>
""",
        "related": [
            ("/glossary/payback-period/", "Payback period for AI agents"),
            ("/glossary/ticket-volume-normalization/", "Ticket volume normalization"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
            ("/compare/quarterly-audits/", "agentworth vs Quarterly audits"),
        ],
        "meta": "A realistic timeline for when an AI agent program starts producing a trustworthy ROI number, and why the first few weeks are usually misleading.",
    },
]

# ---------------------------------------------------------------------------
# GENERATION
# ---------------------------------------------------------------------------
all_urls = []

def write_file(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def bullets_html(items):
    return "<ul>" + "".join(f"<li>{b}</li>" for b in items) + "</ul>"

# ---- Industry pages ----
industry_cards = []
for item in INDUSTRIES:
    slug = item["slug"]
    canonical = f"/roi-for/{slug}/"
    title = f"AI agent ROI for {item['name']} — agentworth"
    meta = f"How to measure AI agent ROI for {item['name'].lower()}, the signals that matter, and where the number usually breaks."
    body = f"""
  <p>{item['intro']}</p>
  <h2>Where the number usually breaks</h2>
  {bullets_html(item['bullets'])}
  <h2>What this looks like with agentworth</h2>
  <p>{item['closing']} Typical agents in this category include {item['agents']}.</p>
"""
    others = [(i["slug"], i["name"]) for i in INDUSTRIES if i["slug"] != slug][:4]
    related = related_links(others, "/roi-for/")
    html = content_page("/roi-for/", "All industries", "ROI BY INDUSTRY", f"AI agent ROI for {item['name']}",
                         f"What proving ROI actually looks like for {item['name'].lower()} support and operations teams.",
                         body, related, title, meta, canonical)
    write_file(f"roi-for/{slug}/index.html", html)
    all_urls.append(canonical)
    industry_cards.append(f'<a href="/roi-for/{slug}/" class="af-hubcard" style="display:block"><h3>{item["name"]}</h3><p>{item["agents"]}</p></a>')

hub = hub_page("ROI BY INDUSTRY", "AI agent ROI, by industry",
               "Every industry breaks the ROI number in a different way. Pick yours.",
               "".join(industry_cards),
               "AI agent ROI by industry — agentworth", "How to measure AI agent ROI across different industries.",
               "/roi-for/")
write_file("roi-for/index.html", hub)
all_urls.append("/roi-for/")

# ---- Comparison pages ----
compare_cards = []
for item in COMPARISONS:
    slug = item["slug"]
    canonical = f"/compare/{slug}/"
    title = f"agentworth vs {item['topic']} — agentworth"
    meta = f"How agentworth compares to {item['topic'].lower()} for measuring AI agent ROI."
    body = f"""
  <h2>What {item['topic'].lower()} actually is</h2>
  <p>{item['what_it_is']}</p>
  <h2>Where it breaks down</h2>
  {bullets_html(item['breaks'])}
  <h2>How agentworth differs</h2>
  <p>{item['differs']}</p>
"""
    others = [(c["slug"], f"agentworth vs {c['topic']}") for c in COMPARISONS if c["slug"] != slug][:4]
    related = related_links(others, "/compare/")
    html = content_page("/compare/", "All comparisons", "COMPARE", f"agentworth vs {item['topic']}",
                         f"How agentworth differs from {item['topic'].lower()} as a way to measure AI agent ROI.",
                         body, related, title, meta, canonical)
    write_file(f"compare/{slug}/index.html", html)
    all_urls.append(canonical)
    compare_cards.append(f'<a href="/compare/{slug}/" class="af-hubcard" style="display:block"><h3>vs {item["topic"]}</h3><p>{item["what_it_is"][:90]}...</p></a>')

hub = hub_page("COMPARE", "agentworth vs the usual way teams measure this",
               "Most teams are not comparing agentworth to another tool, they are comparing it to no real system at all.",
               "".join(compare_cards),
               "agentworth comparisons — agentworth", "How agentworth compares to the usual ways teams try to measure AI agent ROI.",
               "/compare/")
write_file("compare/index.html", hub)
all_urls.append("/compare/")

# ---- Glossary pages ----
glossary_cards = []
for item in GLOSSARY:
    slug = item["slug"]
    canonical = f"/glossary/{slug}/"
    title = f"{item['term']} — definition — agentworth glossary"
    meta = f"What {item['term'].lower()} means, and why it matters for measuring AI agent ROI."
    body = f"""
  <h2>Definition</h2>
  <p>{item['definition']}</p>
  <h2>Why it matters</h2>
  <p>{item['matters']}</p>
"""
    others = [(g["slug"], g["term"]) for g in GLOSSARY if g["slug"] != slug][:5]
    related = related_links(others, "/glossary/")
    html = content_page("/glossary/", "All terms", "GLOSSARY", item['term'],
                         f"A plain definition of {item['term'].lower()}, and why it matters for AI agent ROI.",
                         body, related, title, meta, canonical)
    write_file(f"glossary/{slug}/index.html", html)
    all_urls.append(canonical)
    glossary_cards.append(f'<a href="/glossary/{slug}/" class="af-hubcard" style="display:block"><h3>{item["term"]}</h3><p>{item["definition"][:90]}...</p></a>')

hub = hub_page("GLOSSARY", "The AI agent ROI glossary",
               "Plain definitions for the terms that come up when a finance team starts asking hard questions about AI spend.",
               "".join(glossary_cards),
               "AI agent ROI glossary — agentworth", "Plain definitions for the terms that matter when measuring AI agent ROI.",
               "/glossary/")
write_file("glossary/index.html", hub)
all_urls.append("/glossary/")

# ---- Use case pages ----
usecase_cards = []
for item in USE_CASES:
    slug = item["slug"]
    canonical = f"/use-cases/{slug}/"
    title = f"Proving ROI for an {item['name']} — agentworth"
    meta = f"What to measure to prove ROI for an {item['name'].lower()}, and the signals that actually matter."
    body = f"""
  <h2>The use case</h2>
  <p>{item['scenario']}</p>
  <h2>What to actually measure</h2>
  {bullets_html(item['signals'])}
"""
    others = [(u["slug"], u["name"]) for u in USE_CASES if u["slug"] != slug][:4]
    related = related_links(others, "/use-cases/")
    html = content_page("/use-cases/", "All use cases", "USE CASE", f"Proving ROI for an {item['name']}",
                         f"What actually matters when measuring ROI for an {item['name'].lower()}.",
                         body, related, title, meta, canonical)
    write_file(f"use-cases/{slug}/index.html", html)
    all_urls.append(canonical)
    usecase_cards.append(f'<a href="/use-cases/{slug}/" class="af-hubcard" style="display:block"><h3>{item["name"]}</h3><p>{item["scenario"][:90]}...</p></a>')

# ---- Combination pages (industry x agent type) ----
for item in COMBINATIONS:
    slug = item["slug"]
    canonical = f"/use-cases/{slug}/"
    title = f"ROI for an {item['name']} — agentworth"
    meta = f"What changes in the ROI math for an {item['name'].lower()}, and where the number usually breaks for this combination."
    body = f"""
  <p>{item['intro']}</p>
  <h2>Where the number usually breaks</h2>
  {bullets_html(item['bullets'])}
  <h2>What this looks like with agentworth</h2>
  <p>{item['closing']}</p>
"""
    related = related_links_abs(item["related"])
    html = content_page("/use-cases/", "All use cases", "USE CASE", f"ROI for an {item['name']}",
                         f"What actually changes when you combine this industry and this agent type, and where the ROI number usually breaks.",
                         body, related, title, meta, canonical)
    write_file(f"use-cases/{slug}/index.html", html)
    all_urls.append(canonical)
    usecase_cards.append(f'<a href="/use-cases/{slug}/" class="af-hubcard" style="display:block"><h3>{item["name"]}</h3><p>{item["intro"][:90]}...</p></a>')

hub = hub_page("USE CASES", "Proving ROI, by agent type",
               "The signals that matter change depending on what the agent actually does. Find yours.",
               "".join(usecase_cards),
               "AI agent ROI by use case — agentworth", "What to measure to prove ROI for each type of AI agent.",
               "/use-cases/")
write_file("use-cases/index.html", hub)
all_urls.append("/use-cases/")

# ---- FAQ pages ----
faq_cards = []
for item in FAQS:
    slug = item["slug"]
    canonical = f"/faq/{slug}/"
    title = f"{item['question']} — agentworth FAQ"
    meta = item["meta"]
    related = related_links_abs(item["related"])
    html = content_page("/faq/", "All FAQs", "FAQ", item["question"],
                         item["subhead"],
                         item["body"], related, title, meta, canonical)
    write_file(f"faq/{slug}/index.html", html)
    all_urls.append(canonical)
    faq_cards.append(f'<a href="/faq/{slug}/" class="af-hubcard" style="display:block"><h3>{item["question"]}</h3><p>{item["subhead"][:90]}...</p></a>')

hub = hub_page("FAQ", "AI agent ROI, answered directly",
               "Specific questions people actually ask before they trust an ROI number.",
               "".join(faq_cards),
               "AI agent ROI FAQ — agentworth", "Direct answers to specific questions about measuring AI agent ROI.",
               "/faq/")
write_file("faq/index.html", hub)
all_urls.append("/faq/")

# ---- sitemap.xml ----
existing_urls = ["/", "/blog/", "/ai-agent-roi-report/", "/roi-calculator/"]
all_entries = existing_urls + all_urls
sitemap_items = "\n".join(f"  <url><loc>{SITE}{u}</loc></url>" for u in all_entries)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_items}
</urlset>
"""
write_file("sitemap.xml", sitemap)

print(f"Generated {len(all_urls)} SEO pages + 5 hub pages + sitemap.xml ({len(all_entries)} total URLs).")
