const {app} = require('./index');
const {home} = require('./controllers/homeController')
const {profile} = require('./controllers/profileController')



app.get('/', home);

app.get('/profile/:name', profile)