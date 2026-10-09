# Q2. Student Application - Multilevel Inheritance

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def student_details(self):
        print(f"Roll number: {self.roll_no}")
        print(f"Name: {self.name}")


class Test(Student):
    def __init__(self, roll_no, name, marks):
        super().__init__(roll_no, name)
        self.marks = marks

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks


class Marks(Test):
    def calculate_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def print_class(self):
        average = self.calculate_average()
        if average >= 75:
            result = "Distinction"
        elif average >= 60:
            result = "First Class"
        elif average >= 50:
            result = "Second Class"
        elif average >= 35:
            result = "Pass Class"
        else:
            result = "Fail"
        print(f"Average marks: {average:.2f}")
        print(f"Class: {result}")


def main():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    count = int(input("How many subjects? "))
    marks_list = []
    for i in range(count):
        marks_list.append(float(input(f"Enter marks for subject {i + 1}: ")))
    student = Marks(roll_no, name, marks_list)
    print("\n--- Student Details ---")
    student.student_details()
    print("Marks:", ", ".join(f"{m:g}" for m in student.get_marks()))
    student.print_class()


if __name__ == "__main__":
    main()
