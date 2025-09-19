# config.py
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for sessions & CSRF
    SECRET_KEY = os.environ.get("SECRET_KEY", "hazel")

    # Database URI (use env var if available, fallback to hardcoded)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://root:Hazel123%401009@localhost/school_db"
    )

    # Disable event system to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
