class Truck:

    def __init__(self):
        self.distance = 0.0
        self.destinations = []
        self.packages = []
        self.priority = []
        self.priority_destinations = []
        self.pos = '0'
        self.curr_pos = 0.0
        self.goal = 0.0
        self.returned = False
        self.departed = False
        self.next = None


class Truck1(Truck):

    def __init__(self):
        Truck.__init__(self)
        self.packages = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40, 1, 4, 7, 39, 8, 32]
        self.priority = [13, 14, 15, 16, 29, 30, 31, 34, 37, 40]
        self.late_packages = [9, 19, 27, 28, 33, 35, 2, 5]
        self.late_priority = []


class Truck2(Truck):

    def __init__(self):
        Truck.__init__(self)
        self.packages = [3, 18, 36, 38, 6, 10, 11, 12, 17, 20, 21, 22, 23, 24, 25, 26]
        self.priority = [6, 20, 25]
