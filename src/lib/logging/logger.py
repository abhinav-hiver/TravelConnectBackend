import datetime
import logging
import os
from logging import handlers

import json_log_formatter

user_extras = {}


def initialize():
    formatter = CustomisedJSONFormatter()
    log_file = os.getenv("LOGS_DIR", "logs").replace('"', "") + "/json_backend.log"
    json_handler = handlers.TimedRotatingFileHandler(
        log_file, when="D", interval=1, backupCount=3
    )
    json_handler.setFormatter(formatter)
    logger = logging.getLogger("backend")
    LOGLEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    logger.setLevel(LOGLEVEL)
    logger.handlers = []
    logger.addHandler(json_handler)
    return logger


def add_param(name, value):
    user_extras[name] = value


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra["message"] = message

        # Include builtins
        extra["level"] = record.levelname
        extra["name"] = record.name

        if "time" not in extra:
            extra["time"] = str(datetime.datetime.today())

        if record.exc_info:
            extra["exc_info"] = self.formatException(record.exc_info)

        extra.update(user_extras)
        return extra
