"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from uuid import UUID


INCIDENTS: dict[UUID, dict[str, str]] = {
    UUID("6d5fa4c6-4ec4-415d-9be0-d7f0ba9558b3"): {
        "id": "6d5fa4c6-4ec4-415d-9be0-d7f0ba9558b3",
        "type": "Theft",
        "status": "Pending",
        "priority": "High",
        "location": "Downtown",
        "description": "Reported theft at a convenience store.",
        "timestamp": "2024-12-01T12:00:00Z",
    },
    UUID("6d5fa4c6-4ec4-415d-9be0-d7f0ba9558b3"): {
        "id": "bb7605f1-cba8-40e1-9688-092302bc1778",
        "type": "Accident",
        "status": "In Progress",
        "priority": "Medium",
        "location": "Highway 15",
        "description": "Two-vehicle collision reported.",
        "timestamp": "2024-12-01T13:00:00Z",
    },
}
