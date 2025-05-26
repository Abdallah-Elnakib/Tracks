#  Project Question: Student Grades Management System in Python
# Objective:

# Build a complete Python program that manages student grades using functions, variables, loops, and conditional statements. The program must include a secure login system and two types of users: Admin and Student. Each user type should have access to specific functionalities as outlined below.

# 📌 Functional Requirements:
# 🔐 1. Login System:
# Prompt the user to enter a username and password.

# If the credentials match an admin account, the user is logged in as an Admin.

# If the credentials match a student account, the user is logged in as a Student.

# If the credentials are incorrect, the program should handle the error and allow retrying.

# 👨‍💼 2. Admin Panel:
# Once logged in, the Admin should be presented with the following options:

# a. Add New Student:
# Ask for the student's full name and unique student ID.

# Ask for the student’s password (used later for student login).

# Prompt to enter the student’s grades in the following 4 subjects:

# Arabic

# English

# Math

# Science

# Save the student’s data (name, ID, password, and grades).

# b. Edit Student Grades:
# Ask the admin to enter the student ID.

# If the student is found, display their data in the following format, each item numbered:

# Name

# ID (not editable)

# Arabic Grade

# English Grade

# Math Grade

# Science Grade

# Ask the admin to enter the number corresponding to the item they want to update.

# Update the selected field, ensuring input validation (e.g., grades must be numbers).

# c. Delete a Student:
# Ask for the student ID.

# If found, delete the student’s data from the system.

# Otherwise, display an appropriate error message.

# d. Logout:
# Return to the login screen.

# 👨‍🎓 3. Student Panel:
# Once logged in, a student should be able to:

# View their full name and student ID.

# View their grades in Arabic, English, Math, and Science.

# See the total grade and the percentage.

# See whether they Passed (percentage ≥ 50%) or Failed (percentage < 50%).

# ⚙️ Technical Requirements:
# Use Python functions to organize the code (e.g., login, add_student, edit_student, etc.).

# Use dictionaries or lists to store student records.

# Use loops for menus and repeated prompts.

# Use conditional statements for decision-making.

# Validate all user inputs (e.g., no letters in grade fields).

# Handle incorrect data gracefully without crashing the program



# | Criteria                             | Points  |
# | ------------------------------------ | ------- |
# | Functional login system              | 20      |
# | Admin features (Add/Edit/Delete)     | 30      |
# | Student view and grade report        | 20      |
# | Proper use of functions              | 30      |
# | Input validation & error handling    | 50      |
# | Code readability & organization      | 50      |
# | **Total**                            | **200** |
