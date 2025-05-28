users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

students = {'abdallah' : {'name': 'abdallah', 'password': '123', 'grades': {'Arabic': 90, 'English': 85, 'Math': 95, 'Science': 88}}}

def validate_grade(input_str):
    if not input_str.isdigit():
        return False
    val = int(input_str)
    return 0 <= val <= 100

def input_grade(subject):
    while True:
        grade = input(f"Enter {subject} grade (0-100): ")
        if validate_grade(grade):
            return int(grade)
        else:
            print("Invalid grade! Please enter a number between 0 and 100.")

def login():
    while True:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username in users and users[username]["password"] == password:
            print(f"Welcome {username}!")
            return username, users[username]["role"]
        elif username in students and students[username]["password"] == password:
            print(f"Welcome student {students[username]['name']}!")
            return username, "student"
        else:
            print("Incorrect username or password. Try again.\n")

def add_student():
    print("\n--- Add New Student ---")
    while True:
        student_id = input("Enter unique student ID: ").strip()
        if student_id in students:
            print("Student ID already exists! Please enter another.")
        elif student_id == "":
            print("Student ID cannot be empty!")
        else:
            break
    while True:
        name = input("Enter student's full name: ").strip()
        if name == "":
            print("Name cannot be empty!")
        else:
            break
    while True:
        password = input("Enter password for student: ").strip()
        if password == "":
            print("Password cannot be empty!")
        else:
            break
    grades = {}
    for subject in ["Arabic", "English", "Math", "Science"]:
        grades[subject] = input_grade(subject)

    students[student_id] = {
        "name": name,
        "password": password,
        "grades": grades
    }
    print(f"Student '{name}' with ID '{student_id}' added successfully!\n")

def edit_student():
    print("\n--- Edit Student Grades ---")
    student_id = input("Enter student ID to edit: ").strip()
    if student_id not in students:
        print("Student not found!\n")
        return
    student = students[student_id]
    print(f"Editing student: {student['name']} (ID: {student_id})")
    grades = student["grades"]
    while True:
        print("\nSelect field to edit:")
        print("1. Name")
        print("2. Arabic grade")
        print("3. English grade")
        print("4. Math grade")
        print("5. Science grade")
        print("6. Exit editing")
        choice = input("Enter choice number: ").strip()

        if choice == "1":
            new_name = input("Enter new full name: ").strip()
            if new_name:
                student["name"] = new_name
                print("Name updated successfully.")
            else:
                print("Name cannot be empty.")
        elif choice in ["2", "3", "4", "5"]:
            subject = { "2": "Arabic", "3": "English", "4": "Math", "5": "Science" }[choice]
            new_grade = input(f"Enter new grade for {subject} (0-100): ").strip()
            if validate_grade(new_grade):
                grades[subject] = int(new_grade)
                print(f"{subject} grade updated.")
            else:
                print("Invalid grade input.")
        elif choice == "6":
            print("Exiting edit menu.\n")
            break
        else:
            print("Invalid choice, please try again.")

def delete_student():
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ").strip()
    if student_id in students:
        confirm = input(f"Are you sure you want to delete student '{students[student_id]['name']}'? (y/n): ").lower()
        if confirm == 'y':
            del students[student_id]
            print("Student deleted successfully.\n")
        else:
            print("Deletion cancelled.\n")
    else:
        print("Student not found!\n")

def admin_panel():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add New Student")
        print("2. Edit Student Grades")
        print("3. Delete a Student")
        print("4. Logout")
        choice = input("Enter your choice number: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Logging out from admin...\n")
            break
        else:
            print("Invalid choice, please try again.")

def student_panel(student_id):
    student = students[student_id]
    grades = student["grades"]
    total = sum(grades.values())
    max_total = 4 * 100
    percentage = (total / max_total) * 100
    status = "Passed" if percentage >= 50 else "Failed"

    while True:
        print(f"\n--- Student Panel ({student['name']}) ---")
        print(f"Student ID: {student_id}")
        print("Grades:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade}")
        print(f"Total: {total} / {max_total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Status: {status}")

        print("\nOptions:")
        print("1. Logout")
        choice = input("Enter your choice number: ").strip()
        if choice == "1":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    print("=== Welcome to Student Grades Management System ===")
    while True:
        username, role = login()
        if role == "admin":
            admin_panel()
        elif role == "student":
            student_panel(username)

main()