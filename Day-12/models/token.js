const mongoose = require('mongoose');


const token = new mongoose.Schema({
    username : {
        type : String,
        required : true,
    },
    email : {
        type : String,
        required : true,
    },
    role : {
        type : String,
        enum : ['user', 'admin'],
        default: "user" 
    },
     createdAt: {
        type: Date,
        default: Date.now,
        expires: 60 * 60
    }
})

const tokenData = mongoose.model('token', token);
module.exports = {tokenData}