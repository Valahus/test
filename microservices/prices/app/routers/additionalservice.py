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
from app.crud.additionalservice import additionalservice
from app import schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.AdditionalService])
def read_additional_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    additionalservice_list = additionalservice.get_multi(db, skip=skip, limit=limit)
    return additionalservice_list


@router.get("/{additionalservice_id}", response_model=schemas.AdditionalService)
def read_additional_service(additional_service_id: int, db: Session = Depends(get_db)):
    db_additional_service = hotel.get(db, id=additional_service_id)
    if db_additional_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_additional_service


@router.post("/", response_model=schemas.AdditionalService)
def create_additional_service(additional_service_create: schemas.AdditionalServiceCreate, db: Session = Depends(get_db)):
    return additionalservice.create(db, obj_in=additional_service_create)

@router.put("/{additional_service_id}", response_model=schemas.AdditionalService)
def update_additional_service(
    additional_service_id: int,
    additional_service_update: schemas.AdditionalServiceUpdate,
    db: Session = Depends(get_db),
):
    db_additional_service = additionalservice.get(db, id=additional_service_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return additionalservice.update(db, db_obj=db_additional_service, obj_in=additional_service_update)


@router.delete("/{additional_service_id}", status_code=200)
def delete_service(additional_service_id: int, db: Session = Depends(get_db)):
    db_hotel = hotel.get(db, id=hotel_id)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    hotel.remove(db, id=hotel_id)
