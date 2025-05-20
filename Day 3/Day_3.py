# vars => str int bool float list dic tuble range
# x = [1,9]

# data = {
#     'name' : 'abdallah',
#     'age' : 27,
#     'phone' : {'num1' : 123, 'num2' : 5987}
# }

# # data['name'] = 'ahmed'

# # data['phone'] = '0120259874'

# # data.pop('name')
# # print(data)

# print(data['phone']['num2'])


# x = True
# y = False


# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# x = False

# name = input('Enter Your Name : ')

# if name == 'abdallah' :
#     x = True


# if x :
#     print('Hello Abdallah')

# x = ''
# y = 0

# t = ' '
# u = 55
# r = 'hgg'


# x = [1,9,87,4]

# name = 'ahmed'

# y = (1,8,'abdallah', True, [1,9,7], name)

# print(y[5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# x =  (1,9,8)
# y = list(x)
# y[0] = 5
# z = tuple(y)
# print(z)

# x = (1,9,8)

# y = list(x)

# y.append(7)

# z = tuple(y)

# print(z)


# x = ("abdallah", "ahmed", "ali")

# y = ('ali',)

# x -= y


# print(x)

# x = [1,9,8]

# x.append(2)



# index fun

# x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5,3]

# print(x.index(3))


# count fun
# x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]

# print(x.count(3))
# print('abdallah' == 'abdallah ')

# Username = input('Enter Your Username : ').lower()

# print(Username)

# x = 'Abdallah'.lower()

# print(x)


# Username = input('1. Swimming, 2. Climbing, 3. Horseback riding, 4. Cycling. : ')


# x = Username.split(' , ')

# print(x)


# x =  'hello my name is abdallah'

# print(x.find('my'))


# x = ['a','d','c','g']
# y = [1,5,9,8]

# z = dict(zip(x,y))

# print(z)


# zip()
# index()
# find()
# count()
# split()
# lower()


# list()
# dict()
# int()
# str()
# float()
# tuple()


# print(55)

# x = 10

# if x == 5:
#     print('yes')


# name = input('Enter Your Name : ').lower()

# if name == 'abdallah':
#     print('hello Abdallah :) ')

# elif name == 'ahmed':
#     print('hello Ahmed :) ')

# elif name == 'ali' :
#     print('hello Ali :) ')

# else :
#     print(f'Hello {name}')


# > < >= <=

# number = int(input('Enter Number : '))

# if number >= 10 :
#     print(f'This Number {number} >= 10')

# elif number <= 0 :
#     print(f'This Number {number} < or = 0')

# else : 
#     print('Error :(')

# == > < >= <=


# data = {
#     'username' : 'abdallah',
#     'password' : '123456',
#     'email' : 'abdallah@gmail.com'
# }

# username = input('Username : ')
# password = input('Password : ')
# email = input('Email : ')

# if username == data['username']:
#     if password == data['password']:
#         if email == data['email']:
#             print('Login Done :)')
#         else : 
#             print('Wrong Email :(')
#     else : 
#         print('Wrong Passwrd :(')
# else : 
#     print('Wrong Username :(')


# == > < >= <= and


# اطلب من الطالب كتابه الدرجه الخاصه به 
# في حاله كانت اكبر من 
# 85 => A
# من 
# 75 : 85 
# اطبع له 
# B
# من 
# 65 : 74 
# اطبع له 
# C
# غير ذالك اطبع له راسب


# d = int(input('D : '))

# if d > 85 : 
#     print('A')
# elif d >= 75 and d <= 85:
#     print('B')
# elif d >= 65 and d <= 74 :
#     print('C')
# else : 
#     print('Faild')




# == > < >= <= and 

# x = 1
# y = 10

# if (x == 1 and y == 10) or (x == 30 and y == 1):
#     print('Yes')

# in  - not in

# x = [10,3,6,9,8,7]

# y = 1

# if y not in x:
#     print('Yes')

# users = ['abdallah', 'ahmed', 'ali']
# emailList = ['abdallah@gmail.com','ahmed@gmail.com','ali@gmail.com']

# data = {
#     'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : '123456789'},
#     'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : '123456789'},
#     'ali' : {'username' : 'ali', 'age' : 23, 'email' : 'ahmed@gmail.com', 'password' : '123456789'}
# }




# print('============Register============')
# username = input('Enter username : ').lower()
# age = int(input('Enter Your Age : '))
# email = input('Enter Your E-Mail : ')
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


# print('============LOGIN============')
# username = input('Enter username : ').lower()
# password = input('Enter Your Password : ')
# print('=================================')

# if username in users :
#     if username == data[username]['username']:
#         if password == data[username]['password'] :
#             print('Login Done :) ')
#         else :
#             print('Wrong Password :( ')
#     else :
#         print('Wrong Username :( ')
# else : 
#     print('User Not Found :( ')



