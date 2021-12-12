# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

my_dict ={}
all_words = 0
for string in queries:
  string_lengh = len(string.split())
  my_dict.setdefault(string_lengh, [])
  my_dict[string_lengh].append(string)
for words in my_dict.values():
  all_words += len(words)
for num, word in my_dict.items():
  percent = len(word) / all_words *100
  print(f'Запрос из {num} слов(а) составляет {round((percent),1)}%')
  