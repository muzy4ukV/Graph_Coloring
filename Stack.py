class Stack:
    """Цей клас реалізує стек"""
    def __init__(self):
        self.__stack = list()

    def is_empty(self):
        if len(self.__stack) <= 0:
            return True
        else:
            return False

    def push(self, element):
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





