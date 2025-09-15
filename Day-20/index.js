const express = require('express');
const http = require('http');
const cors = require('cors');
const path = require('path');
const { Server } = require("socket.io");
require('dotenv').config({path : path.join(__dirname, ".env")});
const app = express();
const httpServer = http.createServer(app);
const io = new Server(httpServer)


app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './index.html'))
})

io.on('connection', (socket) => {
  socket.on('chat message', (msg) => {
    io.emit('chat message', msg);
  });
});





httpServer.listen(process.env.PORT, () => {
    console.log(`Server is running on port ${process.env.PORT}.........`);
})





