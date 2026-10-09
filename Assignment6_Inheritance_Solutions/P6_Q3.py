# Q3. Student Enrollment - Multiple Inheritance

class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, course):
        self.course = course


class CourseStudent(Student, Course):
    def __init__(self, name, course):
        Student.__init__(self, name)
        Course.__init__(self, course)

    def enroll(self):
        print(f"{self.name} has been enrolled in {self.course}.")


def main():
    name = input("Enter student name: ")
    course = input("Enter course name: ")
    student = CourseStudent(name, course)
    student.enroll()


if __name__ == "__main__":
    main()
