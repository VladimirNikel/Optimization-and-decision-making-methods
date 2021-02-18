import random

general_family = ''
second_family  = ''

def generateStartValue():
	list_lastnames 	= ['Ивановых', 'Петровых', 'Сидоровых', 'Смирновых', 'Зайцевых', 'Семёновых', 'Кузнецовых']
	general_family 	= random.choice(list_lastnames)
	second_family 	= general_family
	while second_family == general_family:
		second_family = random.choice(list_lastnames)

def step_car():
	print("1. Отец не может решить, стоит ли семье поехать на море на своей машине?\n")
	option = ''
	options = {'да':True, 'нет':False}
	while option not in options:
		print('Выберите: {}/{}'.format(*options))
		option = input()


def step2():
	pass

def step3():
	pass

def step4():
	pass

def step5():
	pass


try:
	print("="*50,"\nOh My Duck\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")
	generateStartValue()
	print("\nСемья {}, состоящая из 4 человек уже собирается в отпуск на море, который состоится сразу после окончания коронавирусной инфекции covid-19.\nСостав семьи: отец, мать и сын с дочкой.\n".format(general_family))

	step_car()
	step2()
	step3()
	step4()
	step5()

except KeyboardInterrupt:
	print("\033A\n\n"+"="*50+"\nДо встречи, бро!\nNikel, 2021 ")