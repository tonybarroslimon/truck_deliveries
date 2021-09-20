class Truck:

    truck_speed = 18 / 60

    def __init__(self):
        self.truck_distance = 0.0
        self.truck_destinations = []
        self.truck_packages = []
        self.truck_priority = []
        self.truck_priority_destinations = []
        self.truck_pos = 0
        self.truck_curr_pos = 0.0
        self.truck_goal = 0.0
        self.truck_returned = False
        self.truck_departed = False
        self.package_deliveries = [None] * 41

    def get_truck_distance(self):
        return self.truck_distance

    def set_truck_distance(self, distance):
        self.truck_distance = distance

    def get_truck_destinations(self):
        return self.truck_destinations

    def set_truck_destinations(self, address_id):
        self.truck_destinations.append(address_id)

    def get_truck_packages(self):
        return self.truck_packages

    def set_truck_packages(self, package_id):
        self.truck_packages.append(package_id)

    def get_truck_priority(self):
        return self.truck_priority

    def set_truck_priority(self, package_id):
        self.truck_priority.append(package_id)

    def get_truck_priority_destinations(self):
        return self.truck_priority_destinations

    def set_truck_priority_destinations(self, address_id):
        self.truck_priority_destinations.append(address_id)

    def get_truck_pos(self):
        return self.truck_pos

    def set_truck_pos(self, package_id):
        self.truck_pos.append(package_id)

    def get_truck_curr_pos(self):
        return self.truck_curr_pos

    def set_truck_curr_pos(self, package_id):
        self.truck_curr_pos.append(package_id)

    def get_truck_goal(self):
        return self.truck_goal

    def set_truck_goal(self, package_id):
        self.truck_goal.append(package_id)


class Truck1(Truck):

    def __init__(self):
        self.truck_packages = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40, 1, 4, 7, 39, 8, 32]
        self.truck_priority = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40]


class Truck2(Truck):

    def __init__(self):
        self.truck_packages = [3, 18, 36, 38, 6, 10, 11, 12, 17, 20, 21, 22, 23, 24, 25, 26]
        self.truck_priority = [6, 20, 25]


class Truck3(Truck):

    def __init__(self):
        self.truck_packages = [9, 19, 27, 28, 33, 35, 2, 5]
        self.truck_priority = []