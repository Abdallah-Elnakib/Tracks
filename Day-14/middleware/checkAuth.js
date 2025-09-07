const fs = require('fs');
const path = require('path');
const checkAuth = (req, res, next) => {
    const checkuser = fs.readFileSync(path.join(__dirname, '../controllers/token.json'), 'utf8'); // json
    const data = JSON.parse(checkuser); // {"users" : ['abdallah','mahmed'] }
    const username = req.headers.username;
    if (!username) {
        return res.json({ message: "You are not authorized" });
    }
    for (let user of data.users) {
        if (user === username) {
            return next();
        }
    }
    return res.json({ message: "You are not authorized" });
}


module.exports = {checkAuth}