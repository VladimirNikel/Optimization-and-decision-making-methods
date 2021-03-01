from faker import Faker
import random

fake = Faker('ru_RU')				#инициализация генератора

def get_count_departments() -> int:
	"""функция получения количества отделов
	нужна, чтобы не позволить пользователю с очумелыми ручками сломать программу"""
	count_departments = 0
	while (count_departments <= 0 or count_departments >= 10):
		try:
			count_departments = int(input('Введите количество отделов в фирме: '))
		except ValueError:
			print("Это не число! Не пытайся меня обмануть, а лучше попробуй снова:")

	return count_departments






try:
	print("="*50,"\nГенератор CSV-файлов 3000.\nПредназначен для генерации CSV-файлов, использующихся для тестирования.\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")

	count_departments = get_count_departments()

	for i in range(random.randint(100,140)):
		print("{}\t{}".format(i, fake.name()))

except KeyboardInterrupt:
	print("\033A\n\n" + "="*50 + "\nДо встречи, бро!\nNikel, 2021 ")



