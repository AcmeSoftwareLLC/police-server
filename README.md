# Police Server

## Run the server
```
docker run -p 1234:8000 ghcr.io/acmesoftwarellc/police-server:0.0.1
```

## Authorization
Send Bearer token in the Authorization header to access the API endpoints.

```
TOKEN = SHA256 hash of "acmesoftwarellc".
```

### REST API Endpoints
Access the server docs at http://localhost:8000/docs

### WebSocket Endpoint
http://localhost:8000/ws/incidents