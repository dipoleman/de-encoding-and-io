# Encoding and IO

Interacting and manipulating different file types is an important skill for any Data Engineer. These tasks should provoke you to investigate the **built in modules** available in python and experiment with the different methods they offer.

All data files can be found in the `data` directory.

`CSV` and `JSON` are the most common data types you will encounter out in the wide world of Data Engineering. Work through those tasks first, if you find time you can tackle the extension tasks working with `XML` and `YAML`.

Consider some useful data types and how you can keep your code **DRY** while working through the tasks.

## Pizza CSV

Create a script which reads the pizza data and:

1. Prints a list of dictionaries containing all of the table information.

2. Prints the description of a _Capri pizza_ in a list with each ingredient on a new line.

3. Prints all of the pizzas under £9.00 from price low to high.

4. Write to the pizza data with a new pizza of your choosing.

5. The cost of living has affected the price of pizza, increase the price of each pizza by _10%_.

## Cars JSON

Create a script which reads the cars data and:

1. Prints a list of dictionaries containing all of the table information.

2. Prints a collection of all the different car makes we have data on. There shouldn't be any repeats.

3. Prints a list of cars under 20 years old, youngest to oldest.

4. Add your dream car to the cars data.

5. The Red Ford Tempo year was actually _1985_, please reflect this in the data.

### Extension tasks:

1. In the JSON data, each car needs a `fuel` property with a value of either _petrol_ or _diesel_.

2. Create a new file, `cars.csv` by reading the json data and converting it into csv format.

3. In the CSV data, add a new header to indicate whether the pizza is suitable for `vegetarians`, then fill in the information for each pizza.

4. Create a new file, `pizzas.json` by reading the csv data and converting it into json format.

# Further tasks:

## Properties XML

Create a script which reads the properties data and:

1. Prints the cost of the largest sq.ft detached home for sale.

2. Prints the description of third home from the bungalows for sale.

3. Prints the number of bathrooms that the first flat for rent has.

4. Prints a list of all of the bungalows.

5. Prints a dictionary which lists the average property price for each property type.

6. Add a new bungalow for sale to the properties data.

7. Renting has just become even more unaffordable, increase all properties to rent by _5%_.

8. There is a new `PARK HOME` property type available to rent. This home has 2 bedrooms and cost £2000, update the data to reflect this.

## People YAML

Create a script which reads the people data and:

1. Prints Craig's job.

2. Prints Ron's interests.

3. Prints the Average age of all the people.

4. Prints a list of dictionaries representing all of the data.

5. Prints a list of people who have `Tombolas` listed in their interests.

6. Write to the yaml data to include information about yourself.

7. Add a `favourite colour` key to each person.

8. Find everyone who lives in `London` and change it to `The City`.

## Further Reading - Pandas

Pandas is an open source Python package that is most widely used for data science,data analysis and machine learning tasks.

It is something that we'll cover in more depth later in the course but it's good to know whats around the corner!

For this task you will need to research and play around with Pandas.

## _Helpful links_

[Pandas Docs](https://pandas.pydata.org/docs/)

[Learn Pandas](https://www.learnpython.org/en/Pandas_Basics)

[w3schools](https://www.w3schools.com/python/pandas/default.asp)
