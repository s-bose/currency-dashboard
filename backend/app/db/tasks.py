import logging
from fastapi import FastAPI
from databases import Database


from ..configs.configs import settings

# logging.basicConfig(filename='out.log', level=logging.INFO)
logger = logging.getLogger('uvicorn')


async def connect_to_db(app: FastAPI) -> None:
    database = Database(settings.DATABASE_URI, min_size=2, max_size=10)

    try:
        logger.info('--- establishing database connection ---')
        await database.connect()
        app.state._db = database
        logger.info('--- database connection established ---')

    except Exception as e:
        logger.warn('--- DB CONNECTION ERROR ---')
        logger.warn(e)
        logger.warn('--- DB CONNECTION ERROR ---')
    


async def close_db_connection(app: FastAPI) -> None:
    try:
        logger.info('--- disconnecting database ---')
        await app.state._db.disconnect()
        logger.info('--- database disconnected ---')

    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")


