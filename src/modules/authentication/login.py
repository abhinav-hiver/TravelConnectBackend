from fastapi_jwt_auth import AuthJWT
import datetime
from src.config.constants import TOKEN
from src.database.db_repository import DbRepositories


class Login:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_access_token(self):
        if self.verify_user_exists():
            return self.create_access_token()
        return None

    def verify_user_exists(self):
        # TODO: check user exists in DB here.
        db_repo = DbRepositories(self.user_id)
        user = db_repo.get_main_user()
        if user:
            return True
        return False

    def create_access_token(self):
        authorize = AuthJWT()
        expires = datetime.timedelta(days=TOKEN.expire_time_in_days)
        access_token = authorize.create_access_token(
            subject=self.user_id, expires_time=expires
        )
        return access_token
