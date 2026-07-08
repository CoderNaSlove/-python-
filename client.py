import asyncio
import json
import websockets

async def main():
    uri = "ws://localhost:8000"

    async with websockets.connect(uri) as websocket:
        print("Подключено к серверу")

        while True:
            message = await websocket.recv()   

            print("Получено:", message)

            data = json.loads(message)       

            print(f"Источник: {data['chartId']}")
            print(f"Значение: {data['value']}")
            print()

asyncio.run(main())
