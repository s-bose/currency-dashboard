import jwt
from starlette import status
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from ..configs.configs import settings
from .database import get_crud
from ..db.crud import UsersCrud
from ..models.users import UserSchema
from ..models.token import Token


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_STR}/users/login"
)


async def get_current_user(
    crud: UsersCrud = Depends(get_crud(UsersCrud)),
    token: str = Depends(reusable_oauth2)
) -> UserSchema:


    try:
        payload: dict = jwt.decode(
                                token, 
                                settings.SECRET_KEY,
                                algorithms=[settings.ALGORITHM]
                            )
        print(payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='could not validate credentials'
        )

    token_data = Token(**payload)
    if (user := await crud.get_user_by_id(token_data.id)) is None:
        raise HTTPException(
                            status.HTTP_404_NOT_FOUND,
                            detail='user not found'
                        )

    return user