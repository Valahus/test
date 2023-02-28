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
# from app.crud.hotel import hotel
from app.crud.room import room
from app import schemas


router = APIRouter()

@router.get("/", response_model=List[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms_list = room.get_multi(db, skip=skip, limit=limit)
    return rooms_list


@router.get("/{room_id}", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = room.get(db, id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="room not found")
    return db_room


@router.post("/", response_model=schemas.Room)
def create_room(room_create: schemas.RoomCreate, db: Session = Depends(get_db)):
    return room.create(db, obj_in=room_create)

@router.put("/{room_id}", response_model=schemas.Room)
def update_room(
    room_id: int,
    room_update: schemas.RoomUpdate,
    db: Session = Depends(get_db),
):
    db_room = room.get(db, id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="room not found")
    return room.update(db, db_obj=db_room, obj_in=room_update)


@router.delete("/{room_id}", status_code=200)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = room.get(db, id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="room not found")
    room.remove(db, id=room_id)
