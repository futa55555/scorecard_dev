# backend/schemas/__init__.py

import pkgutil
import importlib
import inspect
from pydantic import BaseModel

__all__ = []

for _, module_name, _ in pkgutil.walk_packages(__path__, prefix=f"{__name__}"):
    module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj is not BaseModel:
            globals()[name] = obj
            __all__.append(name)
