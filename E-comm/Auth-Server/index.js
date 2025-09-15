const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const { connectDB } = require('./config/connDB');
const authRouter = require('./router/authRouter');
const {checkReq} = require('./middleware/checkREQ')
const app = express();
app.use(express.json());
app.use(cors());
app.use(checkReq)



connectDB();




app.use('/auth', authRouter)

const events = require('events');
const eventEmitter = new events.EventEmitter();

eventEmitter.on('serverStarted', () => {
    console.log(`Server started on port 3000`);
});



mongoose.connection.once('connected', () => {
    console.log('Connected to MongoDB');
    app.listen(process.env.PORT, () => {
        eventEmitter.emit('serverStarted');
    });
});

mongoose.connection.on('error', err => {
    console.log(err);
});



// const http = require('http');
// const server = http.createServer((req,res) => {
//     if (req.url == '/login') {
//         const {username , password} = req.body;
        
//     }
//     else if (req.url == '/register') {

//     }
    
// });


// server.listen(3000 , () => {
//     console.log('Server started on port 3000');
// });