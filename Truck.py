import HashTable


class Truck:

    def __init__(self):
        self.truck_distance = 0.0
        self.truck_destinations = []
        self.truck_priority_destinations = []
        self.truck_pos = 0
        self.truck_curr_pos = 0.0
        self.truck_goal = 0.0
        self.truck_returned = False
        self.truck_departed = False
        self.package_deliveries = [None] * 41


class Truck1(Truck):

    def __init__(self):
        self.truck1_packages = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40, 1, 4, 7, 39, 8, 32]
        self.truck1_priority = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40]


class Truck2(Truck):

    def __init__(self):
        self.truck2_packages = [3, 18, 36, 38, 6, 10, 11, 12, 17, 20, 21, 22, 23, 24, 25, 26]
        self.truck2_priority = [6, 20, 25]


class Truck3(Truck):

    def __init__(self):
        self.truck3_packages = [9, 19, 27, 28, 33, 35, 2, 5]
        self.truck3_priority = []