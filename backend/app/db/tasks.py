from fastapi import FastAPI
from databases import Database
import logging

from app.configs.configs import Settings

logger = logging.getLogger(__name__)


async def app_start_handler(app: FastAPI) -> None:
    database = Database(Settings.DATABASE_URI, min_size=2, max_size=10)

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn('--- DB CONNECTION ERROR ---')
        logger.warn(e)
        logger.warn('--- DB CONNECTION ERROR ---')
    

async def app_stop_handler(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")


