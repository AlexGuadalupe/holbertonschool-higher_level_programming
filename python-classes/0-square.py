class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
