# Importações
import websockets
import asyncio

# Função principal que ira conectar e comunicar
# Servidor
async def listen():
    url = "ws://127.0.0.1:7890"
    # Conecta ao servidor
    async with websockets.connect(url) as ws:
        # Envia uma mensagem
        await ws.send("Hello Server!")
        # Continua vivo pra sempre ouvindo as mensagens
        while True:
            msg = await ws.recv()
            print(msg)

# Inicia a conexão
asyncio.get_event_loop().run_until_complete(listen())