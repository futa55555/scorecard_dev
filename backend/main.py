# backend/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import importlib
import pkgutil
import os
from backend.models import Base
from backend.database import engine
from backend.routers.__init__ import init_data

# DBの初期化（毎回リセットして作り直す）
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
init_data()

app = FastAPI()

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
