const {usersData} = require('../models/users')
const bcrypt = require('bcrypt');
const fs = require('fs');
const path = require('path');

const register = async(req,res) => {
    const {username, password} = req.body;
    if (!username || !password){
        return res.json({message : "All inputs are required"});
    }
    const checkUser = await usersData.findOne({username});
    if (checkUser) {
        return res.json({message : "Username  already exists"});
    }
    if (password.length < 8) {
        return res.json({message : "Password must be at least 8 characters"});
    }
    const hashPassword = await bcrypt.hash(password, 10);

    const addNewUser = new usersData({
        username,
        password : hashPassword
    })
    await addNewUser.save()
    try {
        const addToken = fs.readFileSync(path.join(__dirname, 'token.json'), 'utf8'); // json
        const user = JSON.parse(addToken); // {"users" : ['abdallah','mahmed']}
        user.users.push(username);
        fs.writeFileSync(path.join(__dirname, 'token.json'), JSON.stringify(user), 'utf8');
    }
    catch (err) {
        console.log(err)
    }
    
    

    return res.json({message : "User registered successfully"});

   
}


module.exports = {register}