const mongoose = require('mongoose');
const express = require('express');
const cors = require('cors');
const session = require('express-session');
const {connectDB} = require('./config/connDB');
const authRouter = require('./router/authRouter');
const {checkAuth} = require('./middleware/checkAuth');

const app = express();

app.use(express.json())



const ips = ['http://127.0.0.1:3000', "http://localhost:3000", "http://127.0.0.1:5500"];
app.use(cors({
    origin: (ip, callback) => {
        try {
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
        
    },
    credentials: true
}))

app.use(session({
    secret : process.env.SESSION_SECRET,
    resave : false,
    saveUninitialized : false,
    cookie : {
        maxAge : 1000 * 60,
        httpOnly : true,
        secure : false
    }
}))

connectDB()

app.use('/auth', authRouter)
// app.use('/users')
// app.use('/students')

app.use(checkAuth) // req.user = {}

app.get('/', (req,res) => {
    if (req.user.role !== 'admin') {
        return res.status(401).json({ message: "Unauthorized" });
    }
    res.send(req.user)
})


mongoose.connection.once('connected' ,()=>{
    console.log("MongoDB connected..............");
    app.listen(process.env.PORT,()=>console.log('Server Runing...........'))
})

mongoose.connection.on('error', (err)=>{
    console.log(err);
})