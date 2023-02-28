# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import Payment
from app.schemas import PaymentCreate, PaymentUpdate
from app.crud.base import CRUDBase


class CRUDPayment(CRUDBase[Payment, PaymentCreate, PaymentUpdate]):
    pass


payment = CRUDPayment(Payment)
