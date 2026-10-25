from fastapi import APIRouter, HTTPException

from app.data import (
    PERFORMANCE_OVERVIEW,
    INTERNAL_RECRUITERS,
    EXTERNAL_AGENCIES,
    HIRING_FUNNEL,
    COST_ROI,
)

router = APIRouter()

# Maps each tab slug (used by the frontend) to its dataset
TABS = {
    "performance-overview": PERFORMANCE_OVERVIEW,
    "internal-recruiters": INTERNAL_RECRUITERS,
    "external-agencies": EXTERNAL_AGENCIES,
    "hiring-funnel": HIRING_FUNNEL,
    "cost-roi": COST_ROI,
}


@router.get("/{tab}")
def get_analytics_tab(tab: str) -> dict:
    """Return the analytics payload for one dashboard tab."""
    data = TABS.get(tab)
    if data is None:
        raise HTTPException(status_code=404, detail=f"Unknown analytics tab: {tab}")
    return data
