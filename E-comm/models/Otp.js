const e = require('cors');
const mongoose = require('mongoose');


const otp = new mongoose.Schema({
    email: {
        type: String,
        required: true
    },
    otp: {
        type: String,
        required: true
    },
    createdAt: {
        type: Date,
        default: Date.now,
        expires: '5m'
    }
})
const Otp = mongoose.model('otp', otp)
module.exports = { Otp }