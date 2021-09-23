from Models.HashTable import HashTable
from Models.Truck import Truck, Truck1, Truck2, Truck3
from Models.Package import Package
from Models.Distance import Distance
import datetime


class App:

    def __init__(self):
        # sets the speed to miles per minute
        self.speed = 18 / 60
        # creates a hash table of packages from the Package class
        self.packages = Package().package_hash
        # creates three truck instances
        self.truck1 = Truck1()
        self.truck2 = Truck2()
        self.truck3 = Truck3()
        # creates a list with 41 items set to None.
        self.package_deliveries = [None for i in range(41)]
        # adds an item to the package hash table
        self.packages.set_item('9', ['9', '300 State St', 'Salt Lake City', 'UT', '84103', 'EOD', '2',
                                     'Wrong address listed'])

    def reset(self):
        # deletes the objects created when App is constructed.
        del self.packages
        del self.truck1
        del self.truck2
        del self.truck3


