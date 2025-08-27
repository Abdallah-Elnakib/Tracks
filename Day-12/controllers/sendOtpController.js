const {UsersData} = require('../models/users')
const {otpData} = require('../models/otp')
const sendOtp = async(req,res) => {
    try {
        const {email} = req.body;
        if (!email) {
            return res.json({message: "Email required"})
        }
        const getUser = await UsersData.findOne({email}) // {}
        if (!getUser){
            return res.json({message: "User not found"})
        }
        const randomSix = Math.floor(100000 + Math.random() * 900000);
        const addOtp = new otpData({
            email,
            otp : randomSix
        })
        await addOtp.save()
        return res.json({message : randomSix})
    }
    catch (error) {
        return res.json({message: error.message})
    }

}


module.exports = {sendOtp}