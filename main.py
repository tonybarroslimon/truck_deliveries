"""Antonio Barros-Limon Student ID: 000950459"""
from app import App
import sys

print("Name: Tony Barros-Limon")
print("Student ID: 000950459")
print("Python Version: 3.10.0rc2")
print("IDE: PyCharm 2021.2.1 (Professional Edition)")

simulation = App()
simulation.run_simulation("22:00")
print(f"\nAll packages were delivered in {simulation.get_total_distance()} miles.")

while True:
    print("\n1. Package Search")
    print("2. Check Current Simulation State")
    print("3. Exit Application")
    choice = input("\nPlease make a selection: ")

    if choice == '1':
        one_simulation = App()
        one_simulation.run_simulation(input("\nEnter time in 'HH:MM' format: "))
        one_simulation.simulation_output(input("Enter package ID: "))
    if choice == '2':
        two_simulation = App()
        two_simulation.run_simulation(input("\nEnter time in 'HH:MM' format: "))
        two_simulation.simulation_output()
    if choice == '3':
        sys.exit()

