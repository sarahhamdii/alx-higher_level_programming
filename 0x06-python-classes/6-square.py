#!/usr/bin/python3
'''defines a square based on 5-square.py'''


class Square:
    '''defines a square'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return ((self.__size) ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
