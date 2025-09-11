const logout = (req, res) => {
    try {
        req.session.destroy((err) => {
            if (err) {
                return res.status(500).json({ message: err.message });
            }
            return res.json({ message: "Logout successful" });
        });

    }
    catch (error) {
        return res.status(500).json({ message: error.message });
    }
}



module.exports = { logout }