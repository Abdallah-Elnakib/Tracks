const mongoose = require("mongoose");

const product = new mongoose.Schema({
    id : {
        type : Number,
        required : true,
    },
    title : {
        type : String,
        required : true,
    },
    description : {
        type : String,
        required : true,
    },
    price : {
        type : Number,
        required : true,
    },
    quantity : {
        type : Number,
        required : true,
    }
});

const productsData = mongoose.model('products', product);
module.exports = { productsData }; 