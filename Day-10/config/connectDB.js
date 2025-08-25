const mongoose = require('mongoose');
const env = require('dotenv')
const path = require('path')
env.config({path : path.join(__dirname, '../.env')})

const connectDB = async ()=> {
    try {
        await mongoose.connect(process.env.MONGO_URI);
        console.log('Database Connected.........')
        
    } catch (error) {
        console.error("Database connection failed:", error);
    }
};




module.exports = {connectDB}