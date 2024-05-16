class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def draw(self):
        for _ in range(self.__size):
            print('*' * self.__size)


# Crear una instancia de Square con tamaño 5
square = Square(5)

# Dibujar el cuadrado
square.draw()
