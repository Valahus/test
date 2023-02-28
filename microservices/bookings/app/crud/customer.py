# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Customer
from app.schemas import CustomerCreate, CustomerUpdate
from app.crud.base import CRUDBase


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    pass


customer = CRUDCustomer(Customer)
