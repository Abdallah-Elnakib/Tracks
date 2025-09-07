const express = require('express');
const authRouter = require('./router/authRouter');
const productRouter = require('./router/productsRouter');
const { connectDB } = require('./config/connDB');
const mongoose = require('mongoose');
const {checkAuth} = require('./middleware/checkAuth')
const app = express();
const { usersData } = require('./models/users')


app.use(express.json());
// 127.0.0.1:3000/
connectDB()







// app.use('/auth', authRouter)

// app.get('/users', checkAuth, async(req, res) => {
//     const users = await usersData.find()
//     res.json(users)
// })

// for (var i = 0; i < 3; i++) {
//   setTimeout(() => console.log(i), 1);
// }

// for (let i = 0; i < 3; i++) {
//   setTimeout(() => console.log(i), 1);
// }


// let x = 10

// let x = 20

// console.log(x)

// true = 1
// false = 0


// console.log(typeof(+true))
// let c = { greeting: "Hey!" };
// let d;

// d = Object.assign({}, c);
// d.greeting = "Hello";
// console.log(c.greeting);


mongoose.connection.once('connected', () => {
    console.log('MongoDB connected........');
    app.listen(3000, () => {
        console.log('Server is running on port 3000......');
    });
})

mongoose.connection.on('error', (err) => {
    console.log(err);
})