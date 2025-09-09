const jwt = require("jsonwebtoken");

const checkAuth = (req, res, next) => {
    const getToken = req.session.token; 
    if (!getToken) {
        return res.status(401).json({ message: "Unauthorized" });
    } else {
        jwt.verify(getToken, process.env.JWT_SECRET, (err, decode) => {
            if (err) {
                return res.status(401).json({ message: "Unauthorized" });
            } else {
                req.user = decode;
                next();
            }
        });
        
    }
    // verify(getToken, process.env.JWT_SECRET);
}


module.exports = {checkAuth}