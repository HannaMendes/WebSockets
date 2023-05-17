import websockets
import asyncio

PORT = 7890

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("Um cliente acaba de se conectar")
    try:
        async for message in websocket:
            print("Mensagem recebida pelo cliente: " + message)
            await websocket.send("De volta pra você: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("Um cliente acaba de se desconectar")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

