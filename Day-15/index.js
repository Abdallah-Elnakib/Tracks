const express = require('express');
const { connectDB } = require('./config/connDB');
const mongoose = require('mongoose');
const authRouter = require('./router/authRouter')
const session = require("express-session");
const cors = require('cors')
const { usersData } = require('./models/users');
const { checkAuth } = require('./middleware/checkAuth');

const app = express();

app.use(express.json())

const ips = ['http://127.0.0.1:3000', "http://localhost:3000", "http://127.0.0.1:5500"];
app.use(cors({
    origin: (ip, callback) => {
        try {
            console.log(ip);
            if (!ip || ips.includes(ip)) {
                callback(null, true);
            }
            else {
                callback("Not allowed by CORS");
            }
        }
        catch (error) {
            console.log(error);
        }
        
    }
}))


// app.use(cors({
//   origin: (origin, callback) => {
//     if (allowedOrigins.includes(origin)) {
//       callback(null, true);
//     } else {
//       callback(new Error("Not allowed by CORS"));
//     }
//   },
//   credentials: true,
// }));




app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        maxAge: 1000 * 60,
        httpOnly: true,
        secure: false
    }
}));

connectDB()


app.use('/auth', authRouter) // login register logout



app.get('/users', async (req, res) => {
    const users = await usersData.find();
    res.json(users)
})

app.get('/:username', checkAuth, async (req, res) => {
    const username = req.params.username;
    if (!username) {
        return res.status(400).send('username  is required');
    }
    const getUser = await usersData.findOne({ username })
    if (!getUser) {
        return res.status(404).send('user not found');
    }
    res.json(getUser)
})



mongoose.connection.once('connected', () => {
    console.log("MongoDB connected..............");
    app.listen(process.env.PORT, () => console.log('Server Runing...........'))
})

mongoose.connection.on('error', (err) => {
    console.log(err);
})


