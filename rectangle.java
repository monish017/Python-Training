class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example Test Case
rectangle = Rectangle(length=5, width=3)
print(f'area: {rectangle.area()}, perimeter: {rectangle.perimeter()}')  # Output: area: 15, perimeter: 16
