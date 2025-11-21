from typing import Dict


class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        popped_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return popped_item

    def delete(self, index):
        def shift_left(index):
            for i in range(index, self.length - 1):
                self.data[i] = self.data[i+1]

        deleted_item = self.data[index]
        shift_left(index)
        del self.data[self.length-1]
        self.length -= 1
        return deleted_item


new_array = MyArray()
new_array.push("how")
new_array.push("are")
new_array.push("!")
new_array.push("you")
new_array.push("!")
new_array.pop()
new_array.delete(2)

print(new_array)
