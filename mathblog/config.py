"""Flask configuration."""
import os

# the basedir is the parent directory
basedir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))
database_uri = os.path.join(basedir, "db.sqlite")


class Config:
    """Base config."""

    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProdConfig(Config):
    """Prod config."""

    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv("PROD_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)


class DevConfig(Config):
    """Dev config."""

    TESTING = False
    FLASK_ENV = "development"
    SECRET_KEY = os.getenv("SECRET_KEY", "5791628bb0b13ce0c676dfde280ba245")
    SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME", "cookie")
    DATABASE_URI = os.getenv("DEV_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////" + database_uri
    )
    ASSETS_DEBUG = True  # Flask assets configurations.
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)


class TestConfig(Config):
    """Test config."""

    TESTING = True
    SECRET_KEY = os.getenv("SECRET_KEY", "5791628bb0b13ce0c676dfde280ba245")
    SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME", "cookie")
    DATABASE_URI = os.getenv("DEV_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
