# Police Server

## Run the server
```
docker run -p 1234:8000 ghcr.io/acmesoftwarellc/police-server:2.0.1
```

## Authorization
Send Bearer token in the Authorization header to access the API endpoints.

```
TOKEN = SHA256 hash of "acmesoftwarellc".
```

### REST API Endpoints
Access the server docs at http://localhost:1234/docs

### WebSocket Endpoint
```ws://localhost:1234/ws/incidents```

> [!NOTE]  
For web, headers are not supported in WebSocket connections. Use `token` query parameter for authentication.
```ws://localhost:1234/ws/incidents?token=$TOKEN```