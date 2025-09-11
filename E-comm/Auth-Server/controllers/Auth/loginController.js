const { usersData } = require('../../models/users');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const login = async (req, res) => {
    try {
        const { usernameOrEmail, password } = req.body;
        if (!usernameOrEmail || !password) {
            return res.status(400).json({ message: "All inputs are required" })
        }
        const getUser = await usersData.findOne({ $or: [{ email: usernameOrEmail.toLowerCase() }, { username: usernameOrEmail.toLowerCase() }] }) // {}
        if (!getUser) {
            return res.status(400).json({ message: "Invalid username or email" })
        }
        const comparePassword = await bcrypt.compare(password, getUser.password)// true or false
        if (!comparePassword) {
            return res.status(400).json({ message: "Invalid password" })
        }

        if (getUser.status === false) {
            return res.status(400).json({ message: "Your account is not verified" })
        }

        const token = jwt.sign({ firstName: getUser.firstName, lastName: getUser.lastName, email: getUser.email, role: getUser.role }, process.env.JWT_SECRET, { expiresIn: "1m" });
        req.session.token = token;

        return res.json({ message: 'login done' })
    }
    catch (error) {
        console.log(error)
    }

}


module.exports = { login }