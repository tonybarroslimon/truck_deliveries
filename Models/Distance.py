import csv
from Models.HashTable import HashTable


class Distance:

    address_hash = HashTable()

    def __init__(self):
        self.distance_data = list(csv.reader(open("data/distance_table.csv"), delimiter=','))

        with open("data/addresses.csv") as addresses:
            self.address_data = csv.reader(addresses, delimiter=',')

            for address in self.address_data:
                address_key = address[2]

                Distance.address_hash.set_item(address_key, [address[0], address[1], address_key])

    def distance_home(self, start):
        return float(self.distance_data[int(start)][0])

    def next_closest_stop(self, start, stops):
        start_location = int(start)
        closest_distance = 100.0
        closest_location = None

        for stop in stops:
            if float(stops.index(stop)) < start_location:
                if (float(self.distance_data[start_location][stops.index(stop)]) < float(closest_distance)) and (str(stop) in stops):
                    closest_location = str(stop)
                    closest_distance = self.distance_data[start_location][stops.index(stop)]

            if float(stops.index(stop)) > start_location:
                if (float(self.distance_data[stops.index(stop)][start_location]) < float(closest_distance)) and str(stop) in stops:
                    closest_location = str(stop)
                    closest_distance = self.distance_data[stops.index(stop)][start_location]
        return closest_location, closest_distance
