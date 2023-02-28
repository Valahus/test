# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from sqlalchemy.orm import Session

# BeeOS
from app.models import AdditionalService
from app.schemas import AdditionalServiceCreate, AdditionalServiceUpdate
from app.crud.base import CRUDBase


class CRUDAdditionalService(CRUDBase[AdditionalService, AdditionalServiceCreate, AdditionalServiceUpdate]):
    pass


additionalservice = CRUDAdditionalService(AdditionalService)
