const { Otp } = require('../../models/Otp')
const {usersData} = require('../../models/users')
const verified = async (req, res) => {
    try {
        const { email, otp } = req.body;
        if (!email || !otp) {
            return res.status(400).json({ message: "All inputs are required" });
        }
        const checkUser = await usersData.findOne({ email: email });
        if (!checkUser) {
            return res.status(400).json({ message: "User not found" });
        }
        if (checkUser.status === true) {
            return res.status(400).json({ message: "Account already verified" });
        }
        const checkOtp = await Otp.findOne({ email: email });
        if (!checkOtp) {
            return res.status(400).json({ message: "Invalid email or expired" });
        }
        if (checkOtp.otp !== otp) {
            return res.status(400).json({ message: "Invalid otp or expired"});
        }
        await Otp.findOneAndDelete({ email: email });
        await usersData.findOneAndUpdate({ email: email }, { status: true });
        return res.json({ message: "Account verified successfully" });
    }
    catch (error) {
        return res.status(500).json({ message: error.message })
    }
    
}


module.exports = { verified }