class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def remove(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:
                    self.head = curr.next
                return True
            curr = curr.next
        return False

    def find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]

    def _hash(self, key):
        A = 0.6180339887
        return int(self.capacity * ((key * A) % 1))

    def _resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_table:
            current = bucket.head
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value):
        if self.size >= 0.75 * self.capacity:
            self._resize(self.capacity * 2)
        index = self._hash(key)
        self.table[index].insert(key, value)
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        if self.table[index].remove(key):
            self.size -= 1
            if self.size <= 0.25 * self.capacity and self.capacity > 8:
                self._resize(max(self.capacity // 2, 8))
            return True
        return False

    def find(self, key):
        index = self._hash(key)
        return self.table[index].find(key)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Cell {i}: ", end="")
            current = bucket.head
            while current:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("None")

hash_table = HashTable()

print("---------------- adding elements ----------------")

a = [5, 28, 19, 15, 20, 33, 12, 17, 10]

for i in range(9):
    hash_table.insert(a[i], (i + 1) * 100)

hash_table.display()

print("---------------- removing elements ----------------")

b = [10, 22, 31, 4, 15, 28, 17, 88, 59]

hash_table.remove(10)
hash_table.remove(20)
hash_table.remove(5)
hash_table.remove(12)
hash_table.remove(33)
hash_table.display()

print("---------------- adding elements ----------------")

for i in range(9):
    hash_table.insert(b[i], 900 + ((i + 1) * 100))

hash_table.display()
