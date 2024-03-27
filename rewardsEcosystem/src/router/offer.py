from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ..service import offer_service
from ..database import core
from ..schema import offer_schema

router = APIRouter(
    prefix="/offers",
    tags=["offers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}", response_model=offer_schema.OfferOut)
async def getOffer(id: UUID, db: Session = Depends(core.get_db)):
    try:
        offer = offer_service.get_offer(db=db, id=id)
        return offer
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

    
@router.get("/", response_model=offer_schema.OfferListOut)
async def getOffers(db: Session = Depends(core.get_db)):
    try:
        offers = offer_service.get_offers(db=db)
        return offers
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
