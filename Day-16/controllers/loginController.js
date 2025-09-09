const { usersData } = require('../models/users');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const login = async (req, res) => {
    try {
        const { usernameOrEmail, password } = req.body;
        if (!usernameOrEmail || !password) {
            return res.status(400).json({ message: "All inputs are required" })
        }
        const getUser = await usersData.findOne({ $or: [{ email: usernameOrEmail }, { username: usernameOrEmail }] }) // {}
        if (!getUser) {
            return res.status(400).json({ message: "Invalid username or email" })
        }
        const comparePassword = await bcrypt.compare(password, getUser.password)// true or false
        if (!comparePassword) {
            return res.status(400).json({ message: "Invalid password" })
        }
        const token = jwt.sign({ firstName: getUser.firstName, lastName: getUser.lastName, email: getUser.email, role: getUser.role }, process.env.JWT_SECRET, { expiresIn: "1m" });
        req.session.token = token;

        
        // res.cookie("token", token, {
        //     httpOnly: true,
        //     secure: false,
        //     maxAge: 1000 * 60 
        // });
        // cookie("key","value", {})

        return res.json({ message: 'login done' , token})
    }
    catch (error) {
        console.log(error)
    }

}


module.exports = { login }