class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self, value):
        self.data.append(value)
        self.length += 1

    def pop(self):
        temp = self.data.pop()
        return temp

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        if self.length == 0:
            return True
        return False


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack)
print(my_stack.peek())
print(my_stack.is_empty())
