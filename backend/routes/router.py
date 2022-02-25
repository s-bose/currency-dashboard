from datetime import datetime
from fastapi import APIRouter
from configs import settings
from models.response import meta

dt = datetime.now().strftime(settings.PY_DATETIME_FORMAT)
router = APIRouter()

@router.get('/', tags=['Info'], response_model=dict)
def index():
    return {'msg': 42}


@router.get('/meta', tags=['Info'], response_model=meta.Meta)
def get_metadata() -> meta.Meta:
    response = meta.Meta(
        started_at=dt,
        available_endpoints=[route.path for route in router.routes]
    )
    return response


@router.get('/currencies', tags=['Currency'])
def get_currencies():
    return {'ep': '/currencies'}


@router.get('/convert/', tags=['Convert'])
# the kwarg names will be changed later down the road
def get_convert(from_: str = 'usd', to_: str = 'inr'):
    return {'from': from_, 'to': to_}


@router.post('/convert', tags=['Convert'])
def post_convert():
    return {'ep': '/convert'}


@router.get('/forecast/today', tags=['Forecast'])
def get_todays_forecast():
    return {'ep': '/forecast/today'}


@router.get('/forecast/tomorrow', tags=['Forecast'])
def get_tomorrows_forecast():
    return {'ep': '/forecast/tomorrow'}


@router.get('/forecast/next/days/{days}', tags=['Forecast'])
def get_forecast_for_next_n_days(days: int):
    return {'ep': '/forecast/next/days/{days}'}


@router.post('/forecast', tags=['Forecast'])
def get_forecast():
    return {'ep': '/forecast'}


@router.get('/exchange_rate/currency', tags=['Exchange rates'])
def get_currency_exchange_rate():
    return {'ep': '/exchange_rate/currency'}


@router.post('/exchange_rate/currency', tags=['Exchange rates'])
def post_currency_exchange_rate():
    return {'ep': '/exchange_rate/currency'}

