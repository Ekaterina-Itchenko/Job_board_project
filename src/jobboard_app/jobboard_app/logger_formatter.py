from __future__ import annotations

import logging


class ContextFormatter(logging.Formatter):
    def format(self, log_record: logging.LogRecord) -> str:
        formatted_message = super().format(record=log_record)
        default_record = logging.LogRecord("", 0, "", 0, None, None, None, None, None).__dict__
        context_message = "Context: "
        for key in log_record.__dict__:
            if key not in default_record and key not in ("message", "asctime"):
                context_message += f"{key}={log_record.__dict__[key]} "
        if context_message != "Context: ":
            formatted_message += " " + context_message
        return formatted_message