"""
Copyright © 2024 Acme Software LLC. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution,
modification, or use of this software, in whole or in part, is strictly prohibited
without prior written permission from Acme Software LLC.

For inquiries, contact: legal@acmesoftware.com
"""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import IncidentRouter, OfficerRouter, WebsocketRouter
from src.utils.api_exception import APIException
from src.utils.auth_bearer import AuthBearer


def create_app() -> FastAPI:
    app = FastAPI(
        title="Incident Management API",
        description="A simple API to manage incidents and assign officers.",
        version="1.0.0",
        contact={
            "name": "Acme Software LLC",
            "url": "https://acmesoftware.com",
            "email": "info@acmesoftware.com",
        },
        swagger_ui_parameters={
            "syntaxHighlight.theme": "tomorrow-night",
            "tryItOutEnabled": True,
            "persistAuthorization": True,
        },
    )

    app.include_router(
        IncidentRouter,
        prefix="/api/v1",
        dependencies=[Depends(AuthBearer())],
    )
    app.include_router(
        OfficerRouter,
        prefix="/api/v1",
        dependencies=[Depends(AuthBearer())],
    )
    app.include_router(WebsocketRouter)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(APIException, APIException.handler)

    return app


app = create_app()
