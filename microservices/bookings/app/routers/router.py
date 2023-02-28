# -*- coding: utf-8 -*-
# !/usr/bin/python3

# BeeOS
from app.database import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
