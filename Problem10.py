while True:
	username = input('Введите логин :')
	if not (username in users_db.keys()):
		password = input('Введите пароль : ')
		photo_path = input('Введите путь к файлу :')
		try:
			with open('Работа с файлами/images/'+photo_path, 'rb'):
				with open('Работа с файлами/textfiles/database2.txt', 'a') as file:
					file.write(usersname + ' ' + password + ' ' +photo_path + '\n' )
					print('Вы успешно зарегистрировались\n' )
					break
		except FileNotFoundError:
		else:
			print('Пользователь с таким логином уже существует')
			elif q == '0'
			break
			print('Неправильный ввод\n'