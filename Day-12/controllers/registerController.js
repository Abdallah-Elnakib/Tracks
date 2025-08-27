const {UsersData} = require('../models/users');
const bcrypt = require('bcrypt');
const {tokenData} = require('../models/token')

const register = async(req, res) => {
    try {
        const {firstName, lastName, username, email, password, role} = req.body;
        if (!firstName || !lastName || !username || !email || !password){
            return res.json({message: "All fields are required"})
        }
        if (!role) {
            role = "user"
        }
        const checkUser = await UsersData.findOne({username});
        if (checkUser) {
            return res.json({message: "Username  already exists"})
        }
        if (password.length < 8) {
            return res.json({message: "Password must be at least 8 characters"})
        }
        const hashPassword = await bcrypt.hash(password, 10);
        const addUser = await new UsersData({
            firstName,
            lastName,
            username,
            email,
            password : hashPassword,
            role
        })
        await addUser.save();
        const addToken = new tokenData({
        username,
        email ,
        role 
        })
        await addToken.save();
        return res.json({message: "User registered successfully"})
    }
    catch (error) {
        return res.json({message: error.message})
    }
    

}


module.exports = {register}