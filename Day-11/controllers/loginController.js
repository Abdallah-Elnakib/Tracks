const login = async(req,res) => {
    const {username , password} = req.body;
    if (!username || !password) {
        return res.status(400).json({message : "All inputs are required"})
    }
}



module.exports = {login}