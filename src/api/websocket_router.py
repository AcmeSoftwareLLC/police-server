"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

import asyncio
import random
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.data.incidents import INCIDENTS
from src.models.incident_model import IncidentModel
from src.models.socket_message_model import SocketMessageModel
from src.utils.auth_bearer import AuthBearer
from src.utils.connection_manager import ConnectionManager


WebsocketRouter = APIRouter(prefix="/ws")

manager = ConnectionManager()


@WebsocketRouter.websocket("/incidents")
async def track_incident_updates(websocket: WebSocket):
    """
    WebSocket endpoint to broadcast incident updates.
    """
    AuthBearer.validate_auth(websocket.headers.get("Authorization"))

    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(5)
            incident_id = random.choice(list(INCIDENTS.keys()))
            incident = IncidentModel.model_validate(INCIDENTS[incident_id])
            updated_incident = incident.model_copy(
                update={"status": random.choice(["Pending", "In Progress", "Resolved"])}
            )

            await manager.broadcast(
                SocketMessageModel(event="update", data=updated_incident)
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
