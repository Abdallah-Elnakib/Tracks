const events = require('events')
const dataUsers = require('./Data')


const Emit = new events.EventEmitter()


Emit.on('Register' , (data) =>{
    if (dataUsers[data.username]){
        console.log('Usernmame Found')
    }
    else if (data.password.length < 8){
        console.log('Error')
    }
    else {
        dataUsers[data.username] = data
    }
    
})

module.exports = Emit


let sum = (x,y) => x + y 
let hello = (Name) => console.log(Name) 


module.exports = sum 


