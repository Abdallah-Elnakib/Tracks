const e = require("express");

const checkReq = (req, res, next) => {
    try {
        if (req.headers['username']  !== 'abdallah' || !req.headers['password'] == 'abdallah') {
            return res.status(400).json({ error: 'Unauthorized' })
        }
        next();
    }
    catch (error) {
        console.log(error)
    }
}


module.exports = {checkReq}


