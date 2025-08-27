const {app} = require('./index');
const {login} = require('./controllers/loginController')
const {register} = require('./controllers/registerController')
const {logout} = require('./controllers/logoutController')
const {sendOtp} = require('./controllers/sendOtpController')
const {newPassword} = require('./controllers/newPasswordController') 



app.post('/login', login)
app.post('/register', register)
app.post('/logout', logout)
app.post('/send-otp',sendOtp)
app.post('/new-password',newPassword)