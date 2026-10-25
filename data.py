"""
Sample data mirroring the KAN ATS Analytics screens.
Replace each dict with SQLAlchemy queries (filtered by period, team, recruiter, etc.) later.
"""

# ---------------------------------------------------------------------------
# 1. Performance overview
# ---------------------------------------------------------------------------
PERFORMANCE_OVERVIEW = {
    "cohort_note": "Cohort: candidates submitted in selected period · Outcomes as of 17 Oct 2026 · Currency: INR",
    "kpis": [
        {"label": "Candidates submitted", "value": "480", "delta": "▲ 12% vs. previous quarter", "tone": "good"},
        {"label": "Qualified candidates", "value": "288", "sub": "60.0% qualification rate"},
        {"label": "Interviews attended", "value": "192", "delta": "▲ 8% vs. previous quarter", "tone": "good"},
        {"label": "Offers released", "value": "48", "delta": "▲ 9% vs. previous quarter", "tone": "good"},
        {"label": "Joiners", "value": "36", "sub": "75.0% offer-to-join"},
        {"label": "Median time to fill", "value": "32 days", "delta": "▼ 18% vs. previous quarter", "tone": "good"},
    ],
    "funnel": [
        {"label": "Submitted", "value": 480},
        {"label": "Qualified", "value": 288},
        {"label": "Interviewed", "value": 192},
        {"label": "Offered", "value": 48},
        {"label": "Joined", "value": 36},
    ],
    "internal_vs_external": [
        {"stage": "Submitted", "internal": 300, "external": 180},
        {"stage": "Offers", "internal": 32, "external": 16},
        {"stage": "Joiners", "internal": 24, "external": 12},
    ],
    "agency_economics": [
        {"label": "Fees incurred", "value": "₹6.0L"},
        {"label": "Cost per agency joiner", "value": "₹50,000"},
        {"label": "90-day retention", "value": "90%"},
    ],
    "performance_table": [
        {"name": "Aditi Sharma", "type": "Internal", "assigned_reqs": 12, "submitted": 120, "qualified_pct": "65.0%",
         "interviews": 52, "offers": 14, "joiners": 11, "offer_to_join": "78.6%", "median_ttf": "28d", "retention_90d": "95%"},
        {"name": "Rahul Mehta", "type": "Internal", "assigned_reqs": 10, "submitted": 100, "qualified_pct": "60.0%",
         "interviews": 40, "offers": 10, "joiners": 7, "offer_to_join": "70.0%", "median_ttf": "31d", "retention_90d": "90%"},
        {"name": "Sneha Patel", "type": "Internal", "assigned_reqs": 8, "submitted": 80, "qualified_pct": "52.5%",
         "interviews": 28, "offers": 8, "joiners": 6, "offer_to_join": "75.0%", "median_ttf": "34d", "retention_90d": "92%"},
        {"name": "TalentBridge", "type": "External", "assigned_reqs": 8, "submitted": 90, "qualified_pct": "60.0%",
         "interviews": 36, "offers": 8, "joiners": 6, "offer_to_join": "75.0%", "median_ttf": "30d", "retention_90d": "94%"},
        {"name": "HireSphere", "type": "External", "assigned_reqs": 6, "submitted": 60, "qualified_pct": "60.0%",
         "interviews": 24, "offers": 6, "joiners": 5, "offer_to_join": "83.3%", "median_ttf": "35d", "retention_90d": "91%"},
        {"name": "Apex Staffing", "type": "External", "assigned_reqs": 4, "submitted": 30, "qualified_pct": "60.0%",
         "interviews": 12, "offers": 2, "joiners": 1, "offer_to_join": "50.0%", "median_ttf": "42d",
         "median_ttf_flag": True, "retention_90d": "75%"},
    ],
    "needs_attention": [
        {"title": "Apex Staffing", "detail": "42-day median time to fill", "cta": "View", "tone": "warning"},
        {"title": "Rahul Mehta", "detail": "3 offers without a joining", "cta": "View", "tone": "warning"},
    ],
    "drilldowns": [
        {"title": "View candidate outcomes", "detail": "See stage-wise conversion by recruiter or agency", "cta": "Open"},
        {"title": "Inspect source attribution", "detail": "Identify top performing sources", "cta": "Open"},
        {"title": "Review agency fees", "detail": "Analyse cost, joiners and ROI", "cta": "Open"},
    ],
}

# ---------------------------------------------------------------------------
# 2. Internal recruiters
# ---------------------------------------------------------------------------
INTERNAL_RECRUITERS = {
    "kpis": [
        {"label": "Submitted", "value": "300", "delta": "▲ 12% vs. previous quarter", "tone": "good"},
        {"label": "Qualified", "value": "180", "sub": "60.0% of submitted"},
        {"label": "Interviews attended", "value": "120", "delta": "▲ 8% vs. previous quarter", "tone": "good"},
        {"label": "Offers released", "value": "32", "delta": "▲ 6% vs. previous quarter", "tone": "good"},
        {"label": "Joiners", "value": "24", "sub": "75.0% offer-to-join"},
        {"label": "Median time to fill", "value": "31 days", "delta": "▼ 15% vs. previous quarter", "tone": "good"},
    ],
    "funnel": [
        {"label": "Submitted", "value": 300},
        {"label": "Qualified", "value": 180},
        {"label": "Interviewed", "value": 120},
        {"label": "Offered", "value": 32},
        {"label": "Joined", "value": 24},
    ],
    "joiners_vs_target": [
        {"month": "July 2026", "joined": 6, "target": 8},
        {"month": "August 2026", "joined": 8, "target": 10},
        {"month": "September 2026", "joined": 10, "target": 12},
    ],
    "workload": [
        {"label": "Open requisitions", "value": 30},
        {"label": "Overdue follow-ups", "value": 18},
        {"label": "Feedback requests pending", "value": 7},
    ],
    "recruiters": [
        {"name": "Aditi Sharma", "assigned_reqs": 12, "submitted": 120, "qualified_pct": "65.0%", "interviews": 52,
         "offers": 14, "joiners": 11, "target": 12, "achievement": 91.7, "offer_to_join": "78.6%", "median_ttf": "28d"},
        {"name": "Rahul Mehta", "assigned_reqs": 10, "submitted": 100, "qualified_pct": "60.0%", "interviews": 40,
         "offers": 10, "joiners": 7, "target": 10, "achievement": 70.0, "offer_to_join": "70.0%", "median_ttf": "31d"},
        {"name": "Sneha Patel", "assigned_reqs": 8, "submitted": 80, "qualified_pct": "52.5%", "interviews": 28,
         "offers": 8, "joiners": 6, "target": 8, "achievement": 75.0, "offer_to_join": "75.0%", "median_ttf": "34d"},
    ],
    "totals": {"name": "Total", "assigned_reqs": 30, "submitted": 300, "qualified_pct": "60.0%", "interviews": 120,
               "offers": 32, "joiners": 24, "target": 30, "achievement": 80.0, "offer_to_join": "75.0%", "median_ttf": "31d"},
    "selected": {"name": "Aditi Sharma", "joining_progress": "11 / 12", "submission_to_join": "9.2%", "pending_offers": "3"},
    "actions": [
        {"title": "Rahul Mehta", "detail": "Confirm 3 outstanding offer outcomes", "cta": "View", "tone": "neutral"},
        {"title": "Sneha Patel", "detail": "Review screening rejection reasons", "cta": "View", "tone": "neutral"},
        {"title": "Team", "detail": "Resolve 7 pending feedback requests", "cta": "View", "tone": "neutral"},
    ],
}

# ---------------------------------------------------------------------------
# 3. External agencies
# ---------------------------------------------------------------------------
EXTERNAL_AGENCIES = {
    "kpis": [
        {"label": "Submissions", "value": "180"},
        {"label": "Qualified", "value": "108", "sub": "60% of submitted"},
        {"label": "Interviews", "value": "72"},
        {"label": "Offers", "value": "16"},
        {"label": "Joiners", "value": "12", "sub": "75% offer-to-join"},
        {"label": "Agency fees", "value": "₹6.0L", "sub": "₹50,000 per joiner"},
    ],
    "partners": [
        {"name": "TalentBridge", "type": "Agency", "assigned_reqs": 8, "submitted": 90, "qualified_pct": "60%",
         "interviews": 36, "offers": 8, "joiners": 6, "offer_to_join": "75%", "median_ttf": "30d", "fees": "₹3.0L"},
        {"name": "HireSphere", "type": "Agency", "assigned_reqs": 6, "submitted": 60, "qualified_pct": "60%",
         "interviews": 24, "offers": 6, "joiners": 5, "offer_to_join": "83.3%", "median_ttf": "35d", "fees": "₹2.5L"},
        {"name": "Apex Staffing", "type": "Agency", "assigned_reqs": 4, "submitted": 30, "qualified_pct": "60%",
         "interviews": 12, "offers": 2, "joiners": 1, "offer_to_join": "50%", "median_ttf": "42d",
         "median_ttf_flag": True, "fees": "₹0.5L"},
    ],
    "totals": {"name": "Total", "assigned_reqs": 18, "submitted": 180, "qualified_pct": "60%", "interviews": 72,
               "offers": 16, "joiners": 12, "offer_to_join": "75%", "median_ttf": "34d", "fees": "₹6.0L"},
    "selected": {
        "name": "Apex Staffing",
        "submissions": 30,
        "qualified": 18,
        "joiners": 1,
        "offer_to_join": "50%",
        "median_ttf": "42d",
        "fees": "₹50,000",
        "cost_per_joiner": "₹50,000",
        "sla_breached": True,
        "issues": ["1 replacement case open", "2 feedback requests pending"],
    },
    "funnel": [
        {"label": "Submitted", "value": 180},
        {"label": "Qualified", "value": 108},
        {"label": "Interviewed", "value": 72},
        {"label": "Offered", "value": 16},
        {"label": "Joined", "value": 12},
    ],
    "sla": [
        {"partner": "TalentBridge", "first_qualified_cv": "2 days", "target": "≤ 3 days", "status": "Met"},
        {"partner": "HireSphere", "first_qualified_cv": "4 days", "target": "≤ 3 days", "status": "At risk"},
        {"partner": "Apex Staffing", "first_qualified_cv": "6 days", "target": "≤ 3 days", "status": "Breached"},
    ],
    "actions": [
        {"title": "Apex Staffing · Replacement case overdue", "detail": "Owner: Agency manager", "cta": "Review case", "tone": "critical"},
        {"title": "HireSphere · First submission SLA at risk", "detail": "Owner: Vendor coordinator", "cta": "Review SLA", "tone": "warning"},
        {"title": "Finance · Reconcile ₹1.5L unpaid fees", "detail": "Included in ₹6.0L incurred fees", "cta": "View invoices", "tone": "neutral"},
    ],
}

# ---------------------------------------------------------------------------
# 4. Hiring funnel
# ---------------------------------------------------------------------------
HIRING_FUNNEL = {
    "kpis": [
        {"label": "Applications submitted", "value": "480"},
        {"label": "Joiners", "value": "36"},
        {"label": "End-to-end conversion", "value": "7.5%", "sub": "36 of 480"},
        {"label": "Largest stage drop-off", "value": "144", "sub": "Interviewed → Offered"},
        {"label": "Slowest stage", "value": "9 days", "sub": "Client interview"},
    ],
    "funnel": [
        {"label": "Submitted", "value": 480, "from_prev": "—"},
        {"label": "Screened", "value": 360, "from_prev": "75%"},
        {"label": "Qualified", "value": 288, "from_prev": "80%"},
        {"label": "Interviewed", "value": 192, "from_prev": "66.7%"},
        {"label": "Offered", "value": 48, "from_prev": "25%"},
        {"label": "Joined", "value": 36, "from_prev": "75%"},
    ],
    "stage_outcomes": [
        {"transition": "Submitted → Screened", "exited": 90, "still_active": 30},
        {"transition": "Screened → Qualified", "exited": 60, "still_active": 12},
        {"transition": "Qualified → Interviewed", "exited": 72, "still_active": 24},
        {"transition": "Interviewed → Offered", "exited": 120, "still_active": 24},
        {"transition": "Offered → Joined", "exited": 8, "still_active": 4},
    ],
    "stage_durations": [
        {"stage": "Screening", "days": 2},
        {"stage": "Assessment", "days": 4},
        {"stage": "Client interview", "days": 9, "target": 5},
        {"stage": "Offer decision", "days": 3},
        {"stage": "Joining notice period", "days": 21},
    ],
    "source_comparison": [
        {"source": "Internal", "submitted": 300, "qualified": 180, "interviewed": 120, "offers": 32, "joined": 24, "submit_to_join": "8.0%"},
        {"source": "External", "submitted": 180, "qualified": 108, "interviewed": 72, "offers": 16, "joined": 12, "submit_to_join": "6.7%"},
        {"source": "Total", "submitted": 480, "qualified": 288, "interviewed": 192, "offers": 48, "joined": 36, "submit_to_join": "7.5%"},
    ],
    "bottlenecks": [
        {"title": "24 interviewed applications still active", "detail": "Owner: Hiring managers", "cta": "Review feedback", "tone": "critical"},
        {"title": "4 offers awaiting joining", "detail": "Owner: Recruiters", "cta": "Confirm dates", "tone": "warning"},
        {"title": "Client interview exceeds 5-day target", "detail": "Median: 9 days", "cta": "Review delays", "tone": "warning"},
    ],
}

# ---------------------------------------------------------------------------
# 5. Cost & ROI  (cost values are in lakhs, ₹L)
# ---------------------------------------------------------------------------
COST_ROI = {
    "kpis": [
        {"label": "Total hiring cost", "value": "₹12.0L", "sub": "36 joiners"},
        {"label": "Cost per joiner", "value": "₹33,333"},
        {"label": "Budget utilisation", "value": "80%", "sub": "₹12.0L of ₹15.0L"},
        {"label": "Modelled benefit", "value": "₹15.0L", "sub": "Assumption-based"},
        {"label": "Modelled net ROI", "value": "25%", "sub": "Benefit less cost ÷ cost"},
    ],
    "cost_breakdown": [
        {"label": "Internal recruiter allocation", "value": 3.6},
        {"label": "Agency fees", "value": 6.0},
        {"label": "Job boards & sourcing", "value": 1.2},
        {"label": "Assessments", "value": 0.6},
        {"label": "ATS & tools", "value": 0.6},
    ],
    "cost_total": "₹12.0L",
    "internal_vs_agency": [
        {"metric": "Joiners", "internal": "24", "agency": "12"},
        {"metric": "Allocated cost", "internal": "₹4.8L", "agency": "₹7.2L"},
        {"metric": "Cost per joiner", "internal": "₹20,000", "agency": "₹60,000"},
    ],
    "budget_vs_actual": [
        {"month": "Jul", "budget": 4.0, "actual": 3.0},
        {"month": "Aug", "budget": 5.0, "actual": 4.0},
        {"month": "Sep", "budget": 6.0, "actual": 5.0},
    ],
    "budget_variance": "₹3.0L below budget",
    "agency_costs": [
        {"partner": "TalentBridge", "joiners": 6, "fees_incurred": "₹3.0L", "shared_allocation": "₹0.6L",
         "total_cost": "₹3.6L", "cost_per_joiner": "₹60,000", "unpaid_fees": "₹0.5L"},
        {"partner": "HireSphere", "joiners": 5, "fees_incurred": "₹2.5L", "shared_allocation": "₹0.5L",
         "total_cost": "₹3.0L", "cost_per_joiner": "₹60,000", "unpaid_fees": "₹0.75L"},
        {"partner": "Apex Staffing", "joiners": 1, "fees_incurred": "₹0.5L", "shared_allocation": "₹0.1L",
         "total_cost": "₹0.6L", "cost_per_joiner": "₹60,000", "unpaid_fees": "₹0.25L"},
    ],
    "agency_totals": {"partner": "Total", "joiners": 12, "fees_incurred": "₹6.0L", "shared_allocation": "₹1.2L",
                      "total_cost": "₹7.2L", "cost_per_joiner": "₹60,000", "unpaid_fees": "₹1.5L"},
    "roi": [
        {"label": "Estimated benefit per joiner", "value": "₹41,667"},
        {"label": "Joiners", "value": "36"},
        {"label": "Total modelled benefit", "value": "₹15.0L"},
        {"label": "Less hiring cost", "value": "₹12.0L"},
        {"label": "Net modelled value", "value": "₹3.0L"},
        {"label": "Formula", "value": "(₹15.0L − ₹12.0L) / ₹12.0L = 25%"},
    ],
    "actions": [
        {"title": "₹1.5L agency fees unpaid", "detail": "Follow up with partners to clear outstanding fees.", "cta": "View invoices", "tone": "warning"},
        {"title": "Shared cost allocation", "detail": "Review and refine allocation rules across recruiters, tools and infrastructure.", "cta": "Review rules", "tone": "neutral"},
        {"title": "Benefit assumptions", "detail": "Validate per-joiner benefit estimates with finance.", "cta": "Validate", "tone": "neutral"},
    ],
}
