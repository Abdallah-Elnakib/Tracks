/**
 * Load users from JSON file
 *
 * @param {string} dbFile
 *     This is the path to the json file
 */
const fs = require('fs');
const { join } = require('path');

function loadUsers(users, dbFile) {
    try {
        const usersData = fs.readFileSync(dbFile,'utf8')
        const usersJson = JSON.parse(usersData);
        users.push(...usersJson);
    }
    catch (error){
        console.error("Error loading users:", error);
    }
    
}


/**
 * Load tasks from JSON file
 *
 * @param {string} dbFile
 *     This is the path to the json file
 */
function loadTasks(tasks, dbFile) {
    try {
        const tasksData = fs.readFileSync(dbFile, 'utf8')
        const tasksJson = JSON.parse(tasksData);
        tasks.push(...tasksJson);
    }
    catch (error) {
        console.error("Error loading tasks:", error);
    }
    

}

/**
 * Save tasks to JSON file
 *
 * @param {string} dbFile
 *     This is the path to the json file
 */
function saveTasks(tasks, dbFile) {
    try {
        const tasksJson = JSON.stringify(tasks);
        fs.writeFileSync(dbFile, tasksJson,'utf8')
        console.log('Task Saved')
    }
    catch (error) {
        console.log('Error' , error)
    }
    

}

/**
 * Save users to JSON file
 *
 * @param {string} dbFile
 *     This is the path to the json file
 */
function saveUsers(users, dbFile) {
    try {
        const userData = JSON.stringify(users)
        fs.writeFileSync(dbFile, userData,'utf8')
        console.log('Save Users')
    }
    catch (error) {
        console.log('Error : ', error)
    }
    
}

module.exports = {
    loadUsers,
    loadTasks,
    saveTasks,
    saveUsers
};
