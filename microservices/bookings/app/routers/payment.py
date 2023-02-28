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
from app.crud.payment import payment
from app import schemas


router = APIRouter()

@router.get("/", response_model=List[schemas.Payment])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments_list = payment.get_multi(db, skip=skip, limit=limit)
    return payments_list


@router.get("/{payment_id}", response_model=schemas.Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = payment.get(db, id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found")
    return db_payment


@router.post("/", response_model=schemas.Payment)
def create_payment(payment_create: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return payment.create(db, obj_in=payment_create)

@router.put("/{payment_id}", response_model=schemas.Payment)
def update_payment(
    payment_id: int,
    payment_update: schemas.PaymentUpdate,
    db: Session = Depends(get_db),
):
    db_payment = payment.get(db, id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found")
    return payment.update(db, db_obj=db_payment, obj_in=payment_update)


@router.delete("/{payment_id}", status_code=200)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = payment.get(db, id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found")
    payment.remove(db, id=payment_id)

