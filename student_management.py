should_run = True
students = [
    {
        'name': 'Dhaval',
        'course_name': 'Android'
    },
    {
        'name': 'Jay',
        'course_name': 'Android'
    },
    {
        'name': 'Niral',
        'course_name': 'Android'
    }
]


def print_menu():
    print("""
1. Add new student
2. Show student details
3. Find students for a course
0. Exit
""")


def get_user_choice() -> int:
    return int(input("Select an option: "))


def show_student_details():
    for student in students:
        print(f"Name: {student['name']}, Course Name: {student['course_name']}")


def add_new_student():
    student_name = input("Enter student name: ")
    course_name = input("Course name: ")
    students.append({
        "name": student_name,
        "course_name": course_name
    })


def is_student_part_of_course(student, course) -> bool:
    return student['course_name'] == course


def find_student_for_course():
    course_name = input("Enter course name: ")
    filtered_students = filter(lambda student: is_student_part_of_course(student, course_name), students)

    for student in filtered_students:
        print(f"Name: {student['name']}")


while should_run:
    print_menu()
    user_choice = get_user_choice()

    if user_choice == 0:
        should_run = False
    elif user_choice == 2:
        show_student_details()
    elif user_choice == 1:
        add_new_student()
    elif user_choice == 3:
        find_student_for_course()
    else:
        print("Invalid Input")
