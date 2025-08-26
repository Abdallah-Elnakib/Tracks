const {app} = require('./index')
const {register} = require('./controllers/registerController')
const {login} = require('./controllers/loginController')
const {users} = require('./controllers/usersController')

app.post('/register' , register)
app.post('/login', login)
app.post('/users', users)