class MyQueue:
    def __init__(self):
        self.data = []
        self.size = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self, x: int) -> None:
        self.data.append(x)
        self.size += 1
        return self.data

    def pop(self) -> int:
        temp = self.data[0]
        del self.data[0]
        self.size -= 1
        return temp

    def peek(self) -> int:
        if self.size == 0:
            return None
        return self.data[0]

    def empty(self) -> bool:
        return self.size == 0


obj = MyQueue()
print(obj.push(10))
print(obj.push(20))
print(obj.push(30))
print(obj.push(40))
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.peek())
print(obj.empty())
print(obj)
