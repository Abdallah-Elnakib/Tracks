const express = require('express');
const path = require('path')
const app = express();
const {connectDB} = require('./config/connectDB') 
app.use(express.json())
app.set('view engine' , 'ejs')
app.set('views', path.join(__dirname, '/views'))



app.use(express.static(path.join(__dirname, '/public')))


app.listen(3000,()=>{
    connectDB()
    console.log("Server is running on port 3000..........");
})


module.exports = {app}