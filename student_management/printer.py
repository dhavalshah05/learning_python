from beautifultable import BeautifulTable

from student import Student


class Printer:

    def __init__(self):
        self.table = BeautifulTable()
        self.table.columns.header = ["Name", "Course Name"]

    def print_student_details(self, students: list[Student]):
        for student in students:
            self.table.rows.append([student.name, student.course_name])
        print(self.table)

    def print_student(self, student):
        self.table.rows.append([student.name, student.course_name])
        print(self.table)
