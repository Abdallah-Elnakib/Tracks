# if > elif > else:

# == !=  > < => <= and or

# x = 5
# y = 10

# if x == 5 :
#     print('x')

# elif y == 10 :
#     print('y')


# users = ["abdallah", "ahmed", "ali"]
# emailList = ["abdallah@gmail.com", "ahmed@gmail.com", "ali@gmail.com"]

# data = {
#     "abdallah": {
#         "username": "abdallah",
#         "age": 27,
#         "email": "abdallah@gmail.com",
#         "password": "123456789",
#     },
#     "ahmed": {
#         "username": "ahmed",
#         "age": 28,
#         "email": "ahmed@gmail.com",
#         "password": "123456789",
#     },
#     "ali": {
#         "username": "ali",
#         "age": 23,
#         "email": "ahmed@gmail.com",
#         "password": "123456789",
#     },
# }


# print('============Register============')
# username = input('Enter username : ').lower()
# age = int(input('Enter Your Age : '))
# email = input('Enter Your E-Mail : ').lower()
# password = input('Enter Your Password : ')
# confirmPass = input('Confirm Password : ')
# print('=================================')

# if username not in users :
#     if email not in emailList :
#         if len(password) >= 8 :
#             if password == confirmPass:
#                 data[username] = {'username' : username, 'age' : age, 'email' : email, 'password' : password}
#                 users.append(username)
#                 emailList.append(email)
#                 print('Register Done :) ')
#                 print(data)
#             else :
#                 print('!=')
#         else :
#             print('Low Password :( ')
#     else :
#         print('This Emali Is Userd :( ')
# else :
#     print('usernmae Is found :( ')


# z = email.split('@') # -> ['abdallah']
# print(z)

# if len(z) <= 1 :
#     print('Error')

# elif z[1] != "gmail.com" and z[1] != 'yahoo':
#     print('Error')

# else :
#     print('Done')


# day = 10

# if day == 1:
#     print("Saturday")
# elif day == 2 :
#     print("Sunday")
# elif day == 3:
#     print("Monday")
# elif day == 4:
#     print("Tuesday")
# elif day == 5:
#     print("Wednesday")
# elif day == 6:
#     print("Thursday")
# elif day == 7:
#     print("Friday")
# else :
#     print('Error')

# x = 2


# match x:
#     case 1  :
#         print("Saturday")
#     case 2 :
#         print("Sunday")
#     case 3 :
#         print("Monday")
#     case 4 :
#         print("Tuesday")
#     case 5 :
#         print("Wednesday")
#     case 6 :
#         print("Thursday")
#     case 7 :
#         print("Friday")
#     case _ :
#         print('Error')


# month = 5
# day = 4
# match day:
#     case 1  if month == 4:
#         print("A Saturday in April")
#     case 2 if match == 4:
#         print("A Sunday in April")


# print(int(11/2))

# print(11/2)


# loops

# print('Hello')

# for loop
# while loop


# x = 0

# while True:
#     print(x)
#     x += 1
#     if x == 100:
#         break

# data = {
#     'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : '123456789'},
#     'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : '123456789'},
#     'ali' : {'username' : 'ali', 'age' : 23, 'email' : 'ahmed@gmail.com', 'password' : '123456789'}
# }
# check = 0

# while check < 5:
#     username = input('Enter username : ').lower()
#     password = input('Enter Your Password : ')

#     if username in users :
#         if username == data[username]['username']:
#             if password == data[username]['password'] :
#                 print('Login Done :) ')
#                 break
#             else :
#                 print('Wrong Password :( ')
#         else :
#             print('Wrong Username :( ')
#     else :
#         print('User Not Found :( ')

#     check += 1


# x = [1,2,6,5,8,5,5]

# check = 0

# while check < len(x):
#     print(x[check])
#     check += 1


# اطلب من المتخدم الرقم الاول
# نوع العمليه
# الرقم الثاني
# اطبع نتيجه العمليه حسب اختيار المستخدم
# بعد ذالك اسأل المستخدم هل تريد التكمله
# في حاله كانت الاجابه نعم
# اعد الاسأله
# في حاله كانت الاجابه لا
# اطبع رساله شكرا واغلق البرنامج


# while True:
#     num1 = float(input("Number 1 : "))
#     Op = input("Op (* , - / , +) : ")
#     num2 = float(input("Number 2 : "))

#     if Op == "+":
#         print(num1 + num2)
#     elif Op == "-":
#         print(num1 - num2)
#     elif Op == "*":
#         print(num1 * num2)
#     elif Op == "/":
#         print(num1 / num2)
#     else:
#         print("Error")

#     q = input("Yes Or No : ").lower()
#     if q == "no":
#         print("Thank You :) ")
#         break





#=================================================================================

# Write a supermarket management program.
# There is a database containing the following: the name of each product, 
# the quantity available in the warehouse, whether it is on sale, 
# the product's price, and the product's section.
# The program displays the product name, the price per item, 
# and a brief description. It displays all products in a simple and attractive way, 
# with each product having its own unique number.
# Then, the user is prompted to first select the product numbers they want to purchase. 
# After entering the numbers, a request appears, 
# specifying the required quantities for each product.
# Then, the purchase invoice displays the product name, 
# the price per item, the price per selected item, the quantity for each product, 
# and the total amount due. A discount is added to the product, 
# if applicable, and this is noted on the invoice. Example:
#
# ===============Welcome===============
# product 1 :
# Name -> milk
# Price -> 10$
# Description -> Fresh and healthy milk
# -----
# product 2 :
# Name -> Rice
# Price -> 20$
# Description -> Premium and pure rice
# -----
# product 3 :
# Name -> Bread
# Price -> 2$
# Description -> fresh bread
# =====================================
# Please write the numbers of the products you want to buy like this 1,2 : 1,3
# Please write the value of each product you want to purchase in order of your previous selection : 2,5
#
# ================Purchase Invoice================
# Product Name        Price per piece        Number of pieces        Total price
#
# milk                10$                    2                       20$
# Bread               2$                     5                       10$
#
# Total due before discount : 30$
# Total due after discount  : 25$


# product = {
#     "product 1" : {
#         'name' : 'Milk',
#         'price' : '10$',
#         'description' : 'Fresh and healthy milk',
#         'quantity' : 100,
#         'on_sale' : False
#     },
#     "product 2" : {
#         'name' : 'Rice',
#         'price' : '20$',
#         'description' : 'Premium and pure rice',
#         'quantity' : 50,
#         'on_sale' : True
#     },
#     "product 3" : {
#         'name' : 'Bread',
#         'price' : '2$',
#         'description' : 'Fresh bread',
#         'quantity' : 200,
#         'on_sale' : False
#     }
# }
# x = list(product.keys())
# check = 0
# print('===========Welcome===========')

# while check < len(x):
    
#     print(f'{x[check]} :')
#     print('Name ->', product[x[check]]['name'])
#     print('Price ->', product[x[check]]['price'])
#     print('Description ->', product[x[check]]['description'])
#     print('-----')
#     check += 1

# print('=====================================')




# while True:
#     break


# while True:
#     name  = input('Enter Your Name : ')
#     if name == 'abdallah':
#         break



# check = 1

# while check < 6 :
#     username  = input('Enter Your username : ')
#     password = input('Enter Your password : ')

#     if username == 'abdallah':
#         if password == '123456':
#             print('login Done')
#             break
#         else :
#             print(f"Wrong {5 - check}")
#             print('Wrong Password')
#             check += 1
#     else :
#         print('Wrong Username')

    
# while True:
#     print(555)



# while True:
#     x = input('enter number : ')
#     if x == 10:
#         break


# x = 0
# while x < 5:
#     x += 1




