# app/infra/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import Config

engine = None
SessionLocal = None

def init_db(database_url: str = None, echo: bool = None):
    """
    Inicializa el motor y la sesión de SQLAlchemy.
    Se llama desde app/__init__.py (en create_app()).
    """
    global engine, SessionLocal

    db_url = database_url or Config.DATABASE_URL
    echo = echo if echo is not None else Config.ECHO_SQL

    engine = create_engine(db_url, echo=echo, future=True)
    SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    return engine, SessionLocal
