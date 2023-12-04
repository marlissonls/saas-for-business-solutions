# configurar conexões
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('HOST')}:{getenv('DB_PORT')}/{getenv('DB_DATABASE')}"
engine = create_engine(DATABASE_URL, echo=True)

jwt_configs = {
    "hash_key": getenv('JWT_SECRET'),
}