import tkinter as tk
import mysql.connector
from tkinter import ttk

DataBaseConnect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Bdallh1722',
    database='books'
)
DB = DataBaseConnect.cursor()

# DB.execute('CREATE TABLE Favorite (username VARCHAR(255), book_name VARCHAR(255))')

# DB.execute('DELETE FROM Favorite WHERE book_name = "python"')
# DataBaseConnect.commit()

# DB.execute('DROP TABLE favorite')

def FavoriteBooks(user):
    sql = 'SELECT * FROM favorite WHERE username = %s'
    val = (user,)
    DB.execute(sql,val)
    BookOFUser = DB.fetchall()
    for i in BookOFUser:
        print(i)

def interFace(user):
    def addToFavorite(bookName):
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
                    print('This Book In Favorite')
                    return
        
        sql = 'INSERT INTO  Favorite (username, book_name) VALUES (%s, %s)'
        val = (user, final)
        DB.execute(sql,val)
        DataBaseConnect.commit()
        print('Book Add')


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

    row = 0
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
        Library.config(command= lambda book = Library : addToFavorite(book))

        column += 1
    Favorite = tk.Button(scrollable_frame, text='Favorite Books',
                  font=('Segoe UI', 10, 'bold'), bg='#007bff', fg='white',
                  activebackground='#0056b3', activeforeground='white',
                  relief='flat', cursor='hand2', height=1)
    Favorite.grid(row=0,column=4)
    Favorite.config(command= lambda : FavoriteBooks(user))

    home.mainloop()

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

