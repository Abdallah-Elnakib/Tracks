# def test():
#         number = ["1","2","3","4","5","6","7","8","9","0"]
#         numbers = input('Enter Number : ')
#         for i in numbers :
#                 if i not in number :
#                     print('Wrong Number')
#                     return test()   


        

# test()


# def test():
#     try:
#         numbers = int(input('Enter Number : '))
#     except :
#         print('Wrong Number')
#         return test()


# test()


# try:
#     print(x)
# except :
#     print("An exception occurred")



# print(555)

# ValueError
# NameError

# x = 5
# try:
#     numbers = int(input('Enter Number : '))

# except :
#     print("An exception occurred")




# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# try :
#     print(x)
# except :
    

# finally :
#     print('Error')

# numbers = int(input('Enter Number : '))

# print(555455)


# try :
#     numbers = int(input('Enter Number : '))
#     print(numbers)
# except :
#     print('Wrong number')

# print(555455)


# def test():
#     try :
#         numbers = int(input('Enter Number : '))
#         print(numbers)
#     except :
#         print('Wrong number')
#         return test()


# test()


# try :
#     numbers = int(input('Enter Number : '))
#     try :
#         number2 = int(input('Enter Number  2 : '))
#     except :
#         print('Wrong number 2 ')

# except :
#     print('Wrong number 1 ')



# try : 
#     username = input('Username : ')
#     if usernameeeee == 'abdallah':
#         print('Login Done')
#     else :
#         print('wrong username')
# except :
#     print('Error')

# print(4444)


# username = input('Username : ')
# if usernameee == 'abdallah':
#         print('Login Done')
# else :
#         print('wrong username')


# print(4444)



# with open('',"r") as data :
#     database = json.load(data)



# id  = '1'

# for i in database['products'] :
#     if id i['id'] == id:
#         database['products'].remove(i)
#         with open('', 'w') as dataAfterDelete :
#             json.dump(database, dataAfterDelete, indint= 4)
#         return 
# print('product Id Not Found')




# tkinter

data = {
    'abdallah' : {
        "username" : 'abdallah',
        "password" : "123456789"
    },
    'ahmed' : {
        "username" : 'ahmed',
        "password" : "123456789"
    },
}










# import tkinter as tk

# master = tk.Tk()
# master.title('Login')
# master.geometry("400x400")
# master.maxsize(400, 400)
# master.minsize(400, 400)
# master['bg'] = "#2381B0"
       

# master.columnconfigure(0, weight=1)
# master.columnconfigure(1, weight=1)
# master.columnconfigure(2, weight=1)
# master.columnconfigure(3, weight=1)

# def login():
#     user = username.get()
#     passwordOfUser = password.get()

#     if user in data:
#         if data[user]["password"] == passwordOfUser :
#             loginDone = tk.Label(master, text='Welcome Back')
#             loginDone.grid(row=1, column=3, padx=5)
#             master.destroy()
#         else :
#             wrongPasswrd = tk.Label(master, text='Wrong Password', fg='red')
#             wrongPasswrd.grid(row=2, column=3, padx=5)
#     else :
#         wrongUsername = tk.Label(master, text='Wrong Username', fg='red')
#         wrongUsername.grid(row=1, column=3, padx=5)


# welcome = tk.Label(master, text='Ⓟⓛⓔⓐⓢⓔ Ⓛⓞⓖⓘⓝ', font=('Segoe UI', 24, "bold"), fg='white', background='#2381B0')
# welcome.grid(row=0, column=0, columnspan=4, pady=30)




# usernameLabel = tk.Label(master, text='ᴜᴤᴇʀɴᴀᴍᴇ', font=('Segoe UI', 10, "bold"), fg='white', background='#2381B0')
# usernameLabel.grid(row=1, column=1, sticky="e", padx=1, pady=10)

# username = tk.Entry(master, width=30)
# username.grid(row=1, column=2, padx=1, pady=10)


# passwordLabel = tk.Label(master, text='ᴘᴀᴤᴤᴡᴏʀᴅ', font=('Segoe UI', 10, "bold"), fg='white', background='#2381B0')
# passwordLabel.grid(row=2, column=1, sticky="e", padx=1, pady=10)

# password = tk.Entry(master, show="*", width=30)
# password.grid(row=2, column=2, padx=1, pady=10)


# login = tk.Button(master, text='Login', background='#7de2d1', width=15, height=1, command=login)
# login.grid(row=3, column=0, sticky='s', columnspan=4)


# master.mainloop()








# import tkinter as tk


# master = tk.Tk()
# master.title('X-O')

# row = 0
# column = 0

# player = "X"
# def game(x):
#     global player
#     x.config(text = player)
#     if player == "X":
#         player = "O"
#     else :
#         player = "X"


# for i in range(0,3):
#     for u in range(0,3):
#        button = tk.Button(master, text='', font=("Segoe UI", 24, "bold"), width=10, height=3)
#        button.config(command= lambda gameCheck = button: game(gameCheck))
#        button.grid(row=row, column=column, padx=2, pady=2)
#        column += 1
    
#     row += 1
#     column = 0



# master.mainloop()









# from tkinter import *

# master = Tk()


# mainMenu = Menu(master)
# master.config(menu=mainMenu)

# filemenu = Menu(mainMenu)
# helpmenu = Menu(mainMenu)
# editMenu = Menu(mainMenu)

# mainMenu.add_cascade(label='File', menu=filemenu)
# mainMenu.add_cascade(label='Help', menu=helpmenu)
# mainMenu.add_cascade(label='Edit', menu=editMenu)


# editMenu.add_command(label='Edit File')
# def exit():
#     master.destroy()


# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=exit)


# helpmenu.add_command(label='About')

# mainloop()



# import tkinter as tk

# master = tk.Tk()
# master.geometry('400x400')

# w = tk.Scale(master, background='red', from_=0, to=40)
# w.grid(row=0, column=20, pady=10)

# row = 1
# column = 0

# player = "X"
# def game(x):
#     global player
#     x.config(text = player)
#     if player == "X":
#         player = "O"
#     else :
#         player = "X"


# for i in range(0,3):
#     for u in range(0,3):
#        button = tk.Button(master, text='', font=("Segoe UI", 24, "bold"), width=10, height=3)
#        button.config(command= lambda gameCheck = button: game(gameCheck))
#        button.grid(row=row, column=column, padx=2, pady=2)
#        column += 1
    
#     row += 1
#     column = 0

# master.mainloop()





# import tkinter as tk

# root = tk.Tk()  # Create the main window

# # Create a TV remote UI
# turn_on = tk.Button(root, text="ON")
# turn_on.pack()

# turn_off = tk.Button(root, text="OFF", command=root.destroy)
# turn_off.pack()

# volume = tk.Label(root, text="VOLUME")
# volume.pack()

# vol_up = tk.Button(root, text="+")
# vol_up.pack()

# vol_down = tk.Button(root, text="-")
# vol_down.pack()

# root.mainloop()