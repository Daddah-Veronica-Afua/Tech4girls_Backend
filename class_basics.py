# Define the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Create an instance of the Car class with sample values
my_car = Car("Toyota", "Camry", 2020)

# Call display_info() to test the functionality
my_car.display_info()

