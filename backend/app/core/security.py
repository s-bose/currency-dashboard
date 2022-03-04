from typing import Optional
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import SecretStr

from ..configs.configs import settings

pwd_context: CryptContext = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gen_hash(*, password: SecretStr) -> str:
    return pwd_context.hash(password.get_secret_value())


def verify_password(*, plain_pwd: str, hash_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd, hash_pwd)


def create_access_token(data: dict) -> str:
    expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire: datetime = datetime.utcnow() + expires_delta

    to_encode = data.copy()
    to_encode |= {'exp': expire}
    encoded_jwt: str = jwt.encode(
                            to_encode, 
                            settings.SECRET_KEY, 
                            algorithm=settings.ALGORITHM
                        )

    return encoded_jwt
