persons = [
    {"name": "Alice", "age": 15},
    {"name": "Vladyslav", "age": 21},
    {"name": "Volodymyr", "age": 53},
    {"name": "Georgy", "age": 20},
    {"name": "Vanessa", "age": 22},
    {"name": "Pavel", "age": 18},
    {"name": "Vadim", "age": 28},
    {"name": "Svetlana", "age": 47},
]

min_age = float('inf')
max_len = float('-inf')

for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_len:
        max_len = len(person['name'])

names_min_age = [p['name'] for p in persons if p['age'] == min_age]
names_max_len = [p['name'] for p in persons if len(p['name']) == max_len]

# Посмотрел формулу, как получить средний возраст,
# пишут формулу "среднее значение = (сумма) / (количество)", будем пробовать:)

sum = 0
for person in persons:
    sum += person.get('age')

print(sum // len(persons))

print(names_min_age)
print(names_max_len)

# Вторая часть домашнего задания.

my_dict_1 = {'q': 1,
             'w': 2,
             'e': 3,
             'r': 4}
my_dict_2 = {'q': 1,
             'w': 2,
             'e1': 13,
             'r1': 14}

res = dict((key, my_dict_1[key]) for key in my_dict_1 if key in my_dict_2)

print(res)

res1 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)

print(res1)

my_dict_3 = {}

for i in my_dict_1.keys() - my_dict_2.keys():
    my_dict_3[i] = my_dict_1[i]

print(my_dict_3)

my_dict_4 = {}
for x in my_dict_1.keys() | my_dict_2.keys():
    if x in my_dict_1:
        if x in my_dict_2:
            my_dict_4[x] = [my_dict_1[x], my_dict_2[x]]
        else:
            my_dict_4[x] = my_dict_1[x]
    else:
        my_dict_4[x] = my_dict_2[x]

print(my_dict_4)