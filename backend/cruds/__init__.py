# backend/cruds/init.py

import pkgutil
import importlib
import inspect

__all__ = []

for _, module_name, _ in pkgutil.walk_packages(__path__, prefix=f"{__name__}."):
    module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            globals()[name] = obj
            __all__.append(name)
