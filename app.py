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
        # creates an instance of a Distance object
        self.distance = Distance()
        # creates a list with 41 items set to None.
        self.package_deliveries = [None for i in range(41)]
        self.removal_list = []
        # adds an item to the package hash table
        self.packages.set_item('9', ['9', '300 State St', 'Salt Lake City', 'UT', '84103', 'EOD', '2',
                                     'Wrong address listed'])

    def reset(self):
        # deletes the objects created when App is constructed.
        del self.packages
        del self.truck1
        del self.truck2
        del self.truck3
        del self.distance

    # method to finding the total distance traveled of the three trucks.
    def get_total_distance(self):
        return float(self.truck1.truck_distance + self.truck2.truck_distance + self.truck3.truck_distance)

    # Method to build the delivery locations for each truck
    @staticmethod
    def load_packages(truck):
        for index in truck.truck_packages:
            address = App.packages.get_item(str(index))[1]
            address_id = Distance.address_hash.get_item(address)[0]

            if address_id not in truck.truck_packages:
                truck.truck_destinations.append(address_id)
                if index in truck.truck_priority:
                    truck.truck_priority_destinations.append(address_id)

    def unload_packages(self, truck_packages, truck_priority, truck_pos):
        for index in truck_packages:
            address = App.packages.get_item(str(index))[1]
            address_id = Distance.address_hash.get_item(address)[0]

            if address_id == str(truck_pos):
                self.removal_list.append(index)
                self.package_deliveries[index] = self.current_time.time()

        for item in self.removal_list:
            truck_packages.remove(item)
            if item in truck_priority:
                truck_priority.remove(item)

"""
        App.build_lists(self.truck1)
        App.build_lists(self.truck2)
        App.build_lists(self.truck3)
"""
