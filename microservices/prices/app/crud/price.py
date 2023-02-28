# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Price
from app.schemas import PriceCreate, PriceUpdate
from app.crud.base import CRUDBase


class CRUDPrice(CRUDBase[Price, PriceCreate, PriceUpdate]):
    pass


price = CRUDPrice(Price)
