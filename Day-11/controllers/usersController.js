const {usersData} = require('../models/users');
const {tokenData} = require('../models/tokens')

const users = async(req,res) => {
    const username = req.body.username;
    if (!username) {
        return res.status(400).json({msg : "username is required"})
    }
    const CheckToken = await tokenData.findOne({username : username})
    if (!CheckToken) {
        return res.status(401).json({msg : "you are not logged in"})
    }

    const getUsers = await usersData.find()
    return res.json(getUsers)
}


module.exports = {users}