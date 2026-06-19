import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:

    HOST = os.getenv("DB_HOST")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DATABASE = os.getenv("DB_NAME")