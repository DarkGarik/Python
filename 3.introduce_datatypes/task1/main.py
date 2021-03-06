# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! "Познакомить" пары нам поможет функция zip, а в цикле распакуем zip-объект и выведем информацию в виде:

# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# Внимание! Если количество людей в списках будет не совпадать, то мы никого знакомить не будем и выведем пользователю предупреждение, что кто-то может остаться без пары!

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
  boys_girls = list(zip(sorted(boys), sorted(girls)))
  print('Идеальные пары:')
  for pair in boys_girls:
    print(f'{pair[0]} и {pair[1]}')
else:
  print('Внимание! Rоличество людей в списках не совпадает. Кто-то может остаться без пары!')
