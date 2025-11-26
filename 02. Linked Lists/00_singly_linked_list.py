class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if self.length <= index:
            self.append(value)
            return
        if index == 0:
            self.prepend(value)
            return

        # Navigate to the node just before the insertion point
        node_before = self.traverse_to_index(index - 1)

        # Save reference to the node that will come after the new node
        node_after = node_before.next

        # Create new node and link it into the chain
        new_node = Node(value)
        new_node.next = node_after

        node_before.next = new_node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return

        node_before = self.traverse_to_index(index - 1)
        node_to_delete = node_before.next
        node_before.next = node_to_delete.next

        del node_to_delete
        self.length -= 1

    def traverse_to_index(self, index):
        node = self.head
        for i in range(index):
            node = node.next

        return node

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        print(" -> ".join(values))

    def __str__(self):
        return str(self.__dict__)


my_linked_list = LinkedList(5)  # a {10, b}
my_linked_list.append(10)  # b {5, c}
my_linked_list.append(15)  # c {16, None}
my_linked_list.append(30)  # c {16, None}
my_linked_list.insert(2, 99)
my_linked_list.remove(0)
my_linked_list.append(25)  # c {16, None}
my_linked_list.append(35)  # c {16, None}
my_linked_list.print_list()
print(my_linked_list.length)
