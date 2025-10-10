# ==============================================
# File: backend/schemas/__init__.py
# ----------------------------------------------
# ✅ 自動import + 全モデルの model_rebuild(force=True)
# ✅ 循環参照を防ぎ、--reload でも安定動作
# ==============================================

from pydantic import BaseModel
import pkgutil
import importlib
import inspect
import traceback

__all__ = []

# ---- すべての schema モジュールを自動 import ----
for _, module_name, _ in pkgutil.walk_packages(__path__, prefix=f"{__name__}."):
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"[WARN] Failed to import {module_name}: {e}")
        traceback.print_exc()
        continue

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseModel) and obj is not BaseModel:
            globals()[name] = obj
            __all__.append(name)

# ---- 各モデルの model_rebuild(force=True) を実行 ----
for cls_name in list(__all__):
    cls = globals().get(cls_name)
    if hasattr(cls, "model_rebuild"):
        try:
            cls.model_rebuild(force=True)
        except Exception as e:
            print(f"[WARN] model_rebuild failed for {cls_name}: {e}")

# print("[INFO] ✅ All schema models imported and rebuilt successfully.")
