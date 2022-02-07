#!/usr/bin/python3
""""despues lo hago"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """despues lo hago"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """despues lo hago"""
        return self.width

    @size.setter
    def size(self, value):
        """despues lo hago"""
        self.width = value
        self.height = value

    def __str__(self):
        """despues lo hago"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates Square values """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """despues lo hago"""
        return {"id": self.id, "x": self.x, "size": self.width,
                "y": self.y}
