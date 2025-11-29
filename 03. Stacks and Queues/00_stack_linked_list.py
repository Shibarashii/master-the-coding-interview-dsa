class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = self.top
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def pop(self):
        if not self.top:
            return None

        temp = self.top.value
        self.top = self.top.next
        self.length -= 1

        if self.length == 0:
            self.bottom = None
        return temp

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        if self.length == 0:
            self.bottom = new_node
        self.length += 1

    def peek(self):
        return self.top.value

    def is_empty(self):
        if not self.bottom:
            return True
        else:
            return False

    def is_full(self):
        pass


my_stack = Stack()
my_stack.push("Discord")
my_stack.push("Amazon")
my_stack.push("Facebook")
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
my_stack.push("hello")
print(my_stack)
print(my_stack.is_empty())
