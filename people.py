import yaml

with open("./data/people.yml", "r", encoding="UTF-16") as f:
    people = yaml.safe_load(f)

#  Task 1
# print(people['people'][0]['job'])

#  Task 2

for person in people['people']:
    if person['name'] == 'Ron':
        # print(person['interests'])
        pass

# TASK 3

total_age = 0
num_of_people = 0

for person in people['people']:
    if type(person['age']) == int:
        num_of_people += 1
        total_age += person['age']

print(round(total_age / num_of_people, 0))