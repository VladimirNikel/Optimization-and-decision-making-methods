import os
import numpy

input_file_name 	= 'test.csv'
finaly_word 		= "="*50 + "\nДо встречи, бро!\nNikel, 2021"
menu 			= """==================Меню=действий===================
Меню действий:
	1. Вывести все отделы
	2. Вывести сводный отчёт по отделам
	3. Сохранить сводный отчёт в CSV-файл
	4. Изменить название/путь входного файла
	5. Выйти из программы\n"""+"="*50

output_data = ""
separator = ';'

"""функция получения списка из значений "ячеек" по строкам из файла"""
def get_str_from_file(name_file: str) -> list:
	str_from_file = []
	with open(name_file, 'r') as file:
		for n, line in enumerate(file, 1):
			line = line.rstrip('\n')
			str_from_file.append(line.split(separator))
	return str_from_file

"""функция получения списка только уникальных значений из списка отделов"""
def get_unique_list_department(name_file: str) -> list:
	list_department = []
	for i in get_str_from_file(name_file):
		list_department.append(i[2])
	return set(list_department)

def get_list_data_department(name_file: str, department: str) -> list:
	out_list = []
	with open(name_file, 'r') as file:
		for n, line in enumerate(file, 1):
			line = line.rstrip('\n')
			tmp = line.split(separator)
			if tmp[2] == department:
				out_list.append([tmp[0], tmp[3], tmp[4]])
	return out_list

"""функция получения ответа от пользователя"""
def asking_questions(question: str, answer1: str, answer2: str) -> bool:
	global number_question
	print(question)
	options = {answer1: True, answer2: False}
	while option not in options:
		print('\tВыберите: {}/{}'.format(*options))
		option = input("\tВаш ответ: ")
	if options[option]:
		return True
	return False


"""вызываемый скрипт для вывода списка отделов, которые перечислены во входном файле"""
def print_departments():
	print("***************Вывод*списка*отделов***************")
	unique_list_department = get_unique_list_department(input_file_name)
	print("\nВ файле {} были перечислены следующие отделы:".format(input_file_name))
	for n, item in enumerate(unique_list_department, 1):
		print("\t{}) {}".format(n,item))

"""вызываемый скрипт для вывода сводного отчета по отделам, которые перечислены во входном файле"""
def print_report():
	global output_data
	print("*********Вывод*сводного*отчета*по*отделам*********\n")
	output_data += (f"Отчёт по файлу {input_file_name}\n")
	tmp = (f"Название отдела", "Численность", "min-max зарплата", "Средняя зарплата")
	output_data += (separator.join(tmp)+'\n')
	for n, department in enumerate(get_unique_list_department(input_file_name), 1):
		count_worker = 0
		list_salary = []

		for item_in_department in get_list_data_department(input_file_name, department):
			count_worker += 1
			list_salary.append(int(item_in_department[2]))

		fork_salary = "{}-{}".format(min(list_salary), max(list_salary))
		average_salary = str(int(numpy.average(list_salary)))

		print("Название {} отдела: {}\n\tЧисленность: {}\n\tДиапазон зарплат: {}\n\tСредняя зарплата: {}\n".format(
			n, 					#номер отдела
			department, 			#название
			count_worker,			#численность
			fork_salary,			#min-max
			average_salary			#средняя зарплата
			)
		)
		tmp = (department, str(count_worker), fork_salary, average_salary)
		output_data += (separator.join(tmp)+'\n')

	
"""функция сохранения сводного отчета в CSV-файл"""
def save_report_in_csv():
	print("*******Сохранение*сводного*отчёта*в*CSV-файл******")
	if output_data == "":
		print("\n\t\t!!!ВНИМАНИЕ!!!\nВы не сформировывали сводный отчёт. Операция прервана.\n")
		return
	while True:
		name_output_file = input("\nВведите название выходного файла: ")
		if name_output_file[-4:] != ".csv":
			name_output_file += ".csv"
		if not os.path.exists(name_output_file):
			break
		if asking_questions("\n\t\t!!!ВНИМАНИЕ!!!\nТакой файл уже существует! Вы хотите перезаписать файл?", "да", "нет"):
			break
		print("\tТогда необходимо повторить операцию.")
	print("\nИмеющийся отчет записан в файл: {}".format(name_output_file))
	file = open(name_output_file, 'w')
	file.write(output_data)
	file.close()

"""функция изменения пути входного/анализируемого файла"""
def change_file_name():
	global input_file_name
	tmp = ""
	print("************Смена*пути*входного*файла*************")
	while True:
		tmp = input("Введите полный путь до csv-файла: ")
		if os.path.exists(tmp):
			input_file_name = tmp
			break
		print("\n\t\t!!!ВНИМАНИЕ!!!\nТакого файла не существует. Проверьте правильность ввода.\n")

try:
	print("="*50,"\nПарсер CSV-файлов 3000.\nПредназначен для анализа CSV-файлов.\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")
	action_code = 0
	while True:	
		try:
			print("Для анализа используется файл: {}\n\n{}".format(input_file_name, menu))
			action_code = int(input("Ваш выбор: "))
			if action_code == 1:
				print_departments()
			elif action_code == 2:
				print_report()
			elif action_code == 3:
				save_report_in_csv()
			elif action_code == 4:
				change_file_name()
			elif action_code == 5:
				print("\n{}".format(finaly_word))
				break
			print("*"*50,"\n")
		except ValueError:
			print("Вы ввели не число. Попробуйте снова.\n")

except KeyboardInterrupt:
	print("\033A\n\n" + finaly_word)
