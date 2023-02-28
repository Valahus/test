# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Room
from app.schemas import RoomCreate, RoomUpdate
from app.crud.base import CRUDBase


class CRUDRoom(CRUDBase[Room, RoomCreate, RoomUpdate]):
    pass


room = CRUDRoom(Room)
