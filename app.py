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
        self.package = []
        # creates three truck instances
        self.truck1 = Truck1()
        self.truck2 = Truck2()
        self.truck3 = Truck3()
        # creates an instance of a Distance object
        self.distance = Distance()
        # creates a list with 41 items set to None.
        self.package_deliveries = [None for i in range(41)]
        # Blank list to hold removed packages
        self.removal_list = []
        # Keeps track of the next stop for a truck
        self.truck_next = None
        self.simulation_end = None
        self.current_time = None
        # adds an item to the package hash table


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
    def load_packages(self, truck):
        for index in truck.truck_packages:
            address = Package.package_hash.get_item(str(index))[1]
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
                self.package_deliveries[index] = [index, self.current_time.time(), "Delivered"]

        for item in self.removal_list:
            truck_packages.remove(item)
            if item in truck_priority:
                truck_priority.remove(item)

    # Sets the initial next destination for a truck
    # If there is a priority package on the truck, then the method will choose the closest priority package
    def set_initial_next_destination(self, truck):
        if len(truck.truck_priority_destinations) > 0:
            self.truck_next = Distance.next_closest_stop(truck.truck_pos, truck.truck_priority_destinations)
        elif len(self.truck_destinations) > 0:
            self.truck_next = self.distance.next_closest_stop(truck.truck_pos, truck.truck_destinations)
        truck.truck_goal = float(self.truck_next[1])

    # method updates the current position and the distance to the next location
    def update_pos_and_distance(self, truck):
        if not truck.truck_returned and truck.truck_departed:
            truck.truck_curr_pos += self.speed
            truck.truck_distance += self.speed

    # method grabs closest destination to current destination and updates truck route
    # it also unloads packages as they are delivered
    def set_truck_destinations(self, truck):
        if truck.truck_curr_pos >= truck.truck_goal:
            truck.truck_curr_pos -= truck.truck_goal
            truck.truck_pos = self.truck_next[0]
            self.unload_packages(truck.truck_packages, truck.truck_priority, truck.truck_pos)
            truck.truck_destinations.remove(self.truck_next[0])
            if len(truck.truck_priority_destinations) > 0:
                truck.truck_priority_destinations.remove(self.truck_next[0])
                self.truck_next = Distance.next_closest_stop(truck.truck_pos, truck.truck_priority_destinations)
            elif len(truck.truck_destinations) > 0:
                self.truck_next = Distance.next_closest_stop(truck.truck_pos, truck.truck_destinations)
            elif len(truck.truck_destinations) < 1 and self.truck_next[0] != 0:
                truck.truck_destinations.append(0)
                self.truck_next = (0, Distance.distance_home(truck.truck_pos))
            truck.truck_goal = float(self.truck_next[1])

    def update_truck_returned(self, truck):
        if len(truck.truck_destinations) < 1:
            truck.truck_returned = True

    def run_simulation(self, time):
        self.simulation_end = datetime.datetime.strptime(time, '%H:%M').time()
        self.current_time = datetime.datetime.strptime('08:00', '%H:%M')
        self.load_packages(self.truck1)
        self.load_packages(self.truck2)
        self.load_packages(self.truck3)

        self.set_initial_next_destination(self.truck1)
        self.set_initial_next_destination(self.truck2)
        self.set_initial_next_destination(self.truck3)

        self.truck1.truck_departed = True

        while ((len(self.truck1.truck_destinations) >= 1 and
                len(self.truck2.truck_destinations) >= 1 and
                len(self.truck3.truck_destinations) >= 1) or
               (self.simulation_end >= self.current_time.time())):

            # Increments the current time by one minute each loop
            self.current_time += datetime.timedelta(minutes=1)

            # Triggers for truck 2 and truck 3 to depart
            if self.current_time.time() == datetime.datetime.strptime('09:05:00', '%H:%M:%S').time():
                self.truck2.truck_departed = True
            if self.truck1.truck_returned and self.current_time.time() >= datetime.datetime.strptime('10:20:00', '%H:%M:%S').time():
                self.packages.set_item('9', ['9', '300 State St', 'Salt Lake City', 'UT', '84103', 'EOD', '2',
                                             'Wrong address listed'])
                self.truck3.truck_departed = True

            self.update_pos_and_distance(self.truck1)
            self.update_pos_and_distance(self.truck2)
            self.update_pos_and_distance(self.truck3)

            self.set_truck_destinations(self.truck1)
            self.set_truck_destinations(self.truck2)
            self.set_truck_destinations(self.truck3)

            self.update_truck_returned(self.truck1)
            self.update_truck_returned(self.truck2)
            self.update_truck_returned(self.truck3)

    def simulation_output(self, hash_id=None):

        if hash_id is None:
            for i in range(1,41):
                self.package.append(Package.package_hash.get_item(str(i)))

                if self.package_deliveries[i] is not None:
                    self.package.append(str(self.package_deliveries[i]))

                if i in self.package_deliveries[i]:
                    for j in self.package_deliveries[i]:
                        self.package.append(self.package_deliveries[i][j+1])

                elif i in self.truck1.truck_packages and self.truck1.truck_departed:
                    self.package.append("Out for Delivery")
                    self.package.append(str(self.current_time))

                elif i in self.truck2.truck_packages and self.truck2.truck_departed:
                    self.package.eppend("Out for Delivery")
                    self.package.append(str(self.current_time))

                elif i in self.truck3.truck_packages and self.truck3.truck_departed:
                    self.package.append("Out for Delivery")
                    self.package.append(str(self.current_time))

                else:
                    self.package.append("At Hub")
                    self.package.append(str(self.current_time))

                print(self.package)
                self.package.pop()

        else:
            self.package.append(Package.package_hash.get_item(str(hash_id)))

            if self.package_deliveries[hash_id] is not None:
                self.package.append(str(self.package_deliveries[hash_id]))

            if hash_id in self.package_deliveries[hash_id]:
                for j in self.package_deliveries[hash_id]:
                    self.package.append(self.package_deliveries[hash_id][j + 1])

            elif hash_id in self.truck1.truck_packages and self.truck1.truck_departed:
                self.package.append("Out for Delivery")
                self.package.append(str(self.current_time))

            elif hash_id in self.truck2.truck_packages and self.truck2.truck_departed:
                self.package.eppend("Out for Delivery")
                self.package.append(str(self.current_time))

            elif hash_id in self.truck3.truck_packages and self.truck3.truck_departed:
                self.package.append("Out for Delivery")
                self.package.append(str(self.current_time))

            else:
                self.package.append("At Hub")
                self.package.append(str(self.current_time))

            print(self.package)
            self.package.pop()
        return
