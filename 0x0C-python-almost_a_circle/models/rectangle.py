#!/usr/bin/python3
"""despues lo hago"""


from models.base import Base
"""despues lo hago"""


class Rectangle(Base):
    """lo hago despues"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """despues lo hago"""
        return self.__width

    @width.setter
    def width(self, value):
        """despues lo hago"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """despues lo hago"""
        return self.__height

    @height.setter
    def height(self, value):
        """despues lo hago"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """despues lo hago"""
        return self.__x

    @x.setter
    def x(self, value):
        """despues lo hago"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """despues lo hago"""
        return self.__y

    @y.setter
    def y(self, value):
        """despues lo hago"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """despues lo hago"""
        return self.__width * self.__height

    def display(self):
        """despues lo hago"""
        print('\n' * self.__y, end='')
        for height in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """despues lo hago"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates rectangle values """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """despues lo hago"""
        return {"x": self.__x, "y": self.y, "id": self.id,
                "height": self.__height, "width": self.__width}
