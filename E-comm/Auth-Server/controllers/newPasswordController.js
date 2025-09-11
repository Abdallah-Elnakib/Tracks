const { Otp } = require('../models/Otp')
const { usersData } = require('../models/users')
const bcrypt = require('bcrypt')




const newPassword = async (req, res) => {
    try {
        const { email, otp, password, confirmPassword } = req.body;
        if (!email || !otp || !password || !confirmPassword) {
            return res.status(400).json({ message: "All inputs are required" });
        }
        const checkUser = await usersData.findOne({ email: email });
        if (!checkUser) {
            return res.status(400).json({ message: "User not found" });
        }
        const checkOtp = await Otp.findOne({ email: email }); // { email: email , otp: otp }
        if (!checkOtp) {
            return res.status(400).json({ message: "Invalid email or expired" });
        }
        if (checkOtp.otp !== otp) {
            return res.status(400).json({ message: "Invalid otp or expired" });
        }
        if (password.length < 8) {
            return res.status(400).json({ message: "Password must be at least 8 characters" });
        }
        if (password !== confirmPassword) {
            return res.status(400).json({ message: "Passwords do not match" });
        }
        if (bcrypt.compareSync(password, checkUser.password)) {
            return res.status(400).json({ message: "New password cannot be the same as the old password" });
        }
        await Otp.findOneAndDelete({ email: email });
        const hashPassword = await bcrypt.hash(password, 10);
        await usersData.findOneAndUpdate({ email: email }, { password: hashPassword });

        return res.json({ message: "Password changed successfully" });
        
    }
    catch (error) {
        return res.status(500).json({ message: error.message })
    }
}


module.exports = { newPassword }
