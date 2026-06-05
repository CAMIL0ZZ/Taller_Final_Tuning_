from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.analytics_service import (
    AnalyticsService
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/dashboard")
def dashboard(
    request: Request
):

    top_cars = (
        AnalyticsService.top_cars()
    )

    top_mods = (
        AnalyticsService.top_mods()
    )

    expensive_builds = (
        AnalyticsService.expensive_builds()
    )

    build_stats = (
        AnalyticsService.build_approach_stats()
    )

    fuel_stats = (
        AnalyticsService.fuel_type_stats()
    )

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "top_cars": top_cars,
            "top_mods": top_mods,
            "expensive_builds": expensive_builds,
            "build_stats": build_stats,
            "fuel_stats": fuel_stats
        }
    )