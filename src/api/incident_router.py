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
from src.data.officers import OFFICERS
from src.models.incident_model import IncidentModel
from src.models.message_model import MessageModel
from src.models.officer_model import OfficerModel
from src.utils.api_exception import APIException

IncidentRouter = APIRouter(prefix="/incidents", tags=["Incidents"])


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
async def assign_officer(incident_id: UUID, officer_id: UUID) -> MessageModel:
    """
    Assigns an officer to an incident.

    Note: The officer will be assigned temporarily until the server restarts.
    """
    incident = INCIDENTS.get(incident_id)
    if incident:
        if incident["status"] != "In Progress":
            incident["status"] = "In Progress"

            raw_officer = OFFICERS[officer_id]
            if raw_officer:
                officer = OfficerModel.model_validate(raw_officer)
                if officer.status == "available":
                    incident["assignee"] = officer.id
                    return MessageModel(
                        message=f"{officer.name} assigned to the incident."
                    )
                raise APIException("Officer is not available!")
            raise APIException("Officer not found!")
        raise APIException("Incident already in progress.")
    raise APIException("Incident not found!")
