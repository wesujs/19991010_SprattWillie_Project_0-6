import os

FILENAME = 'allowed_vehicles.txt'

# Function to read vehicles from the file
def read_vehicles_from_file():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            vehicles = [line.strip() for line in file]
    else:
        vehicles = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]
        write_vehicles_to_file(vehicles)
    return vehicles

# Function to write vehicles to the file
def write_vehicles_to_file(vehicles):
    with open(FILENAME, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

def print_authorized_vehicles(vehicles):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for make in vehicles:
        print(make)

def search_authorized_vehicle(vehicles):
    search = input("""
********************************
Please Enter the full Vehicle name: """)
    if search in vehicles:
        print(search, "is an authorized vehicle\n\n")
    else:
        print(search, "is not an authorized vehicle, if you received this in error please check the spelling and try again\n\n")

def add_authorized_vehicle(vehicles):
    new_add = input("What Model Would you like to add: ")
    vehicles.append(new_add)
    write_vehicles_to_file(vehicles)
    print(f"""You have added "{new_add}" as an authorized vehicle""")

def delete_authorized_vehicle(vehicles):
    new_delete = input("Please Enter the full Vehicle name you would like to REMOVE: ")

    assurance = input(f"""Are you sure you want to remove "{new_delete}" from the Authorized Vehicles List (yes/no): """)
    
    if assurance.lower() == "yes":
        if new_delete in vehicles:
            vehicles.remove(new_delete)
            write_vehicles_to_file(vehicles)
            print(f"""You have removed "{new_delete}" as an authorized vehicle""")
        else:
            print(f"""Vehicle "{new_delete}" not found in the list""")
    else:
        print("Operation cancelled")

def onLoad():
    AllowedVehiclesList = read_vehicles_from_file()

    execution = int(input(""" 
********************************
AutoCountry Vehicle Finder v0.5
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit                         
"""))

    if execution == 1:
        print_authorized_vehicles(AllowedVehiclesList)
        onLoad()
        
    elif execution == 2:
        search_authorized_vehicle(AllowedVehiclesList)
        onLoad()

    elif execution == 3:
        add_authorized_vehicle(AllowedVehiclesList)
        onLoad()

    elif execution == 4:
        delete_authorized_vehicle(AllowedVehiclesList)
        onLoad()
    
    elif execution == 5:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    
    else:
        print("Sorry, Try Again with the available options")
        onLoad()

onLoad()
