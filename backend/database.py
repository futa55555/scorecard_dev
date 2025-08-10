# database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# # Renderの環境変数 DATABASE_URL を使用
# SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
# ローカルのMySQLに接続するためのURL（←必要に応じて書き換えて）
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:8ruzoSyukatsu@localhost:3306/scorecard_dev?charset=utf8mb4"


# PostgreSQL用の接続（dialect+driver）
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
