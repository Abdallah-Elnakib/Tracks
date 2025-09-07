const { usersData } = require('../models/users')
const bcrypt = require('bcrypt');
const fs = require('fs');
const path = require('path');

const login = async (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) {
        return res.json({ message: "All inputs are required" });
    }
    const getUser = await usersData.findOne({ username }); // {username : 'abdallah', password : 123456}
    if (!getUser) {
        return res.json({ message: "User not found" });
    }
    const match = await bcrypt.compare(password, getUser.password); // true or false
    if (!match) {
        return res.json({ message: "Invalid Password" });
    }
    try {
        const addToken = fs.readFileSync(path.join(__dirname, 'token.json'), 'utf8'); // json
        const user = JSON.parse(addToken); // {"users" : ['abdallah','mahmed']}
        user.users.push(username);
        fs.writeFileSync(path.join(__dirname, 'token.json'), JSON.stringify(user), 'utf8');
    }
    catch (err) {
        console.log(err)
    }

    return res.json({ message: "Login Successful" });

}


module.exports = { login }