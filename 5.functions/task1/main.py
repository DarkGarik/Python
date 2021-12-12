documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

def get_people(documents):
  number = input('Введите номер документа: ')
  for numbers in documents:
    if str(numbers['number']) == str(number):
      people = numbers['name']
      return people
  return "Нет такого документа"
  
def get_directories(directories):
  number = input('Введите номер документа: ')
  for dir in directories.items():
    for dir1 in dir[1]:
      if dir1 == number:
        return dir[0]
  return "Нет такого документа"

def get_documents(documents):
  docs = str()
  for doc in documents:
    for obj in list(doc.values()):
      docs += '"'
      docs += str(obj)
      docs += '"'
      docs += " "
    docs = docs[0:-1] + ";\n"
  return docs

def add_documents(directories):
  in_number = input('Введите номер документа: ')
  in_type = input('Введите тип документа: ')
  in_name = input('Введите Имя и Фамилию владельца: ')
  while True:
    in_dir = input('Введите номер полки: ')
    if in_dir in directories:
      documents.append({"type": in_type, "number": in_number, "name": in_name})
      directories[in_dir].append(in_number)
      result = (f'Документ с номером {in_number} добавлен на полку {in_dir} успешно')
      break
    elif in_dir == "q":
      result = "Документ не добавлен"
      break
    else:
      print(f'Полки с номером {in_dir} не существует, попробуйте ввести другой номер или наберите "q" для выхода')
  return result

# Задача №2
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

def del_documents(directories):
  in_doc = input('Введите номер документа: ')
  for dir, doc in directories.items():
    if in_doc in doc:
      for doc_doc in documents:
        if in_doc in doc_doc['number']:
          documents.remove(doc_doc)
          del(directories[dir][directories[dir].index(in_doc)])
          result = ("Документ удален")
          return result
  result = ("Документ не найден")
  return result

def move_documents(directories):
  in_doc = input('Введите номер документа: ')
  in_dir = input('Введите номер полки: ')
  for dir, doc in directories.items():
    if in_doc in doc:
      print(dir)
      for dir, doc in directories.items():
        if in_dir in dir:
          print(doc)
          result = ("OK")
          return result  
      result = ("Ошибка")
      return result   
    else:
      result = ("Dir error")
      return result 
  


print(move_documents(directories))

# def main():
#   while True:
#     user_input = input('Введите команду ("h" для справки): ')
#     if user_input == "p":
#       print(get_people(documents))
#     elif user_input == "s":
#       print(get_directories(directories))
#     elif user_input == "l":
#       print(get_documents(documents))
#     elif user_input == "a":
#       print(add_documents(directories))
#     elif user_input == "d":
#       print(del_documents(directories))
#     elif user_input == "h":
#       print("h- help - справка.\np – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\ns – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\nl– list – команда, которая выведет список всех документов;\na – add – команда, которая добавит новый документ в каталог и в перечень полок.\nd – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.\nq - выход.")
#     elif user_input == "q":
#       break

# main()