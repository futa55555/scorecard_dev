# backend/routers/__init__.py

from fastapi import APIRouter
import pkgutil
import importlib

routers = APIRouter()

for _, module_name, _ in pkgutil.walk_packages(__path__, prefix=f"{__name__}"):
    module = importlib.import_module(module_name)
    if hasattr(module, "router"):
        routers.include_router(module.router)
