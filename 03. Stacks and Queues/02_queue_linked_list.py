class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if not self.first:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if not self.first:
            return None

        if self.length == 0:
            self.last = None

        self.first = self.first.next
        self.length -= 1


my_queue = Queue()
my_queue.enqueue("Discord")
my_queue.enqueue("Amazon")
my_queue.enqueue("Facebook")
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.enqueue("Google")
my_queue.enqueue("Netflix")
print(my_queue.peek())
print(my_queue)
