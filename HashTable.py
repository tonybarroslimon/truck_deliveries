class HashTable:
    """"Creates a hash table of size 16. This hash table handles collisions using chaining."""
    def __init__(self):
        self.PACKAGES = 16

        # Creates an array of arrays of the size of PACKAGES.
        self.array = [[] for i in range(self.PACKAGES)]

    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.PACKAGES

    def set_item(self, key, value):
        hash_val = self.get_hash(key)
        found = False
        for index, element in enumerate(self.array[hash_val]):
            if element[0] == key and len(element) == 2:
                self.array[hash_val][index] = (key,value)
                found = True
                break
        if not found:
            self.array[hash_val].append((key,value))

    def get_item(self, key):
        hash_val = self.get_hash(key)
        for element in self.array[hash_val]:
            if element[0] == key:
                return element[1]

    def delete_item(self, key):
        hash_val = self.get_hash(key)
        for index, key_value in enumerate(self.array[hash_val]):
            if key_value[0] == key:
                del self.array[hash_val][index]
