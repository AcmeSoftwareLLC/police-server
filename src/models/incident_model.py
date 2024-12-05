"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from pydantic import BaseModel


class IncidentModel(BaseModel):
    id: str
    type: str
    status: str
    priority: str
    location: str
    description: str
    timestamp: str
