import uuid

from fastapi import Request, Depends

from ...lib.api_response import send_response
from ...lib.logging.logger import add_param, initialize
# from fastapi_jwt_auth import AuthJWT
# from src.modules.authentication import Authorize


class BackendMiddleware:
    routes = {
        "ignored_routes": [],
        "doc_routes": ["docs", "openapi.json"],
    }

    def is_tokenless_route(self, path, part):
        routes = self.routes
        return (
            path in routes["ignored_routes"]
            or part in routes["doc_routes"]
        )

    async def __call__(self, request: Request, call_next):
        self.get_origin(request)
        routes = self.routes
        if "OPTIONS" in request.__dict__["scope"]["method"]:
            return await call_next(request)

        log = initialize()
        request_id = str(uuid.uuid4())
        add_param("request_id", request_id)
        add_param("request_url", request.url)
        log.info(f"Backend call recieved {request.url}")

        full_path = request.__dict__["scope"]["path"].split("/")
        part = full_path[-1]
        path = full_path[-2]
        try:
            if self.is_tokenless_route(path, part):
                response = await call_next(request)
                log.info(f"Tokenless Route: Response status {response.status_code}")
                return response
            # auth = Authorize(request)
            # auth.authorize()
            # user_id = auth.get_user_id_from_jwt()
            # request.state.user_id = user_id
            response = await call_next(request)
            log.info(f"Response status : {response.status_code}")
            return response
        except Exception as e:
            import traceback

            print("Exception in backend", traceback.format_exc())
            log.error("Exception in backend", exc_info=True)
            return self.send_response(
                dict(
                    detail=f"Something went wrong {e}",
                ),
                500,
            )

    def get_origin(self, request: Request):
        request_origin = ""
        for header in request.__dict__["scope"]["headers"]:
            name = header[0].decode("utf-8")
            if name == "origin":
                request_origin = header[1].decode("utf-8")
        self.request_origin = request_origin

    # Method to append CORS headers via request_origin before sending response
    def send_response(self, content, code):
        return send_response(dict(detail=content), code, self.request_origin)
