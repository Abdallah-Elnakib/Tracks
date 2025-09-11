const { fetchPOSTREQUEST } = require('../../utils/fetchServer');


const register = async (req, res) => {
    const { firstName, lastName, username, email, address, password, role } = req.body;
    if (!firstName || !lastName || !username || !email || !address || !password || !role) {
        return res.status(400).json({ message: "All inputs are required" })
    }
    const data = await fetchPOSTREQUEST('http://127.0.0.1:3000/auth/register', { firstName, lastName, username, email, address, password, role })
    return res.json({ message: data })
}


module.exports = { register }