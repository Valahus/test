
# -*- coding: utf-8 -*-
# !/usr/bin/python3

# External
from fastapi import FastAPI

# BeeOS
from app.database import engine, Base
from app.routers.users import router as UserRouter

# from app.routers.companies import router as CompanyRouter
from app.routers.hotel import router as HotelRouter
from app.routers.room import router as RoomRouter
from app.routers.roomcategory import router as RoomCategoryRouter

# from app.routers.price import router as PriceRouter
# from app.routers.additionalservice import router as AdditionalServiceRouter
# from app.routers.payment import router as PaymentRouter
# from app.routers.booking import router as BookingRouter
# from app.routers.customer import router as CustomerRouter
# from app.routers.auth import router as AuthRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi.testclient import TestClient

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/hotels/docs", openapi_url="/hotels/openapi")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["Users"], prefix="/hotels/users")
# app.include_router(CustomerRouter, tags=["Customers"], prefix="/customers")
app.include_router(HotelRouter, tags=["Hotel"], prefix="/hotels/hotel")
app.include_router(RoomRouter, tags=["Room"], prefix="/hotels/room")
app.include_router(
    RoomCategoryRouter, tags=["RoomCategory"], prefix="/hotels/roomcategory"
)
# app.include_router(PriceRouter, tags=["Price"], prefix="/price")
# app.include_router(AdditionalServiceRouter, tags=["AdditionalService"], prefix="/additionalservice")
# app.include_router(PaymentRouter, tags=["Payment"], prefix="/payment")
# app.include_router(BookingRouter, tags=["Booking"], prefix="/booking")

# app.include_router()


@app.get("/hotels", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


# TODO
# - Order : post, get, put, delete


client = TestClient(app)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://postgres:changeme@db:5432/pgdb'

def test_read_main():
    response = client.get("/hotels")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}