const {app} = require('./index');
const {login} = require('./controllers/loginController')
const {register} = require('./controllers/registerController')
const {logout} = require('./controllers/logoutController')


app.post('/login', login)
app.post('/register', register)
app.post('/logout', logout)