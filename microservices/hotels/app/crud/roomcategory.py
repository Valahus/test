# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import RoomCategory
from app.schemas import RoomCategoryCreate, RoomCategoryUpdate
from app.crud.base import CRUDBase


class CRUDRoomCategory(CRUDBase[RoomCategory, RoomCategoryCreate, RoomCategoryUpdate]):
    pass


roomcategory = CRUDRoomCategory(RoomCategory)
