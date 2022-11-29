from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime,time,timedelta
from typing import Optional, List

app = FastAPI() 


class Item(BaseModel):
    name: str
    dob: datetime


@app.get("/")
async def root():
    return{"message":"API is working"}

@app.get("/api/v1/train_model")
async def root():
    return{"message":"Training API is working"}

@app.post("/api/v1/test_data")
async def create_item(item: Item):
    return item
