from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import Optional

import app.domains.entities as entities
import app.usecases as usecases
import app.interfaces as interfaces
from app.drivers.rdb.base import ENGINE, Base
from app.drivers.api.deps import get_user_usecase
from app.drivers.rdb.models.test import TestUserTable
from app.domains.entities.test import TestUser, TestUserCreate

router = APIRouter()


# @router.post("/", response_model=entities.User)
# async def create_user(
#     *,
#     user_in: entities.UserCreate,
#     uu: usecases.UserUsecase = Depends(get_user_usecase)
# ) -> entities.User:
#     return uu.create(obj_in=user_in)


@router.post("/", response_model=entities.User)
async def create_user(
    *,
    user_in: entities.UserCreate,
    uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    return uu.create(obj_in=user_in)


@router.post("/login", response_model=entities.User)
async def login_user(
    *, auth_in: entities.UserAuth, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    logined_user: Optional[entities.User] = uu.authenticate(auth_in=auth_in)
    if logined_user is None:
        raise HTTPException(status_code=404)
    return logined_user


@router.put("/", response_model=entities.User)
async def update_user(
    *,
    id: int,
    user_in: entities.UserUpdate,
    uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    updated_user: Optional[entities.User] = uu.update(id=id, obj_in=user_in)
    if updated_user is None:
        raise HTTPException(status_code=404)
    return updated_user


@router.delete("/", response_model=entities.User)
async def delete_user(
    *, id: int, uu: usecases.UserUsecase = Depends(get_user_usecase)
) -> entities.User:
    deleted_user: Optional[entities.User] = uu.delete(id=id)
    if deleted_user is None:
        raise HTTPException(status_code=404)
    return deleted_user


@router.get("/", response_model=str)
async def test_user() -> str:
    return "aaa"


# ユーザー情報取得(id指定)
@router.get("/test/{id}")
def get_user(user_id: int) -> TestUser:
    user = session.query(TestUserTable).filter(TestUserTable.id == user_id).first()
    return user


# ユーザー情報登録
@router.post("/test", response_model=TestUser)
def post_user(user: TestUserCreate) -> TestUserCreate:
    db_test_user = TestUserCreate(name=user.name, email=user.email)
    session.add(db_test_user)
    session.commit()
    session.refresh(db_test_user)
    return db_test_user
