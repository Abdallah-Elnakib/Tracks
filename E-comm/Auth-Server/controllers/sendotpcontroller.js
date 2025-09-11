const { usersData } = require("../models/users");
const {Otp} = require('../models/Otp')
const {SendEmailToUser} = require('../utils/mailSender')
const sendotp = async (req, res) => {
    try {
        const { email } = req.body;
        if (!email) {
            return res.status(400).json({ message: "Email is required" });
        }
        const checkUser = await usersData.findOne({ email: email });
        if (!checkUser) {
            return res.status(400).json({ message: "User not found" });
        }
        const checkOtp = await Otp.findOne({ email: email });
        if (checkOtp) {
            return res.status(400).json({ message: "Otp already sent" });
        }
        const otp = Math.floor(1000000 + Math.random() * 9000000)
        const newOtp = new Otp({ email: email, otp: otp });
        await newOtp.save();
        SendEmailToUser(email, "OTP Verification", `Your OTP is ${otp}`);
        return res.json({ message: "Otp sent successfully" });
    }
    catch (error) {
        return res.status(500).json({ message: error.message })
    }
}




module.exports = {sendotp}