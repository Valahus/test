# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
from typing import List

# External
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException


# BeeOS

from app.routers.router import get_db
# from app.crud.roomcategorie import roomcategorie
from app.crud.roomcategory import roomcategory
from app import schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.RoomCategory])
def read_roomcategories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roomcategories_list = roomcategory.get_multi(db, skip=skip, limit=limit)
    return roomcategories_list


@router.get("/{roomcategory_id}", response_model=schemas.RoomCategory)
def read_roomcategory(roomcategory_id: int, db: Session = Depends(get_db)):
    db_roomcategory = roomcategory.get(db, id=roomcategory_id)
    if db_roomcategory is None:
        raise HTTPException(status_code=404, detail="roomcategory not found")
    return db_roomcategory


@router.post("/", response_model=schemas.RoomCategory)
def create_roomcategory(roomcategory_create: schemas.RoomCategoryCreate, db: Session = Depends(get_db)):
    return roomcategory.create(db, obj_in=roomcategory_create)

@router.put("/{roomcategory_id}", response_model=schemas.RoomCategory)
def update_roomcategory(
    roomcategory_id: int,
    roomcategory_update: schemas.RoomCategoryUpdate,
    db: Session = Depends(get_db),
):
    db_roomcategory = roomcategory.get(db, id=roomcategory_id)
    if db_roomcategory is None:
        raise HTTPException(status_code=404, detail="roomcategory not found")
    return roomcategory.update(db, db_obj=db_roomcategory, obj_in=roomcategory_update)


@router.delete("/{roomcategory_id}", status_code=200)
def delete_roomcategory(roomcategory_id: int, db: Session = Depends(get_db)):
    db_roomcategory = roomcategory.get(db, id=roomcategory_id)
    if db_roomcategory is None:
        raise HTTPException(status_code=404, detail="roomcategory not found")
    roomcategory.remove(db, id=roomcategory_id)

