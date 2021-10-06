class HashTable:
    """"Creates a hash table and handles collisions using chaining"""
    def __init__(self):
        # Maximum number of packages that can be placed in a truck.
        self.PACKAGES = 45

        # Creates an array of arrays of the size of PACKAGES.
        self.array = [[] for i in range(self.PACKAGES)]

    # Creates the hash instance using the asci values of the characters in the key value
    def get_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.PACKAGES

    # This method allows an item to be added to the hash table
    def set_item(self, key, value):
        hash_val = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[hash_val]):
            if len(element) == 2 and element[0] == key:
                self.array[hash_val][idx] = (key, value)
                found = True
        if not found:
            self.array[hash_val].append((key, value))

    # This method lets the user query the hash table
    def get_item(self, key):
        hash_val = self.get_hash(key)
        for key_value in self.array[hash_val]:
            if key_value[0] == key:
                return key_value[1]

    # This method allows a user to delete an item from the hash table
    def delete_item(self, key):
        hash_val = self.get_hash(key)
        for index, key_value in enumerate(self.array[hash_val]):
            if key_value[0] == key:
                print(f"del {index}")
                del self.array[hash_val][index]