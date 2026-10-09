# Q5. Employee Details - Hierarchical Inheritance

class Employee:
    def employee_details(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")


class Designer(Employee):
    def designer_details(self, tool):
        self.tool = tool

    def display_details(self):
        print("\n--- Designer Details ---")
        self.display_employee_details()
        print(f"Design tool: {self.tool}")


class Developer(Employee):
    def developer_details(self, tool):
        self.tool = tool

    def display_details(self):
        print("\n--- Developer Details ---")
        self.display_employee_details()
        print(f"Development tool: {self.tool}")


def main():
    print("1. Designer\n2. Developer")
    choice = input("Choose employee type: ")
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    tool = input("Enter tool used: ")

    if choice == "1":
        employee = Designer()
        employee.employee_details(emp_id, name)
        employee.designer_details(tool)
        employee.display_details()
    elif choice == "2":
        employee = Developer()
        employee.employee_details(emp_id, name)
        employee.developer_details(tool)
        employee.display_details()
    else:
        print("Invalid employee type.")


if __name__ == "__main__":
    main()
