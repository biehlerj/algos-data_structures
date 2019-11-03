#!/usr/bin/python3
class Stack:
    def __init__(self, max_size: int):
        self.__stack = []
        self.__max_size = max_size

    def push(self, new_num: int):
        if len(self.__stack) >= self.__max_size:
            raise IndexError('The max size of the stack has been reached')
        self.__stack.append(new_num)

    def peak(self):
        return self.__stack[-1]

    def pop(self):
        try:
            popped = self.__stack.pop()
        except IndexError as e:
            print('The stack is empty')
            return None

        return popped

    def print_stack(self):
        print(self.__stack)

    def size(self):
        return len(self.__stack)

    def __repr__(self):
        return self.__stack
