const {app} = require('./index');
const {login} = require('./controllers/loginController')
const {register} = require('./controllers/registerController')
const {logout} = require('./controllers/logoutController')
const {sendOtp} = require('./controllers/sendOtpController')
const {newPassword} = require('./controllers/newPasswordController') 
const {UsersData} = require('./models/users')


app.post('/auth/login', login)
app.post('/auth/register', register)
app.post('/logout', logout)
app.post('/send-otp',sendOtp)
app.post('/new-password',newPassword)



app.post('/', async(req,res)=>{
    const username = req.headers.username;
    const password  = req.headers.password;

    if (!username || !password){
        return res.status(401).send({message:"Unauthorized"})
    }

    if (username !== 'abdallah' || password !== '123456789'){
        return res.send({message:"Unauthorized"})
    }
    return res.send('hello')
})