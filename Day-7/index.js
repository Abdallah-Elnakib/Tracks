// let x = 50

// let promise_1 = new Promise((resolve, rejected) => {
//     if (x >= 50) {
//         resolve({'username' : 'abdallah'})
//     }else {
//         rejected('error')
//     }
// })

// promise_1.then((res) => {
//     console.log(res)

// }).catch((error) => {
//     console.log(error)
// })

// new Promise((resolve, reject) => {}).then().catch()

// let x = 100
// let y = 20
// let z = 300

// console.log(54);

// let promise_1 = new Promise((resolve, reject) => {
//     console.log(55);
//     if (x === 10) {
//         resolve('Done 1')
//     } 
//     else {
//         reject('Error 1')
//     }
// })

// console.log(56);

// let promise_2 = new Promise((resolve, reject) => {
//     if (y === 20) {
//         resolve('Done 2')
//     } 
//     else {
//         reject('Error 2')
//     }
// })

// let promise_3 = new Promise((resolve, reject) => {
//     if (z === 30) {
//         resolve('Done 3')
//     } 
//     else {
//         reject('3')
//     }

//     console.log('1')
    
// }).then((res) => {
//     console.log(res)

// }).catch((error) => {
//     console.log(error)
// })


// console.log('2')


// Promise.all([promise_1,promise_2,promise_3]).then((res) => {
//     console.log(res)
// }).catch((error) => {
//     console.log(error)
// })




// let x = 100
// let y = 200
// let z = 300


// let promise_1 = new Promise((resolve, reject) => {
//     setTimeout(() =>  resolve(1), 2000)
// })
// let promise_2 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(2), 1000)
// })
// let promise_3 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(3), 2000)
// })


// Promise.race([promise_1,promise_2,promise_3]).then((res) => {
//     console.log(res)
// }).catch((error) => {
//     console.log(error)
// });



// let promise_1 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(1), 2000)
// })
// let promise_2 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(2), 1000)
// })
// let promise_3 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(3), 3000)
// })


// Promise.any([promise_1,promise_2,promise_3]).then((res) => {
//     console.log(res)
// }).catch((error) => {
//     console.log(error)
// });



// let promise_1 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(1), 2000)
// })
// let promise_2 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(2), 1000)
// })
// let promise_3 = new Promise((resolve, reject) => {
//     setTimeout(() =>  reject(3), 3000)
// })

// Promise.reject([promise_1,promise_2,promise_3]).catch((res) => {
//     for (let i of res) {
//         i.catch((error) => {
//             console.log(error);
//         });
//     }
// })




// let promise_Me = new Promise((resolve, rejected) => {
//     setTimeout(() => {
//         resolve({'username' : "abdallah", "password" : "123"})
//     }, 1000)
// })


// promise_Me.then((res) => {let data = res.username += '5'}).then((res2) => {
//     console.log(res2)
// })



// let y = () => {
//     5
// }


// console.log(x(),y())

// let x = (num1, num2)  => num1 + num2

// function x (){
//     return 5;
// }


// let url = https://gghjklp


// let api = {
//     '1' : "https://gghjklp",
//     '2' : "https://gghjklp"
// }




// fetch('https://dummyjson.com/posts')
// .then((res) => res.json())
// .then((data) => console.log(data))
// .catch((error) => {
//     console.log(error);
// }) 