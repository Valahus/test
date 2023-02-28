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
from app.crud.hotel import hotel
from app.crud.room import room
from app import schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.Hotel])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hotels_list = hotel.get_multi(db, skip=skip, limit=limit)
    return hotels_list


@router.get("/{hotel_id}", response_model=schemas.Hotel)
def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = hotel.get(db, id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel


@router.post("/", response_model=schemas.Hotel)
def create_hotel(hotel_create: schemas.HotelCreate, db: Session = Depends(get_db)):
    return hotel.create(db, obj_in=hotel_create)

@router.put("/{hotel_id}", response_model=schemas.Hotel)
def update_hotel(
    hotel_id: int,
    hotel_update: schemas.HotelUpdate,
    db: Session = Depends(get_db),
):
    db_hotel = hotel.get(db, id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel.update(db, db_obj=db_hotel, obj_in=hotel_update)


@router.delete("/{hotel_id}", status_code=200)
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    db_hotel = hotel.get(db, id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    hotel.remove(db, id=hotel_id)
