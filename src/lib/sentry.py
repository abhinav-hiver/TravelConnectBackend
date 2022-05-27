# from typing import Dict, List

# import sentry_sdk
# from fastapi import Request

# from src.config import env
# from src.exceptions.exception import Unauthorized


# def start_sentry(integrations: List = []) -> None:
#     """
#     Initialize Sentry to capture errors
#     """
#     sentry_sdk.init(
#         environment=env.APP_ENV,
#         dsn=env.SENTRY_DSN,
#         integrations=integrations,
#         before_send=before_send,
#         debug=env.APP_DEBUG,
#     )


# def send_sentry_event(exc: BaseException, request: Request):
#     if env.APP_DEBUG:
#         return
#     with sentry_sdk.push_scope() as scope:
#         scope.set_context("request", request)
#         scope.user = {"ip_address": request.client.host, "request": request}
#         sentry_sdk.capture_exception(exc)


# def before_send(event: Dict, hint: Dict):
#     """
#     Ignore specific types of exceptions here
#     Source: https://github.com/getsentry/sentry-python/issues/149#issuecomment-434448781
#     """

#     if "exc_info" in hint:
#         exc_type, exc_value, tb = hint["exc_info"]
#         if is_error_ignored(exc_value):
#             return None

#     return event


# def is_error_ignored(exception: Exception) -> bool:
#     """
#     Check if the given exception is to be ignored
#     """
#     return isinstance(exception, (Unauthorized))
