#=================================================================================

# Write a supermarket management program.
# There is a database containing the following: the name of each product, 
# the quantity available in the warehouse, whether it is on sale, 
# the product's price, and the product's section.
# The program displays the product name, the price per item, 
# and a brief description. It displays all products in a simple and attractive way, 
# with each product having its own unique number.
# Then, the user is prompted to first select the product numbers they want to purchase. 
# After entering the numbers, a request appears, 
# specifying the required quantities for each product.
# Then, the purchase invoice displays the product name, 
# the price per item, the price per selected item, the quantity for each product, 
# and the total amount due. A discount is added to the product, 
# if applicable, and this is noted on the invoice. Example:
#
# ===============Welcome===============
# product 1 :
# Name -> milk
# Price -> 10$
# Description -> Fresh and healthy milk
# -----
# product 2 :
# Name -> Rice
# Price -> 20$
# Description -> Premium and pure rice
# -----
# product 3 :
# Name -> Bread
# Price -> 2$
# Description -> fresh bread
# =====================================
# Please write the numbers of the products you want to buy like this 1,2 : 1,3
# Please write the value of each product you want to purchase in order of your previous selection : 2,5
#
# ================Purchase Invoice================
# Product Name        Price per piece        Number of pieces        Total price
#
# milk                10$                    2                       20$
# Bread               2$                     5                       10$
#
# Total due before discount : 30$
# Total due after discount  : 25$