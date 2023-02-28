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
# from app.crud.customer import customer
from app.crud.customer import customer
from app import schemas


router = APIRouter()

@router.get("/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers_list = customer.get_multi(db, skip=skip, limit=limit)
    return customers_list


@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customer.get(db, id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="customer not found")
    return db_customer


@router.post("/", response_model=schemas.Customer)
def create_customer(customer_create: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return customer.create(db, obj_in=customer_create)

@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(
    customer_id: int,
    customer_update: schemas.CustomerUpdate,
    db: Session = Depends(get_db),
):
    db_customer = customer.get(db, id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="customer not found")
    return customer.update(db, db_obj=db_customer, obj_in=customer_update)


@router.delete("/{customer_id}", status_code=200)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customer.get(db, id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="customer not found")
    customer.remove(db, id=customer_id)
