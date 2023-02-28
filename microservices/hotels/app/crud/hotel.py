# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Hotel
from app.schemas import HotelCreate, HotelUpdate
from app.crud.base import CRUDBase


class CRUDHotel(CRUDBase[Hotel, HotelCreate, HotelUpdate]):
    pass


hotel = CRUDHotel(Hotel)
