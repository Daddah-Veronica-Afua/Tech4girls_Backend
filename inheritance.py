# Define the parent class Employee
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}"

# Define the child class Manager that inherits from Employee
class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    # Override the get_details() method to include the department
    def get_details(self):
        return f"Name: {self.name}, Position: {self.position}, Department: {self.department}"

# Create instances of both classes and demonstrate functionality
employee = Employee("Daddah Veronica", "Developer")
manager = Manager("Daddah Caleb", "Manager", "IT")

# Call get_details() for each instance
print(employee.get_details())
print(manager.get_details())
