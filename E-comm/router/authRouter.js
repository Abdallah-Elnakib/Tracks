const express = require('express')
const router = express.Router()
const { login } = require('../controllers/Auth/loginController');
const { register } = require('../controllers/Auth/registerController');

router.post('/login', login)
router.post('/register', register)



module.exports = router