# backend/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware   # ← 追加
import importlib
import pkgutil
import os
from backend.database import Base
from backend.database import engine, SessionLocal
from backend.seeds import init_data

# DBの初期化（毎回リセットして作り直す）
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()
init_data(db)
db.close()

app = FastAPI()

# CORS 設定 ← ここ追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",   # Live Serverなど
        "http://127.0.0.1:5500",
        "http://localhost:3000",   # 将来ViteやReactを使うとき用
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター自動登録（backend/routers/*.py すべて読み込み）
import backend.routers  # パッケージとして認識させる
for _, module_name, _ in pkgutil.iter_modules(backend.routers.__path__):
    module = importlib.import_module(f"backend.routers.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)

# 静的ファイル
app.mount("/static", StaticFiles(directory="frontend/public"), name="static")
app.mount("/pages", StaticFiles(directory="frontend/public/pages", html=True), name="pages")
app.mount("/scripts", StaticFiles(directory="frontend/public/scripts", html=True), name="scripts")
