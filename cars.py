import json
import csv

cars_info = []

#  Task 1
with open('./data/cars.json', 'r', encoding='UTF-16') as f:
    cars = json.load(f)
    cars_info = cars['Cars']

# print(cars_info)

#  Task 2
car_makes = []

for cars in cars_info:
    car_makes.append(cars['make'])


unique_car_makes = [*set(car_makes)]

# print(unique_car_makes)


# TASK 3
young_cars = []

for car in cars_info:
    age = 2023 - car['year']
    if age < 20:
        young_cars.append(car)

sorted_young_cars = sorted(young_cars, key = lambda car: car['year'])
# print(sorted_young_cars)

#  Task 4

# cars_info.append({"vin": "WERT1234567890", 'make':"Jaguar", 'model':'spider',"year": 1963, 'colour':'red'})

with open('./data/cars.json', 'w', encoding='UTF-16') as f:
    json.dump({'Cars':cars_info}, f)


# TASK 5

updated_car_info = []
for car in cars_info:
    if car['colour'] == 'Red' and car['make'] == 'Ford' and car['model'] == 'Tempo':
        car['year'] = 1985
        updated_car_info.append(car)
    else:        
        updated_car_info.append(car)

with open('./data/cars.json', 'w', encoding='UTF-16') as f:
    json.dump({ 'Cars': updated_car_info }, f)

# Extension Task 1

cars_info_fuel = []

for car in updated_car_info:
    if car['year'] % 2 == 0:
        car['fuel'] = 'petrol'
        cars_info_fuel.append(car)
    else:
        car['fuel'] = 'diesel'
        cars_info_fuel.append(car)

with open('./data/cars.json', 'w', encoding='UTF-16') as f:
    json.dump({ 'Cars': cars_info_fuel }, f)

    
# EXTENSION Task 2

with open('./data/cars.csv', 'w', newline='') as csvfile:
    cars_writer = csv.writer(csvfile, delimiter= ',')
    cars_writer.writerow(['Vin', 'Make', 'Model', 'Year', 'Colour', 'Fuel'])
    for car in updated_car_info:
        cars_writer.writerow([car['vin'], car['make'], car['model'], car['year'], car['colour'], car['fuel']])