const express = require('express');
const router = express.Router();



router.post('/login', (req, res) => {
    try {
        const { username, password } = req.body
        if (!username || !password) {
            return res.status(400).json({ error: 'Username and password are required' })
        }
        fetch('http://127.0.0.1:3000/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                "username": "abdallah",
                "password": "abdallah"
            },
            body: JSON.stringify({ username, password })
        })
            .then((data) => data.json())
            .then((finalData) => res.status(200).json(finalData))
            .catch((error) => console.log(error))
    }
    catch (error) {
        console.log(error)
    }
})


module.exports = router;