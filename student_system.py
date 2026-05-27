# Student Management System - Simple Version
import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE_NAME, 'w') as f:
        json.dump(students, f, indent=2)

def add_student():
    name = input("Student Name: ")
    roll_no = input("Roll No: ")
    marks = input("Marks: ")
    
    students = load_students()
    students.append({"name": name, "roll_no": roll_no, "marks": marks})
    save_students(students)
    print("Student Added ✅\n")

def view_students():
    students = load_students()
    if not students:
        print("No students found\n")
        return
    
    print("\n--- Student List ---")
    for s in students:
        print(f"Roll No: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")
    print()

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    students = load_students()
    new_students = [s for s in students if s['roll_no'] != roll_no]
    
    if len(new_students) == len(students):
        print("Student not found\n")
    else:
        save_students(new_students)
        print("Student Deleted ✅\n")

def main():
    while True:
        print("1. Add Student")
        print("2. View Students") 
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()