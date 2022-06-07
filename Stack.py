class Stack:
    """Цей клас реалізує стек"""
    def __init__(self):
        self.__num_recursion = 0
        self.__stack = list()

    def is_empty(self):
        if len(self.__stack) <= 0:
            return True
        else:
            return False

    def push(self, element):
        self.__num_recursion += 1
        self.__stack.append(element)

    def pop(self):
        if len(self.__stack) > 0:
            return self.__stack.pop()
        else:
            print("Stack is already empty")
            raise IndexError

    def top(self):
        if len(self.__stack) > 0:
            return self.__stack[-1]
        else:
            print("Stack is already empty")
            raise IndexError

    def get_num_recursion(self):
        return self.__num_recursion





