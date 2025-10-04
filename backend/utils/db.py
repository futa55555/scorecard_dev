from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
import traceback
import logging

logger = logging.getLogger(__name__)

def db_exception_handler(func):
    """
    CRUD関数の共通エラーハンドリングデコレーター
    SQLAlchemyErorrはDBエラーとして、その他のエラーはサーバーエラーとしてHTTPExceptionを返す
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = kwargs.get("db") or (args[0] if len(args) > 0 else None)
        try:
            return func(*args, **kwargs)

        except SQLAlchemyError as e:
            if db:
                db.rollback()
            logger.error(f"[DB Error] {func.__name__}: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {str(e)}"
            )

        except ValueError as e:
            logger.warning(f"[Value Error] {func.__name__}: {str(e)}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid value: {str(e)}"
            )

        except KeyError as e:
            logger.warning(f"[Key Error] {func.__name__}: Missing key {str(e)}")
            raise HTTPException(
                status_code=400,
                detail=f"Missing key: {str(e)}"
            )

        except Exception as e:
            if db:
                db.rollback()
            logger.exception(f"[Unhandled Error] {func.__name__}: {str(e)}\n{traceback.format_exc()}")
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected server error: {str(e)}"
            )

    return wrapper
