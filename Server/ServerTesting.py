import asyncio
import json
import websockets

clients_connected = []

async def new_connection(websocket, room_id):
  clients_connected.append([websocket, room_id])
  print("Cliente conectado na sala: " + room_id)

async def propagate_message(message):
  for client in clients_connected:
    if client[1] == message['RoomID']:
      await client[0].send(json.dumps(message))

async def hear_messages(websocket, path):
  try:
    async for message in websocket:
      msg = json.loads(message)
      if msg['first_connection']:
        await new_connection(websocket, msg['RoomID'])
      await propagate_message(msg)
  except websockets.exceptions.ConnectionClosed as e:
    for client in clients_connected:
      if client[0] == websocket:
        print("Cliente desconectado da sala: " + client[1])
        clients_connected.remove(client)

async def start_server():
  server = await websockets.serve(hear_messages, "localhost", 8765)
  print("Server started")
  return server

async def main():
  await start_server()
  await asyncio.Event().wait()


if __name__ == "__main__":
  asyncio.run(main())
