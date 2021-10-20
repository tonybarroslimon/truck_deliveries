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
        # creates truck instances
        self.truck1 = Truck1()
        self.truck2 = Truck2()
        self.truck3 = Truck3()
        # creates an instance of a Distance object
        self.distances = Distance()
        self.package_deliveries = [None for i in range(41)]
        self.simulation_end = None
        self.current_time = None

    def reset(self):
        pass
        #self.packages.set_item("9", ['9','300 State St','Salt Lake City','UT','84103','EOD','2','Wrong address listed'])

    # method to finding the total distance traveled.
    def get_total_distance(self):
        return float(self.truck1.distance + self.truck2.distance + self.truck3.distance)

    # Method to build the delivery locations for each truck
    def load_packages(self, packages, priority, destinations, priority_destinations):
        for index in packages:
            address = self.packages.get_item(str(index))[1]
            address_id = self.distances.address_hash.get_item(address)[0]
            if address_id not in destinations:
                destinations.append(address_id)
                if index in priority:
                    priority_destinations.append(address_id)

    def unload_packages(self, packages, priority, pos):
        removal_list = []
        for index in packages:
            address = self.packages.get_item(str(index))[1]
            address_id = Distance().address_hash.get_item(address)[0]

            if address_id == str(pos):
                removal_list.append(index)
                self.package_deliveries[index] = self.current_time.time()

        for item in removal_list:
            if item in packages:
                packages.remove(item)
            if item in priority:
                priority.remove(item)

    # Sets the initial next destination for a truck
    # If there is a priority package on the truck, then the method will choose the closest priority package
    @staticmethod
    def find_initial_destination(destinations, priority_destinations, next_stop, goal, pos):
        if priority_destinations:
            next_stop = Distance().next_closest_stop(pos, priority_destinations)
        else:
            next_stop = Distance().next_closest_stop(pos, destinations)
        return next_stop

    def set_initial_destination(self, truck):
        truck.next = self.find_initial_destination(
            truck.destinations,
            truck.priority_destinations,
            truck.next,
            truck.goal,
            truck.pos)

        truck.goal = float(truck.next[1])

    # method grabs closest destination to current destination and updates truck route
    # it also unloads packages as they are delivered
    def set_truck_destinations(self, truck):
        if truck.curr_pos >= truck.goal:
            truck.curr_pos -= truck.goal
            truck.pos = truck.next[0]
            self.unload_packages(truck.packages, truck.priority, truck.pos)
            truck.destinations.remove(truck.next[0])

            if truck.next[0] in truck.priority_destinations:
                truck.priority_destinations.remove(truck.next[0])

            if truck.priority_destinations:
                truck.next = Distance().next_closest_stop(truck.pos, truck.priority_destinations)
            elif truck.destinations:
                truck.next = Distance().next_closest_stop(truck.pos, truck.destinations)
            elif not truck.destinations and truck.next[0] != 0:
                truck.destinations.append(0)
                truck.next = (0, Distance().distance_home(truck.pos))
            truck.goal = float(truck.next[1])

    @staticmethod
    def update_truck_returned(truck):
        if not truck.destinations:
            truck.returned = True
            truck.departed = False

    def load(self, truck):
        self.load_packages(
            truck.packages,
            truck.priority,
            truck.destinations,
            truck.priority_destinations
        )

    # method updates the current position and the distance to the next location
    def update_pos_and_distance(self, truck):
        if truck.returned:
            truck.curr_pos = 0.0

        if not truck.returned and truck.departed:
            truck.curr_pos += self.speed
            truck.distance += self.speed

    def run_simulation(self, time):
        self.simulation_end = datetime.datetime.strptime(time, '%H:%M').time()
        self.current_time = datetime.datetime.strptime('08:00', '%H:%M')

        self.load(self.truck1)
        self.load(self.truck2)
        self.load(self.truck3)

        self.set_initial_destination(self.truck1)
        self.set_initial_destination(self.truck2)
        self.set_initial_destination(self.truck3)

        self.truck1.departed = True
        self.truck1.returned = False

        while not (self.truck1.returned and self.truck2.returned and self.truck3.returned or self.current_time.time() >= self.simulation_end):

            # Increments the current time by one minute each loop
            self.current_time += datetime.timedelta(minutes=1)

            # Checks the time, if it is after 9:05AM, then it loads the packages to the second truck and departs
            if not self.truck2.returned and self.current_time.time() >= datetime.datetime.strptime("09:05:00", "%H:%M:%S").time():
                self.truck2.departed = True

            # checks if truck1 has returned and if the time is after 10:20AM. If so it loads the truck and departs
            if not self.truck3.returned and self.truck1.returned and self.current_time.time() >= datetime.datetime.strptime("10:20:00", "%H:%M:%S").time():
                self.packages.set_item("9", ["9", "410 S State St", "Salt Lake City", "UT", "84111", "EOD", "2", "None"])
                self.truck3.departed = True

            if self.truck1.departed:
                self.update_pos_and_distance(self.truck1)
                self.set_truck_destinations(self.truck1)

            if self.truck2.departed:
                self.update_pos_and_distance(self.truck2)
                self.set_truck_destinations(self.truck2)

            if self.truck3.departed:
                self.update_pos_and_distance(self.truck3)
                self.set_truck_destinations(self.truck3)

            self.update_truck_returned(self.truck1)
            self.update_truck_returned(self.truck2)
            self.update_truck_returned(self.truck3)

    def simulation_output(self, hash_id=None):
        package = []
        if hash_id is None:
            for index in range(1,41):
                package = self.packages.get_item(str(index))

                if self.package_deliveries[index]:
                    package.append(str(self.package_deliveries[index]))
                    package.append("Delivered")
                elif int(index) in self.truck1.packages and self.truck1.departed:
                    package.append("En Route")
                elif int(index) in self.truck2.packages and self.truck2.departed:
                    package.append("En Route")
                else:
                    package.append("At The Hub")
                print(package)
                package.pop()
        else:
            package = self.packages.get_item(str(hash_id))

            if self.package_deliveries[int(hash_id)]:
                package.append(str(self.package_deliveries[int(hash_id)]))
                package.append("Delivered")
            elif int(hash_id) in self.truck1.packages and self.truck1.departed:
                package.append("Out for Delivery")
            elif int(hash_id) in self.truck2.packages and self.truck2.departed:
                package.append("Out for Delivery")
            else:
                package.append("At Hub")
            print(package)
            package.pop()
        return
