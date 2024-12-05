"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from uuid import UUID
from fastapi import APIRouter

from src.data.incidents import INCIDENTS
from src.models.incident_model import IncidentModel
from src.models.message_model import MessageModel
from src.utils.api_exception import APIException

IncidentRouter = APIRouter(prefix="/incidents")


@IncidentRouter.get("")
async def get_incidents() -> list[IncidentModel]:
    """
    Fetches a list of incidents.
    """
    return [IncidentModel.model_validate(incident) for incident in INCIDENTS.values()]


@IncidentRouter.get("/{incident_id}")
async def get_incident(incident_id: UUID) -> IncidentModel:
    """
    Fetches an incident by ID.
    """
    incident = INCIDENTS.get(incident_id)
    if incident:
        return IncidentModel.model_validate(incident)

    raise APIException("Incident not found!")


@IncidentRouter.post("/{incident_id}/assign")
async def assign_officer(incident_id: UUID, officer_name: str) -> MessageModel:
    """
    Assigns an officer to an incident.
    """
    incident = INCIDENTS.get(incident_id)
    if incident:
        if incident["status"] != "In Progress":
            incident["status"] = "In Progress"
            return MessageModel(message=f"{officer_name} assigned to incident.")

        return MessageModel(message="Incident already in progress.")

    raise APIException("Incident not found!")
