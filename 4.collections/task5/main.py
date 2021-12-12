# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
my_dict = {}
default = str()
my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list.reverse()
one = my_list[0]
for el in my_list:
  if el ==  one:
    pass
  elif el != one:
    if not my_dict:
      my_dict[el] = one
    else:
      my_dict = {el:my_dict}
print(my_dict)