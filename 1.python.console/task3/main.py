salary = int(input('Введите заработную плату в месяц: '))
mortgage_perc = int(input('Введите, какой процент(%) уходит на ипотеку: '))
life_perc = int(input('Введите, какой процент(%) уходит на жизнь: '))
mortgage_cash = salary // 100 * mortgage_perc * 12
print()
print('На ипотеку было потрачено:', mortgage_cash)
life_cash = (salary - (salary // 100 * (mortgage_perc + life_perc))) * 12
print('Было накоплено:', life_cash)