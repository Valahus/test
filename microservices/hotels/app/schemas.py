# -*- coding: utf-8 -*-
# !/usr/bin/python3

# Python standard dependencies
import enum
from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field

# BeeOS
from app.models import UserRole


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    profile_picture: Optional[str] = None
    role: Optional[UserRole] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    # company_id: Optional[int] = None
    # orders

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
    keepMeLoggedIn: bool = Field(...)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str

class HotelBase(BaseModel):
    id: int 
    name: str
    description: str 
    address: str 
    phone: str 
    room_id: int 
    created_at: datetime 
    updated_at: datetime 
    deleted_at: datetime 

class HotelCreate(HotelBase):
    pass

class HotelUpdate(HotelBase):
    pass 

class Hotel(HotelBase):
    id: int 
    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    id: int 
    name: str
    description: str 
    hotel_id: int 
    category_id: int 
    occupants_max: int 
    created_at: datetime 
    updated_at: datetime 
    deleted_at: datetime 

class RoomCreate(RoomBase):
    pass

class RoomUpdate(RoomBase):
    pass 

class Room(RoomBase):
    id: int 
    
    class Config:
        orm_mode = True

class RoomCategoryBase(BaseModel):
    id: int 
    name: str 
    abreviation: str 
    occupants_max: int 
    price_id: int 
    created_at: datetime 
    updated_at: datetime 
    deleted_at: datetime

class RoomCategory(RoomCategoryBase):
    id: int 
    class Config:
        orm_mode = True 

class RoomCategoryCreate(RoomCategoryBase):
    pass 

class RoomCategoryUpdate(RoomCategoryBase):
    pass 

# class PriceBase(BaseModel):
#     id: int 
#     room_category_id: int 
#     additional_service_id: int 
#     price: float
#     created_at: datetime 
#     updated_at: datetime 
#     deleted_at: datetime  

# class Price(PriceBase): 
#     id: int 
#     class Config:
#         orm_mode = True

# class PriceCreate(PriceBase):
#     pass

# class PriceUpdate(PriceBase):
#     pass 

# class AdditionalServiceBase(BaseModel):
#     id: int 
#     name: str 
#     created_at: datetime 
#     updated_at: datetime 
#     deleted_at: datetime 

# class AdditionalService(AdditionalServiceBase):
#     id: int 
#     class Config:
#         orm_mode = True

# class AdditionalServiceCreate(AdditionalServiceBase):
#     pass

# class AdditionalServiceUpdate(AdditionalServiceBase):
#     pass 

# class PaymentBase(BaseModel):
#     id: int 
#     amount: float
#     booking_id: int 
#     customer_id: int 
#     created_at: datetime
#     updated_at: datetime 
#     deleted_at: datetime 

# class Payment(PaymentBase):
#     id: int 
#     class Config:
#         orm_mode = True

# class PaymentCreate(PaymentBase):
#     pass

# class PaymentUpdate(PaymentBase):
#     pass 

# class BookingBase(BaseModel):
#     id: int 
#     number_guests: int 
#     room_id: int 
#     customer_id: int 
#     arrival_date: datetime 
#     departure_date: datetime
#     payment_id: int 
#     booking_status: bool 
#     created_at: datetime 
#     updated_at: datetime 
#     deleted_at: datetime 

# class Booking(BookingBase):
#     id: int
#     class Config:
#         orm_mode: True

# class BookingCreate(BookingBase):
#     pass 

# class BookingUpdate(BookingBase):
#     pass 

# class CustomerBase(BaseModel):
#     id: int 
#     username: str 
#     password: str 
#     first_name: str 
#     last_name: str 
#     email: str 
#     phone: str 
#     address: str 
#     created_at: datetime 
#     updated_at: datetime 
#     deleted_at: datetime 

# class CustomerCreate(CustomerBase):
#     pass

# class CustomerUpdate(CustomerBase):
#     pass 

# class Customer(CustomerBase):
#     id: int 
#     class Config:
#         orm_mode: True


