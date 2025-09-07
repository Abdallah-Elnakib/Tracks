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

    const alreadyHaveToken = await tokenData.findOne({
        email: getUser.email
    });

    // if (alreadyHaveToken.createdAt.getTime() + (30 * 1000) > Date.now()) {
    //     return res.json({message: "Already Logged In"})
    // }

    // console.log("AlreadyHaveToken", alreadyHaveToken);

    if (alreadyHaveToken) {
        return res.json({message: "Already Logged In"})
    }

    const addToken = new tokenData({
        email : getUser.email,
        role : getUser.role,
        token: crypto.randomUUID()
    });

    await addToken.save();

    return res.json({message: "Login Successful"})
}

module.exports = {login}