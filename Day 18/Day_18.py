# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.

# def sum(num1, num2):
#     if num1 * num2 > 1000 :
#         print(num1 + num2)
#     else :
#         print(num1 * num2)

# sum(100,20)



# Exercise 2: Print the following pattern
# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# for i in range(1,6): 
#     for u in range(1, i + 1):
#         print(u, end=" ")
#     print('') 



# Exercise 3: Calculate sum of all numbers from 1 to a given number
# Write a Python program to accept a number from a user and calculate the sum of all numbers 
# from 1 to a given number

# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)




# number = int(input('Please Enter Number : '))

# total = 0
# for i in range(1, number + 1):
#     total += i

# print(total)



numbers = [12, 75, 150, 180, 145, 525, 50]

# Exercise 5: Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions

# If the number is greater than 500, then stop the loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number




# for i in numbers :
#     if i > 500 :
#         break
#     elif i == 150:
#         continue
#     elif i % 5 == 0 :
#         print(i)
    
# **********************************************************************



# Exercise 9: Find the largest item from list
# Given:

# x = [4, 6, 8, 24, 12, 2, 5, 8, 24, 24,25,25]

# res = x[0] 
# con = 2

# for i in x : 
#     if i > res:
#         res = i
#         con = 1
#     elif i == res:
#         con += 1
    

# con = x.count(res)
# for i in x :
#     if res == i:
#         con += 1

# print(res, con)


# ================================================================



import bcrypt
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = mysql.connector.connect(
    host = os.getenv('HOST'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
    database = os.getenv('DATABASE')
)


DB = DATABASE.cursor()


# username = input('USERNAME : ')
# password = input('password : ')  
# confirm = input('confirm : ')


# sql = "SELECT * FROM users WHERE username = %s"
# val = (username,)
# DB.execute(sql,val)
# user = DB.fetchone()  

# if user == None :
#     if len(password) >= 8:
#         if password == confirm :
#             passowrdAfterUTF = password.encode('utf-8')
#             salt = bcrypt.gensalt()
#             hash = bcrypt.hashpw(passowrdAfterUTF,salt)
#             sql = 'INSERT INTO users (username, password, role) VALUES (%s, %s, %s)'
#             val = (username,hash,'user')
#             DB.execute(sql,val)
#             DATABASE.commit()
#         else :
#             print('password != confirm')
#     else :
#         print('Low Password')
# else :
#     print('This Username is Found')
# python -m pip install bcrypt
# py -m pip install bcrypt

# username = input('USERNAME : ')
# password = input('password : ')  # str


# sql = "SELECT * FROM users WHERE username = %s"
# val = (username,)
# DB.execute(sql,val)
# user = DB.fetchone()  # ['abdallah','$2b$12$DoP17th.zO1RzmXOCiy8d.dWEzSQ5m3OEZXwTWxRtyuFYTzHklqiS','user']


# if user != None:
#     passwordFromUser = password.encode('utf-8')
#     passwordFromDB = user[1].encode('utf-8')
#     res = bcrypt.checkpw(passwordFromUser,passwordFromDB) 
#     if res == True:
#         print('Login Done')
#     else :
#         print('Wrong Password')
# else :
#     print('Wrong Username')



# hash_1 = {
#     'a' : '/qws*/',
#     'b' : '/oijm*/',
#     'd' : '/ew#vc/',
#     'l' : '/tr$5r/',
#     'h' : '/ya7nc*2/'
# }



# def hash(text):
#     res = ''
#     for i in text:
#         if i == 'a' :
#             res += hash_1['a']
#         elif i == 'b' :
#             res += hash_1['b']
#         elif i == 'd' :
#             res += hash_1['d']
#         elif i == 'l' :
#             res += hash_1['l']
#         elif i == 'h' :
#             res += hash_1['h']

#     return res



# print(hash('abdallah'))


# def CheckHash(text):
#     res = ''
#     textCut = []
#     x = text.split('/')
#     for i in x :
#         if i == '':
#             continue
#         else :
#             textCut.append(f'/{i}/')
    
#     for u in textCut :
#         if u == '/qws*/' :
#             res += list(hash_1.keys())[0]
#         elif u == '/oijm*/':
#             res += list(hash_1.keys())[1]
#         elif u == '/ew#vc/':
#             res += list(hash_1.keys())[2]
#         elif u == '/tr$5r/':
#             res += list(hash_1.keys())[3]
#         elif u == '/ya7nc*2/':
#             res += list(hash_1.keys())[4]

#     return res

# print(CheckHash('/qws*//oijm*//ew#vc//qws*//tr$5r//tr$5r//qws*//ya7nc*2/'))



numbers = [20,6,18,19,7,5,2,16,15,10,4,3,14,1,13,17,8,9,11,12] # -> [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# list_1 = []
# while numbers: 
#     ckeck = numbers[0]  
#     for num in numbers:
#         if num < ckeck:
#             ckeck = num
#     list_1.append(ckeck)
#     numbers.remove(ckeck)

# print(list_1)


def result(data) :
    