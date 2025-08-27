const {UsersData} = require('../models/users');
const {tokenData} = require('../models/token')
const bcrypt = require('bcrypt');

const login = async(req,res) => {
    const {username , password} = req.body;
    if (!username || !password){
        return res.json({message: "Username and Password required"})
    }
    const getUser = await UsersData.findOne({username}); // {}
    if (!getUser){
        return res.json({message: "User not found"})
    }
    const match = await bcrypt.compare(password, getUser.password);
    if (!match) {
        return res.json({message: "Invalid Password"})
    }
    const addToken = new tokenData({
        username : getUser.username,
        email : getUser.email,
        role : getUser.role
    })
    await addToken.save();
    return res.json({message: "Login Successful"})
}

module.exports = {login}