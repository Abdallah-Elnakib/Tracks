const {usersData} = require('../models/users')
const {tokenData} = require('../models/tokens')

const deleteUser = async(req,res) => {
    const username = req.body.username;
    if (!username) {
        return res.status(400).json({ error: 'Username is required' });
    }
    const checkToken = await tokenData.findOne({username : username})
    if (!checkToken) {
        return res.status(401).json({ error: 'Invalid username or expired token' });
    }

    const checkUser = await usersData.findOne({username})
    if (!checkUser) {
        return res.status(404).json({ error: 'User not found' });
    }
    await usersData.deleteOne({username :username})
    return res.json({message : "user deleted..."})

}


module.exports = {deleteUser}