from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def index():
    return {'msg': 'Hello, World!'}
