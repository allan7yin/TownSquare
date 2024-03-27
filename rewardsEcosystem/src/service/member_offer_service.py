from typing import List
from uuid import UUID
from square.client import Client
from ..square import square_config
from fastapi import Depends
from ..enums import OFFER_STATUS
from sqlalchemy import or_
from sqlalchemy.orm import Session
from src.model.member_offer_model import MemberOffer

import logging

logger = logging.getLogger(__name__)  # Get logger for currenØt module

"""Pulbishes offers, creating corresponding member offers for the vendor, offer pair
    - Find all offers that match the vendor_id, offer_id, and constraints, create member offers for those
"""
def create_member_offers(db: Session, vendor_ids: List[UUID], offer_id: UUID, client: Client):
    # create member offers for each pair (vendor_id, offer_id)
    # make retrieve members with API call to Square, or use SDK
    response = client.customers.list_customers()
    member_list = response["body"]["customers"]
    member_ids = [customer["id"] for customer in member_list]
    print(member_ids)

    published_member_offers = []
    for member_id in member_ids:
        for vendor_id in vendor_ids:
            published_member_offers.append(
                create_member_offer(db, member_id, vendor_id, offer_id)
            )
    return published_member_offers


"""Helper function. Creates a single member offer for a single vendor and single offer
"""
def create_member_offer(db: Session, vendor_id: UUID, member_id: UUID, offer_id: UUID):
    # create a single member offer 
    db_member_offer = MemberOffer(
        member_id=member_id, vendor_id=vendor_id, offer_id=offer_id, status=OFFER_STATUS.active
    )
    db.add(db_member_offer)
    db.commit()
    db.refresh(db_member_offer)
    return db_member_offer
    