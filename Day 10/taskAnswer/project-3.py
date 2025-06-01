import json

def getDataDataBase():
    with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "r") as productsData :
        Data = json.load(productsData)

    return Data

def addNewUser():
    username = input('Please Enter Username : ').lower()
    password = input('Please Enter Password : ')
    role = input('Please Enter User Role (Admin/Employee) : ').lower()

    users = getDataDataBase()

    for user in users['users']:
        if username == user['username']:
            print('User Already Exists')
            return addNewUser()
    if len(password) < 8:
        print('Password Must Be At Least 8 Characters')
        return addNewUser()
    elif role != 'admin' and role != 'employee':
        print('Wrong Role')
        return addNewUser()
    else:
        users['users'].append({
            'username' : username,
            'password' : password,
            'role' : role
        })

        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
            json.dump(users, productsData, indent = 4)

        print('User Added Successfully')
        return
    
def addNewProduct():
    products = getDataDataBase()
    try :
        productName = input('Please Enter Product Name : ').lower()
        for product in products['products'] :
            if product['name'] == productName :
                print('Product Already Exists')
                return addNewProduct()
        
        productId = str(len(products['products']) + 1)
        productPrice = int(input('Please Enter Product Price : '))
        productQuantity = int(input('Please Enter Product Quantity : '))
        productDescription = input('Please Enter Product Description : ')

        products['products'].append({
            'id' : productId,
            'name' : productName,
            'price' : productPrice,
            'quantity' : productQuantity,
            'Description' : productDescription
        })


        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
            json.dump(products, productsData, indent = 4)

        print('Product Added Successfully')
        return

    except ValueError:
        print('Wrong Input')
        return addNewProduct()
    
def deleteProduct():
    products = getDataDataBase()

    productId = input('Please Enter Product Id : ')
    for product in products['products'] :
        if product['id'] == productId :
            products['products'].remove(product)
            with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
                json.dump(products, productsData, indent = 4)
            print('Product Deleted Successfully')
            return

    print('Product Not Found')
    return deleteProduct()

def editProduct():
    products = getDataDataBase()
    check = False
    productId = input('Please Enter Product Id : ')
    productsName = []
    for product in products['products'] :
        productsName.append(product['name'])
    for product in products['products'] :
        if check == True :
            break
        if product['id'] == productId :
            while True:
                print('==================================')
                print(f'1. Name({product["name"]})')
                print(f'2. Price({product["price"]})')
                print(f'3. Quantity({product["quantity"]})')
                print(f'4. Description({product["Description"]})')
                print('5. Exit')
                print('==================================')
                choice = input('Please Enter Your Choice (1-4): ')
                try :
                    if choice == '1':
                        productName = input('Please Enter New Product Name : ')
                        if productName in productsName :
                            print('Product Name Already Exists')
                            continue
                        product['name'] = productName
                        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
                            json.dump(products, productsData, indent = 4)
                        print('Product Name Updated Successfully')
                        check = True
                    elif choice == '2':
                        productPrice = int(input('Please Enter New Product Price : '))
                        product['price'] = productPrice
                        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
                            json.dump(products, productsData, indent = 4)
                        print('Product Price Updated Successfully')
                        check = True
                    elif choice == '3':
                        productQuantity = int(input('Please Enter New Product Quantity : '))
                        product['quantity'] = productQuantity
                        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
                            json.dump(products, productsData, indent = 4)
                        print('Product Quantity Updated Successfully')
                        check = True
                    elif choice == '4':
                        productDescription = input('Please Enter New Product Description : ')
                        product['Description'] = productDescription
                        with open("C:/Users/Dell/OneDrive/Desktop/Project-3/DataBase.json", "w") as productsData :
                            json.dump(products, productsData, indent = 4)
                        print('Product Description Updated Successfully')
                        check = True
                    elif choice == '5':
                        return
                    else:
                        print('Wrong Choice')
                        continue
                except ValueError:
                    print('Wrong Input')
                    continue

    print('Product Not Found')
    return editProduct()

def viewAllProducts():
    products = getDataDataBase()['products']
    for product in products:
        print(f'Id : {product["id"]}')
        print(f'Name : {product["name"]}')
        print(f'Price : {product["price"]}')
        print(f'Quantity : {product["quantity"]}')
        print(f'Description : {product["Description"]}')
        print('====================')

def searchInProducts():
    products = getDataDataBase()['products']
    productId = input('Please Enter Product ID : ')
    for product in products:
        if product['id'] == productId:
            print(f'Id : {product["id"]}')
            print(f'Name : {product["name"]}')
            print(f'Price : {product["price"]}')
            print(f'Quantity : {product["quantity"]}')
            print(f'Description : {product["Description"]}')
            print('====================')
            return
    print('Product Not Found')
    return searchInProducts()

def login():
    username = input('Please Enter Username : ')
    password = input('Please Enter password : ')
    users = getDataDataBase()['users']
    for user in users:
        if username == user['username'] :
            if password == user['password']:
                print(f'==== Welcome Back {username} ====')
                return [username, user['role']]
            else :
                print('Wrong Password')
                return login()
    print(f'Username {username} Is Not Found')
    return login()

def adminInterface():
    while True:
        print('1. ➕  Add New product')
        print('2. 📦  View All Products')
        print('3. 🔍  Search for a product')
        print('4. 📝  Edit a product')
        print('5. ❌  Delete a product')
        print('6. ➕  Add New User')
        print('7. 🚪  Logout')
        
        choice = input('Please Enter Your Choice (1-7): ')
        if choice == '1':
            addNewProduct()
        elif choice == '2':
            viewAllProducts()
        elif choice == '3':
            searchInProducts()
        elif choice == '4':
            editProduct()
        elif choice == '5':
            deleteProduct()
        elif choice == '6':
            addNewUser()
        elif choice == '7':
            break
        else:
            print('Wrong Choice')
            continue

def employeeInterface():
    products = getDataDataBase()['products']
    numberOfProducts = []
    print('1. new invoice')
    print('2. logout')
    q = input('Please Enter Your Choice (1-2): ')
    if q == '2' :
        return
    elif q == '1' :
        pass
    else :
        print('Wrong Input')
        return employeeInterface()
    
    for product in products:
            print(f'Id : {product["id"]}')
            print(f'Name : {product["name"]}')
            print(f'Price : {product["price"]}')
            print(f'Quantity : {product["quantity"]}')
            print(f'Description : {product["Description"]}')
            print('====================')
            numberOfProducts.append(product['id'])
    while True:
        check = False
        ProductIds = input('Please Enter Product Ids (separated by commas) : ')
        productsQuantities = input('Please Enter Product Quantities (separated by commas) : ')
        listOfproductsQuantities = productsQuantities.split(',')
        listOfProductIds = ProductIds.split(',')
        if len(listOfproductsQuantities) != len(listOfProductIds):
            print('Wrong Input')
            continue
        for i in listOfProductIds:
            if i not in numberOfProducts:
                print('Wrong Product Id')
                check = True
                break
            
        if check == True:
            continue

        CombineTheProductNameAndItsQuantity = list(zip(listOfProductIds, listOfproductsQuantities))
        total = 0
        print('================Purchase Invoice================')
        print('Product Name        Price per piece        Number of pieces        Total price')
        for i in CombineTheProductNameAndItsQuantity:
            for product in products:
                if product['id'] == i[0]:
                    print(f'{product["name"]}                {product['price']}$                    {i[1]}                       {float(product['price']) * float(i[1])}$')
                    total += float(product['price']) * float(i[1])

        print(f'Total Price : {total}$')
        break
    print('================================')
    return employeeInterface()

def main():
    print('========== Welcome To The Supermarket Program ==========')
    while True:
        print('1. Login')
        print('2. Exit')
        choice = input('Please Enter Your Choice (1-2): ')
        if choice == '2':
            print('Good-bye :)')
            break
        elif choice == '1':
            roleOfUser = login()
        else:
            print('Wrong Choice')
            continue

        if roleOfUser[1] == 'admin':
            adminInterface()
        elif roleOfUser[1] == 'employee':
            employeeInterface()
        else:
            print('Wrong Role')
            continue

main()


