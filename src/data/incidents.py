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
        "location_coordinates": "40.7128,-74.0060",  # New York City
        "description": "Reported theft at a convenience store.",
        "timestamp": "2024-12-01T12:00:00Z",
    },
    UUID("bb7605f1-cba8-40e1-9688-092302bc1778"): {
        "id": "bb7605f1-cba8-40e1-9688-092302bc1778",
        "type": "Accident",
        "status": "In Progress",
        "priority": "Medium",
        "location": "Highway 15",
        "location_coordinates": "34.0522,-118.2437",  # Los Angeles
        "description": "Two-vehicle collision reported.",
        "timestamp": "2024-12-01T13:00:00Z",
    },
    UUID("d1a9f14c-4a8d-4335-a2e6-cde6cfbe3f43"): {
        "id": "d1a9f14c-4a8d-4335-a2e6-cde6cfbe3f43",
        "type": "Fire",
        "status": "Resolved",
        "priority": "High",
        "location": "Suburban Apartment Complex",
        "location_coordinates": "34.0522,-118.2437",  # Los Angeles
        "description": "Fire in the kitchen of an apartment building.",
        "timestamp": "2024-12-01T14:30:00Z",
    },
    UUID("c458ed14-ec6c-4df7-a9d5-2d0d694fdb0b"): {
        "id": "c458ed14-ec6c-4df7-a9d5-2d0d694fdb0b",
        "type": "Vandalism",
        "status": "Pending",
        "priority": "Low",
        "location": "City Park",
        "location_coordinates": "37.7749,-122.4194",  # San Francisco
        "description": "Damaged park benches and graffiti on walls.",
        "timestamp": "2024-12-01T15:00:00Z",
    },
    UUID("e548e6f2-7f3c-4bcd-91d2-3a8aef1a3ed1"): {
        "id": "e548e6f2-7f3c-4bcd-91d2-3a8aef1a3ed1",
        "type": "Robbery",
        "status": "In Progress",
        "priority": "Critical",
        "location": "Downtown Bank",
        "location_coordinates": "40.7128,-74.0060",  # New York City
        "description": "Armed robbery in progress at a local bank.",
        "timestamp": "2024-12-01T16:00:00Z",
    },
    UUID("f9e22f9b-f248-421b-a2cd-df6578f7a2c3"): {
        "id": "f9e22f9b-f248-421b-a2cd-df6578f7a2c3",
        "type": "Hit and Run",
        "status": "Pending",
        "priority": "Medium",
        "location": "City Center",
        "location_coordinates": "41.8781,-87.6298",  # Chicago
        "description": "Driver fled the scene after hitting a pedestrian.",
        "timestamp": "2024-12-01T17:30:00Z",
    },
    UUID("b9c9f215-c92f-4c3d-9c91-34e6c8ad2c5d"): {
        "id": "b9c9f215-c92f-4c3d-9c91-34e6c8ad2c5d",
        "type": "Missing Person",
        "status": "Pending",
        "priority": "High",
        "location": "Greenwood High School",
        "location_coordinates": "40.7608,-111.8910",  # Salt Lake City
        "description": "Teenager reported missing after school hours.",
        "timestamp": "2024-12-01T18:00:00Z",
    },
    UUID("b22c9a8a-8f9b-453b-a7b7-49f7dcd1ac52"): {
        "id": "b22c9a8a-8f9b-453b-a7b7-49f7dcd1ac52",
        "type": "Explosion",
        "status": "Resolved",
        "priority": "High",
        "location": "Industrial District",
        "location_coordinates": "36.1627,-86.7816",  # Nashville
        "description": "Gas explosion at a chemical plant, several casualties.",
        "timestamp": "2024-12-02T10:00:00Z",
    },
    UUID("4ac4bc49-0514-4577-bc9e-36e4429f1e6a"): {
        "id": "4ac4bc49-0514-4577-bc9e-36e4429f1e6a",
        "type": "Flood",
        "status": "In Progress",
        "priority": "High",
        "location": "Riverbank Road",
        "location_coordinates": "29.7604,-95.3698",  # Houston
        "description": "Flash flood affecting nearby homes.",
        "timestamp": "2024-12-02T11:00:00Z",
    },
    UUID("ae2eaa7f-c8bb-4b93-8189-ccd180e2a2ba"): {
        "id": "ae2eaa7f-c8bb-4b93-8189-ccd180e2a2ba",
        "type": "Chemical Spill",
        "status": "Pending",
        "priority": "Medium",
        "location": "Main Street Warehouse",
        "location_coordinates": "34.0522,-118.2437",  # Los Angeles
        "description": "Hazardous chemical spill in a warehouse.",
        "timestamp": "2024-12-02T12:00:00Z",
    },
    UUID("9b21d5e9-0b72-4729-b29f-3183c8cbb90e"): {
        "id": "9b21d5e9-0b72-4729-b29f-3183c8cbb90e",
        "type": "Domestic Dispute",
        "status": "In Progress",
        "priority": "Low",
        "location": "Residential Area",
        "location_coordinates": "37.7749,-122.4194",  # San Francisco
        "description": "Ongoing dispute between neighbors.",
        "timestamp": "2024-12-02T13:00:00Z",
    },
    UUID("7e93f17b-9f92-44f9-a833-1631f5b14be2"): {
        "id": "7e93f17b-9f92-44f9-a833-1631f5b14be2",
        "type": "Burglary",
        "status": "Pending",
        "priority": "Medium",
        "location": "Greenwood Mall",
        "location_coordinates": "40.7608,-111.8910",  # Salt Lake City
        "description": "Break-in at a shopping mall after hours.",
        "timestamp": "2024-12-02T14:30:00Z",
    },
    UUID("5fba8a97-e905-49f7-ae8b-8d563ff24f8b"): {
        "id": "5fba8a97-e905-49f7-ae8b-8d563ff24f8b",
        "type": "Terrorist Attack",
        "status": "Resolved",
        "priority": "Critical",
        "location": "Downtown City Square",
        "location_coordinates": "40.7128,-74.0060",  # New York City
        "description": "Explosion and gunfire in a crowded area.",
        "timestamp": "2024-12-02T15:30:00Z",
    },
    UUID("d7e87c5d-3c3f-40a5-bb9b-f2f460e79924"): {
        "id": "d7e87c5d-3c3f-40a5-bb9b-f2f460e79924",
        "type": "Shooting",
        "status": "Pending",
        "priority": "Critical",
        "location": "Downtown Bar",
        "location_coordinates": "39.7392,-104.9903",  # Denver
        "description": "Active shooter situation in a downtown bar.",
        "timestamp": "2024-12-02T16:00:00Z",
    },
}
