const mongoose = require('mongoose');


const token = new mongoose.Schema({
    username : {
        type : String,
        required : true
        
    },
    createdAt: {
        type: Date,
        default: Date.now,
        expires: 60
    }
})

const tokenData = mongoose.model('tokens', token)
module.exports = {tokenData}