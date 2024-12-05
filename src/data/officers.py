"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from uuid import UUID


OFFICERS: dict[UUID, dict[str, str]] = {
    UUID("addf2302-fb3d-4519-a845-b676a4a3ba34"): {
        "id": "addf2302-fb3d-4519-a845-b676a4a3ba34",
        "name": "Officer John Doe",
        "rank": "Sergeant",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=john",
    },
    UUID("9cd07393-d4f2-453c-a086-06656f4f7d06"): {
        "id": "9cd07393-d4f2-453c-a086-06656f4f7d06",
        "name": "Officer Jane Smith",
        "rank": "Officer",
        "status": "unavailable",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=janesm",
    },
    UUID("a17007e2-3154-41cf-a966-2993e7b4456f"): {
        "id": "a17007e2-3154-41cf-a966-2993e7b4456f",
        "name": "Officer Mike Johnson",
        "rank": "Lieutenant",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=mike",
    },
    UUID("8a5329dd-3f3b-4a22-bf2f-581786f50978"): {
        "id": "8a5329dd-3f3b-4a22-bf2f-581786f50978",
        "name": "Officer Sarah Brown",
        "rank": "Officer",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=aobsarah",
    },
    UUID("d1f2b3c4-e5d6-4b7c-bf6e-9ac54a99bc34"): {
        "id": "d1f2b3c4-e5d6-4b7c-bf6e-9ac54a99bc34",
        "name": "Officer Tom Clark",
        "rank": "Detective",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=tomclark",
    },
    UUID("0e71b7a5-44ac-42d7-a739-d3d1b18a0a9e"): {
        "id": "0e71b7a5-44ac-42d7-a739-d3d1b18a0a9e",
        "name": "Officer Emily Davis",
        "rank": "Sergeant",
        "status": "unavailable",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=emilyda",
    },
    UUID("c7d8f9a4-739b-4a72-9896-c032e9b55747"): {
        "id": "c7d8f9a4-739b-4a72-9896-c032e9b55747",
        "name": "Officer Brian Taylor",
        "rank": "Officer",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=briantaylor",
    },
    UUID("5e2f306d-4d3e-4859-b053-d72634b7464f"): {
        "id": "5e2f306d-4d3e-4859-b053-d72634b7464f",
        "name": "Officer Lisa Moore",
        "rank": "Lieutenant",
        "status": "available",
        "image_url": "https://api.dicebear.com/9.x/personas/svg?seed=lisamoo",
    },
}
