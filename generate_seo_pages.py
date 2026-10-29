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
    {
        "topic": "Task completion rate alone", "slug": "task-completion-rate-alone",
        "what_it_is": "Reporting the percentage of tasks an AI agent finished start to finish as the primary measure of whether the agent is working, without weighing what each task was actually worth.",
        "breaks": [
            "A high completion rate treats a trivial task and a complex, high stakes one as equally valuable, which flattens a picture a finance team actually needs to see",
            "Completion says nothing about whether the output was correct, only that the agent reached an end state",
            "It gives no way to compare the cost of reaching that completion against what a human would have spent reaching the same one",
        ],
        "differs": "agentworth starts from the dollar value and verified correctness of each completed task rather than the raw count of tasks finished, so two agents with the same completion rate can still show very different ROI once what they actually completed is weighed.",
    },
    {
        "topic": "Headcount reduction alone", "slug": "headcount-reduction-alone",
        "what_it_is": "Reporting the number of support or operations roles not backfilled, or roles eliminated outright, after an AI agent went live, and treating that as the dollar value the agent produced.",
        "breaks": [
            "Headcount decisions usually have several causes at once, attrition, a budget freeze, a reorganization, and crediting the full reduction to the agent overstates what it actually did",
            "It says nothing about whether the remaining team is now quietly absorbing more rework or more escalations because of gaps the agent left behind",
            "It is a single point in time measurement that never updates, while an agent's actual performance can improve or decline every month after that headcount decision was made",
        ],
        "differs": "agentworth ties savings to verified resolutions and their ongoing outcomes rather than a staffing count taken once, so the reported number keeps reflecting what the agent is doing right now instead of a decision made a year earlier for a mix of reasons.",
    },
    {
        "topic": "A/B testing agent versions without a shared ROI baseline", "slug": "ab-testing-agent-versions",
        "what_it_is": "Running two versions of an AI agent side by side and declaring whichever one shows a higher resolution or containment rate the winner, without first agreeing on what a dollar of value from either version actually looks like.",
        "breaks": [
            "A resolution rate comparison between two versions says nothing about which one is actually cheaper or more accurate if the two versions are not being measured against the same definition of a resolution",
            "A version that resolves more conversations by being more willing to close uncertain cases can look like the winner on paper while quietly producing more repeat contacts than the version it replaced",
            "Running the test for too short a window lets whichever version happened to handle an easier slice of traffic that week look better than it actually is",
        ],
        "differs": "agentworth applies the same verified ROI calculation to every version being tested, so a test between two agent configurations compares what each one was actually worth, not just which one closed more conversations during the test window.",
    },
    {
        "topic": "Vendor case studies from other customers", "slug": "vendor-case-studies",
        "what_it_is": "A published case study or benchmark figure from a different company already running the same AI agent platform, used as a stand in for what your own program is likely to achieve.",
        "breaks": [
            "A case study customer's ticket mix, team structure, and starting cost per resolution are rarely close enough to yours for their percentage improvement to transfer directly to your own numbers",
            "Vendors publish their best results, so any single case study is a sample of one taken from the high end of the outcome range, not a typical outcome",
            "A published figure almost never shows enough of its own methodology to tell whether it was calculated the way you would calculate yours, so comparing the two numbers is comparing two different definitions wearing the same label",
        ],
        "differs": "agentworth calculates ROI from your own resolutions and your own cost baseline instead of borrowing someone else's outcome, so the number you report is specific to what your agent actually did, not to what a different company's agent did somewhere else.",
    },
    {
        "topic": "Engagement metrics like session length or messages per conversation", "slug": "engagement-metrics-alone",
        "what_it_is": "Reporting how long a conversation with an AI agent ran, or how many messages it took to get through it, as a stand in for whether the agent is actually doing a good job.",
        "breaks": [
            "A longer conversation can mean the agent is working through a genuinely complex issue, or it can mean the agent is struggling and making the customer repeat themselves, and engagement metrics alone cannot tell those two apart",
            "A short, low message count conversation looks efficient on a dashboard even when it ended because the customer gave up rather than because the issue actually got solved",
            "Session length and message count say nothing about cost or outcome, so neither one converts into a number finance can use to judge whether the agent is worth what it costs to run",
        ],
        "differs": "agentworth calculates ROI from the verified outcome and cost of each resolution rather than from how long or how chatty the conversation was, so a short conversation that solved nothing and a long conversation that solved something complex are never confused with each other.",
    },
    {
        "topic": "Average handle time alone", "slug": "average-handle-time-alone",
        "what_it_is": "Reporting how quickly an AI agent gets through a conversation, from first message to close, as a stand in for whether the agent is doing a good job.",
        "breaks": [
            "A fast handle time can mean the agent solved the issue efficiently, or it can mean the agent closed the conversation before the issue was actually fixed, and handle time alone cannot tell those two apart",
            "A longer conversation that correctly worked through a genuinely complicated issue looks worse on a handle time chart than a short conversation that gave the customer a wrong answer and sent them away",
            "Handle time has no concept of cost or outcome built into it, so it cannot be converted into a number finance can use to decide whether the agent is worth what it costs to run",
        ],
        "differs": "agentworth calculates ROI from the verified outcome and cost of each resolution rather than from how long the conversation took to close, so a fast conversation that never actually solved anything and a slower conversation that solved something difficult are judged on what they accomplished, not on the clock.",
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
    {
        "term": "Build versus buy for AI agents", "slug": "build-versus-buy-for-ai-agents",
        "definition": "The decision between purchasing a prebuilt AI agent platform and building a custom one in house, weighed not just on upfront cost but on who ends up responsible for the ongoing accuracy, maintenance, and reporting work once it is live.",
        "matters": "Teams usually compare this decision on licensing cost alone, but the real cost difference tends to show up later, in whichever side ends up responsible for proving the agent actually works and keeps working as volume and use cases change.",
    },
    {
        "term": "Vendor lock in for AI agents", "slug": "vendor-lock-in-for-ai-agents",
        "definition": "The degree to which a company's resolution data, workflows, and reporting are tied to a single AI agent vendor's platform, making it difficult or costly to switch providers or compare vendors against each other later.",
        "matters": "A heavily locked in setup makes it hard to challenge a vendor's own reported numbers, since there is no independent way to check them without first extracting data the platform was never built to export.",
    },
    {
        "term": "Quality assurance scorecard", "slug": "quality-assurance-scorecard",
        "definition": "A structured set of criteria used to score an individual support interaction, usually covering whether the information given was accurate, whether policy was followed, and whether the tone matched what the situation called for.",
        "matters": "An AI agent program that only tracks resolution rate can look healthy while quietly failing most of the dimensions a quality scorecard would catch, since a conversation can end in a technical resolution and still be wrong, rude, or off policy.",
    },
    {
        "term": "Agent confidence score", "slug": "agent-confidence-score",
        "definition": "An internal probability or score an AI agent assigns to its own answer before deciding whether to respond directly or hand the conversation to a human.",
        "matters": "The threshold behind this score is a tuning choice, not a measure of accuracy on its own, set it too conservatively and false escalations climb, set it too aggressively and the agent starts delivering wrong answers with full confidence, so reporting the score itself as an ROI metric tells you almost nothing without knowing where the threshold sits.",
    },
    {
        "term": "Average handle time", "slug": "average-handle-time",
        "definition": "The average length of time an agent, human or AI, spends on a single interaction from the moment it starts to the moment it is marked resolved or closed.",
        "matters": "A falling average handle time is often presented as proof an AI agent is working well, but a faster interaction that ends in a wrong or incomplete answer costs more later than a slower one that actually solved the problem, so handle time on its own says nothing about whether the resolution held.",
    },
    {
        "term": "Shadow IT in support", "slug": "shadow-it-in-support",
        "definition": "Support or operations staff adopting an AI agent, browser extension, or automation tool on their own, without it going through procurement, security review, or the official system a company uses to track resolutions and cost.",
        "matters": "An agent running outside the official reporting system can still be handling real conversations and producing real cost outcomes that never make it into the ROI number anyone is tracking, so the reported figure can be wrong in either direction without anyone noticing until a security review or an unrelated audit turns it up.",
    },
    {
        "term": "SLA attainment", "slug": "sla-attainment",
        "definition": "The percentage of support interactions that meet the specific response and resolution time commitments written into a service level agreement, measured against that agreement rather than against a general sense of how fast the team feels.",
        "matters": "A team can report a healthy average resolution time while still missing SLA attainment on exactly the accounts that matter most, since an average quietly absorbs the slow outliers that a contract actually penalizes, which is why an AI agent program needs this tracked as its own number instead of folded into a general speed metric.",
    },
    {
        "term": "Ticket backlog", "slug": "ticket-backlog",
        "definition": "The number of support conversations sitting unresolved at a single point in time, waiting for either a human or an AI agent to pick them up, as distinct from how many conversations came in or got closed during the same period.",
        "matters": "A shrinking queue count looks good on a dashboard, but it can shrink because an AI agent is closing cases quickly without actually solving them, just as easily as it can shrink because the agent is doing good work, so backlog size on its own cannot tell the two apart.",
    },
    {
        "term": "Silent failure", "slug": "silent-failure",
        "definition": "A resolution an AI agent marks as successfully closed that did not actually solve the customer's problem, with no error message, confidence flag, or escalation anywhere in the system to show that anything went wrong.",
        "matters": "A silent failure is the most expensive kind of mistake an AI agent can make, because it never shows up as a flagged case for a reviewer to catch, it only shows up later as a repeat contact, a churned account, or a frustrated customer, usually long after anyone would think to go looking for it.",
    },
    {
        "term": "Agent utilization rate", "slug": "agent-utilization-rate",
        "definition": "The share of an AI agent's available capacity spent on conversations that actually reach a resolution, as opposed to idle time, retries, or conversations that end without one.",
        "matters": "A high utilization number can describe an agent that stays constantly busy without being effective, since retries and abandoned conversations both use up capacity without producing a resolution worth counting toward ROI, so utilization needs to be read alongside resolution rate rather than on its own.",
    },
    {
        "term": "Cost center vs profit center framing", "slug": "cost-center-vs-profit-center-framing",
        "definition": "Whether an AI agent program gets evaluated as an expense to be minimized, the way a cost center is judged, or as an investment expected to produce a return, the way a profit center is judged.",
        "matters": "The framing a finance team picks changes which questions get asked about the program. A cost center framing rewards cutting the agent's own spend, even if that means a cheaper setup that resolves less, while a profit center framing asks whether the net value produced is growing, which can justify spending more on the agent when the resolutions it produces are worth more than they cost.",
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
    {
        "name": "AI support agent in ecommerce", "slug": "ecommerce-ai-support-agent",
        "intro": "A generic support agent gets measured on resolution rate and cost per ticket. A support agent sitting inside ecommerce lives inside order cycles, return windows, and payment processing, and that context changes what a resolution is actually worth.",
        "bullets": [
            "A where is my order question closed before the package actually arrives is not a real resolution if the customer contacts support again once it still has not shown up",
            "Return and refund conversations carry a real dollar cost that has to be subtracted from the savings, since granting a refund the policy did not call for is not a win even if the ticket closed cleanly",
            "Checkout and payment failure questions spike hard around sales events, and a support agent handling that spike needs to be judged against that volume, not against a normal week",
        ],
        "closing": "agentworth ties this combination's resolutions to order status and refund outcomes rather than ticket count alone, so an ecommerce support agent's ROI case reflects whether packages actually arrived and refunds were actually warranted, not just whether the conversation ended.",
        "related": [
            ("/roi-for/ecommerce/", "AI agent ROI for Ecommerce"),
            ("/use-cases/ai-support-agent/", "Proving ROI for an AI support agent"),
            ("/glossary/first-contact-resolution/", "First contact resolution"),
            ("/glossary/cost-avoidance-vs-cost-savings/", "Cost avoidance vs cost savings"),
        ],
    },
    {
        "name": "AI collections agent in fintech", "slug": "fintech-ai-collections-agent",
        "intro": "A collections agent handling overdue retail accounts is one kind of system. A collections agent working inside a fintech lender or card issuer sits under fair lending and debt collection rules that govern exactly what can be said, how often, and through which channel, and that changes what a good resolution actually looks like.",
        "bullets": [
            "A payment plan the agent talked a customer into that gets reversed or disputed within the week was never a real recovery, even though it closed the conversation as resolved that day",
            "Communication frequency and channel limits mean a technically correct reminder sent at the wrong time or too often can turn into a complaint that costs far more than the balance it was chasing",
            "Recovery rate on its own hides whether the agent is reaching people earlier in the delinquency cycle, when recovery is cheap, or only catching the harder, later stage accounts where recovery was always going to be expensive",
        ],
        "closing": "agentworth ties this combination's resolutions to whether a payment plan actually held and whether contact rules were followed, not just whether the balance was eventually paid, so the ROI case for a fintech collections agent survives a compliance review as well as a finance one.",
        "related": [
            ("/roi-for/fintech/", "AI agent ROI for Fintech"),
            ("/use-cases/ai-collections-agent/", "Proving ROI for an AI collections agent"),
            ("/glossary/false-escalation/", "False escalation"),
            ("/compare/customer-satisfaction-scores/", "agentworth vs Customer satisfaction scores"),
        ],
    },
    {
        "name": "AI scheduling agent in healthcare", "slug": "healthcare-ai-scheduling-agent",
        "intro": "A scheduling agent booking restaurant reservations is one kind of system. A scheduling agent booking patient appointments sits inside provider calendars, insurance eligibility windows, and clinical urgency rules, and that context changes what counts as a good booking.",
        "bullets": [
            "A booked appointment that gets cancelled once insurance eligibility turns out not to cover the visit was never really booked, and that gap rarely shows up until the claim is filed weeks later",
            "No show reduction only counts as savings if the slot that opened back up actually got filled by another patient, otherwise the agent reduced no shows without recovering any revenue",
            "Rescheduling a routine checkup and rescheduling a time sensitive followup carry very different costs if the delay affects a patient's care, and a flat reschedule count treats them the same",
        ],
        "closing": "agentworth ties this combination's bookings to whether the visit actually happened and whether the freed up slot got filled, not just whether a confirmation was sent, so the ROI case for a healthcare scheduling agent reflects filled calendars and completed visits rather than booking activity alone.",
        "related": [
            ("/roi-for/healthcare/", "AI agent ROI for Healthcare"),
            ("/use-cases/ai-scheduling-agent/", "Proving ROI for an AI scheduling agent"),
            ("/glossary/cost-avoidance-vs-cost-savings/", "Cost avoidance vs cost savings"),
            ("/compare/headcount-reduction-alone/", "agentworth vs Headcount reduction alone"),
        ],
    },
    {
        "name": "AI onboarding agent in SaaS", "slug": "saas-ai-onboarding-agent",
        "intro": "An onboarding agent guiding a free trial user through initial setup is one kind of system. An onboarding agent working inside a SaaS product sits upstream of activation, expansion, and renewal, and that position changes what a good onboarding resolution is actually worth.",
        "bullets": [
            "A completed setup step that never leads to the user reaching their first meaningful outcome in the product was not really onboarding, it was just a checklist getting ticked off",
            "An onboarding agent that answers questions quickly but skips the configuration steps that predict long term retention looks efficient in week one and shows up as churn two quarters later",
            "Self serve accounts and sales assisted accounts need different onboarding paths, and crediting the agent with activation on an account a customer success manager was already walking through overstates what it actually did",
        ],
        "closing": "agentworth ties this combination's resolutions to activation and the retention outcomes that follow, not to setup steps completed, so the ROI case for a SaaS onboarding agent reflects accounts that actually got value, not just accounts that got through a checklist.",
        "related": [
            ("/roi-for/saas/", "AI agent ROI for SaaS"),
            ("/use-cases/ai-onboarding-agent/", "Proving ROI for an AI onboarding agent"),
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/compare/task-completion-rate-alone/", "agentworth vs Task completion rate alone"),
        ],
    },
    {
        "name": "AI ops or triage agent in logistics and shipping", "slug": "logistics-and-shipping-ai-ops-triage-agent",
        "intro": "A triage agent sorting generic support requests is one kind of system. A triage agent sorting incoming shipment exceptions, delayed packages, and carrier incident reports sits inside delivery promises and the carrier contracts that back them, and that context changes what a correctly triaged case is actually worth.",
        "bullets": [
            "A delay correctly flagged as urgent three hours after the shipment already missed its delivery window did not actually prevent anything, even though the triage step technically happened on time",
            "Carrier dispute routing has to point a case at the specific carrier relationship and the specific contract clause that applies, since sending it to the wrong queue can burn the limited window a contract allows for filing a claim",
            "A spike in exception volume during a single severe weather event or a carrier network outage should not be allowed to make a normally reliable triage agent look like it suddenly got worse, the ROI math needs to separate a bad week from a bad agent",
        ],
        "closing": "agentworth ties this combination's triage decisions to whether the right team or carrier actually received the case in time to act on it, not just whether a priority label got applied, so the ROI case for a logistics triage agent reflects shipments actually saved and disputes actually filed on time, not routing activity alone.",
        "related": [
            ("/roi-for/logistics-and-shipping/", "AI agent ROI for Logistics and shipping"),
            ("/use-cases/ai-ops-triage-agent/", "Proving ROI for an AI ops or triage agent"),
            ("/glossary/false-escalation/", "False escalation"),
            ("/glossary/sla-attainment/", "SLA attainment"),
        ],
    },
    {
        "name": "AI sales agent in real estate", "slug": "real-estate-ai-sales-agent",
        "intro": "A sales agent qualifying leads for a software trial is one kind of system. A sales agent qualifying leasing inquiries and buyer interest in real estate sits inside tour schedules, listing availability, and financing qualification, and that context changes what a good qualified lead is actually worth.",
        "bullets": [
            "A lead the agent marks as qualified that never actually shows up for the scheduled tour was not really a qualified lead, even though the booking itself happened without any issues",
            "Financing and affordability questions have to be answered correctly before a lead is worth passing to a leasing agent or broker, since a wrong prequalification wastes a human agent's time on someone who was never going to close",
            "Listing availability changes constantly, and a sales agent working from a stale listing feed can qualify real interest in a unit that is no longer on the market, which costs more goodwill than the lead itself was worth",
        ],
        "closing": "agentworth ties this combination's qualified leads to whether the tour or showing actually happened and whether the listing was still available when the conversation occurred, not just whether the agent collected the right information, so the ROI case for a real estate sales agent reflects tours completed and applications started rather than qualification activity alone.",
        "related": [
            ("/roi-for/real-estate/", "AI agent ROI for Real estate"),
            ("/use-cases/ai-sales-agent/", "Proving ROI for an AI sales agent"),
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/compare/task-completion-rate-alone/", "agentworth vs Task completion rate alone"),
        ],
    },
    {
        "name": "AI ops or triage agent in telecom", "slug": "telecom-ai-ops-triage-agent",
        "intro": "A triage agent sorting generic internal requests is one kind of system. A triage agent sorting incoming telecom outage reports, billing escalations, and field technician dispatch requests sits inside customer SLA commitments and network restoration timelines, and that context changes what a correctly triaged case is actually worth.",
        "bullets": [
            "A case flagged urgent after an outage has already cascaded to a wider service area did not actually help, even though the flag itself was technically correct",
            "Billing escalations and network outage reports need to route to completely different teams with completely different urgency models, and a triage agent that treats them on the same priority scale will misroute the one that actually has a ticking SLA clock",
            "A single regional outage can flood the queue with hundreds of reports of the same root issue, and the ROI math needs to recognize duplicate reports instead of crediting the agent with resolving hundreds of separate cases",
        ],
        "closing": "agentworth ties this combination's triage decisions to whether the right technician or team received the case while the SLA clock still had room left, and collapses duplicate reports of the same outage into one tracked incident, so the ROI case for a telecom triage agent reflects outages actually addressed on time, not raw ticket volume routed.",
        "related": [
            ("/roi-for/telecom/", "AI agent ROI for Telecom"),
            ("/use-cases/ai-ops-triage-agent/", "Proving ROI for an AI ops or triage agent"),
            ("/glossary/sla-attainment/", "SLA attainment"),
            ("/glossary/false-escalation/", "False escalation"),
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
    {
        "question": "What counts as a resolution for ROI purposes?",
        "slug": "what-counts-as-a-resolution-for-roi-purposes",
        "subhead": "Not every closed ticket is a resolution, and the gap between the two is where a lot of ROI numbers quietly fall apart.",
        "body": """
  <h2>Short answer</h2>
  <p>A resolution, for ROI purposes, should mean the customer's actual issue was solved and stayed solved, not that a ticket status changed to closed. Those are two different things, and a system that only tracks the second one will always report a higher number than the first one would support.</p>
  <h2>Why the difference matters</h2>
  <p>A ticket can be closed for reasons that have nothing to do with the issue being fixed. A customer gives up and stops responding, an agent closes a case to clear a queue, or a conversation times out after a set number of hours. None of those are resolutions in any meaningful sense, but all of them can inflate a reported resolution count if the system counts by status rather than by outcome.</p>
  <p>A tighter definition checks whether the same issue comes back within a reasonable window. If it does, the original closure was not really a resolution regardless of what the status field said, and counting it as one overstates what the agent actually accomplished.</p>
""",
        "related": [
            ("/glossary/first-contact-resolution/", "First contact resolution"),
            ("/glossary/resolution-rate/", "Resolution rate"),
            ("/glossary/deflection-rate/", "Deflection rate"),
            ("/compare/vanity-metrics/", "agentworth vs Vanity metrics like tickets closed"),
        ],
        "meta": "A direct answer to what should count as a resolution when measuring AI agent ROI, and why closed ticket counts overstate the real number.",
    },
    {
        "question": "Should AI agent ROI include the cost of failed deployments?",
        "slug": "cost-of-failed-deployments",
        "subhead": "At the company level, yes, even though that cost will never show up in the ROI of the one agent that finally worked.",
        "body": """
  <h2>Short answer</h2>
  <p>If you are asking whether a single agent's own ROI number should be penalized for a different, earlier attempt that was scrapped, the answer is no, that number should reflect what this agent is actually doing today. But if you are asking whether the company should count that earlier failed attempt somewhere when deciding whether the overall AI agent program has paid off, the answer is yes, and most teams quietly skip this step.</p>
  <h2>Why it still belongs in the bigger picture</h2>
  <p>A failed deployment is rarely free. There is the platform cost paid before it was scrapped, the engineering and operations time spent integrating and then unwinding it, and the support team's time spent working around an agent that was not yet reliable. None of that disappears just because the project ended before producing a usable resolution number.</p>
  <p>Treating each new deployment attempt as a clean slate makes the program as a whole look better than it has actually been, since the cost of the attempts that did not work never gets weighed against the savings of the one that did. A company level view should add up every attempt, successful or not, against the total savings delivered so far, while each individual agent's reported ROI stays focused on what that agent is doing right now.</p>
""",
        "related": [
            ("/glossary/payback-period/", "Payback period for AI agents"),
            ("/glossary/build-versus-buy-for-ai-agents/", "Build versus buy for AI agents"),
            ("/compare/building-it-in-house/", "agentworth vs Building it in house"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
        ],
        "meta": "A direct answer on whether the cost of a scrapped or failed AI agent deployment should count against the program's AI agent ROI.",
    },
    {
        "question": "Does AI agent ROI include the cost of LLM API calls?",
        "slug": "llm-api-costs-in-ai-agent-roi",
        "subhead": "It should, and a number that only counts the subscription fee is leaving out a cost that moves with volume.",
        "body": """
  <h2>Short answer</h2>
  <p>Yes. The cost of calling the underlying language model, whether that is a per token fee to a model provider or usage based pricing baked into a platform's bill, is a direct cost of running the agent and belongs in the same place as the platform subscription fee. Leaving it out understates what the agent actually costs to operate.</p>
  <h2>Why it gets left out</h2>
  <p>A platform's sticker price is usually a flat monthly or annual number that is easy to drop into a spreadsheet. The underlying model cost is usage based and can swing with ticket volume, conversation length, and how many times the agent calls the model to reach a single resolution, so it is harder to pin down and easier to quietly ignore. A team that compares only the subscription fee against the cost of a human agent is comparing an apples to oranges pair of numbers, since the human cost already includes everything needed to do the work.</p>
  <p>The gap matters most at scale. A model cost that looks trivial per conversation can add up to a meaningful figure once it is multiplied across a full quarter of volume, and a sudden jump in conversation length or model calls per resolution can erode margin that a flat subscription fee view would never catch.</p>
""",
        "related": [
            ("/glossary/cost-per-resolution/", "Cost per resolution"),
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/compare/native-reporting/", "agentworth vs Your agent platform's own native reporting"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
        ],
        "meta": "A direct answer on whether AI agent ROI should include the cost of LLM or model API calls, and why that cost is easy to leave out.",
    },
    {
        "question": "How often should AI agent ROI be reported to the board?",
        "slug": "how-often-to-report-ai-agent-roi-to-the-board",
        "subhead": "Quarterly is the common rhythm, but the number behind that update should already be tracked continuously, not assembled from scratch each time.",
        "body": """
  <h2>Short answer</h2>
  <p>Most finance and operations leaders settle on a quarterly cadence for a formal board update, since that matches how most other operating metrics get reported and gives enough time for a trend to actually mean something. A monthly update is common at the operational level, between the team running the agent and whoever they report to day to day, but a quarterly figure is usually what reaches the board itself.</p>
  <h2>Why the cadence matters less than the process behind it</h2>
  <p>The real risk is not reporting too rarely, it is building the report from scratch each time. A team that pulls a fresh export, reconciles it by hand, and recalculates the ROI figure every quarter is likely to produce a slightly different number using a slightly different method on each pass, which invites exactly the kind of scrutiny a board update is supposed to survive.</p>
  <p>A program that calculates ROI continuously can report on whatever cadence the board actually wants, monthly, quarterly, or on demand ahead of a specific decision, because the underlying number does not change depending on when someone happens to ask for it. Cadence then becomes a reporting choice rather than a constraint set by how much manual work it takes to produce the figure.</p>
""",
        "related": [
            ("/glossary/payback-period/", "Payback period for AI agents"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
            ("/compare/quarterly-audits/", "agentworth vs Quarterly audits"),
            ("/glossary/ticket-volume-normalization/", "Ticket volume normalization"),
        ],
        "meta": "A direct answer on how often AI agent ROI should reach the board, and why the reporting cadence matters less than whether the number is built the same way every time.",
    },
    {
        "question": "What is a good ROI percentage for an AI agent?",
        "slug": "what-is-a-good-roi-percentage-for-an-ai-agent",
        "subhead": "There is no universal number, and a figure that looks great on its own can still be wrong once you check how it was calculated.",
        "body": """
  <h2>Short answer</h2>
  <p>There is no single percentage that counts as good across every team, since the right number depends on what the agent costs to run, what it replaced, and how that cost baseline was set in the first place. A team with a very low cost per resolution to begin with will show a smaller percentage gain than a team starting from an expensive, inefficient process, even if the second team's agent is actually doing worse work.</p>
  <h2>Why the percentage matters less than the method behind it</h2>
  <p>A reported return of several hundred percent sounds impressive, but it is only meaningful if the cost side of that calculation includes everything it should, the platform fee, the underlying model cost, the labor still spent reviewing escalations, and the cost of resolutions that did not actually hold. A number built from an incomplete cost picture will always look better than one built honestly, regardless of what the agent is actually doing.</p>
  <p>Before comparing a reported ROI percentage against some benchmark, it is worth asking the more basic question first, what counts as a resolution in that calculation, and what costs were subtracted to arrive at the final number. Two teams reporting the same percentage can be describing very different realities underneath it.</p>
""",
        "related": [
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
            ("/glossary/cost-per-resolution/", "Cost per resolution"),
            ("/compare/vanity-metrics/", "agentworth vs Vanity metrics like tickets closed"),
        ],
        "meta": "A direct answer on what counts as a good ROI percentage for an AI agent, and why the percentage matters less than how it was calculated.",
    },
    {
        "question": "Can AI agent ROI be negative, and what does that actually mean?",
        "slug": "can-ai-agent-roi-be-negative",
        "subhead": "Yes, and a negative number is sometimes more trustworthy than a positive one that was calculated carelessly.",
        "body": """
  <h2>Short answer</h2>
  <p>Yes. If the agent's cost, including the platform fee, the cost of the human review it still requires, and the cost of resolutions that did not actually hold, adds up to more than the value of what it resolved, the ROI number is negative. That is a real possible outcome, not a sign the calculation went wrong.</p>
  <h2>Why a negative number can be the honest one</h2>
  <p>Most of the pressure on an ROI report runs in one direction, toward a positive number that justifies the program. A team under that pressure can get there by leaving out a cost category, counting a resolution that did not really hold, or picking a generous baseline for what a human would have cost to do the same work. A negative number that survives an honest accounting of every cost is more trustworthy than a positive one built on a few convenient omissions.</p>
  <p>A negative ROI is also not necessarily a verdict on the agent itself. It can mean the agent is still early in its rollout, that escalation volume has not yet settled down, or that the use case it was pointed at was simply too hard for the agent in its current state. The honest next step is to look at which part of the calculation is driving the negative number, not to adjust the calculation until it turns positive.</p>
""",
        "related": [
            ("/glossary/net-value-per-resolution/", "Net value per resolution"),
            ("/glossary/verified-roi-vs-estimated-roi/", "Verified ROI vs estimated ROI"),
            ("/glossary/payback-period/", "Payback period for AI agents"),
            ("/compare/vanity-metrics/", "agentworth vs Vanity metrics like tickets closed"),
        ],
        "meta": "A direct answer on whether AI agent ROI can be negative, why that can still be the honest number, and what it actually indicates about the program.",
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
