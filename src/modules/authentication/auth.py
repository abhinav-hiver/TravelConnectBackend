from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class JWTSecret(BaseModel):
    authjwt_secret_key: str = "test_secret"  # TODO: get it from env or config variable


@AuthJWT.load_config
def get_config():
    return JWTSecret()


class Authorize:
    def __init__(self, request):
        self.request = request
        self.auth_jwt = AuthJWT(request)

    def authorize(self):
        self.auth_jwt.jwt_required()

    def get_user_id_from_jwt(self):
        return self.auth_jwt.get_jwt_subject()
