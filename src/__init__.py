import uuid

from fastapi import FastAPI, Request

from src.api.middlewares.backend_middleware import BackendMiddleware
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse


from .api.routers import router
from .config import env
from .lib.api_response import send_response


# Enable/Disable Swagger Schema
# docs_url = "/docs" if env.APP_DEBUG else None
docs_url = "/docs"
redoc_url = "/redocs"

app = FastAPI(
    title="Backend API", version="2.0.0", docs_url=docs_url, redoc_url=redoc_url
)

app.debug = env.APP_DEBUG


@app.get("/api/ping")
async def index():
    return send_response({"backend-service": {"status": "up"}})


app.middleware("http")(BackendMiddleware())

# backend APIs
app.include_router(router.router, prefix="/api")


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
