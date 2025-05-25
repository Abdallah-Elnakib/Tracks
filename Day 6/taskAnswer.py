product = {
    "product 1" : {
        'name' : 'Milk',
        'price' : '10',
        'description' : 'Fresh and healthy milk',
        'quantity' : 100,
        'on_sale' : False
    },
    "product 2" : {
        'name' : 'Rice',
        'price' : '20',
        'description' : 'Premium and pure rice',
        'quantity' : 50,
        'on_sale' : True
    },
    "product 3" : {
        'name' : 'Bread',
        'price' : '2',
        'description' : 'Fresh bread',
        'quantity' : 200,
        'on_sale' : False
    }
}

productNumber = ['1', '2', '3']
x = list(product.keys())
check = 0
print('===========Welcome===========')

while check < len(x):
    
    print(f'{x[check]} :')
    print('Name ->', product[x[check]]['name'])
    print('Price ->', f'{product[x[check]]['price']}$')
    print('Description ->', product[x[check]]['description'])
    print('-----')
    check += 1

print('=====================================')



while True:
    total = 0
    check = 0
    totalAfteron_sale = 0
    checkInput = False
    q1 = input('Please write the numbers of the products you want to buy like this 1,2 : ')
    q2 = input('Please write the value of each product you want to purchase in order of your previous selection : ')

    if q1 == 'esc' or q2 == 'esc':
        print('Thank you for shopping!')
        break

    q1 = q1.split(',')
    q2 = q2.split(',')
    final = list(zip(q1, q2))

    while check < len(q1):
        if q1[check] not in productNumber:
            print('Invalid product number!')
            checkInput = True
            break
        check += 1

    if checkInput:
        continue

    check = 0
    while check < len(final):
        
        total += float(product[f"product {final[check][0]}"]['price']) * float(final[check][1])
        if product[f"product {final[check][0]}"]['on_sale']:
            totalAfteron_sale += float(product[f"product {final[check][0]}"]['price']) * float(final[check][1]) * 0.90
        else:
            totalAfteron_sale += float(product[f"product {final[check][0]}"]['price']) * float(final[check][1])

        check += 1

    check = 0
    print('================Purchase Invoice================')
    print('Product Name        Price per piece        Number of pieces        Total price')

    while check < len(final):
        print(f'{product[f'product {final[check][0]}']['name']}                {product[f"product {final[check][0]}"]['price']}$                    {final[check][1]}                       {float(product[f"product {final[check][0]}"]['price']) * float(final[check][1])}')
        check += 1

    print(f'Total due before discount : {total}$')
    print(f'Total due after discount  : {totalAfteron_sale}$')
    print('=====================================')
