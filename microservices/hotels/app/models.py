# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
import enum

# External
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship

# BeeOS
from app.database import Base


class UserRole(enum.Enum):
    one = 1
    two = 2
    three = 3


# class OrderStatus(enum.Enum):
#     started = 1
#     cancelled = 2
#     done = 3
#     failed = 4


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    profile_picture = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    role = Column(Enum(UserRole))

    # Relationships
    # company_id = Column(Integer, ForeignKey("company.id"))
    # orders = relationship("Order")

class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    address = Column(String)
    phone = Column(String)
    room_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    
    #Relationships

class Room(Base): 
    __tablename__ = "room"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    hotel_id=Column(Integer)
    category_id=Column(Integer)
    ocupants_max=Column(Integer)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
    deleted_at=Column(DateTime)

    #Relationships

class RoomCategory(Base):
    __tablename__ = "roomcategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    abreviation=Column(String)
    occupants_max=Column(Integer)
    price_id=Column(Integer)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
    deleted_at=Column(DateTime)

    #Relationships

# class Price(Base):
#     __tablename__ = "price"

#     id = Column(Integer, primary_key=True, index=True)
#     room_category_id=Column(Integer)
#     additional_service_id=Column(Integer)
#     price=Column(Float)
#     created_at=Column(DateTime)
#     updated_at=Column(DateTime)
#     deleted_at=Column(DateTime)

#     #Relationships

# class AdditionalService(Base):
#     __tablename__ = "additionalservice"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)

#     #Relationships

# class Payment(Base): 
#     __tablename__ = "payment"

#     id=Column(Integer, primary_key=True, index=True)
#     amount = Column(Float)
#     booking_id = Column(Integer)
#     customer_id = Column(Integer)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)

#     #Relationships 

# class Booking(Base):
#     __tablename__= "booking"

#     id= Column(Integer, primary_key=True, index=True)
#     number_guests=Column(Integer)
#     room_id = Column(Integer)
#     customer_id = Column(Integer)
#     arrival_date = Column(DateTime)
#     departure_date = Column(DateTime)
#     payment_id = Column(Integer)
#     booking_status = Column(Boolean) # to change
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
#     # Relationships 

# class Customer(Base):
#     __tablename__="customer"

#     id=Column(Integer, primary_key=True, index=True)
#     username=Column(String)
#     password=Column(String)
#     first_name=Column(String)
#     last_name=Column(String)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String)
#     address=Column(String)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
    #Relationships 
    

# class Company(Base):
#     __tablename__ = "company"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     siret = Column(String, index=True)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)

#     # Relationships
#     members = relationship("User")


# class Order(Base):
#     __tablename__ = "order"

#     id = Column(Integer, primary_key=True, index=True)
#     price = Column(Integer)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
#     status = Column(Enum(OrderStatus))

#     # Relationships
#     user_id = Column(Integer, ForeignKey("user.id"))
#     bounds_id = Column(Integer, ForeignKey("bounds.id"))
#     bounds = relationship("Bounds")
