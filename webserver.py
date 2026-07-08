import asyncio
import json
import math
import random
import time
import websockets

am=2
ct=23
fr=0.1

def generate_data():
    value = ct + am * math.sin(fr*time.time())
    value += random.gauss(0, 0.2)

    return round(value, 1)


async def handle_client(websocket):
    print("Клиент подключился")

    while True:
        data = {
            "chartId": "sensor_1",
            "value": generate_data()
        }

        await websocket.send(json.dumps(data))

        await asyncio.sleep(0.1)


async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        print("Сервер запущен")
        await asyncio.Future()


asyncio.run(main())
