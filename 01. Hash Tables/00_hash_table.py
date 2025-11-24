class HashTable:
    def __init__(self, size):
        self.size = size
        self.data: list = [None] * size

    def __str__(self):
        return str(self.__dict__)

    def get(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        if bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return None

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    def keys(self):
        key_array = []
        for address in range(len(self.data)):
            if self.data[address]:
                key_array.append(self.data[address][0][0])
        return key_array

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash += ord(key[i])
        hash %= self.size
        return hash


my_hash_table = HashTable(50)
my_hash_table.set("apples", 500)
my_hash_table.set("grapes", 1000)
my_hash_table.set("apple", 5000)

grapes = my_hash_table.get("grapes")
apples = my_hash_table.get("apples")
apple = my_hash_table.get("apple")

print(grapes, apple, apples)
print(my_hash_table.keys())
print(my_hash_table.__str__())
