import asyncio
import json
import math
import random
import time
import websockets

am1 = 2
ct1 = 23
fr1 = 0.1

am2 = 8
ct2 = 50
fr2 = 0.1


async def handle_client(websocket):
    print("Клиент подключился")

    while True:
        current_time = time.time()
        

        val1 = ct1 + am1 * math.sin(fr1 * current_time)
        val1 += random.gauss(0, 0.2)
        

        val2 = ct2 + am2 * math.cos(fr2 * current_time)
        val2 += random.gauss(0, 0.4)
        

        data = {
            "sensor_1": round(val1, 1),
            "sensor_2": round(val2, 1)
        }


        await websocket.send(json.dumps(data))

        await asyncio.sleep(0.1)


async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        print("Сервер запущен")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
