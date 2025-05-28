data = {
    'abdallah' : {
        'username' : 'abdallah',
        'password' : "123456789",
        'email' : 'abdallah.elnakib@gmail.com',
        'phone' : "0120456987",
        'Tasks' : [{'Task Name' : 'task 1' , 'Maximum Grade' : 100, 'Grade' : 80, "Status" : 'Done'}]
    }
}

def login():
    username = input('Please Enter Username : ')
    password = input('Please Enter Password : ')
    if username not in data:
        print('Username Is Not Found ')
        return login()
    elif data[username]['password'] != password :
        print('Wrong Password ')
        return login()
    else :
        return username

def register():
    username = input('Please Enter Username : ')
    password = input('Please Enter Password : ')
    confirmPassword = input('Please Enter Confirm Password : ')
    email = input('Please Enter Email : ').lower()
    phone = input('Please Enter Phone Number : ')

    checkEmail = email.split('@')
    if username not in data:
        if len(password) >= 8:
            if password == confirmPassword :
                if len(checkEmail) == 2 and checkEmail[1] == 'gmail.com':
                    data[username] = {
                            'username' : username,
                            'password' : password,
                            'email' : email,
                            'phone' : phone,
                            'Tasks' : []
                        }
                    print('Register Done')
                    return username
                else :
                    print('Error in Email')
                    return register()
            else :
                print('!=')
                return register()
        else :
            print('Password Low')
            return register()
    else :
        print('This Useername Is used')
        return register()

def addTask(username) :
    taskName = input('Enter Task Name : ')
    MaximumGrade = input('Enter  Maximum Grade : ')
    Grade = input('Enter  Grade : ')
    Status = input('Enter Status Task : ')

    data[username]['Tasks'].append({'Task Name' : taskName, 'Maximum Grade' : MaximumGrade, 'Grade' : Grade, 'Status' : Status})
    print('Task Add Done')
    
def viewTasks(username) :
    for i in data[username]['Tasks'] :
        print('=======================================')
        print(f'Task Name : {i['Task Name']}')
        print(f'Maximum Grade : {i['Maximum Grade']}')
        print(f'Grade : {i['Grade']}')
        print(f'Status : {i['Status']}')
        print('=======================================')

def editTask(username) :
    ckeck = False
    taskname = input('Enter Task Name : ')
    for i in data[username]['Tasks'] :
        if ckeck:
            break
        if i['Task Name'] == taskname :
            while True:
                print(f'Task Name : {i['Task Name']}')
                print(f'Maximum Grade : {i['Maximum Grade']}')
                print(f'Grade : {i['Grade']}')
                print(f'Status : {i['Status']}')
                print('======================================')
                print('1. Edit Task Name ')
                print('2. Edit Task Maximum Grade ')
                print('3. Edit Task Grade')
                print('4. Edit Task Status')
                print('5. Exit')
                q = input("Choose an option (1-5): ")
                if q == '5':
                    ckeck = True
                    break
                elif q  == '1':
                    name = input('Enter New task Name : ')
                    i['Task Name'] = name
                    print('Edit Done')
                elif q  == '2':
                    MaximumGrade = input('Enter New Maximum Grade : ')
                    i['Maximum Grade'] = MaximumGrade
                    print('Edit Done')
                elif q  == '3':
                    Grade = input('Enter New Maximum Grade : ')
                    i['Grade'] = Grade
                    print('Edit Done')
                elif q == '4' :
                    while True:
                        status = input('Enter New Status : ').lower()
                        if status != 'done' and status != 'panding' :
                            print('Wrong Status')
                            continue
                        i['Status'] = status
                        print('Edit Done')
                        break
                else : 
                    print('Wrong Number :(')
                    continue

def deleteTask(username) :
    check = False
    while True :
        taskName = input('Enter Task Name : ')
        for i in data[username]['Tasks'] :
            if i['Task Name'] == taskName :
                data[username]['Tasks'].remove(i)
                print('Task Delete Done')
                check = True
                break
        if check :
            break
        else :
            print('Task Name Is Not Found')

def Choose(name):
    while True :
        print('1. view All Tasks ')
        print('2. Add New Task ')
        print('3. Edit task ')
        print('4. Delete task ')
        print('5. Exit ')
        q = input("Choose an option (1-5): ")
        if q == '1':
            viewTasks(name)
        elif q == '2' :
            addTask(name)
        elif q == '3':
            editTask(name)
        elif q == '4' :
            deleteTask(name)
        elif q == '5':
            print('good Bye :)')
            break
        else :
            print('Error')
            continue

def interFace():
    while True :
        login_or_Register = input('Do You Want Login Or Register : ').lower()
        if login_or_Register == 'login':
            getUsername = login()
        elif login_or_Register == 'register':
            getUsername = register()
        else : 
            print('Error')
            continue
        print(f'===== Welcome {getUsername} =======')
        Choose(getUsername)
        break

interFace()