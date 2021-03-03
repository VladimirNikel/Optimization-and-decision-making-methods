from faker import Faker
import random
import os

list_joke_string 	= [	'Это не число. Попробуй снова:',
						'Ну вот опять: ну не число это. Понимаешь? НЕ ЧИСЛО! Давай по новой:',
						'Никогда такого не было, и вот опять... Ты смеешься?',
						'Ну всё! Крайний шаг: перевожу на китайский!',
						'Выйди и зайди нормально!']
count_joke_moment 	= 5
joke 				= False
list_departments 	= []
file_name 			= 'test.csv'
new_file_name 		= 'test-old.csv'


def get_count_departments() -> int:
	"""функция получения количества отделов
	нужна, чтобы не позволить пользователю с очумелыми ручками сломать программу"""

	global list_joke_string
	global count_joke_moment
	global joke

	count_departments = 0
	"""далее код проверок написан в личных интересах (чисто поржать)"""
	while True:
		try:
			count_departments = int(input('Введите количество отделов в фирме: '))
			if (count_departments > 0 and count_departments < 10):
				return count_departments
			else:
				print("Давай это число будет от 1 до 9... А то что это за фирма такая?)\n")
		except ValueError:
			print("{}\n".format(list_joke_string.pop(0)))
			if count_joke_moment == 2:
				joke = True
			elif count_joke_moment == 1:
				exit(0)
			count_joke_moment -= 1

"""основной скрипт программы"""
try:
	print("="*50,"\nГенератор CSV-файлов 3000.\nПредназначен для генерации CSV-файлов, использующихся для тестирования.\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")

	count_departments = get_count_departments()
	if joke:
		fake = Faker('zh_CN')				#инициализация ржачного генератора
	else:
		fake = Faker('ru_RU')				#инициализация генератора

	for i in range(count_departments):
		list_departments.append(fake.bs())
	
	"""основная генерация данных"""
	if os.path.exists(file_name):
		os.rename(file_name, new_file_name)
		print("\nДля сохранения предыдущих результатов, имеющийся файл {} был переименован в {}.".format(file_name, new_file_name))

	file = open(file_name,'w')
	if file:
		current_count_record = random.randint(100,140)
		for i in range(current_count_record):
			list_param = (
				fake.name(),
				fake.job(),
				random.choice(list_departments),
				str(fake.random_int(min=1, max=5)),
				str(fake.random_int(min=25000, max=150000, step=500))
			)
			file.write(';'.join(list_param)+'\n')

		file.close()
		print("\nУспешно создан файл {} с количеством записей: {}".format(file_name, current_count_record))
		print("\n" + "="*50 + "\nДо встречи, бро!\nNikel, 2021")
		exit(0)

	print("Не удалось открыть файл. Программа завершается."+ "="*50 + "\nДо встречи, бро!\nNikel, 2021")

	
except KeyboardInterrupt:
	print("\033A\n\n" + "="*50 + "\nДо встречи, бро!\nNikel, 2021")
