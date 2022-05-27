from starlette.responses import JSONResponse, Response

from src.config import env


def send_response(content, status_code=200, origin=""):
    headers = {
        "content-type": "application/json",
        "access-control-allow-credentials": "true",
    }

    # if origin in env.ALLOWED_CORS_ORIGINS.split(","):
    #     headers["access-control-allow-origin"] = origin

    return JSONResponse(
        content=content,
        status_code=status_code,
        headers=headers,
    )
