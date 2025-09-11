const express = require('express');
const {login} = require('../controllers/Auth/loginController')
const {register} = require('../controllers/Auth/registerController')
const {verifiedAccount} = require('../controllers/Auth/verifiedAccountController')
const {sendOtp} = require('../controllers/Auth/sendOtpController')
const {newPassword} = require('../controllers/Auth/newPasswordController')
const {logout} = require('../controllers/Auth/logoutController')
const router = express.Router();


router.post('/login', login)
router.post('/register', register)
router.post('/verified-account', verifiedAccount)
router.post('/send-otp',sendOtp)
router.post('/new-password',newPassword)
router.get('/logout', logout)






module.exports = router