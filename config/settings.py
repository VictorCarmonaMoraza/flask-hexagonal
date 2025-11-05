
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "sportPerformance API"
    DEBUG = True
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"
    API_KEY = os.getenv("API_KEY")
    DATABASE_URL = "postgresql+psycopg2://sport_user:SportVictor@localhost:5432/sportPerformance"

settings = Settings()
