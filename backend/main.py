from fileinput import close
from fastapi import FastAPI
from app.routes.router import router
from fastapi.openapi.utils import get_openapi

from app.core.services import create_start_app_handler, \
                              create_stop_app_handler

app = FastAPI()
app.include_router(router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Currency Dashboard Backend',
        version='0.0.1',
        description='A very descriptive description, describing everything',
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Adding OpenAPI configuration
app.openapi = custom_openapi
app.add_event_handler('startup', create_start_app_handler(app))
app.add_event_handler('shutdown', create_stop_app_handler(app))