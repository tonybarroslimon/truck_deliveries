from app import App
import sys

print("Name: Tony Barros-Limon")
print("Student ID: 000950459")
print("Python Version: 3.10.0rc2")
print("IDE: PyCharm 2021.2.1 (Professional Edition)")

simulation = App()
simulation.run_simulation("18:00")
print(f"\nAll packages were delivered in {simulation.get_total_distance()} miles.")

while True:
    print("\n1. Package Search")
    print("2. Check Current Simulation State")
    print("3. Exit Application")
    choice = input("\nPlease make a selection: ")

    if choice == '1':
        del simulation
        simulation = App()
        simulation.run_simulation(input("\nEnter time in 'HH:MM' format: "))
        simulation.simulation_output(input("Enter package ID: "))
    if choice == '2':
        del simulation
        simulation = App()
        simulation.run_simulation(input("\nEnter time in 'HH:MM' format: "))
        simulation.simulation_output()
    if choice == '3':
        sys.exit()

