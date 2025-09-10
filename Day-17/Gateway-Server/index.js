const express = require('express');
const authRouter = require('./router/authRouter');
require('dotenv').config()

const app = express();
app.use(express.json());

app.use('/auth', authRouter)

app.listen(process.env.PORT, () => console.log('Server started on port 5000.......'))