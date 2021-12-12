# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

#Вариант1
print('Вариант 1')
print(list(set(ids['user1']) | set(ids['user2']) | set(ids['user3'])))

#Вариант2
print('Вариант 2')
ids_unique = []
for value in ids.values():
  for string in value:
    ids_unique.append(string)
print(list(set(ids_unique)))

#Вариант3
print('Вариант 3')
ss = set()
for value in ids.values():
  ss |= set(value)
print(list(ss))
