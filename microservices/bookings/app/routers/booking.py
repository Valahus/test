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
# from app.crud.booking import booking
from app.crud.booking import booking
from app import schemas


router = APIRouter()

@router.get("/", response_model=List[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings_list = booking.get_multi(db, skip=skip, limit=limit)
    return bookings_list


@router.get("/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking.get(db, id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="booking not found")
    return db_booking


@router.post("/", response_model=schemas.Booking)
def create_booking(booking_create: schemas.BookingCreate, db: Session = Depends(get_db)):
    return booking.create(db, obj_in=booking_create)

@router.put("/{booking_id}", response_model=schemas.Booking)
def update_booking(
    booking_id: int,
    booking_update: schemas.BookingUpdate,
    db: Session = Depends(get_db),
):
    db_booking = booking.get(db, id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="booking not found")
    return booking.update(db, db_obj=db_booking, obj_in=booking_update)


@router.delete("/{booking_id}", status_code=200)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking.get(db, id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="booking not found")
    booking.remove(db, id=booking_id)
