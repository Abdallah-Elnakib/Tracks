const mongoose  = require('mongoose');

const users = new mongoose.Schema({
    firstName : {
        type : String,
        required : true
    },
    lastName : {
        type : String,
        required : true
    },
    username : {
        type : String,
        required : true,
    },
    age : {
        type : Number,
        required : true
    },
    email : {
        type : String,
        required : true,
    },
    password : {
        type : String,
        required : true
    }
})
const usersData = mongoose.model('users', users)
module.exports = {usersData}