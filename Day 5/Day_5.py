data = input('-> : ')

numbers = []
ops = []

op = ['+','-','/','*']
nums = ['1','2','3','4','5','6','7','8','9','0']

# data = 5+50-10

check = 0
x = ''

while check < len(data) :
    if data[check] in op:
        ops.append(data[check])
        numbers.append(x)
        x = '' 
    elif data[check] in nums :
        x += data[check]
    else :
        print('Error')
        break

    check += 1

if x != '':
    numbers.append(x)


# numbers = [50,10,9,8]
# ops = ['+','*','+']


# data = 50+10*9+8
res = float(numbers[0])
check = 0

while check < len(ops) :
    if ops[check] == '+':
        res += float(numbers[check + 1])
    elif ops[check] == '-':
        res -= float(numbers[check + 1])
    elif ops[check] == '*':
        res *= float(numbers[check + 1])
    elif ops[check] == '/':
        res /= float(numbers[check + 1])
        
    check += 1


print(f'RES -> : {res}')
