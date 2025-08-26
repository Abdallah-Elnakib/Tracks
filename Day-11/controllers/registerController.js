const {usersData} = require('../models/users');
const bcrypt = require('bcrypt');

const register = async(req,res) => {
    const {firstName, lastName, username, age, email, password} = req.body;
    if (!firstName || !lastName || !age ||!email || !password || !username) {
        return res.status(400).json({message : "All inputs are required"})
    }

    const CheckUser = await usersData.findOne({email : email})
    console.log(CheckUser)
    if (CheckUser) {
        return res.json({message : "This email is alrady userd"})
    }
    const hashPassword = await bcrypt.hash(password, 10)

    const addNewUser = new usersData({
        firstName,
        lastName,
        username,
        age,
        email,
        password : hashPassword
    })
    await addNewUser.save()
    return res.status(201).json({message : "User registered successfully"})
}


module.exports = {register}