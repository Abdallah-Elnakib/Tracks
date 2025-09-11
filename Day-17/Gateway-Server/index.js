const express = require('express');
const authRouter = require('./router/authRouter');
require('dotenv').config()
const cors = require('cors')
const app = express();
app.use(express.json());
app.use(cors())
app.use((req, res, next) => {
  res.setHeader("X-Powered-By", "Node.js");
  res.setHeader("Content-Type", "application/json");
  next();
});

app.use('/auth', authRouter)




app.listen(process.env.PORT, () => console.log('Server started on port 5000.......'))


