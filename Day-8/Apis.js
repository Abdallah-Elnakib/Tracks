const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });


// rl.question('Enter Username Name : ', (username)=>{
//     fetch(`http://127.0.0.1:3000/profile?username=${username}&age=24&country=eg`)
//     .then((res) => res.json())
//     .then((data) => console.log(data))
//     .catch((error) => console.log(error))
//     rl.close()
// })

let getFetchReq = (url) => {
    fetch(url)
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((error) => console.log(error))
}

let postFetchReq = (url, data) => {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then((res) => res.text())
    .then((data) => console.log(data))
    .catch((error) => console.log(error))
} 

console.log('1. New User')
console.log('2. Existing User')
console.log('3. Get User Data')
console.log('4. Exit')

rl.question('Enter A Number (1 to 4) : ', (number)=>{
    if (number === '1') {
        rl.question('Enter Username : ', (username) => {
            rl.question('Enter Password : ', (password) => {
                rl.question('Enter Email : ' ,(email) =>{
                    postFetchReq('http://127.0.0.1:3000/register', {username, password, email})
                    rl.close()
                })
            })
        })
    }
    else if (number === '2') {
        rl.question('Enter Username : ', (username) => {
            rl.question('Enter Password : ', (password) => {
                postFetchReq(`http://127.0.0.1:3000/login`,{username, password})
                rl.close()
            })
        })
    }
    else if (number === '3') {
        rl.question('Enter Username : ', (username) => {
            getFetchReq(`http://127.0.0.1:3000/user?username=${username}`)
            rl.close()
        })
    }
    else if (number === '4') {
        rl.close()
    }
     
})