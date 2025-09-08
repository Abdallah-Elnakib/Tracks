const express = require('express');
const {login} = require('../controllers/loginController');
const {register} = require('../controllers/registerController');
const {logout} = require('../controllers/logoutController');
const router = express.Router();

router.post('/login', login);
router.post('/register', register);
router.post('/logout', logout);




module.exports = router