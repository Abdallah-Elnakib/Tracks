const { usersData } = require('../models/users');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { Otp } = require('../models/Otp');
const { SendEmailToUser } = require('../utils/mailSender');

const register = async (req, res) => {
    try {
        const { firstName, lastName, username, email, address, password, role } = req.body;
        if (!firstName || !lastName || !username || !email || !address || !password || !role) {
            return res.status(400).json({ message: "All inputs are required" })
        }
        const checkUser = await usersData.findOne({ $or: [{ username: username }, { email: email }] });
        if (checkUser) {
            if (checkUser.username === username) {
                return res.status(400).json({ message: "Username already exists" });
            } else if (checkUser.email === email) {
                return res.status(400).json({ message: "Email already exists" });
            }
        }
        if (password.length < 8) {
            return res.status(400).json({ message: "Password must be at least 8 characters" });
        }
        if (!['user', 'admin'].includes(role)) {
            return res.status(400).json({ message: "Role must be either 'user' or 'admin'" });
        }
        if (typeof (address) !== 'object') {
            return res.status(400).json({ message: "Address must be an array of objects" });
        }
        if (address.length === 0) {
            return res.status(400).json({ message: "Address must not be empty" });
        }
        let checkEmail = email.split('@'); // ['abdallah.elnakib', 'gmail.com']
        if (!['gmail.com', 'yahoo.com', 'hotmail.com'].includes(checkEmail[1])) {
            return res.status(400).json({ message: "Email must be a Gmail address" });
        }
        const hashPassword = await bcrypt.hash(password, 10),
            newUser = new usersData({
                firstName,
                lastName,
                username: username.toLowerCase(),
                email: email.toLowerCase(),
                address,
                password: hashPassword,
                role
            });
        await newUser.save();

        const otp = Math.floor(1000000 + Math.random() * 9000000);
        const addOtp = new Otp(
            {
                email,
                otp
            });
        await addOtp.save();
        await SendEmailToUser(email, "Email Verification", `Your verification code is ${otp}`);
        return res.status(200).json({ message: 'Register Done please verify your email' })

    }
    catch (error) {
        return res.status(500).json({ message: error })
    }
}


module.exports = { register }