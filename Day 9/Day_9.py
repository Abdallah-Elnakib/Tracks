# lambda
# filter
# map
# recursion
# *******************************************************************************

# import tkinter as tk


# window = tk.Tk()
# window.title("Login")

# window.maxsize(500,200)
# window.minsize(500,200)

# label = tk.Label(window, text="Username")
# label.pack()
# entry = tk.Entry(window)
# entry.pack()
# label2 = tk.Label(window, text="Password")
# label2.pack()
# entry2 = tk.Entry(window)
# entry2.pack()
# button = tk.Button(window, text="Login", command=lambda: print('Login Done'))
# button.pack()  

# window.mainloop()





# x = [1,2,34,56,78,9] 

# for i in range(0,len(x)):
#     x[i] = x[i] * 2

# print(x)


# map
# x = [1,2,34,56,78,9] -> * 2 -> [2,4,68,112,156,18]


# filter
# x = [1,2,34,56,78,9] -> >= 34 -> False False True True True False ->list([34,56,78])

# numbers = [1,2,3,4,5,6,7,8,9,10] 


# def test(n):
#     if n % 2 == 0:
#         return True
#     else :
#         False


# x = filter(test, numbers)

# print(list(x))



# x  = filter(lambda n : n % 2 == 0,numbers)
# print(list(x))

# def test(n):
#     print(n)


# x = lambda n : print(n)


# test(10)

# x(10)



# def test(x) :
#     if x % 2 == 0:
#         return True
#     else :
#         return False
# print(test(9))


# test = lambda x : x % 2 == 0
# print(test(9))





# numbers = [1,2,3,4,5,6,7,8,9,10]

# x = []
# for i in numbers :
#     if i % 2 == 0:
#         x.append(i)


# print(x)


# def cond(n):
#     if n % 2 == 0:
#         return True
#     else :
#         return False
    
# numbers = [1,2,3,4,5,6,7,8,9,10]
# x = filter(cond,numbers)
# print(list(x))



# numbers = [1,2,3,4,5,6,7,8,9,10]
# x = filter(lambda n : n % 2 == 0,numbers)
# print(list(x))


# y = filter(lambda u : u % 2 != 0 , numbers)
# print(list(y))


# print(numbers)


# if list(filter(lambda u : u % 2 != 0 , numbers))[1] == 3 :
#     print('Yes')


# numbers = [1,2,3,6]
# x = []

# for i in range(0, len(numbers)):
#     x.append(numbers[i]**2)

# print(x)

# x = map(lambda n : n**2, numbers)
# print(list(x))
# print(numbers)


data = {
    'abdallah' : {
                    'username' : 'abdallah', 
                    'password' : '123456789', 
                    'Grade' : [100,30,60,90,4,70]
                }   
}

# for i in range(0, len(data['abdallah']['Grade'])) :
#     if data['abdallah']['Grade'][i] < 50 :
#         data['abdallah']['Grade'][i] += 10


# indexes_to_update = -1
# grades_to_increment = {}
# def get(x):
#     global indexes_to_update
#     if x < 50:
#         indexes_to_update += 1
#         grades_to_increment[str(indexes_to_update)] = x
#         return True
#     else :
#         indexes_to_update += 1
#         return False
    
# y = list(filter(get, data['abdallah']['Grade']))
# value = list(grades_to_increment.values())
# key = list(grades_to_increment.keys())
# add = list(map(lambda number : number + 10, value))
# final = dict(zip(key,add))


# for i in list(final.keys()):
#     data['abdallah']['Grade'][int(i)] = final[i]


# print(data)





# data['abdallah']['Grade'] = list(map(lambda grade : grade + 10 if grade < 50 else grade, data['abdallah']['Grade']))


# print(data)


# Grade = 100
# if Grade == 80:
#     print('yes')
# else :
#     print('No')


# print('yes') if Grade == 80 else print('No')


# def test():
    
#     x = 10
#     return x

# u = test()
# print(u)



# def test_1(number):

#     number_After_Add = test_2(number) # -> 100

#     if number_After_Add == 100: 
#         return number_After_Add
#     else :
#         return test_1(number_After_Add)
    


# def test_2(x):
#     x += 1
#     return x 


# data = test_1(10)
# print(data)



text = 'wwwwoooollllddddddddddddd' # -> wold


# def clearText(wold) :

#     if len(wold) == 1:
#         return wold

#     elif wold[0] == wold[1]: 
#         return clearText(wold[1:])
    
#     else :
#         return wold[0] + clearText(wold[1:])


# print(clearText(text))


def sumOfTwoNumbers(Number_1,Number_2):

    return Number_1 + Number_2