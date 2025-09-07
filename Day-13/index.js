const express = require('express');
const {connectDB} = require('./config/connDB');
const path = require('path');
const mongoose = require('mongoose');
require('dotenv').config();
const app = express();

app.use(express.json())
app.set('view engine' , 'ejs')
app.set('views', path.join(__dirname, '/views'))
app.use(express.static(path.join(__dirname, '/public')))

app.use((err, req, res, next) => {
  res.status(err.statusCode || 500).json({
    status: err.status || 'error',
    message: err.message || 'Internal Server Error'
  });
});

// app.use('/auth', require('./routes/index')) 
// app.get('/login' , (req,res)=>{

connectDB()



mongoose.connection.once('connected' ,()=>{
    console.log("MongoDB connected..............");
    app.listen(process.env.PORT,()=>console.log('Server Runing...........'))
})

mongoose.connection.on('error', (err)=>{
    console.log(err);
})

module.exports = {app}