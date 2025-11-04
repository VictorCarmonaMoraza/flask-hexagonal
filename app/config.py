# app/config.py
import os
from dataclasses import dataclass

@dataclass
class Config:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sportperformance.db")
    DEBUG: bool = os.getenv("DEBUG", "1") == "1"
    ECHO_SQL: bool = os.getenv("ECHO_SQL", "0") == "1"
