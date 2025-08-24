// login 
// register
// profile
// /api/tasks
// /api/tasks/search
// get "/api/tasks"


const express = require('express');
const fs = require('fs');
const { loadTasks, loadUsers, saveTasks , saveUsers} = require('./bouns');
const path = require('path')

let users = []; // [{},{},{}]
let tasks = [];

const app = express();
app.use(express.json());
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, '/views'))

// console.log(path.join(__dirname,'/views'))

loadUsers(users, 'users.json')
loadTasks(tasks, 'tasks.json')


// http://127.0.0.1:3000/login

    // for (let user of users){
    //     if (user.username === username && user.password === password){
    //         return res.json({message: "Login successful"});

app.post('/login' ,(req,res) =>{
    const username = req.body.username;
    const password = req.body.password;
    if (!username || !password) {
        return res.json({message: "Username and password are required"});
    }
    const getUser = users.find((user) => user.username === username) // {}
    if (!getUser) {
        return res.json({message : "username not found"});
    }
    if (getUser.password === password) {
        return res.json({message : "Login successful"});
    }
    else {
        return res.json({message : "Password is incorrect"});
    }
})

app.post('/register' , (req,res) => {
    const {username ,email, password} = req.body;
    if (!username || !email || !password) {
        return res.json({message: "All fields are required"});
    }
    const getUser = users.find((user) => user.username === username || user.email === email);
    if(getUser) {
        return res.json({message : "Username or Email already exists"});
    }
    users.push({'username' :username, "email" : email, "password":password})
    saveUsers(users, 'users.json')
    return res.json({message : "register Done"})
})

app.get('/profile/user' ,(req,res) => {
    const username = req.query.username;
    if (!username) {
        return res.json({message : 'Username are required'})
    }
    const getuser = users.find((user) => username === user.username)
    if (!getuser) {
        return res.json({message : "username not found"});  
    }
    return res.json({user : getuser})
})

app.get('/api/tasks', (req,res) => {
    return res.json({tasks : tasks})
})

app.get('/api/tasks/search' ,(req,res) => {
    const keyword = req.query.keyword;
    if (!keyword) {
        return res.json({message : 'Keyword are required'})
    }
    const search = tasks.find((task) => task.title.includes(keyword) || task.description.includes(keyword))
    if (!search) {
        return res.json({message : "No task found"});
    }
    return res.json({"tast" : search})

})

app.post('/api/tasks', (req,res) => {
    const {title, description, priority} = req.body;
    if (!title || !description || !priority) {
        return res.json({message: "All fields are required"});
    }
    tasks.push({title, description, priority})
    saveTasks(tasks, 'tasks.json')
    return res.json({message : "Task Added"})

})

app.delete('/api/delete/user', (req,res) => {
    const {username, password} = req.body;
    if (!username || !password) {
        return res.json({message: "All fields are required"});
    }
    const getUser = users.find( 
        (user) => user.username === username && user.password === password);
    if (!getUser) {
        return res.json({message : "username or password not found"});
    } 
    const deleteuser = users.filter((user) => 
        user.username !== getUser.username)
    saveUsers(deleteuser, 'users.json')
    return res.json({message : 'user deleted'})
})

app.patch('/api/Edit-username', (req,res) => {
    const {username, newusername} = req.body;
    if (!username || !newusername) {
        return res.json({message: "Username is required"});
    }
    const getUser = users.find((user) => user.username === username);
    if (!getUser) {
        return res.json({message : "username not found"});
    }
    for(let user of users) {
        if (user.username == username){
            user.username = newusername;
            saveUsers(users, 'users.json')
            return res.json({message : "username updated"})
        }
    }

})

app.get('/', (req,res) => {
    res.render('home.ejs',{username : 'ahmed', age : 27})
})
//"/{*any}"

app.all(/.*/, (req, res) => {
  res.status(404).send('404 - Page not found');
});

app.listen(3000,() => {
    console.log("Server is running on port 3000 .........");
})

