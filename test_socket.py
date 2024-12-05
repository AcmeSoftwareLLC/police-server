import asyncio
import websockets


async def test_websocket():
    uri = "ws://localhost:8000/ws/incidents"

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")

        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(test_websocket())
