# logging.py
'''Logging Config for LogiNet'''

import logging
import logging.config
from pathlib import Path

from app.config import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "%(asctime)s | %(levelname)s | [%(name)s] | %(message)s",
        },
        "uvicorn": {
            "format": "%(levelprefix)s %(message)s",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": LOG_DIR / "backend_app.log",
            "maxBytes": 5_000_000,
            "backupCount": 5,
        },
    },

    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG" if settings.debug else "INFO",
        },

        # Uvicorn
        "uvicorn.error": {
            "handlers": ["console", "file"],
            "level": "DEBUG" if settings.debug else "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console", "file"],
            "level": "DEBUG" if settings.debug else "INFO",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console", "file"],
            "level": "DEBUG" if settings.debug else "INFO",
            "propagate": False,
        },

        # SQLAlchemy
        "sqlalchemy.engine": {"level": "WARNING"} if not settings.debug else {"level": "DEBUG"},
        "sqlalchemy.pool": {"level": "WARNING"} if not settings.debug else {"level": "DEBUG"},

        # Redis / aioredis
        "redis": {"level": "WARNING"} if not settings.debug else {"level": "DEBUG"},
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
