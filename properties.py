import xml.etree.ElementTree as ET

tree = ET.parse('./data/properties.xml')
root = tree.getroot()

#  Task 1

detached_homes_for_sale = []

for child in root:
    if child.tag == 'sale':
        for grand_child in child:
            if grand_child.tag == 'detached':
                for home in grand_child:
                    home_info = {}
                    for properties in home:
                        home_info[properties.tag] = properties.text
                    detached_homes_for_sale.append(home_info)

largest_plot_size = int(detached_homes_for_sale[0]['plot_size'].split(' ')[0])
largest_house_index = 0

for index, detached_home in enumerate(detached_homes_for_sale):
    square_feet = int(detached_home['plot_size'].split(' ')[0])
    if square_feet > largest_plot_size:
        largest_plot_size = square_feet
        largest_house_index = index

# print(detached_homes_for_sale[largest_house_index]['cost'])


# TASK 2

bungalows_for_sale = []

for child in root:
    if child.tag == 'sale':
        for grand_child in child:
            if grand_child.tag == 'bungalow':
                for home in grand_child:
                    home_info = {}
                    for properties in home:
                        home_info[properties.tag] = properties.text
                    bungalows_for_sale.append(home_info)

# print(bungalows_for_sale[2]['description'])


# TASK 3

flats_for_rent = []

for child in root:
    if child.tag == 'rent':
        for grand_child in child:
            if grand_child.tag == 'flat':
                for flat in grand_child:
                    flat_info = {}
                    for properties in flat:
                        flat_info[properties.tag] = properties.text
                    flats_for_rent.append(flat_info)

# print(flats_for_rent[0]['bathrooms'])

# Task 4

all_bungalows = []

for child in root:
    for grand_child in child:
        if grand_child.tag == 'bungalow':
            for home in grand_child:
                home_info = {}
                for properties in home:
                    home_info[properties.tag] = properties.text
                all_bungalows.append(home_info)

# print(len(all_bungalows))

#  Task 5

property_type_prices = {}

for child in root:
    if child.tag == 'sale':
        for grand_child in child:
            property_type = grand_child.tag
            # print(property_type)
            num_of_houses = 0
            total_cost_of_houses = 0
            for home in grand_child:
                for properties in home:
                    if properties.tag == 'cost':
                        total_cost_of_houses += int(properties.text[1:])
                num_of_houses += 1
            average_price = round(total_cost_of_houses / num_of_houses,0)
            property_type_prices[property_type] = average_price

# print(property_type_prices)

# TASK 6

for child in root:
    if child.tag == 'sale':
        for grand_child in child:
            if grand_child.tag == 'bungalow':
                home4 = ET.Element('home4')
                grand_child.append(home4)

                cost = ET.SubElement(home4, 'cost')
                description = ET.SubElement(home4, 'description')
                bedroooms = ET.SubElement(home4, 'bedroooms')
                bathrooms = ET.SubElement(home4, 'bathrooms')
                plot_size = ET.SubElement(home4, 'plot_size')

                cost.text = '£90000'
                description.text = 'A very nice house'
                bedroooms.text = '2'
                bathrooms.text = '2'
                plot_size.text = '1800 sq.ft'

                tree.write('./data/properties.xml', 'utf-8')