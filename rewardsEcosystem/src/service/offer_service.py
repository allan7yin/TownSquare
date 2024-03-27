from uuid import UUID
from ..schema import offer_schema
from sqlalchemy.orm import Session
from ..model.offer_model import Offer

import logging

logger = logging.getLogger(__name__)  # Get logger for current module

"""Gets an offer by id
"""
async def get_offer(db: Session, id: UUID):
    offer = db.query(Offer).get(id)
    return offer


"""Gets all offers
"""
async def get_offers(db: Session):
    offers = db.query(Offer).all()
    return offers


"""Creates an offer
"""
async def create_offer(db: Session, offer: offer_schema.OfferIn):
    db_offer = Offer(
        startDate=offer.startDate,
        endDate=offer.endDate,
        description=offer.description,
        termsAndConditions=offer.termsAndConditions,
        offerType=offer.offerType
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer
