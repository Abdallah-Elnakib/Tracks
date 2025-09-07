const express = require('express');
const authRouter = require('./router/authRouter');
const productRouter = require('./router/productsRouter');
const app = express();

app.use(express.json());
// 127.0.0.1:3000/

app.use('/auth',authRouter)
app.use('/products',productRouter)


app.listen(3000, () => {
  console.log('Server is running on port 3000');
});