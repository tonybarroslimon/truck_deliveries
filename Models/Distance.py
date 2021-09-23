import csv
from Models.HashTable import HashTable


class Distance:

    def __init__(self):
        self.distance_data = list(csv.reader(open("data/distance_data.csv"), delimiter=','))
        self.address_hash = HashTable()

        with open("data/addresses.csv", delimiter = ',') as addresses:
            self.address_data = csv.reader(addresses, delimiter=',')

            for address in self.address_data:
                address_key = address[2]

                self.address_hash.set_item(address_key, [address[0], address[1], address_key])

    def distance_home(self, start):
        return float(self.distance_data[int(start)][0])

    def next_closest_stop(self, start, stops):
        start_location = int(start)
        less_stops = [int(stop) for stop in stops if int(stop) < start_location]
        more_stops = [int(stop) for stop in stops if int(stop) > start_location]
        closest_distance = 100.0
        closest_location = None

        for stop in less_stops:
            if float(self.distance_data[start_location][stop]) < float(closest_distance) and str(stop) in stops:
                closest_location = str(stop)
                closest_distance = self.distance_data[start_location][stop]

        for stop in more_stops:
            if float(self.distance_data[start_location][stop]) < float(closest_distance) and str(stop) in stops:
                closest_location = str(stop)
                closest_distance = self.distance_data[stop][start_location]

        return closest_location, closest_distance


