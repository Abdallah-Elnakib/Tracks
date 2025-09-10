const express = require('express');
const router = express.Router();



router.post('/login' , (req,res) => {
    const {username , password} = req.body
    if (!username || !password) {
        return res.status(400).json({error : 'Username and password are required'})
    }
    res.json({message : 'Login successful'})
})







module.exports = router