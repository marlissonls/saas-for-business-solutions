# Definir um schema para as tabelas:
# User
# Company
# Dashboard
# Mlmodels
from sqlalchemy.orm import sessionmaker
from app.config import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)