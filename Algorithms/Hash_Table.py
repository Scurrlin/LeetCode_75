class HashTable:
    def __init__(self):
        self.table = [None] * 1000

    def hash_function(self, key):
        return key % len(self.table)

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]