# DataFile = open("D:\Tracks\Python 1\Day 10\Source.txt", "r")

# print(DataFile.read())


# file = open("D:\Tracks\Python 1\Day 10\myfile.py", "x")

# file1 = open("D:\Tracks\Python 1\Day 10\myfile.txt", "x")


# with open("d:/Tracks/Python 1/Day 10/myfile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")


# with open("d:/Tracks/Python 1/Day 10/myfile.txt", "a") as f:
#   f.write("Hi My NAMe Is Abdallah")


# f = open("Source.txt", 'r')
# print(f.read())



# DataFile = open("D:\Tracks\Python 1\Day 8\Source.txt", "r")

# print(DataFile.read())





# import json  


# with open("D:\Tracks\Python 1\Day 10\StudentData.json", "r") as StudentData:
#     data = json.load(StudentData)


# data['student'][0]['grads']['english'] = 0

# print(data['student'][0]['grads']['english'])



# import json


# with open("D:/Tracks/Python 1/Day 10/Users.json" , "r") as Users :
#     DataUsers = json.load(Users)


# username = input('Username : ')
# password = input('Password : ')


# if username in DataUsers:
#     if password == DataUsers[username]['password']:
#         print('login Done')
#     else :
#         print('Wrong Password')
# else :
#     print('Username Not Found')



# import json 

# with open("D:/Tracks/Python 1/Day 10/Users.json" , "r") as Users :
#     DataUsers = json.load(Users)


# newUser = []
# for user in DataUsers:
#     if user['username'] != 'abdallah':
#         newUser.append(user)


# with open("D:/Tracks/Python 1/Day 10/Users.json", 'w') as AfterDeleteUser :
#     json.dump(newUser, AfterDeleteUser, indent=4)
    



# import json 

# with open("D:/Tracks/Python 1/Day 10/Users.json" , "r") as Users :
#     DataUsers = json.load(Users)



# DataUsers.append({"username": "ehab","password": "12345678911"})

# with open("D:/Tracks/Python 1/Day 10/Users.json", 'w') as AfterDeleteUser :
#     json.dump(DataUsers, AfterDeleteUser, indent=4)




# import json 

# with open("D:/Tracks/Python 1/Day 10/Users.json" , "r") as Users :
#     DataUsers = json.load(Users)


# DataUsers[2]['password'] = 'ehab'


# with open("D:/Tracks/Python 1/Day 10/Users.json", 'w') as AfterDeleteUser :
#     json.dump(DataUsers, AfterDeleteUser, indent=4)



# import json 

# with open("D:/Tracks/Python 1/Day 10/Users.json" , "r") as Users :
#     DataUsers = json.load(Users)


# print('======Register=======')

# username = input('Please Enter Username : ')
# password = input('Please Enter Password : ')
# check = False

# for user in DataUsers :
#     if user['username'] == username:
#         print('Username Is Found')
#         check = True
#         break

# if check :
#     print('Try')
# elif len(password) < 8 :
#     print('low Password')
# else :
#     DataUsers.append({'username' : username, "password" : password})
#     with open("D:/Tracks/Python 1/Day 10/Users.json", 'w') as AfterDeleteUser :
#         json.dump(DataUsers, AfterDeleteUser, indent=4)
#     print('Register Done')