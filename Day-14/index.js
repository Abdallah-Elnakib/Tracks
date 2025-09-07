const express = require('express');
const authRouter = require('./router/authRouter');
const productRouter = require('./router/productsRouter');
const { connectDB } = require('./config/connDB');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());
// 127.0.0.1:3000/
connectDB()
app.use('/auth', authRouter)

mongoose.connection.once('connected', () => {
    console.log('MongoDB connected........');
    app.listen(3000, () => {
        console.log('Server is running on port 3000......');
    });
})

mongoose.connection.on('error', (err) => {
    console.log(err);
})