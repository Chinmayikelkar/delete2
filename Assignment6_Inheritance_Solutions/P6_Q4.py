# Q4. Academic Application - Multiple Inheritance

class Academic:
    def academic_details(self, roll_no, marks):
        self.academic_roll_no = roll_no
        self.academic_marks = marks

    def display_academic_details(self):
        print(f"Academic roll number: {self.academic_roll_no}")
        print(f"Academic marks: {self.academic_marks}")


class Sports:
    def sports_details(self, roll_no, marks):
        self.sports_roll_no = roll_no
        self.sports_marks = marks

    def display_sports_details(self):
        print(f"Sports roll number: {self.sports_roll_no}")
        print(f"Sports marks: {self.sports_marks}")


class Student(Academic, Sports):
    def student_details(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display_all_details(self):
        print("\n--- Student Details ---")
        print(f"Roll number: {self.roll_no}")
        print(f"Name: {self.name}")
        self.display_academic_details()
        self.display_sports_details()


def main():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    academic_marks = float(input("Enter academic marks: "))
    sports_roll_no = input("Enter sports roll number: ")
    sports_marks = float(input("Enter sports marks: "))

    student = Student()
    student.academic_details(roll_no, academic_marks)
    student.sports_details(sports_roll_no, sports_marks)
    student.student_details(roll_no, name)
    student.display_all_details()


if __name__ == "__main__":
    main()
