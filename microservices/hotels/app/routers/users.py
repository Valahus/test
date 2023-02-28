# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
from typing import List

# External
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from fastapi import APIRouter

# BeeOS
from app.routers.router import get_db
from app.crud.users import user
from app import models
from app import schemas


router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(user.model).filter(user.model.email == user_create.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user.create(db, obj_in=user_create)


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)
):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.update(db, db_user, user_update)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.remove(db, user_id)


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users_list = user.get_multi(db, skip=skip, limit=limit)
    return users_list
