# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )


# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute('SHOW TABLES')
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()


# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()


# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()


# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()


# sql = "DROP TABLE customers"
# mycursor.execute(sql)


# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()


# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()



# sql  -> tables
# nosql  -> dict



# users = [{'username' : 'abdallah', 'password' :'123'},{'username' : 'Ahmed', 'password' :'123'},{'username' : 'mohamed', 'password' :'123'}]




import mysql.connector


DATABASEConnect = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@Bdallh1722',
    database = 'books'
)


DB = DATABASEConnect.cursor()


# DB.execute('CREATE DATABASE Books')
# DB.execute('CREATE TABLE users (username VARCHAR(60), password VARCHAR(100), role VARCHAR(50))')
# DB.execute('CREATE TABLE books (name VARCHAR(100), title VARCHAR(100),author  VARCHAR(200) ,year VARCHAR(100))')





# def addNewUser():
    # username = input('Please Enter Username : ')
    # password = input('Please Enter Paswword : ')
    # sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    # val = (username,password,'user')
    # DB.execute(sql,val)
    # DATABASEConnect.commit()



# DB.execute('SELECT * FROM users')
# users = DB.fetchall() # [["abdallah","123456789","users"],["ahmed","123456789","users"],["ali","123456789","users"]]

# username = input('Please Enter Username : ')
# password = input('Please Enter Paswword : ')

# def checkuser():
#     for i in users:
#         if username == i[0] :
#             if password == i[1]:
#                 print('Login Done')
#                 return
#             else :
#                 print('Wrong password')
#                 return

#     print('Username Not Found')

# checkuser()


# username = input('Please Enter Username : ')
# password = input('Please Enter Paswword : ')

# sql = "SELECT * FROM users WHERE username = %s"
# val = (username,)
# DB.execute(sql,val)
# user = DB.fetchone()


# if user != None:
#     if password == user[1]:
#         print('Login Done')
#     else :
#         print('Wrong Password')
# else :
#     print('Username Not Found')




# sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
# val = ('asmaa', 'hhghghfh', 'admin')
# DB.execute(sql,val)
# DATABASEConnect.commit()




# DB.execute("SELECT * FROM users WHERE username LIKE '%a%' ")
# user = DB.fetchall()

# print(user)



# sql = "DELETE FROM users WHERE username = %s"
# val = ('abdallah',)
# DB.execute(sql,val)
# DATABASEConnect.commit()




sql = "UPDATE books SET title = %s WHERE name = %s"
val = ("abdallah", "python")
DB.execute(sql, val)
DATABASEConnect.commit()

# sql = "UPDATE books SET name = %s WHERE name = %s"
# val = ("data", "python")
# DB.execute(sql, val)
# DATABASEConnect.commit()



# ==============================================================================
def EditInDataBase(new,book):
    NewData = input(f'Please Enter New Book {new} : ')
    sql = f"UPDATE books SET {new} = %s WHERE name = %s"
    val = (NewData, book)
    DB.execute(sql, val)
    DATABASEConnect.commit()
    print('Edit Book Done')
    return

def login():
    username = input('Please Enter Username : ')
    password = input('Please Enter Password : ')

    sql = "SELECT * FROM users WHERE username = %s"
    val = (username,)
    DB.execute(sql,val)
    user =  DB.fetchone()

    if user == None:
        print('Username Not Found :( ')
        return login()
    elif password != user[1]:
        print('Wrong Password :( ')
        return login()
    else :
        print('==== Login Done ====')
        return

def register():
    username = input('Please Enter Username : ')
    password = input('Please Enter Password : ')
    confirmPassword = input('Please Enter Confirm  Password : ')

    sql = "SELECT * FROM users WHERE username = %s"
    val = (username,)
    DB.execute(sql,val)
    user =  DB.fetchone()

    if user != None:
        print('This Username Is Used')
        return register()
    elif password != confirmPassword :
        print('password != Confirm Password')
        return register()
    elif len(password) < 8 :
        print('Low Password')
        return register()
    else :
        sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
        val = (username, password, 'user')
        DB.execute(sql,val)
        DATABASEConnect.commit()
        print('==== Register Done ====')
        return

def addNewBook():
    bookName = input('Please Enter Book Name : ')
    bookTitle = input('Please Enter Book Title : ')
    bookAuthor = input('Please Enter Book Author : ')
    bookYear = input('Please Enter Book Year : ')

    sql = 'SELECT * FROM books WHERE name = %s'
    val = (bookName,)
    DB.execute(sql,val)
    book = DB.fetchone()

    if book != None:
        print('This Name Is Found ')
        return addNewBook()
    else :
        sql = "INSERT INTO books (name, title, author, year) VALUES (%s, %s, %s, %s)"
        val = (bookName, bookTitle, bookAuthor, bookYear)
        DB.execute(sql,val)
        DATABASEConnect.commit()
        print('Book Add Done')

def deleteBook():
    bookName = input('Please Enter Book Name :')
    sql = 'SELECT * FROM books WHERE name = %s'
    val = (bookName,)
    DB.execute(sql,val)
    book = DB.fetchone()

    if book == None:
        print('This Book Is Not Found ')
        return deleteBook()
    else :
        sql = "DELETE FROM books WHERE name = %s"
        val = (bookName,)
        DB.execute(sql,val)
        DATABASEConnect.commit()
        print('Book Delete Done')

def searchInBook():
    bookName = input('Please Enter Book Name :')
    sql = 'SELECT * FROM books WHERE name = %s'
    val = (bookName,)
    DB.execute(sql,val)
    book = DB.fetchone()

    if book == None:
        print('This Book Is Not Found ')
        return searchInBook()
    else :
        print('=========================')
        print(f'Book name : {book[0]}')
        print(f'Book title : {book[1]}')
        print(f'Book Author : {book[2]}')
        print(f'Book Year : {book[3]}')
        print('******************************')

def updateBook():
    bookName = input('Please Enter Book Name :')
    sql = 'SELECT * FROM books WHERE name = %s'
    val = (bookName,)
    DB.execute(sql,val)
    book = DB.fetchone()

    if book == None:
        print('This Book Is Not Found ')
        return updateBook()
    else :
        while True:
            print('=========================')
            print(f'1. Book name : {book[0]}')
            print(f'2. Book title : {book[1]}')
            print(f'3. Book Author : {book[2]}')
            print(f'4. Book Year : {book[3]}')
            print('5. Back')
            print('******************************')
            q = input('Number (1-5) : ')
            if q  == '1':
                EditInDataBase('name', book[0])
            elif q == '2': 
                EditInDataBase('title', book[0])
            elif q == '3':
                EditInDataBase('author', book[0])
            elif q == '4':
                EditInDataBase('year', book[0])
            elif q == '5':
                break
            else :
                print('Wrong Number :(')
                continue

def getAllBooks():
    DB.execute('SELECT * FROM books')
    books = DB.fetchall()
    for book in books:
        print('=========================')
        print(f'Book name : {book[0]}')
        print(f'Book title : {book[1]}')
        print(f'Book Author : {book[2]}')
        print(f'Book Year : {book[3]}')
        print('******************************')

def interFace():
    while True:
        print('1. View All Books')
        print('2. Search')
        print('3. Add New Book')
        print('4. Delete Book')
        print('5. Edit Book')
        print('6. Logout')
        q = input('Number (1-6) : ')
        if q == '1':
            getAllBooks()
        elif q == '2':
            searchInBook()
        elif q == '3':
            addNewBook()
        elif q == '4':
            deleteBook()
        elif q == '5':
            updateBook()
        elif q == '6':
            break
        else :
            print('Wrong Number :(')
            continue

def main():
    while True:
        print('======= Welcome App ==========')
        print('1. Login')
        print('2. Register')
        print('3. Exit')
        
        q  = input('Number : ')

        if q == '1':
            login()

        elif q == '2':
            register()

        elif q == '3':
            print('Good Bye :)')
            break

        else:
            print('Wrong Number')
            continue
        

        interFace()
        

main()