const {app} = require('./index')
const {register} = require('./controllers/registerController')
const {login} = require('./controllers/loginController')

app.post('/register' , register)
app.post('/login', login)