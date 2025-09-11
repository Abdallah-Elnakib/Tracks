const {fetchPOSTREQUEST} = require('../../utils/fetchServer');


const newPassword = async (req, res) => {
    const { email, otp, password, confirmPassword } = req.body;
    if (!email || !otp || !password || !confirmPassword) {
        return res.status(400).json({ message: "All inputs are required" });
    }
    const data = await fetchPOSTREQUEST('http://127.0.0.1:3000/auth/new-password', { email, otp, password, confirmPassword });
    return res.json({ message: data });
}


module.exports = { newPassword }