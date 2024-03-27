from fastapi import Depends, FastAPI
from .internal import admin
from .router import vendor, offer, member_offer
from square.client import Client
from .database.core import Base, engine
from dotenv import load_dotenv
from .square import square_config

import os

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(admin.router)
app.include_router(vendor.router)
app.include_router(offer.router)
app.include_router(member_offer.router)


@app.get("/")
async def root():
    return {"message": "Hello! Connection Established"}

@app.get("/square-test")
async def testSquareConnection(client: Client = Depends(square_config.get_square_client)):
    print(os.getenv("SANDBOX_ACCESS_TOKEN"))
    result = client.customers.list_customers(count=False)
    return result
