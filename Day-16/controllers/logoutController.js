const logout = async (req, res) => {
    try {
        req.session.destroy((err) => {
            if (err) {
                return res.status(500).json({ message: "Error logging out" });
            }
            return res.json({ message: "Logout successful" });
        });
    } catch (error) {
        return res.status(500).json({ message: "Error logging out", error: error.message });
    }
    
}


module.exports = { logout }