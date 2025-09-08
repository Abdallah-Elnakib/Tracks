const express = require('express');
const {connectDB} = require('./config/connDB');
const mongoose = require('mongoose');
const authRouter = require('./router/authRouter')
const session = require("express-session");
const app = express();

app.use(express.json())


app.use(session({
  secret: process.env.SESSION_SECRET,   
  resave: false,           
  saveUninitialized: false,    
  cookie: {
    maxAge: 1000 * 60 ,  
    httpOnly: true,              
    secure: false             
  }
}));

connectDB()



app.use('/auth',authRouter) // login register logout


mongoose.connection.once('connected' ,()=>{
    console.log("MongoDB connected..............");
    app.listen(process.env.PORT,()=>console.log('Server Runing...........'))
})

mongoose.connection.on('error',(err)=>{
    console.log(err);
})


