const express = require('express');
const mongoose = require('mongoose');
const {connectDB} = require('./config/connDB');
const authRouter = require('./router/authRouter');


const app = express();
app.use(express.json());


connectDB()


app.use('/auth', authRouter)


mongoose.connection.once('connected', () => {
    console.log('Connected to MongoDB')
    app.listen(process.env.PORT, () => console.log('Server started on port 3000'))
})

mongoose.connection.on('error', err => {
    console.log(err)
})

