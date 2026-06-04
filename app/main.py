from fastapi import FastAPI

# API

from app.routers.api.users import (
    router as users_router
)

from app.routers.api.stock_cars import (
    router as stock_cars_router
)

from app.routers.api.builds import (
    router as builds_router
)

from app.routers.api.mods import (
    router as mods_router
)

from app.routers.api.build_mods import (
    router as build_mods_router
)

# WEB

from app.routers.web.home import (
    router as home_router
)

from app.routers.web.users_web import (
    router as users_web_router
)

from app.routers.web.stock_cars_web import (
    router as stock_cars_web_router
)

from app.routers.web.builds_web import (
    router as builds_web_router
)

from app.routers.web.mods_web import (
    router as mods_web_router
)

from app.routers.web.dashboard import (
    router as dashboard_router
)

app = FastAPI(
    title="Tuning Community API",
    version="1.0.0"
)

# API Routers

app.include_router(users_router)

app.include_router(stock_cars_router)

app.include_router(builds_router)

app.include_router(mods_router)

app.include_router(build_mods_router)

# WEB Routers

app.include_router(home_router)

app.include_router(users_web_router)

app.include_router(stock_cars_web_router)

app.include_router(builds_web_router)

app.include_router(mods_web_router)

app.include_router(dashboard_router)