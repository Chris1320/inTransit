from typing import Literal

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from centralserver import info
from centralserver.internals.config_handler import app_config
from centralserver.internals.db_handler import populate_db
from centralserver.internals.logger import LoggerFactory, log_app_info
from centralserver.routers import auth_routes, reports_routes, users_routes

logger = LoggerFactory(
    log_level="debug" if app_config.debug.enabled else "warn"
).get_logger(__name__)

log_app_info(logger)
populate_db()


app = FastAPI(
    debug=app_config.debug.enabled,
    title=info.Program.name,
    version=".".join(map(str, info.Program.version)),
)

app.include_router(auth_routes.router)
app.include_router(users_routes.router)
app.include_router(reports_routes.router)


@app.exception_handler(404)
async def not_found_error(request: Request, exc: Exception):
    """Return a 404 error response."""

    logger.warning("Not Found: %s", exc)
    logger.debug("Request: %s", request)
    return JSONResponse(status_code=404, content={"message": "Not found"})


@app.exception_handler(500)
async def internal_server_error(request: Request, exc: Exception):
    """Return a 500 error response."""

    logger.critical("Internal server error: %s", exc, exc_info=True)
    logger.debug("Request: %s", request)
    return JSONResponse(status_code=500, content={"message": "Internal server error"})


@app.get("/healthcheck")
async def root() -> dict[Literal["message"], Literal["Healthy"]]:
    return {"message": "Healthy"}
