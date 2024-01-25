import json

# Open files for reading and writing
with open("cars.json", "r") as file_cars, open("cars2.json", "r") as file_cars2, open("result.json", "w") as result_file:
    # Read data from cars.json
    cars_data = json.load(file_cars)

    # Read data from cars2.json
    car2_data = json.load(file_cars2)

    # Combine both car data into a single list
    all_cars = cars_data + [car2_data]

    # Sort the list of cars by max_speed
    sorted_cars = sorted(all_cars, key=lambda x: x['max_speed'])

    # Write the sorted list to result.json
    json.dump(sorted_cars, result_file, indent=2)


