students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    students[student_id] = {'Name': name, 'Grade': grade}
    print(f"Student {name} with ID {student_id} added to the library.")

def display_student(student_id):
    student = students.get(student_id)
    if student:
        print(f"Student ID: {student_id}")
        for key, value in student.items():
            print(f"{key}: {value}")
    else:
        print(f"Student with ID {student_id} not found.")

def main():
    while True:
        print("\nSchool Library Management System")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            display_student(student_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
