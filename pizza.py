import csv
import json

pizza_info = []
capri_pizza = {}

with open('./data/pizza.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pizza_info.append(row)
        if row['Pizza'] == 'Capri':
            capri_pizza = row

# Task 1
# print(pizza_info)

# task 2
capri_pizza_ingredients = capri_pizza['Description'].split(', ')
for ingredient in capri_pizza_ingredients:
    pass
    # print(ingredient)

# Task 3
cheap_pizza = []
for pizza in pizza_info:
    cost = float(pizza['Cost'][1:])
    if cost<=9.0:
        cheap_pizza.append(pizza)

sorted_pizza = sorted(cheap_pizza, key = lambda x: x['Cost'])
# print(sorted_pizza)


# TASK 4
with open('./data/pizza.csv', 'a', newline='') as csvfile:
    pizza_writer = csv.writer(csvfile, delimiter= ',')
    # pizza_writer.writerow(['Spinach', '£6.32', 'Spinach, cheese, tomato', '750kcal'])

# TASK 5
new_price_pizza = []
for pizza in pizza_info:
    cost = float(pizza['Cost'][1:])
    update_cost = cost + cost*0.1
    pizza['Cost'] = "£{:.2f}".format(update_cost)
    new_price_pizza.append(pizza)

# print(new_price_pizza)

flesh = ['anchovies','pepperoni','salami','ham','chicken']
# Extension Task 3
labeled_pizza = []
for pizza in new_price_pizza:
    if len(pizza['Pizza']) % 2  == 0:
        pizza['Vegetarians'] = True
        labeled_pizza.append(pizza)
    else:
        pizza['Vegetarians'] = False
        labeled_pizza.append(pizza)

# print(labeled_pizza)

with open('./data/pizza.csv', 'w', newline='') as csvfile:
    pizza_writer = csv.writer(csvfile, delimiter= ',')
    pizza_writer.writerow(['Pizza','Cost','Description', 'Vegetarians'])
    for pizza in labeled_pizza:
        pizza_writer.writerow([pizza['Pizza'], pizza['Cost'], pizza['Description'], pizza['Vegetarians']])
        


# EXTENSION TASK 4

with open('./data/pizza.json', 'w', encoding='utf-8') as f:
    json.dump({"Pizza": labeled_pizza}, f)