class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle(Length: {self.length}, Width: {self.width})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return False

# Create two rectangle instances with different dimensions
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 3)

# Demonstrate the use of all methods
print(rect1)  # Uses the __str__ method
print(f"Area: {rect1.area}, Perimeter: {rect1.perimeter}")

print("\n")

print(rect2)  # Uses the __str__ method
print(f"Area: {rect2.area}, Perimeter: {rect2.perimeter}")

# Compare the two rectangles using the __eq__ method
print(f"\nAre the two rectangles equal in area? {'Yes' if rect1 == rect2 else 'No'}")
