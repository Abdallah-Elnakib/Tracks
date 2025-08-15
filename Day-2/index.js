

// x.push('abdallah')
// x[1] = 'hhhh'
// x.pop()
// x.shift()
// x.unshift('abdallah')

// x.push()
// x.unshift()
// -------------------
// x.pop()
// x.shift()

// x[x.length] = 'ahmed'


// let x = [1,5,9,8]

// delete x[2]
// x[2] = 'hello'

// let text_1 = 'abdallah';
// let text_2 = 'elnakib';

// console.log(text_1 + ' ' + text_2)
// console.log(`My name Is  : ${text_1} ${text_2}`)

// let text_3 = text_1.concat(' ',text_2)
// console.log(t);


// let Array1 = [1,3,4,5]
// let Array2 = ['ali','ahmed']

// let Array3 = Array2.concat(Array1)

// console.log(Array3)


// let flatArray = [[1,5,1,8,[2,9,[6,5,9]]],[5,6,7],['abdallah','ahmed']]

// let Flat = flatArray.flat(3)

// console.log(Flat)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits[0] = 'abdallah'

// const x = 'abdallah'

// x = '5'
// console.log(fruits)

// const x = 'abdallah';

// x = 'ahmed'
// console.log(x)

// const x = [1, 2, 3, 4, 5];

// x = [5,9,8,7,1]

// console.log(x)


// let spliceArray = ["Banana", "Orange", "Apple", "Mango"]; //-> -2
// let lengthOfSpliceArray =  spliceArray.length - 2
// spliceArray.splice(-2,1)
// console.log(spliceArray)

// let spliceArray = ["Banana", "Orange", "Apple", "Mango"];
// ["Banana",'abdallah', "Mango"]
// spliceArray[1] = 'abdallah'

// spliceArray.splice(1,2,'abdallah','ahmed')
// console.log(spliceArray)

// const sliceArray = ["Banana", "Orange", "Lemon", "Apple", "Mango"].reverse();
// [ 'Mango', 'Apple', 'Lemon', 'Orange', 'Banana' ]

// let sliceArrayAfterSlice = sliceArray.slice(0,3);
// sliceArray.reverse();
// console.log(sliceArrayAfterSlice)

// slice =>
// اقدر اخد جزء من اليست بتاعتي من غير ميحصل اي تغير في الليست الاصليه"
//  splice =>
//  اقدر امسح جزئ من اليست بتاعتي وحتتمسح من الاصليه 
//  اقدر اعدل قيم في الليست الاصليه
//  اقدر اخد جزئ من الليست الاصليه ولاكن ده حيأثر علي اليست الاصليه

// let sliceArray = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
// sliceArray.splice(1,1,'abdallah')
// console.log(sliceArray)

// let Array = ['abdallah','ahmed','salah', 'aci'].sort()
// console.log(Array)

// let Array = ['abdallah','ahmed','salah', 'aci','abdallah',55]
// console.log(Array.lastIndexOf('abdallah'))


// Array.indexOf('abdallah')
// Array.lastIndexOf('abdallah')

// const includesArray = ["Banana", "Orange", "Apple", "Mango"];
// console.log(includesArray[1].includes('Or'));


// let data = {
//     'firstName': 'abdallah',
//     'lastName': 'elnakib',
//     'age': 20,
//     'phones': ['012345456','1236987'],
//     'address': {
//         'street': '123 Main St',
//         'city': 'Anytown',
//         'state': 'CA',
//         'zip': '12345'
//     },
// }
// data.phones[1] = '0123-58745-444'
// data.UserData = {'username' : 'abdallah','password' : '123456', 'email' : 'abdallah@123456'}
// delete data.age

// let dataKeys = Object.keys(data)
// let datavalues = Object.values(data)

// ['abdallah','elnakib',20,['012345456','1236987'],{'street': '123 Main St','city': 'Anytown','state': 'CA','zip': '12345'}]
// datavalues[4].zip

// console.log(datavalues[datavalues.length -1].zip)


// let data_1 = {
//     'name' : 'abdallah',
//     'age' : 20,
//     'phone' : '01236987'
// };

// let data_2 = Object.assign({},data_1)
// data_2.name = 'ahmed'
// let data_2 = Object.create(data_1)
// data_2.name = 'ahmed'

// console.log('Object 1 : ',data_1,'Object 2 : ',data_2.name)

let number_1 = 10

// if (number_1 === '10') {
//     console.log('Number is greater than 10')
// }
// let number_2 = 20
// let op = '*'
// == , > , < , >=, <= , != , ===

// if (op == '+') {
//     console.log(number_1 + number_2)
// } 
// else if (op == '-') {
//    console.log(number_1 - number_2) 
// }
// else if (op == '*') {
//    console.log(number_1 * number_2) 
// }
// else if (op == '/') {
//    console.log(number_1 / number_2) 
// } else {
    //     console.log('Please Enter Valid Operator')
    // }


// let y = 10

// if (y === '10') {
//     console.log('................')
// }

// let x = 10;
// let y = 10;

// if (x === 10 && y === 20) {
//     console.log('Yes X = 10 And Y = 20')
// }

// if (x === 10 || y === 20) {
//     console.log('Yes X = 10 or Y = 20')
// }

// if (x == 10 && y == 20 && z == 40 && p == 20){
    
// }

let x = 20;
let y = 10;

if (x === 10){
    if (y == 20){
        console.log('Yes X = 10 And Y = 20')
    } else {
        console.log('Yes X = 10 But Y is not equal 20')
    }
} else {
    console.log('No X is not equal 10')
}