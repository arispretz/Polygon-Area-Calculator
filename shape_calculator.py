class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


rectangle = Rectangle(5, 10)
print(rectangle)  # Output: Rectangle(width=5, height=10)

square = Square(9)
print(square)     # Output: Square(side=9)

rectangle.set_width(8)
rectangle.set_height(12)
print(rectangle.get_area())        # Output: 96
print(rectangle.get_perimeter())   # Output: 40
print(rectangle.get_picture())     # Output: ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********
                                   #         ********

small_square = Square(4)
print(rectangle.get_amount_inside(small_square))  # Output: 6
