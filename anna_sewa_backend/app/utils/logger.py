"""
Simple structured JSON logger using the stdlib logging module.
This keeps dependencies low while producing JSON-like logs for ingestion.
"""
import logging
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        # Basic structured JSON record
        log_record = {
            "timestamp": datetime.utcfromtimestamp(record.created).isoformat() + "Z",
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
        }
        # include stack trace if present
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record, default=str)

# create module-level logger that other modules can import
logger = logging.getLogger("anna_sewa")
logger.setLevel(logging.INFO)

if not logger.handlers:
    ch = logging.StreamHandler()
    ch.setFormatter(JsonFormatter())
    logger.addHandler(ch)

