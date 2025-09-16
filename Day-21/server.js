const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, ".env") });
const mongoose = require("mongoose");
const { connectDB } = require('./config/connDB');
const { usersData } = require('./models/users')
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const session = require('express-session');
const cors = require('cors');
const {checkAuth} = require('./middleware/checkAuth');
const {SendEmailToUser} = require('./utils/mailSender');
const {otpData} = require('./models/otp');



const app = express();
const server = http.createServer(app);
const io = new Server(server);




app.use(express.json());
app.use(cors())
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: false,
        maxAge: 1000 * 60 * 5,
        httpOnly: true
    }
}))
app.set('view engine' , 'ejs')
app.set('views', path.join(__dirname, '/views'))
app.use(express.static(path.join(__dirname, '/public')))
connectDB();



app.get("/login", (req, res) => {
    res.render("index.ejs");
});

app.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body;
        if (!username || !password) {
            return res.status(400).json({ message: 'Username and password are required' })
        }
        const checkUser = await usersData.findOne({ username: username });
        if (!checkUser) {
            return res.status(400).json({ message: 'User not found' })
        }
        const isPasswordValid = await bcrypt.compare(password, checkUser.password);
        if (!isPasswordValid) {
            return res.status(400).json({ message: 'Invalid password' })
        }
        const token = jwt.sign({ firstName: checkUser.firstName, lastName: checkUser.lastName, email: checkUser.email, role: checkUser.role }, process.env.JWT_SECRET, { expiresIn: "5m" });
        req.session.token = token;
        return res.json({ message: 'login done' })
    }
    catch (error) {
        console.log(error);
        return res.status(500).json({ message: 'Internal server error' })
    }
    

})

app.get('/register', (req,res) => {
    res.render('register.ejs')
})

app.post('/register', async (req, res) => {
    const { firstName, lastName, username, email, password, role } = req.body;
    if (!firstName || !lastName || !username || !email || !password || !role) {
        return res.status(400).json({ message: "All inputs are required" })
    }
    const checkUser = await usersData.findOne({ username: username });
    if (checkUser) {
        return res.status(400).json({ message: 'Username already exists' })
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new usersData({ firstName, lastName, username, email, password: hashedPassword, role });
    await newUser.save();
    const token = jwt.sign({ firstName, lastName, email, role }, process.env.JWT_SECRET, { expiresIn: "5m" });
    req.session.token = token;
    return res.json({ message: 'User registered successfully' })
})

app.get('/logout', checkAuth,(req, res) => {
    req.session.destroy(
        (err) =>{
            if(err) {
                return res.status(500).json({ message: "Error logging out" });
            }
            return res.json({ message: "Logout successful" });
        }
    );
})

app.get('/chat', checkAuth, (req, res) => {
    res.render('chat.ejs');
})

app.get('/forgot-password', (req, res) => {
    res.render('forgotPassword.ejs');
})

app.post('/send-otp' , async (req, res) => {
    const { email } = req.body;
    if (!email) {
        return res.status(400).json({ message: "Email is required" });
    }
    const checkUser = await usersData.findOne({ email: email });
    if (!checkUser) {
        return res.status(400).json({ message: "email not found" });
    }
    const checkOtp = await otpData.findOne({ email: email });
    if (checkOtp) {
        return res.status(400).json({ message: "Wait for 5 minutes" });
    }
    const generatedOtp = Math.floor(100000 + Math.random() * 900000);
    const addOtp = new otpData({ email: email, otp: generatedOtp.toString()});
    await addOtp.save();
    SendEmailToUser(email, "Your OTP Code", `Your OTP code is ${generatedOtp}. It is valid for 5 minutes.`);
    return res.json({ message: "OTP sent successfully" });
    
    
})

app.get('/new-password', (req, res) => {
    res.render('newPassword.ejs');
})

app.post('/new-password', async (req, res) => {
    const { email, otp, newPassword, confirmPassword } = req.body;
    if (!email || !otp || !newPassword || !confirmPassword) {
        return res.status(400).json({ message: "All fields are required" });
    }
    const checkEmail = await otpData.findOne({ email: email });
    if (!checkEmail) {
        return res.status(400).json({ message: "Email not found or OTP expired" });
    }
    if (checkEmail.otp !== otp) {
        return res.status(400).json({ message: "Invalid OTP" });
    }
    if (newPassword !== confirmPassword) {
        return res.status(400).json({ message: "Passwords do not match" });
    }
    const hashPassword = await bcrypt.hash(newPassword, 10);
    await usersData.updateOne({ email: email }, { password: hashPassword });
    await otpData.deleteOne({ email: email });
    return res.json({ message: "Password updated successfully" });
})

app.all(/.*/, (req, res) => {
    res.status(404).render('404.ejs');
});


io.on("connection", (socket) => {

    socket.on("register", (username) => {
        socket.join(username);
        socket.username = username;
    });

    socket.on("private-message", ({ to, message }) => {
        io.to(to).emit("private-message", {
            from: socket.username,
            message,
        });
    });

    socket.on("disconnect", () => {
        console.log(`${socket.username} disconnected`);
    });
});

mongoose.connection.once("connected", () => {
    console.log("Connected to MongoDB...........");
    server.listen(3000, () => {
        console.log("Server running on http://localhost:3000..........");
    });

});

mongoose.connection.on("error", (err) => {
    console.log(err);
});




