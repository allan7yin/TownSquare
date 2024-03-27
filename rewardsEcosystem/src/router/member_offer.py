from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ..service import member_offer_service
from ..database import core
from ..schema import member_offer_schema

from square.client import Client
from ..square import square_config

router = APIRouter(
    prefix="/memberOffers",
    tags=["memberOffers"],
    responses={404: {"description": "Not found"}},
)

# create vendor endpoint
@router.post("/", response_model=member_offer_schema.MemberOfferOut)
def createMemberOffer(memberOffer: member_offer_schema.MemberOfferIn, db: Session = Depends(core.get_db), client: Client = Depends(square_config.get_square_client)):
    try:
        published_created_member_offers = member_offer_service.create_member_offers(
            db=db,
            vendor_ids=memberOffer.vendor_ids,
            offer_id=memberOffer.offer_id,
            client=client)
        return published_created_member_offers
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


