const mongoose = require('mongoose');

const users = new mongoose.Schema({
    firstName: {
        type: String,
        required: true
    },
    lastName: {
        type: String,
        required: true
    },
    username: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
    },
    address: {
        type: Array,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    role: {
        type: String,
        enum: ['user', 'admin'],
        required: true,
    },
    status : {
        type : Boolean,
        default : false
    }
}, {
    timestamps: true
});

const usersData = mongoose.model('users', users);
module.exports = { usersData }