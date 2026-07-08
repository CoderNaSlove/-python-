import asyncio
import json
import math
import random
import time
import websockets

am1, ct1, fr1 = 2, 23, 0.1
am2, ct2, fr2 = 8, 50, 0.1



async def handle_client(websocket):
    print("Клиент подключился")

    while True:
        current_time = time.time()
        
        val1 = ct1 + am1 * math.sin(fr1 * current_time)
        val1 += random.gauss(0, 0.2)  
        
        data_sensor_1 = {
            "chartId": "sensor_1",
            "value": round(val1, 1)
        }
        
       
        val2 = ct2 + am2 * math.cos(fr2 * current_time)
        val2 += random.gauss(0, 0.3)  
        
        data_sensor_2 = {
            "chartId": "sensor_2",
            "value": round(val2, 1)
        }

        
        await websocket.send(json.dumps(data_sensor_1))
        await websocket.send(json.dumps(data_sensor_2))

        
        await asyncio.sleep(0.1)


async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        print("Сервер запущен")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
