from student import Student


class StudentManagement:

    def __init__(self):
        self.exit = False
        self.students = [
            Student(name="Dhaval", course_name="Android"),
            Student(name="Niral", course_name="Python"),
            Student(name="Rutul", course_name="Android"),
        ]

    def get_students(self) -> list[Student]:
        return self.students

    def add_student(self, name, course_name):
        self.students.append(Student(name=name, course_name=course_name))

    def find_students_for_course(self, course_name):
        return filter(lambda student: student.course_name == course_name, self.students)

    def stop(self):
        self.exit = True
