class HashTable:
    """"Creates a hash table of size 16."""
    def __init__(self):
        # Maximum number of packages that can be placed in a truck.
        self.PACKAGES = 16

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
        self.array[hash_val] = value

    # This method lets the user query the hash table
    def get_item(self, key):
        hash_val = self.get_hash(key)
        return self.array[hash_val]

    # This method allows a user to delete an item from teh hash table
    def delete_item(self, key):
        hash_val = self.get_hash(key)
        self.array[hash_val] = None
