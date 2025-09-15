const express = require('express');
const http = require('http');
const cors = require('cors');
const path = require('path');
const { Server } = require("socket.io");
require('dotenv').config({path : path.join(__dirname, ".env")});
const app = express();
const httpServer = http.createServer(app);

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, './index.html'))
})

httpServer.listen(process.env.PORT, () => {
    console.log(`Server is running on port ${process.env.PORT}.........`);
})





