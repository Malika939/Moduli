from random import choice
rules = {'Камень': 'Бумага', 'Ножницы': 'Камень', 'Бумага' :'Ножницы'}
variants = ['Камень', 'Бумага', 'Ножницы',]
data = {'1' : 'Камень',
        '2' : 'Бумага',
        '3' : 'Ножницы',
        '0' : 'Выход', }
while True:
	human = input('1. Камень\n2.Бумага\n3.Ножницы\n0.Выход\nВыберите действие ')
	print()
	computer = rules(choice(variants))
	if human == 'Выход':
		break
	elif human in rules:
		print('Ты выбрал' , human)
		print('Компьютер выбрал, computer')
	else:
		print('Некорректный вводэ')
		continue
	if rules[computer] == humen:
		print('Ты выйграл.')
	elif rules[human] == computer:
		print('Ты проиграл.')
	else:
		print('Ничьяю')
	print()				
	pass