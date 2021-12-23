from beautifultable import BeautifulTable


class Student:

    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name


class StudentManagement:

    def __init__(self):
        self.exit = False
        self.students = [
            Student(name="Dhaval", course_name="Android"),
            Student(name="Niral", course_name="Python"),
            Student(name="Rutul", course_name="Android"),
        ]

    def print_student_details(self):
        table = BeautifulTable()
        table.columns.header = ["Name", "Course Name"]
        for student in self.students:
            table.rows.append([student.name, student.course_name])
        print(table)

    def add_student(self, name, course_name):
        self.students.append(Student(name=name, course_name=course_name))

    def find_students_for_course(self, course_name):
        return filter(lambda student: student.course_name == course_name, self.students)

    def stop(self):
        self.exit = True


# Start Here
student_management = StudentManagement()


def print_menu():
    print("""
1. Add new student
2. Show student details
3. Find students for a course
0. Exit
""")


def get_user_choice() -> int:
    return int(input("Select an option: "))


def add_new_student():
    name = input("Enter student name: ")
    course_name = input("Course name: ")
    student_management.add_student(name=name, course_name=course_name)


def find_student_for_course():
    course_name = input("Enter course name: ")
    students = student_management.find_students_for_course(course_name=course_name)
    for student in students:
        print(f"Name: {student.name}")


while not student_management.exit:
    print_menu()
    user_choice = get_user_choice()

    if user_choice == 0:
        student_management.stop()
    elif user_choice == 2:
        student_management.print_student_details()
    elif user_choice == 1:
        add_new_student()
    elif user_choice == 3:
        find_student_for_course()
    else:
        print("Invalid Input")
