const express = require('express');
const {connectDB} = require('./config/connDB');
const mongoose = require('mongoose');
const authRouter = require('./router/authRouter')

const app = express();

app.use(express.json())


connectDB()



app.use('/auth',authRouter) // login register logout


mongoose.connection.once('connected' ,()=>{
    console.log("MongoDB connected..............");
    app.listen(process.env.PORT,()=>console.log('Server Runing...........'))
})

mongoose.connection.on('error',(err)=>{
    console.log(err);
})


