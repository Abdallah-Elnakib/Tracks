
# check = 4
# for i in range(1,10):
#     if i >= 6:
#         print('*' * check)
#         check -= 1
#     else :
#         print('*' * i)




# Exercise 15: Print the alternate numbers pattern
# Pattern:

# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15


# 1  =>  1   (1,2)
# 2  =>  2   (2,4)
# 4  =>  3   (4,7)
# 7  =>  4   (7,11)
# 11 =>  5   (11,16)

# for i in range(1,6): 
#     for u in range():  
#         print(u, end=" ") 
#     print('')


# num = 1 
# for i in range(1, 6):
#     for u in range(0,i):
#         print(num, end=" ")
#         num += 1
#     print()


import tkinter as tk
from Hashing import HASH, CHECKHASH

master = tk.Tk()
master.title('🔐 Hash Text Utility')
master.geometry('500x400')
master.configure(bg='#f5f6fa')

def showText(text):
    window = tk.Tk()
    window.title('🔐 Hash Text Tool')
    window.geometry('1000x800')
    window.configure(bg='#f5f6fa')

    frame = tk.Frame(window, bg='white', bd=2, relief='ridge')
    frame.place(relx=0.5, rely=0.5, anchor='center', width=800, height=250)

    title_label = tk.Text(frame, font=('Segoe UI', 16, 'bold'), bg='white', fg='#2f3640')
    title_label.pack(pady=(15, 5))

    title_label.insert(tk.END,text)

    window.mainloop()

def hash():
    window = tk.Tk()
    window.title('🔐 Hash Text Tool')
    window.geometry('500x300')
    window.configure(bg='#f5f6fa')

    def getText():
        text = text_entry.get().lower()
        TEXTAFTERHASHING = HASH(text)
        showText(TEXTAFTERHASHING)


    frame = tk.Frame(window, bg='white', bd=2, relief='groove')
    frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=220)


    title_label = tk.Label(frame, text='Enter Text to Hash', font=('Segoe UI', 16, 'bold'), bg='white', fg='#2f3640')
    title_label.pack(pady=(15, 5))


    text_entry = tk.Entry(frame, font=('Segoe UI', 14), bd=1, relief='solid', width=30)
    text_entry.pack(pady=10)

    hash_button = tk.Button(
        frame,
        text='🔐 Hash Text',
        font=('Segoe UI', 12),
        bg='#00a8ff',
        fg='white',
        activebackground='#0097e6',
        bd=0,
        padx=15,
        pady=5,
        cursor='hand2',
        command= getText
    )
    hash_button.pack(pady=10)


    window.mainloop()

def checkHash():
    window = tk.Tk()
    window.title('🔐 Hash Text Tool')
    window.geometry('500x300')
    window.configure(bg='#f5f6fa')

    def getText():
        text = text_entry.get()
        TEXTAFTERHASHING = CHECKHASH(text)
        showText(TEXTAFTERHASHING)

    frame = tk.Frame(window, bg='white', bd=2, relief='groove')
    frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=220)


    title_label = tk.Label(frame, text='Enter Text to Check Hash', font=('Segoe UI', 16, 'bold'), bg='white', fg='#2f3640')
    title_label.pack(pady=(15, 5))


    text_entry = tk.Entry(frame, font=('Segoe UI', 14), bd=1, relief='solid', width=30)
    text_entry.pack(pady=10)

    hash_button = tk.Button(
        frame,
        text='🔐Check Hash Text',
        font=('Segoe UI', 12),
        bg='#00a8ff',
        fg='white',
        activebackground='#0097e6',
        bd=0,
        padx=15,
        pady=5,
        cursor='hand2',
        command=getText
    )
    hash_button.pack(pady=10)


    window.mainloop()


frame = tk.Frame(master, bg='white', bd=2, relief='ridge')
frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=250)


title_label = tk.Label(frame, text='Hash Text Tool', font=('Segoe UI', 20, 'bold'), bg='white', fg='#2f3640')
title_label.pack(pady=(20, 10))


hash_btn = tk.Button(frame, text='🔐 Hash Text', font=('Segoe UI', 14), bg='#00a8ff', fg='white', bd=0, padx=10, pady=5, cursor='hand2', activebackground='#0097e6', command=hash)
hash_btn.pack(pady=10)


check_btn = tk.Button(frame, text='✔️ Check Hashed Text', font=('Segoe UI', 14), bg='#4cd137', fg='white', bd=0, padx=10, pady=5, cursor='hand2', activebackground='#44bd32', command=checkHash)
check_btn.pack(pady=10)


master.mainloop()





