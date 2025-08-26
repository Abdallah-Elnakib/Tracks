const {app} = require('./index')
const {register} = require('./controllers/registerController')
const {login} = require('./controllers/loginController')
const {users} = require('./controllers/usersController')
const  {deleteUser} = require('./controllers/deleteUserController')


app.post('/register' , register)
app.post('/login', login)
app.post('/users', users)
app.delete('/delete-user', deleteUser)