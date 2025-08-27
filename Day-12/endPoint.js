const {app} = require('./index');
const {login} = require('./controllers/loginController')


app.post('/login', login)