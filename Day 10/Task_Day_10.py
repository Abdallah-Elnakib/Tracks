# "Simple Store Management System – Python + JSON"
# 🎯 Project Objective:
# Design a system to manage products for a small store. It enables:

# ➕ Add a product

# 📦 View all products

# 🔍 Search for a product

# ✏️ Edit a product

# ❌ Delete a product




# store.json file format:

# {
# "products": [
#         {
#             "id": 1,
#             "name": "Laptop",
#             "price": 1500,
#             "quantity": 2,
#         }
#     ],
#   "users":[ 
#            {
#               "username" : "",
#               "password" : "",
#               "Role" : "admin" or "employee"
#            }
#       ]
# }



# Create an entry registration system first. If the user is an employee, 
# he can use the product display system and create invoices. 
# If the user is a manager, the previous list will appear.