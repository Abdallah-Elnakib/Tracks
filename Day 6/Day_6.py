# while True:
#     x = input('Enter number : ')
#     if x  == '10':
#         print('Exiting...')

# x = ['abdallah', 'elnakib', 'ahmed']

# for ahmed in range(0,3):
#     print(x[ahmed])

# x = ['abdallah']

# for i in range(0,3):
#     print(x[i])

# for i in range(0,len(x)):
#     print(x[i])


# for i in range(10):
#     print(i)


# for i in range(1,21,2):
#     print(i)



# i = 1
# while i < 21:
#     print(i)
#     i += 2



# while True:
#     y = '9'
#     x = input('Enter number (1, 10) : ')
#     if y == x :
#         print('You Win...')
#         break
   

# for i in range(1,11):
#     y = '9'
#     x = input('Enter number (1, 10) : ')
#     if y == x :
#         print('You Win...')
#         break


# x = ['abdallah', 'elnakib', 'ahmed']

# for i in range(len(x) - 1, -1 , -1):
#     print(x[i])


# for i in range(10, -1, -1):
#     print(i)



# users = ["abdallah", "ahmed", "ali"]
# emailList = ["abdallah@gmail.com", "ahmed@gmail.com", "ali@gmail.com"]
# data = {
#     'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : 1234},
#     'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : 1234},
#     'ali' : {'username' : 'ali', 'age' : 23, 'email' : 'ahmed@gmail.com', 'password' : 15988963}
# }

# for check in range(0, 5):
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





# while True:
#     username = input('Enter username : ').lower()
#     if username not in users :
#         print('User Not Found :( ')
#         continue
#     for check in range(1, 6):
#         password = input('Enter Your Password : ')
#         if password == data[username]['password'] :
#             print('Login Done :) ')
#             break
#         else :
#             print(f'Wrong Password, Try Again {5 - check} times left')
            
#     break


# x = [1,6,9,87,4]

# total = 0

# for i in range(0,len(x)):
#     total += x[i]


# print(total)


# x = [1,7,9,87,4,4,8]

# for i in range(1,len(x)):
#     x[0] += x[1] 
#     x.pop(1)

# print(x)

# cou = 0
# for i in range(1,11):
#     for u in range(1,11):
#         for t in range(1,11):
#             cou += 1
    
# print(cou)


# password  = '[][][][][][][][]'




# 10000
cou = 0

# for i in range(0,10):
#     for u in range(0,10):
#         for t in range(0,10):
#             for r in range(0,10):
#                 for p in range(0,10):
#                     for z in range(0,10):
#                         for c in range(0,10):
#                             for v in range(0,10):
#                                 cou += 1
#                                 if data['ali']['password'] == int(f'{i}{u}{t}{r}{p}{z}{c}{v}'):
#                                     print('Found Password :', f'{i}{u}{t}{r}{p}{z}{c}{v}', 'after', cou, 'attempts')
#                                     break




# x = [5,8,10]

# y = 3

# if y in x :
#     print('Yes')

# check = 0
# while check < len(x):
#     print(x[check])
#     check += 1



# x = [[1,6,9],8,10]


# for i in x:
#     print(i)

# x = [[1,3,6],[4,5,8],[7,9,5],[1,6,9]]

# for i in x:
#     for u in i:
#         print(u)

# x = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,14]]]

# for i in x:
#     for u in i:
#         for t in u:
#             print(t)


# data = {'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : '!Bdall8h'},
#         'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : 222}
#     }


# for i in data:
#     print(data[i]['password'])



# password = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','#','$','%','&','*','(',')','_','+','-','=','{','}','[',']','|','\\',':',';','<','>','?','/',' ','~','`','��','¿']
# cou = 0
# for i in password:
#     for u in password:
#         for t in password:
#             for r in password:
#                 for p in password:
#                     for z in password:
#                         for c in password:
#                             for v in password:
#                                 cou += 1
#                                 if data['abdallah']['password'] == f'{i}{u}{t}{r}{p}{z}{c}{v}':
#                                     print('Found Password :', f'{i}{u}{t}{r}{p}{z}{c}{v}', 'after', cou, 'attempts')
#                                     break




# x = [1,3,6,9]

# for i in x:
#     print(i)


# i = 0
# while i < len(x):
#     print(x[i])
#     i += 1

# for i in range(0,len(x)):
#     print(x[i])


# x  =  input('Enter Your Email : ') -> 'my name is abdallah'  ['m', 'y',' ' ,'n', 'a','m', 'e',' ', 'i','s',' ', 'a', 'b', 'd', 'a', 'l', 'l', 'a','h']

# for i in x:
#     if i == '@':
#         print('Email is Valid')
#         break


# -> 'abdallah@gmail.com' ->  ['a', 'b', 'd', 'a', 'l', 'l', 'a', 'h', '@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o','m']

# x  =  input('Enter Your Email : ')

# check = ''

# for i in x:
#     if check != '':
#         check += i

#     if i == '@':
#         check += i



# if check == '@gmail.com':
#     print('Email is Valid')
# else :
#     print('Email is Not Valid')




# while True :
#     x = input('Message : ').lower()
#     if x == 'good bye':
#         break

# import random
# message = {
#     'hi' : ['hi', 'hello', 'hey', 'welcome'],
#     'how are you' : ['i am fine', 'good', 'great', 'okay'],
#     'bye' : ['bye', 'goodbye', 'see you later', 'have a nice day'],
#     'thank you' : ['thank you', 'thanks', 'no problem'],
#     'can you help me' : ['of course', 'yes', 'sure', 'i can help'],
#     'what is your name' : ['my name is boot', 'i am a boot', 'i am called bopt'],
# }
# username = ''
# age = ''


# while True:
#     user_input = input('You : ').lower()
#     for i in message:
#         if user_input == i:
#             print('Bot :', random.choice(message[i]))
#         elif user_input == 'bye':
#             print('Bot :', random.choice(message['bye']))
#             break
#         continue
    


#while True:

    # user_input = input('You : ').lower()
    # if user_input == 'hi':
    #     print('Boot :', random.choice(message['hi']))
    # elif user_input == 'how are you':
    #     print('Boot :', random.choice(message['how are you']))
    # elif user_input == 'bye':
    #     print('Boot :', random.choice(message['bye']))
    #     break
    # elif user_input == 'thank you':
    #     print('Boot :', random.choice(message['thank you']))
    # elif user_input == 'can you help me':
    #     print('Boot :', random.choice(message['can you help me']))
    # elif user_input == 'what is your name':
    #     print('Boot :', random.choice(message['what is your name']))
    # elif user_input == 'what is my name':
    #     if username == '':
    #         print('Boot :', "I don't no :(")
    #         name = input('can you tell me your name? : ')
    #         print('Boot :', f'Nice to meet you {name}!')
    #         username = name
    #     else :
    #         print('Boot :', f'Your name is {username}!')
    # elif user_input == 'what is my age':
    #     if age == '':
    #         print('Boot :', "I don't no :(")
    #         userage = input('can you tell me your age? : ')
    #         print('Boot :', f'Now i know youe age is {userage}!')
    #         age = userage
    #     else :
    #         print('Boot :', f'Your age is {age}!')
    # else :
    #     print('Boot :', 'I didn\'t understand that, can you please try again?')