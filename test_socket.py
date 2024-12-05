from asyncio import run
from websockets import connect


async def test_websocket():
    uri = "ws://localhost:8000/ws/incidents"
    headers = {"Authorization": "Bearer test"}

    try:
        async with connect(uri, additional_headers=headers) as websocket:
            print("Connected to WebSocket server")

            while True:
                message = await websocket.recv()
                print(f"Incident: {message}")
    except Exception as e:
        print(e)


run(test_websocket())
