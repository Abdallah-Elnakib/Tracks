const {tokenData} = require('../models/token')

const logout = async(req,res) => {
    try {
        const {username} = req.body;
        if (!username) {
            return res.json({message: "Username required"})
        }
        const checkToken = await tokenData.findOne({username});
        if (!checkToken) {
            return res.json({message: "User not logged in"})
        }
        await tokenData.deleteOne({username})
        return res.json({message: "Logout Successful"})
    }
    catch (error) {
        return res.json({message: error.message})
    }
    

}

module.exports = {logout} 
