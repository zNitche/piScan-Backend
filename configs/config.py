import os
from piScan import PROJECT_ROOT


class Config:
    MIGRATIONS_DIR_PATH = os.path.join(PROJECT_ROOT, "database", "migrations")
    SCAN_FILES_DIR_PATH = os.path.join(PROJECT_ROOT, "files", "scans")

    APP_PORT = 8000
    APP_HOST = "0.0.0.0"

    DEBUG_MODE = int(os.getenv("DEBUG", 0))

    DATABASE_URI = f"sqlite:////{PROJECT_ROOT}/database/app.sqlite3"
    REDIS_URI = "127.0.0.1" if DEBUG_MODE else "redis"
    REDIS_PORT = "6000"

    HOST_DOCS = int(os.getenv("HOST_DOCS", 0))
    SWAGGER_SCHEMA_PATH = os.path.join(PROJECT_ROOT, "swagger.json")
