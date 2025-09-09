const express = require('express')
const router = express.Router()
const { login } = require('../controllers/Auth/loginController');
const { register } = require('../controllers/Auth/registerController');
const { verified } = require('../controllers/Auth/verifiedAccountController');
const {sendotp} = require('../controllers/Auth/sendotpcontroller')

router.post('/login', login)
router.post('/register', register)
router.post('/verified-account', verified)
router.post('/send-otp',sendotp)


module.exports = router