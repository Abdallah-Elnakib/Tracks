const {otpData} = require('../models/otp')
const {UsersData} = require('../models/users')
const bcrypt = require('bcrypt');

const newPassword = async(req,res) => {
    const {email, otp, newPassword, confirmPassword} = req.body;
    if (!email || !otp || !newPassword || !confirmPassword){
        return res.status(400).json({message : "All fields are required"})
    }
    const checkEmail = await otpData.findOne({email :email }) 
    if (!checkEmail) {
        return res.status(400).json({message : "Email not found"})
    }
    if (checkEmail.otp !== otp){
        return res.status(400).json({message : "Invalid OTP"})
    }
    if (newPassword !== confirmPassword){
        return res.status(400).json({message : "Passwords do not match"})
    }
    const hashPassword = await bcrypt.hash(newPassword,10)
    await UsersData.updateOne({email : email},{password : hashPassword})
    return res.status(200).json({message : "Password updated successfully"})
}

module.exports = {newPassword}