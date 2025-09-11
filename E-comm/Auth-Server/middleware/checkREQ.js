const checkReq = (req, res, next) => {
    const {username , password} = req.headers;
    if(!username || !password){
        return res.status(400).json({message: "unauthorized"});
    }
    if (username !== process.env.USERNAME_SERVER || password !== process.env.PASSWORD_SERVER) {
        return res.status(400).json({ message: "unauthorized" });
    }
    next();
}


module.exports = {checkReq}