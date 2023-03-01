from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

@app.get("/hotels", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.get("/hotels/hotel", tags=["Root"])
async def read_root():
    return { "id": 0,
    "name": "string",
    "description": "string",
    "address": "string",
    "phone": "string",
    "room_id": 0,
    "created_at": "2023-03-01T21:30:13.524000",
    "updated_at": "2023-03-01T21:30:13.524000",
    "deleted_at": "2023-03-01T21:30:13.524000"}

def test_read_main():
    response = client.get("/hotels")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}

def test_read_main2():
    response = client.get("/hotels/hotel/?skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() == { 
    "id": 0,
    "name": "string",
    "description": "string",
    "address": "string",
    "phone": "string",
    "room_id": 0,
    "created_at": "2023-03-01T21:30:13.524000",
    "updated_at": "2023-03-01T21:30:13.524000",
    "deleted_at": "2023-03-01T21:30:13.524000"
  }