numbers = [20,6,18,19,7,5,2,16,15,10,4,3,14,1,13,17,8,9,11,12]

List_1 = []
check = numbers[0]
for i in range(0, len(numbers)) :
    for u in range(0, len(numbers)):
        if check > numbers[u]:
            List_1.append(numbers[u])