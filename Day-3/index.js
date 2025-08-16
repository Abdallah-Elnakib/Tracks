// if (x == 10){}
// if (x == 20 && y == 10){}

//  for loop  while loop

// for (let i= 1; i < 11; i++){
//     console.log(i)
// }

// for (let number = 1; number < 20; number++){
//     console.log('5555555555555555')
// }

// for (let i = 1; i = 0; i++){}


// let username = 'abdallah';
// let password = '122223300';

// for (let i = 0; i < 5; i++){

//     if (username === 'abdallah') {
//         if (password === '1222233') {
//             console.log('Hello :)');
//             break;
//         }else {
//             console.log('Wrong Password')
//         }
//     } else {
//         console.log('Wrong username')
//     }    

// }


// for (let i = 10; i > 0; i--){
//     console.log(i);
// }
// let list = [1,6,9,87,1];

// for (let i = 0; i < 10; i++) {
//     if (list[i] === 87){
//         console.log('Yes')
//         break;
//     }
//     continue;
// }


// list = [1,6,9,87,1,40];
// let maxLingth = list.length // 5

// for (let i = 0 ; i < 5; i++){
//     if (list[i] < 20) {
//         list.push(true)
//     }
//     else if (list[i] < 50) {
//         continue
//     }
// }

// console.log(list)


// let username = 'abdallah';
// let password = '122223300';
// let CheckPass = 6
// for (let i = 1; i < 11; i++){
//     if (username === 'abdallah'){
//         if (password === '122223300') {
//             console.log('Hello');
//             break;
//         }else {
//             if (CheckPass >= 6){
//                 break
//             }else {
//                 console.log('Wrong Password');
//                 CheckPass ++
//             }

//         }
//     }else {
//         console.log('Wrong username');
//         continue
//     }
// }


// let list = [1, 6, 9, 87, 1, 40];
// = 87
// من 50 الي 86

// for (let i = 0; i < list.length; i++) {
//     if (list[i] >= 87) {
//         console.log('Yes');
//         break;
//     } else if (list[i] < 87 && list[i] >= 50){
//         continue
//     }
//     else {
//         console.log('No');
//         break
//     }

// }
// let dic = {'name' : 'abdallah', 'age' : 27};

// let x = 'ab'

// console.log(dic , x)


// for (let i in dic) {
//     console.log(dic[i])
// }


// let username = 'abdallah';
// let password = '1222233000';

// while (true){
//     if (username == 'abdallah'){
//         if (password == '122223300') {
//             console.log('Hello :)');
//             break;
//         }
//         else {
//             console.log('Wrong Password');
//             continue;
//         }
//     }else {
//         console.log('Wrong username');
//         continue;
//     }
// }


// let list = ['abdallah','ahmed','ali']
// let i = 5


// while (i < list.length){
//     console.log(list[i]);
//     i++;
// }

// while (i < list.length){
//     i++;
//     console.log(list[i]);
// }


// i = 0

// function hello() {
//     let list = ['abdallah', 'ahmed', 'ali']; // 3
//     let i = 0;
//     while (i < list.length) {
//         console.log(list[i]);
//         i++;
//     }
// }


// hello();
// hello();
// hello();
// hello();



// function hello(name,age){
//     for (let i = 0; i < name.length; i++){
//         console.log(`Name ${name[i]} \n Age : ${age[i]}`)
//     }
// }


// hello([1,6,9],['abdallah'])
// hello(['abdallah','ahmed','ali'],[1,2,3])



// function test(...numbers){
//     console.log(numbers[0][3]) //[[2,9,8,7],9,7,7,'abdallah',true]
// }


// test([2,9,8,7],9,7,7,'abdallah',true)



// function GetAllNumbers(...numbers){
//     let evenNumber = [];
//     let oddNumber = [];
//     for (let i = 0; i < numbers.length; i++){
//         if (numbers[i] % 2 == 0){
//             evenNumber.push(numbers[i]);
//         }
//         else {
//             oddNumber.push(numbers[i]);
//         }
//     }
//     return {
//         even: evenNumber,
//         odd: oddNumber
//     }
// }

// function print(){
//     let x = GetAllNumbers(1,2,3,4,5,6,7,8,9,10);
//     console.log(x.even);
//     console.log(x.odd);
// }


// print()


// function test(usernam , password){
//     if (usernam == 'abdallah'){
//         if (password == '123'){
//             return 'Hello'
//         }
//         else {
//             return 'Wrong Password';
//         }
//     }
//     else {
//         return 'Wrong username';
//     }
// }

// console.log(test('abdallah',12355))

// function x(number1,number2){
//     return number1 + number2;
// }

// let x = (number1,number2) => console.log(number1,number2)

// x(10,5)

// let y = (number1,number2) => number1 + number2

// const add = (a, b) => {
//   return a + b;
// };

// console.log(add(10,5))


