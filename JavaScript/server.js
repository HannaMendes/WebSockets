const WebSocket = require('ws');

//Define a porta
const PORT = 5000;

const wsServer = new WebSocket.Server({
    port: PORT
});

//Cria uma mensagem de limte para o cliente enviar
function messageSizeLimitMiddleware(socket) {
    return function(msg) {
        if (msg.length > 500) {
            socket.send("Error: limite maximo da mensagem excedido");
        } else {
            // Chama o próximo middleware na cadeia de middlewares, ou processa a mensagem
            socket.next(msg);
        }
    }
}

wsServer.on('connection', function (socket) {
    console.log("Um cliente acaba de se conectar!");

    // middleware para limitar o tamanho da mensagem
    socket.on('message', messageSizeLimitMiddleware(socket));

    // middleware para processar a mensagem
    socket.next = function(msg) {
        // Broadcast para conectar todos os clients
        wsServer.clients.forEach(function (client) {
            client.send("Alguem disse: " + msg);
        });
    }
});

console.log( (new Date()) + "Server is listening on port " + PORT);