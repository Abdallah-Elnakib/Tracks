const {fetchPOSTREQUEST} = require('../../utils/fetchServer');

const login = async(req, res) => {
    const { usernameOrEmail, password } = req.body;
    if(!usernameOrEmail || !password){
        return res.status(400).json({message: "All inputs are required"})
    }
    const data = await fetchPOSTREQUEST('http://127.0.0.1:3000/auth/login', {usernameOrEmail, password})
    req.session.token = data.token
    res.json({message: data})
}


module.exports = {login}