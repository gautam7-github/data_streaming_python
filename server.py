import asyncio
import json
from datetime import datetime as dt

import pandas as pd
import requests
import websockets

import generator as gtr


class DataFrameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def serve_dataframe(self, websocket, path):
        print("Serving DF")
        dataframe_person = gtr.generatePersonData()
        print(dataframe_person.head())

        await websocket.send(dataframe_person.to_json())

    async def send_periodically(self, websocket, interval):
        while True:
            await asyncio.sleep(interval)
            await self.serve_dataframe(websocket, None)

    async def handle_connection(self, websocket, path):
        await asyncio.gather(
            self.send_periodically(websocket, 5),
            websocket.recv()
        )

    def start(self):
        start_server = websockets.serve(
            self.handle_connection, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


print("Starting Server")
server = DataFrameServer("localhost", 8000)
print("Started Server on localhost:8000")
server.start()
