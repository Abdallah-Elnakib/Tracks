# name = input("Enter your name: ")

# def input_name():
#     name = input("Enter your name: ")




# input_name()
# print()
# input()
# pop()


# def printMyName():
#     print("My name is Abdallah")


# print(555)
# printMyName()


# def userInput():
#     number_1 = int(input("Enter the first number: "))
#     number_2 = int(input("Enter the second number: "))
#     op = input("Enter the operator (+, -, *, /): ")




# while True :
#     print('====== Calculator Menu =======')
#     userInput()


# print(x)


# while True:
#     print(x)


# def test():
#     x = 5

# x = 10


# print(x)


# print(x)


# x = 5

# def test():
#     print(x)


# test()

# print(x)


# def printMyName():
#     print("My name is Abdallah")



# def userInput():
#     number_1 = int(input("Enter the first number: "))
#     number_2 = int(input("Enter the second number: "))
#     op = input("Enter the operator (+, -, *, /): ")

#     return [number_1,number_2,op]


# def exit():
#     q = input('Do You Want To Exit ? : ').lower()

#     if q == 'no' :
#         return q
    
#     elif q == 'yes' :
#         return q
    
#     else :
#         print('Error')
#         exit()



# while True :
#     print('====== Calculator Menu =======')
#     data = userInput()

#     if data[2] == '+':
#         print(data[0] + data[1])
#     elif data[2] == '-':
#         print(data[0] - data[1])
#     elif data[2] == '*':
#         print(data[0] * data[1])
#     elif data[2] == '/':
#         print(data[0] / data[1])
#     else :
#         print('Error')

#     check = exit()

#     if check == 'no':
#         continue
#     else :
#         print('Good Bye :)')
#         break



# def test():
#     res = 5 + 10

#     if res == 15:
#         return
    
#     print(5555555)


# test()

# print(test())



# while True:
#     number = int(input('Enter Number : '))
#     if number == 10:
#         break
#     else :
#         print('Error') 


# def testNumber():
#     number = int(input('Enter Number : '))
#     if number == 10:
#         return 'abdallah' 
#     else :
#         print('Error')
#         testNumber()


# data =  testNumber()




# x = [1,7,9,87,4,4,8]

# for i in range(1,len(x)):
#     x[0] += x[1] 
#     x.pop(1)


# x = [1,7,9,87,4,4,8]


# def sumOfArray():
#     if len(x) == 1:
#         return x
#     else :
#         x[0] += x[1] 
#         x.pop(1)
#         return sumOfArray()


# return -> 120    
#       return -> 120
#           return -> 120
#               return -> 120

# print(sumOfArray())







# def name(username):
#     print(f'My name is {username}')


# # name('abdallah')
# # name('Ali')
# # name('mohamed')
# # name('ibrahem')

# x = input('Enter Your name : ')
# name(x)


# def data(data) :
#     print(data['name'])


# data({'name' : 'abdallah', "age" : 27})


# def userData(name,age,phone,password):

#     print(name,age,phone,password)


# userData('abdallah',27,'011258963','123456')



# def sum(x):
#     for i in range(1,len(x)):
#         x[0] += x[1] 
#         x.pop(1)

#     return x


# print(sum([1,2,5,9,8,7]))
# print(sum([1,8,7,9,1,75]))
# print(sum([3,2,4,9,8,8]))
# print(sum([3,8,66,8,88,75]))




# print()


# def test(*numbers):
#     print(numbers[1])


# test(1,"abdallah")


# data = {
#     'abdallah' : {'username' :"abdallah", 'age' : 27, 'phone' : "01258996312"}
# }



# def userdata():
#     username = input('Enter Username : ')
#     age = input('Enter Your Age : ')
#     phone = input('Enter Your Phone : ')

#     return [username,age,phone]

# def addUserIndataBase(dataUser):
#     data[dataUser[0]] ={'username' : dataUser[0], 'age' :  dataUser[1], "phone" : dataUser[2]}
#     print('Register Done')

# def checkUsername():
#     gitDataFromUser = userdata()

#     if gitDataFromUser[0] in data :
#         print('This Username is used ')
#     else :
#         addUserIndataBase(gitDataFromUser)


# def interface():
#     while True :
#         print('===== Register ========')
#         checkUsername()

#         q = input('Do you want to exit ? : ')
#         if q == 'yes':
#             print('Good Bye :)')
#             break
#         elif q == 'no':
#             continue
#         else :
#             print('Error')
#             break

# interface()


# انشئ مودل ذكاء صباعي يقوم بأزاله جميع الحروفق المكرره في كلمه معينه مع العلم من التأكد انا المستخدم يكتب كلمه واحده للذكاء الصناعي


