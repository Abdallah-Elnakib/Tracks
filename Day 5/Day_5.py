# data = input('-> : ')
# '50+90*10'
# numbers = []
# ops = []

# op = ['+','-','/','*']
# nums = ['1','2','3','4','5','6','7','8','9','0']

# check = 0
# x = ''

# while check < len(data) :
#     if data[check] in op:
#         ops.append(data[check])
#         numbers.append(x)
#         x = '' 
#     elif data[check] in nums :
#         x += data[check]
#     else :
#         print('Error')
#         break

#     check += 1

# if x != '':
#     numbers.append(x)


# res = float(numbers[0])

# check = 0

# while check < len(ops) :
#     if ops[check] == '+':
#         res += float(numbers[check + 1])
#     elif ops[check] == '-':
#         res -= float(numbers[check + 1])
#     elif ops[check] == '*':
#         res *= float(numbers[check + 1])
#     elif ops[check] == '/':
#         res /= float(numbers[check + 1])
        
#     check += 1


# print(f'RES -> : {res}')

import random

bourd = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
        ]

numbers = ['1','2','3','4','5','6','7','8','9']
check = 0
checkWinX = False
checkWinO = False

while True:
    if checkWinO == True:
        break
    
    print(f'[ {bourd[0][0]} ] [ {bourd[0][1]} ] [ {bourd[0][2]} ]')
    print(f'[ {bourd[1][0]} ] [ {bourd[1][1]} ] [ {bourd[1][2]} ]')
    print(f'[ {bourd[2][0]} ] [ {bourd[2][1]} ] [ {bourd[2][2]} ]')

    playUser = input('-> : ') # 1,2,3,4,5,6,7,8,9


    if playUser == '1' or playUser == '2' or playUser == '3':
        if bourd[0][int(playUser) - 1] in numbers:
            bourd[0][int(playUser) - 1] = 'X'
            check += 1
        else :
            print('Wrong Number :( ')
            continue

    elif playUser == '4' or playUser == '5' or playUser == '6':
        if bourd[1][int(playUser) - 4] in numbers:
            bourd[1][int(playUser) - 4] = 'X'
            check += 1
        else :
            print('Wrong Number :( ')
            continue

    elif playUser == '7' or playUser == '8' or playUser == '9':
        if bourd[2][int(playUser) - 7] in numbers :
            bourd[2][int(playUser) - 7] = 'X'
            check += 1
        else :
            print('Wrong Number :( ')
            continue

    else :
        print('Error')

    testUser = 0
    while testUser < len(bourd) :
        if bourd[testUser][0] == 'X' and bourd[testUser][1] == 'X' and bourd[testUser][2] == 'X':
            print('Player X Is Win')
            checkWinX = True
            break
        elif bourd[0][testUser] == 'X' and bourd[1][testUser] == 'X' and bourd[2][testUser] == 'X':
            print('Player X Is Win')
            checkWinX = True
            break

        testUser += 1


    if check == 9:
        print('Game Over :) ')
        break

    if checkWinX == True:
        break

    while True :
        pcPlay = [random.randint(0,2),random.randint(0,2)]

        if bourd[pcPlay[0]][pcPlay[1]] in numbers :
            bourd[pcPlay[0]][pcPlay[1]] = 'O'
            check += 1
            break
    
    testPc = 0
    while testPc < len(bourd) :
        if bourd[testPc][0] == 'O' and bourd[testPc][1] == 'O' and bourd[testPc][2] == 'O':
            print('Player O Is Win')
            checkWinO = True
            break

        elif bourd[0][testPc] == 'O' and bourd[1][testPc] == 'O' and bourd[2][testPc] == 'O':
            print('Player O Is Win')
            checkWinO = True
            break

        testPc +=1
        
    