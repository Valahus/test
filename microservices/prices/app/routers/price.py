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
from app.crud.price import price
from app import schemas


router = APIRouter()

@router.get("/", response_model=List[schemas.Price])
def read_prices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prices_list = price.get_multi(db, skip=skip, limit=limit)
    return prices_list


@router.get("/{price_id}", response_model=schemas.Price)
def read_price(price_id: int, db: Session = Depends(get_db)):
    db_price = price.get(db, id=price_id)
    if db_price is None:
        raise HTTPException(status_code=404, detail="price not found")
    return db_price


@router.post("/", response_model=schemas.Price)
def create_price(price_create: schemas.PriceCreate, db: Session = Depends(get_db)):
    return price.create(db, obj_in=price_create)

@router.put("/{price_id}", response_model=schemas.Price)
def update_price(
    price_id: int,
    price_update: schemas.PriceUpdate,
    db: Session = Depends(get_db),
):
    db_price = price.get(db, id=price_id)
    if db_price is None:
        raise HTTPException(status_code=404, detail="price not found")
    return price.update(db, db_obj=db_price, obj_in=price_update)


@router.delete("/{price_id}", status_code=200)
def delete_price(price_id: int, db: Session = Depends(get_db)):
    db_price = price.get(db, id=price_id)
    if db_price is None:
        raise HTTPException(status_code=404, detail="price not found")
    price.remove(db, id=price_id)
