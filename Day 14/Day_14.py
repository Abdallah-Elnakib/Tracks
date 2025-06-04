# import mysql.connector


# connectDB = mysql.connector.connect(
#     host = "localhost",
#     user = 'root',
#     password = '@Bdallh1722',
#     database = 'test' 
# )


# DB = connectDB.cursor()


# DB.execute('CREATE DATABASE test')

# DB.execute('CREATE TABLE USERS (username VARCHAR(100), password VARCHAR(100), role VARCHAR (50))')


# def addNewUser(username, password, role):
#     sql = 'INSERT INTO USERS (username , password , role) VALUES (%s , %s, %s)'
#     val = (username, password, role)

#     DB.execute(sql,val)

#     connectDB.commit()



# usernameFromUser = input('Please Enter Username : ')
# passwordFromUser = input('Please Enter Password : ')
# roleFromUser = input('Please Enter Role : ')


# addNewUser(usernameFromUser, passwordFromUser, roleFromUser)



# sql = 'INSERT INTO USERS (username , password , role) VALUES (%s , %s, %s)'


# val = [
#     ('mohamed', '1234567890', 'admin'),
#     ('ali', '147852369', 'user'),
#     ('ehab' , '987654321', 'admin')
# ]

# DB.executemany(sql,val)

# connectDB.commit()



# getAllUsers = DB.execute("SELECT * FROM USERS")


# users = DB.fetchall()


# def checkLogin(username, password):
#     for user in users :
#         if user[0] == username:
#             if user[1] == password:
#                 print("Login Done")
#                 return
#             else :
#                 print('Wrong Password')
#                 return

#     print('Username Not Found')

# usernameFromUser = input('Please Enter Username : ')
# passwordFromUser = input('Please Enter Password : ')

# checkLogin(usernameFromUser, passwordFromUser)




# usernameFromUser = input('Please Enter Username : ')
# passwordFromUser = input('Please Enter Password : ')

# sql = "SELECT * FROM USERS WHERE username = %s"
# val = (usernameFromUser,)

# DB.execute(sql, val)

# user = DB.fetchone()



# if user != None :
#     if user[1] == passwordFromUser:
#         print('Login Done')
#     else :
#         print('Wrong Password')
# else :
#     print('Username Not Found')





# قم بأنشاء برنامج يطبع للمستخدم رساله ترحيب
# بعد ذالك هل تريد عمل تسجيل دخول او انشاء حساب جديد 
# البيانات الموجوده في قاعده البيانات هي اسم المستخدم كلمه المرور والعمر ورقم الهاتف
# في حاله طلب المستخدم انشاء حساب جديد اطلب منه هذه البيانات 
# بعد ذالك تأكد من ان اسم المستخدم لم يتم استخدامه من قبل وان كلمه المرور اكبر من 8
# قم بأضافه البيانات في قاعده البيانات واطبع للمستخدم انه تم تسجيل الدخول بنجاح
# ان كان هناك اي خطاء في البيانات اظهر رساله الخطاء
# اما في حاله طلب المستخدم تسجيل دخول اطلب منه اسم المستخدم وكلمه المرور 
# قم بالتحقق من البيانات من قاعده البيانات وان كانت صحيحه اطبع له تم تسجيل الدخول
# في حاله وجود اي خطاء اطبع الرساله الخاصه بالخطاء



# import mysql.connector 


# connectDB = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '@Bdallh1722',
#     database = 'App'
# )


# DB = connectDB.cursor()

# DB.execute('CREATE TABLE users  (username VARCHAR(100), password VARCHAR(100), age VARCHAR (50), phone VARCHAR (50))')

# DB.execute('CREATE DATABASE App')


# def AddNewUserDataBase(username, password, age, phone):
#     sql = 'INSERT INTO users (username , password , age, phone) VALUES (%s , %s, %s, %s)'
#     val = (username, password, age, phone)
#     DB.execute(sql,val)
#     connectDB.commit()

# def getUserFromDataBase(username):
#     sql = "SELECT * FROM users WHERE username = %s"
#     val = (username,)
#     DB.execute(sql,val)
#     user = DB.fetchone()

#     return user

# def login():
#     username = input('Please Enter Username : ')
#     password = input('Please Enter Password : ')

#     data = getUserFromDataBase(username)

#     if data != None:
#         if data[1] == password:
#             print("login Done")
#             return
#         else :
#             print('Wrong Paswword')
#             return login()
#     else :
#         print('Username Not Found')
#         return login()

# def register():
#     username = input('Please Enter Username : ')
#     password = input('Please Enter Password : ')
#     age = input('Please Enter Your Age : ')
#     phone = input('Please Enter Your Phine Number : ')

#     data = getUserFromDataBase(username)

#     if data == None :
#         if len(password) >= 8 :
#             AddNewUserDataBase(username, password, age, phone)
#             print("Register Done")
#             return
#         else :
#             print('Passwrd Low')
#             return register()
#     else : 
#         print('This Username Is Used')
#         return register()
    
# def main():
#     print('1. Login')
#     print('2. Register')
#     q = input('1 Or 2 : ')

#     if q == '1':
#         login()
#     elif q == '2':
#         register()
#     else :
#         print('Wrong Number')
#         return main()


# main()


# import mysql.connector 


# connectDB = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '@Bdallh1722',
#     database = 'App'
# )


# DB = connectDB.cursor()

# sql = 'DELETE FROM users WHERE username = %s'
# val = ('ahmed',)

# DB.execute(sql,val)

# connectDB.commit()


# import mysql.connector


# ConnectDB = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '@Bdallh1722',
#     database = 'App'
# )

# DB = ConnectDB.cursor()


# sql = "UPDATE users SET age = %s WHERE username = %s"
# val = ('10', 'abdallah')

# DB.execute(sql, val)

# ConnectDB.commit()


# import mysql.connector

# ConnectDB = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '@Bdallh1722',
# )

# BD = ConnectDB.cursor()



# sql = "DROP DATABASE App"
# sql = "DROP TABLE App"

# BD.execute(sql)




# import mysql.connector


# ConnectDB = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '@Bdallh1722',
#     database = 'APP'
# )

# DB  = ConnectDB.cursor()

# DB.execute('CREATE DATABASE APP')


# DB.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), role VARCHAR(50))")


# sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
# val = ('ahmed', '123456789', 'admin')
# DB.execute(sql, val)

# ConnectDB.commit()

# DB.execute('SHOW TABLES')

# tables = DB.fetchall()

# print(tables)







# Tables =>  Users - books - Favorite

# Users -> useranme - password - role - age - email - phone number
# books -> id - boookName - bookTitle - author - year
# Favorite ->  id - username


# resgiter(): -> add user as user
# def login():
# def home():
# def getallBooks():
# def search():
# def addNewUser(): -> add user as admin
# def editBook():
# def deleteBook():
# def addNewBook():
# def main():




