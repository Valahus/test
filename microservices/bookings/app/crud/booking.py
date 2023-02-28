# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Booking
from app.schemas import BookingCreate, BookingUpdate
from app.crud.base import CRUDBase


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    pass


booking = CRUDBooking(Booking)
