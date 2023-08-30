#!/usr/bin/python3
'''defines a square based on 5-square.py'''


class Square:
    '''defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation'''
        self.size = size
        self.position = position

    def area(self):
        '''Public instance'''
        return ((self.__size) ** 2)

    @property
    def size(self):
        '''to retrieve'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print("")

    @property
    def position(self):
        '''to retrieve'''
        return self.__position

    @position.setter
    def position(self, value):
        '''property setter'''
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
