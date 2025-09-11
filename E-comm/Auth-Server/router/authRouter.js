const express = require('express')
const router = express.Router()
const { login } = require('../controllers/loginController');
const { register } = require('../controllers/registerController');
const { verified } = require('../controllers/verifiedAccountController');
const {sendotp} = require('../controllers/sendotpcontroller')
const {newPassword} = require('../controllers/newPasswordController')


router.post('/login', login)
router.post('/register', register)
router.post('/verified-account', verified)
router.post('/send-otp',sendotp)
router.post('/new-password',newPassword)



module.exports = router