import csv
from Models.HashTable import HashTable


class Package:
    # Creates an instance of a hash table
    package_hash = HashTable()

    def __init__(self):
        with open('data/package_file.csv') as package_file:
            self.package_data = csv.reader(package_file, delimiter=',')

            for row_data in self.package_data:
                self.key = row_data[0]
                Package.package_hash.set_item(self.key, [self.key, row_data[1], row_data[2], row_data[3], row_data[4],
                                                         row_data[5], row_data[6], row_data[7]])
