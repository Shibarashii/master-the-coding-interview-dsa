class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.__dict__)


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if self.length <= index:
            self.append(value)
            return
        if index == 0:
            self.prepend(value)
            return

        node_before = self.traverse_to_index(index-1)
        node_after = node_before.next

        new_node = Node(value)
        node_before.next = new_node
        new_node.next = node_after
        new_node.prev = node_before
        node_after.prev = new_node
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.length -= 1
            self.head = self.head.next
            return

        if index+1 > self.length:
            raise IndexError("Index out of bounds")

        node_to_delete = self.traverse_to_index(index)
        node_before = node_to_delete.prev
        node_after = node_to_delete.next

        node_before.next = node_after
        if index == self.length:
            node_after.prev = node_before
        del node_to_delete
        self.length -= 1

    def traverse_to_index(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        print(" -> ".join(values))
        print(f"Length: {self.length}")


doubly_ll = DoublyLinkedList(5)
doubly_ll.insert(1, 99999)
doubly_ll.append(15)
doubly_ll.remove(2)
doubly_ll.print_list()
