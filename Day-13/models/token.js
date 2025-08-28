const mongoose = require('mongoose');


const token = new mongoose.Schema({
    email : {
        type : String,
        required : true,
    },
    role : {
        type : String,
        enum : ['user', 'admin'],
        default: "user" 
    },
    token : {
        type : String,
        required : true,
        unique : true
    },
     createdAt: {
        type: Date,
        default: Date.now,
        expires: '30s'
    }
})

const tokenData = mongoose.model('token', token);
module.exports = {tokenData}