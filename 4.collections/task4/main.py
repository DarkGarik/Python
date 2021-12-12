# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.

#option 1
print('Вариант 1')
print()

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
sales = 0
for value in stats.values():
  if value > sales:
    sales = value
for keys, values in stats.items():
  if values == sales:
    print(keys)
    print()

#option 2
print('Варинат 2')
print()

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
st = sorted(stats.items(), key=lambda item: item[1])
print(st[-1][0])
print()


