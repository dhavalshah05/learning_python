from management import StudentManagement
from printer import Printer

student_management = StudentManagement()


def print_menu():
    print("""
1. Add new student
2. Show student details
3. Find students for a course
0. Exit
""")


while not student_management.exit:
    print_menu()
    user_choice = int(input("Select an option: "))

    if user_choice == 0:
        student_management.stop()

    elif user_choice == 2:
        students = student_management.get_students()
        printer = Printer()
        printer.print_student_details(students)

    elif user_choice == 1:
        name = input("Enter student name: ")
        course_name = input("Course name: ")
        student_management.add_student(name=name, course_name=course_name)

    elif user_choice == 3:
        course_name = input("Enter course name: ")
        students = student_management.find_students_for_course(course_name=course_name)
        printer = Printer()
        printer.print_student_details(students)


    else:
        print(f"Invalid Input")
