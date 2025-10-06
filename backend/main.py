# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ← 追加
import importlib
import pkgutil
from backend.database import Base, engine, SessionLocal
from backend.seeds import init_data
from backend.routers import routers

# DBの初期化（毎回リセットして作り直す）
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()
init_data(db)
db.close()

app = FastAPI()
app.include_router(routers)

# CORS 設定 ← ここ追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",   # Live Serverなど
        "http://127.0.0.1:5500",
        "http://localhost:5501",   # Live Serverなど
        "http://127.0.0.1:5501",
        "http://localhost:3000",   # 将来ViteやReactを使うとき用
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静的ファイル
# app.mount("/static", StaticFiles(directory="frontend/public"), name="static")
# app.mount("/pages", StaticFiles(directory="frontend/public/pages", html=True), name="pages")
# app.mount("/scripts", StaticFiles(directory="frontend/public/scripts", html=True), name="scripts")
