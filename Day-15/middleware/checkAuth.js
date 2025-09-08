const checkAuth = (req, res, next) => {
    const getToken = req.session.token;
    if (!getToken) {
        return res.status(401).json({ message: "Unauthorized" });
    } else {
        return next();
    }
}


module.exports = {checkAuth}