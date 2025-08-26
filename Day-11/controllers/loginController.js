const {usersData} = require('../models/users');
const bcrypt = require('bcrypt');
const {tokenData} =require('../models/tokens')

const login = async(req,res) => {
    const {username , password} = req.body;
    if (!username || !password) {
        return res.status(400).json({message : "All inputs are required"})
    }
    const getUser = await usersData.findOne({username : username}) // {}
    if (!getUser) {
        return res.status(400).json({message : "Invalid username"})
    }
    const comparePassword = await bcrypt.compare(password, getUser.password)// true or false

    if (!comparePassword) {
        return res.status(400).json({message : "Invalid password"})
    }
    const addToken = new tokenData({
        username : username
    })
    await addToken.save()
    return res.json({message : 'login done'})

}



module.exports = {login}