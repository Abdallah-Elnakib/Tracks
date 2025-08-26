const {app} = require('./index')
const {register}= require('./controllers/registerController')
 

app.post('/register' , register)