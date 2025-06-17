import mysql.connector
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk

load_dotenv()

DataBaseConnect = mysql.connector.connect(
    host = os.getenv('HOST'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
    database = os.getenv('DATABASE')
)

DB = DataBaseConnect.cursor()



error_label_Favorite = None
error_label_add_book = None
def ViewErrorInFavorite(text, container, color='red'):
    global error_label_Favorite
    if error_label_Favorite is not None:
        error_label_Favorite.destroy()
    error_label_Favorite = tk.Label(container, text=text, fg=color, bg='white', font=('Segoe UI', 10, 'bold'))
    error_label_Favorite.grid(row=0, column=0, columnspan=2, pady=(5, 0))

def ViewErrorAddBook(text, container, color='red'):
    global error_label_add_book
    if error_label_add_book is not None:
            error_label_add_book.destroy()
    error_label_add_book = tk.Label(container, text=text, fg=color, bg='#f5f6fa', font=('Segoe UI', 10, 'bold'))
    error_label_add_book.grid(row=0, column=1, columnspan=2, pady=(5, 0))

def FavoriteBooks(user):
    sql = 'SELECT * FROM favorite WHERE username = %s'
    val = (user,)
    DB.execute(sql,val)
    BookOFUser = DB.fetchall() # [('abdallah','python'),('abdallah','java')]
    BookNames = []
    for i in BookOFUser:
        BookNames.append(i[1])


    Favorite = tk.Tk()
    Favorite.title('Favorite')
    Favorite.geometry('900x700')
    Favorite.configure(bg='#ecf0f3')

    container = tk.Frame(Favorite, bg='#ecf0f3')
    container.pack(fill='both', expand=True)

    canvas = tk.Canvas(container, bg='#ecf0f3', highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#ecf0f3')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')


    row = 0
    column = 0
    for book in BookNames:
        sql = "SELECT * FROM books WHERE name = %s"
        val = (book,)
        DB.execute(sql,val)
        bookData = DB.fetchone() # ['python', 'python book', 'abdallah', '2025']

        if column == 3:
            row += 1
            column = 0

        frame = tk.Frame(scrollable_frame, bg='white', width=250, height=220,
                         bd=1, relief='solid', highlightbackground="#d0d0d0", highlightthickness=1)
        frame.grid(row=row, column=column, padx=20, pady=20)
        frame.grid_propagate(False)

        tk.Label(frame, text=f'📘 Name: {bookData[0]}',
                 font=('Segoe UI', 10, 'bold'), bg='white', fg='#333', anchor='w').pack(pady=(10, 2), padx=10, anchor='w')
        tk.Label(frame, text=f'📖 Title: {bookData[1]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'✍️ Author: {bookData[2]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'📅 Year: {bookData[3]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')

        column += 1

    Favorite.mainloop()

def interFace(user):
    def addToFavorite(bookName, Frame):
        name = bookName.cget('text')
        nameAfterSplit = name.split('Add to Library (') # ['Add to Library (', 'Python)']
        final = nameAfterSplit[1][0:-1]

        sql = 'SELECT * FROM favorite WHERE username = %s'
        val = (user,)
        DB.execute(sql,val)
        BookOFUser = DB.fetchall()

        if BookOFUser != None :
            for i in BookOFUser:
                if i[1] == final:
                    ViewErrorInFavorite('This Book In Favorite', Frame)
                    return
        
        sql = 'INSERT INTO  Favorite (username, book_name) VALUES (%s, %s)'
        val = (user, final)
        DB.execute(sql,val)
        DataBaseConnect.commit()
        ViewErrorInFavorite('Book Add', Frame, color='green')


    home = tk.Tk()
    home.title('Books Library')
    home.geometry('900x700')
    home.configure(bg='#ecf0f3')

    container = tk.Frame(home, bg='#ecf0f3')
    container.pack(fill='both', expand=True)

    canvas = tk.Canvas(container, bg='#ecf0f3', highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#ecf0f3')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    DB.execute('SELECT * FROM books')
    books = DB.fetchall()

    row = 1
    column = 0
    for book in books:
        if column == 3:
            row += 1
            column = 0

        frame = tk.Frame(scrollable_frame, bg='white', width=250, height=220,
                         bd=1, relief='solid', highlightbackground="#d0d0d0", highlightthickness=1)
        frame.grid(row=row, column=column, padx=20, pady=20)
        frame.grid_propagate(False)

        tk.Label(frame, text=f'📘 Name: {book[0]}',
                 font=('Segoe UI', 10, 'bold'), bg='white', fg='#333', anchor='w').pack(pady=(10, 2), padx=10, anchor='w')
        tk.Label(frame, text=f'📖 Title: {book[1]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'✍️ Author: {book[2]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'📅 Year: {book[3]}',
                 font=('Segoe UI', 10), bg='white', fg='#444', anchor='w').pack(pady=2, padx=10, anchor='w')

        Library = tk.Button(frame, text=f'Add to Library ({book[0]})',
                  font=('Segoe UI', 10, 'bold'), bg='#007bff', fg='white',
                  activebackground='#0056b3', activeforeground='white',
                  relief='flat', cursor='hand2', height=1)
        Library.pack(pady=(10, 10))
        Library.config(command= lambda book = Library : addToFavorite(book, scrollable_frame))

        column += 1
    Favorite = tk.Button(scrollable_frame, text='Favorite Books',
                  font=('Segoe UI', 10, 'bold'), bg='#007bff', fg='white',
                  activebackground='#0056b3', activeforeground='white',
                  relief='flat', cursor='hand2', height=1)
    Favorite.grid(row=0,column=4)
    Favorite.config(command= lambda : FavoriteBooks(user))

    home.mainloop()

def addNewBook():
    addBook = tk.Tk()
    addBook.title('➕ Add New Book - Books Library')
    addBook.geometry('500x400')
    addBook.configure(bg='#f5f6fa')

    def add():
        bookName = name.get().lower()
        booktitle = title.get()
        bookAuthor = author.get()
        bookyear = year.get()

        sql = 'SELECT * FROM books WHERE name = %s'
        val = (bookName,)
        DB.execute(sql,val)
        getBook = DB.fetchone()

        if bookName == '':
            ViewErrorAddBook('Please Enter Book Name', addBook)
        elif booktitle == "" :
            ViewErrorAddBook('Please Enter Book Title', addBook)
        elif bookAuthor == "" :
            ViewErrorAddBook('Please Enter Book Author', addBook)
        elif bookyear == "":
            ViewErrorAddBook('Please Enter Book Year', addBook)
        elif getBook != None :
            ViewErrorAddBook('Name book used', addBook)
        elif int(bookyear) > 2025 :
            ViewErrorAddBook("Year Error", addBook)
        else :
            sql = 'INSERT INTO books (name, title, author, year) VALUES (%s, %s, %s, %s)'
            val = (bookName, booktitle, bookAuthor, bookyear)
            DB.execute(sql,val)
            DataBaseConnect.commit()
            ViewErrorAddBook('Book Add Done', addBook, color='green')
            addBook.destroy()


    form_frame = tk.Frame(addBook, bg='white')
    form_frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(form_frame, text='📘 Book Name:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    name = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    name.pack(padx=20, pady=(0, 10))

    tk.Label(form_frame, text='📖 Book Title:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    title = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    title.pack(padx=20, pady=(0, 10))

    tk.Label(form_frame, text='✍️ Author:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    author = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    author.pack(padx=20, pady=(0, 10))

    tk.Label(form_frame, text='📅 Year:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    year = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    year.pack(padx=20, pady=(0, 20))

    add_btn = tk.Button(form_frame, text='✅ Add Book', font=('Segoe UI', 10, 'bold'),
                        bg='#1e90ff', fg='white', activebackground='#3742fa',
                        relief='flat', width=30, height=2, cursor='hand2', command=add)
    add_btn.pack(pady=(10, 20))

    addBook.mainloop()

def deleteBook():
    delete = tk.Tk()
    delete.title('➕ Add New Book - Books Library')
    delete.geometry('500x400')
    delete.configure(bg='#f5f6fa')

    def deleteFromDB():
        bookName = name.get().lower()

        sql = 'SELECT * FROM books WHERE name = %s'
        val = (bookName,)
        DB.execute(sql,val)
        getBook = DB.fetchone()

        if bookName == '':
            ViewErrorAddBook('Please Enter Book Name', delete)
        elif getBook == None:
            ViewErrorAddBook('Book Not Found', delete)
        else :
            sql = 'DELETE FROM books WHERE name = %s'
            val = (bookName,)
            DB.execute(sql,val)
            DataBaseConnect.commit()
            delete.destroy()


    form_frame = tk.Frame(delete, bg='white')
    form_frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(form_frame, text='📘 Book Name:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    name = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    name.pack(padx=20, pady=(0, 10))

   

    add_btn = tk.Button(form_frame, text='✅ Delete Book', font=('Segoe UI', 10, 'bold'),
                        bg='#1e90ff', fg='white', activebackground='#3742fa',
                        relief='flat', width=30, height=2, cursor='hand2', command=deleteFromDB)
    add_btn.pack(pady=(10, 20))

    delete.mainloop()

def addNewAdmin():
    addAdmin = tk.Tk()
    addAdmin.title('➕ Add New Admin - Books Library')
    addAdmin.geometry('500x400')
    addAdmin.configure(bg='#f5f6fa')

    def addInDB():
        usernameFromUser = username.get().lower()
        passwordFromUser = password.get()
        confirmFromUser = confirm.get()

        sql = 'SELECT * FROM users WHERE username = %s'
        val = (usernameFromUser,)
        DB.execute(sql,val)
        user = DB.fetchone()

        if usernameFromUser == "":
            ViewErrorAddBook('Please Enter Username', addAdmin)
        elif passwordFromUser == "":
            ViewErrorAddBook('Please Enter Password', addAdmin)
        elif confirmFromUser == "" :
            ViewErrorAddBook('Please Confirm Password', addAdmin)
        elif passwordFromUser != confirmFromUser :
            ViewErrorAddBook('Password And Confirm Password Not Match', addAdmin)
        elif len(passwordFromUser) < 8 :
            ViewErrorAddBook('Low Password', addAdmin)
        elif user != None :
            ViewErrorAddBook('This Username Is Used', addAdmin)
        else :
            sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
            val = (usernameFromUser, passwordFromUser, 'admin')
            DB.execute(sql,val)
            DataBaseConnect.commit()
            ViewErrorAddBook('Book Add Done', addAdmin, color='green')
            addAdmin.destroy()



    form_frame = tk.Frame(addAdmin, bg='white')
    form_frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(form_frame, text='Username:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    username = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    username.pack(padx=20, pady=(0, 10))

    tk.Label(form_frame, text='Password:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    password = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    password.pack(padx=20, pady=(0, 10))

    tk.Label(form_frame, text='Confirm Password:', bg='white', font=('Segoe UI', 10, 'bold')).pack(padx=20, pady=(10, 2), anchor='w')
    confirm = tk.Entry(form_frame, width=40, font=('Segoe UI', 10), bg='#ecf0f1', relief='flat')
    confirm.pack(padx=20, pady=(0, 10))


    add_btn = tk.Button(form_frame, text='✅ Add New Admin', font=('Segoe UI', 10, 'bold'),
                        bg='#1e90ff', fg='white', activebackground='#3742fa',
                        relief='flat', width=30, height=2, cursor='hand2', command=addInDB)
    add_btn.pack(pady=(10, 20))

    addAdmin.mainloop()

def InterFaceAdmin():
    homeAdmin = tk.Tk()
    homeAdmin.title('📚 Books Library - Admin Panel')
    homeAdmin.geometry('1000x720')
    homeAdmin.configure(bg='#f5f6fa')

    
    toolbar = tk.Frame(homeAdmin, bg='#2f3542', height=60)
    toolbar.pack(fill='x', side='top')

    button_style = {
        "font": ('Segoe UI', 10, 'bold'),
        "bg": '#1e90ff',
        "fg": 'white',
        "activebackground": '#3742fa',
        "activeforeground": 'white',
        "relief": 'flat',
        "cursor": 'hand2',
        "padx": 15,
        "pady": 5
    }

    tk.Button(toolbar, text='➕ Add New Book', **button_style, command=addNewBook).pack(side='left', padx=10, pady=10)
    tk.Button(toolbar, text='🗑️ Delete Book', **button_style, command=deleteBook).pack(side='left', padx=10, pady=10)
    tk.Button(toolbar, text='✏️ Edit Book', **button_style).pack(side='left', padx=10, pady=10)
    tk.Button(toolbar, text='🔍 Search', **button_style).pack(side='left', padx=10, pady=10)
    tk.Button(toolbar, text='👤 Add New Admin', **button_style, command=addNewAdmin).pack(side='left', padx=10, pady=10)


    container = tk.Frame(homeAdmin, bg='#f5f6fa')
    container.pack(fill='both', expand=True)

    canvas = tk.Canvas(container, bg='#f5f6fa', highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#f5f6fa')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')


    DB.execute('SELECT * FROM books')
    books = DB.fetchall()

    row = 1
    column = 0
    for book in books:
        if column == 3:
            row += 1
            column = 0

        frame = tk.Frame(scrollable_frame, bg='white', width=270, height=200,
                         bd=0, highlightbackground="#ced6e0", highlightthickness=1)
        frame.grid(row=row, column=column, padx=20, pady=20)
        frame.grid_propagate(False)

        tk.Label(frame, text=f'📘 Name: {book[0]}',
                 font=('Segoe UI', 10, 'bold'), bg='white', fg='#2f3542', anchor='w').pack(pady=(12, 5), padx=10, anchor='w')
        tk.Label(frame, text=f'📖 Title: {book[1]}',
                 font=('Segoe UI', 10), bg='white', fg='#57606f', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'✍️ Author: {book[2]}',
                 font=('Segoe UI', 10), bg='white', fg='#57606f', anchor='w').pack(pady=2, padx=10, anchor='w')
        tk.Label(frame, text=f'📅 Year: {book[3]}',
                 font=('Segoe UI', 10), bg='white', fg='#57606f', anchor='w').pack(pady=2, padx=10, anchor='w')

        column += 1

    homeAdmin.mainloop()

error_label = None
def ViewError(text, container, color='red'):
    global error_label
    if error_label is not None:
        error_label.destroy()
    error_label = tk.Label(container, text=text, fg=color, bg='white', font=('Segoe UI', 10, 'bold'))
    error_label.grid(row=5, column=0, columnspan=2, pady=(5, 0))

def register():
    master.destroy()
    root = tk.Tk()
    root.title('Register')
    root.geometry('500x500')
    root.configure(bg='#ecf0f3')

    def addNewUser():
        usernameFromUser = username.get().lower()
        passwordFromUser = password.get()
        confirm_passwordFromUser = confirm_password.get()

        if usernameFromUser == '':
            ViewError('Please Enter Username', frame)
        elif passwordFromUser == '':
            ViewError('Please Enter Password', frame)
        elif confirm_passwordFromUser == '':
            ViewError('Please Confirm Password', frame)
        elif passwordFromUser != confirm_passwordFromUser:
            ViewError('Passwords Do Not Match', frame)
        elif len(passwordFromUser) < 8:
            ViewError('Password Too Short (min 8)', frame)
        else :
            sql = 'SELECT * FROM users WHERE username = %s'
            val = (usernameFromUser,)
            DB.execute(sql,val)
            user = DB.fetchone()

            if user != None:
                ViewError('This Username Is Used', frame)
            else :
                sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
                val = (usernameFromUser, passwordFromUser, 'user')
                DB.execute(sql,val)
                DataBaseConnect.commit()
                ViewError('User Add Done', frame, color='green')
                root.destroy()
                interFace(usernameFromUser)



    frame = tk.Frame(root, bg='white', bd=0, highlightbackground="#d0d0d0", highlightthickness=1)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame, text='Create Account', font=('Segoe UI', 20, 'bold'), bg='white', fg='#222').grid(
        row=0, column=0, columnspan=2, pady=(25, 15))

    username = tk.Entry(frame, font=('Segoe UI', 12), width=28, bd=1, relief='solid')
    password = tk.Entry(frame, font=('Segoe UI', 12), show='*', width=28, bd=1, relief='solid')
    confirm_password = tk.Entry(frame, font=('Segoe UI', 12), show='*', width=28, bd=1, relief='solid')

    tk.Label(frame, text='Username', bg='white', font=('Segoe UI', 12)).grid(row=1, column=0, sticky='w', padx=20)
    username.grid(row=1, column=1, padx=20, pady=8)
    tk.Label(frame, text='Password', bg='white', font=('Segoe UI', 12)).grid(row=2, column=0, sticky='w', padx=20)
    password.grid(row=2, column=1, padx=20, pady=8)
    tk.Label(frame, text='Confirm Password', bg='white', font=('Segoe UI', 12)).grid(row=3, column=0, sticky='w', padx=20)
    confirm_password.grid(row=3, column=1, padx=20, pady=8)

    def toggle_password():
        if password.cget('show') == '':
            password.config(show='*')
            confirm_password.config(show='*')
            toggle_btn.config(text='Show')
        else:
            password.config(show='')
            confirm_password.config(show='')
            toggle_btn.config(text='Hide')

    toggle_btn = tk.Button(frame, text='Show', command=toggle_password,
                           bg='white', fg='#007bff', bd=0, font=('Segoe UI', 10), cursor='hand2')
    toggle_btn.grid(row=3, column=1, sticky='e', padx=25)

    tk.Button(frame, text='Register', command=addNewUser,
              font=('Segoe UI', 12, 'bold'), bg='#28a745', fg='white',
              activebackground='#218838', width=20, bd=0, relief='flat', cursor='hand2').grid(
        row=6, column=0, columnspan=2, pady=(20, 25))

    root.mainloop()

def login_screen():
    global master
    master = tk.Tk()
    master.title('Login')
    master.geometry('500x500')
    master.configure(bg='#ecf0f3')

    frame = tk.Frame(master, bg='white', bd=0, highlightbackground="#d0d0d0", highlightthickness=1)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    def login():
        usernameFromUser = username.get().lower()
        passwordFromUser = password.get()

        if usernameFromUser == '':
            ViewError('Please enter your username', frame)
        elif passwordFromUser == '':
            ViewError('Please enter your password', frame)
        else:
            sql = 'SELECT * FROM users WHERE username = %s'
            val = (usernameFromUser,)
            DB.execute(sql, val)
            user = DB.fetchone()

            if user is None:
                ViewError('User not found', frame)
            elif passwordFromUser != user[1]:
                ViewError('Incorrect password', frame)
            else:
                if user[2] == 'admin':
                    ViewError('Login successful!', frame, color='green')
                    master.destroy()
                    InterFaceAdmin()
                else :
                    ViewError('Login successful!', frame, color='green')
                    master.destroy()
                    interFace(usernameFromUser)

    tk.Label(frame, text='Welcome Back!', font=('Segoe UI', 20, 'bold'), bg='white', fg='#222').grid(
        row=0, column=0, columnspan=2, pady=(25, 15))

    username = tk.Entry(frame, font=('Segoe UI', 12), width=28, bd=1, relief='solid')
    password = tk.Entry(frame, font=('Segoe UI', 12), show='*', width=28, bd=1, relief='solid')

    tk.Label(frame, text='Username', bg='white', font=('Segoe UI', 12)).grid(row=1, column=0, sticky='w', padx=20)
    username.grid(row=1, column=1, padx=20, pady=8)
    tk.Label(frame, text='Password', bg='white', font=('Segoe UI', 12)).grid(row=2, column=0, sticky='w', padx=20)
    password.grid(row=2, column=1, padx=20, pady=8)

    def toggle_password():
        if password.cget('show') == '':
            password.config(show='*')
            toggle_btn.config(text='Show')
        else:
            password.config(show='')
            toggle_btn.config(text='Hide')

    toggle_btn = tk.Button(frame, text='Show', command=toggle_password,
                           bg='white', fg='#007bff', bd=0, font=('Segoe UI', 10), cursor='hand2')
    toggle_btn.grid(row=2, column=1, sticky='e', padx=25)

    tk.Button(frame, text='Login', command=login,
              font=('Segoe UI', 12, 'bold'), bg='#007bff', fg='white',
              activebackground='#0056b3', width=20, bd=0, relief='flat', cursor='hand2').grid(
        row=6, column=0, columnspan=2, pady=(20, 10))

    tk.Button(frame, text='Register', command=register,
              font=('Segoe UI', 11, 'bold'), bg='white', fg='#007bff',
              activebackground='#eef2f7', width=20, bd=1, relief='solid', cursor='hand2').grid(
        row=7, column=0, columnspan=2, pady=(0, 25))

    master.mainloop()



login_screen()


