"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from uuid import UUID
from fastapi import APIRouter

from src.data.officers import OFFICERS
from src.models.officer_model import OfficerModel
from src.utils.api_exception import APIException

OfficerRouter = APIRouter(prefix="/officers", tags=["Officers"])


@OfficerRouter.get("")
async def get_officers() -> list[OfficerModel]:
    return [OfficerModel.model_validate(officer) for officer in OFFICERS.values()]


@OfficerRouter.get("/{officer_id}")
async def get_officer(officer_id: UUID) -> OfficerModel:
    officer = OFFICERS.get(officer_id)
    if officer:
        return OfficerModel.model_validate(officer)

    raise APIException("Officer not found!")
