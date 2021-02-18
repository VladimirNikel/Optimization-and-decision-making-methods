import random

general_family 	= ''
second_family  	= ''
result 			= ''
number_question = 1
ussing_pre_word = False
pre_word 		= "\nВозьмут с собой: "

def generateStartValue():
	global general_family
	global second_family
	list_lastnames 	= ['Ивановых', 'Петровых', 'Сидоровых', 'Смирновых', 'Зайцевых', 'Семёновых', 'Кузнецовых']
	general_family 	= random.choice(list_lastnames)
	second_family 	= general_family
	while second_family == general_family:
		second_family = random.choice(list_lastnames)


def asking_questions(question: str, answer1: str, answer2: str):
	global number_question
	print(question)
	option = ''
	options = {answer1: True, answer2: False}
	while option not in options:
		print('Выберите: {}/{}'.format(*options))
		option = input("Ваш ответ: ")
	number_question += 1
	if options[option]:
		return True
	return False

def step_car():													#1
	global result
	question = "{}. Отец не может решить, стоит ли семье поехать на море на своей машине?\n".format(number_question)
	if asking_questions(question,'да','нет'):
		result += "Семья поедет на море на своей машине. "
		return step_rent()		#9
	return step_join()			#5

def step_raft():												#2
	global result
	global ussing_pre_word
	question = "\n{}. Стоит ли брать надувной плот?\n".format(number_question)
	if asking_questions(question, 'да', 'нет'):
		return step_availability()	#7
	result += "."
	return True							#выход
	
def step_flippers():											#3
	global result
	global ussing_pre_word
	question = "\n{}. Стоит ли отцу взять с собой ласты для себя и сына?\n".format(number_question)
	if asking_questions(question, 'да', 'нет'):
		if not ussing_pre_word:
			result += pre_word
			ussing_pre_word = True
		result += "ласты"
	return step_lifeline()			#6

def step_bus():													#4
	global result
	question = "\n{}. Может тогда им воспользоваться автобусным маршрутом?\n".format(number_question)
	if asking_questions(question, 'да', 'нет'):
		result += "Семья поедет автобусом. "
		return step_rent()			#9
	print("Получается, они не едут никуда. Теперь где-то грустят несколько детей.")
	return False						#выход

def step_join():												#5
	global result
	question = "\n{}. Может тогда им объединиться с семьей {} и поехать в их minivan'е?\n".format(number_question, second_family)
	if asking_questions(question, 'да', 'нет'):
		result += "Семья поедет вместе с семьей {}. ".format(second_family)
		return step_rent()				#9
	return step_bus()					#4

def step_lifeline():											#6
	global result
	global ussing_pre_word
	question = "\n{}. Брать ли для дочки надувной круг?\n".format(number_question, second_family)
	if asking_questions(question, 'да', 'нет'):
		if not ussing_pre_word:
			result += pre_word
			ussing_pre_word = True
		else:
			result += ", "
		result += "надувной круг"
	return step_fridge()				#8

def step_availability():										#7
	global result
	global ussing_pre_word
	question = "\n{}. А есть ли он дома? Или его нужно покупать?\n".format(number_question)
	if asking_questions(question, 'купить', 'есть'):
		if ussing_pre_word:
			result += "."
		result += " Еще необходимо купить надувной плот в магазине."
	if not ussing_pre_word:
		result += pre_word
		ussing_pre_word = True
	else:
		result += ", "
	result += "надувной плот."
	return True							#выход

def step_fridge():												#8
	global result
	global ussing_pre_word
	question = "\n{}. Нужно ли брать с собой переносной холодильник для еды?\n".format(number_question)
	if asking_questions(question, 'нужно', 'нет'):
		if not ussing_pre_word:
			result += pre_word
			ussing_pre_word = True
		else:
			result += ", "
		result += "холодильник"
	return step_raft()					#2

def step_rent():												#9
	global result
	question = "\n{}. Стоит ли арендовать отдельный домик на берегу моря?\n".format(number_question)
	if asking_questions(question, 'конечно', 'нет'):
		result += "\nПомимо этого они арендуют домик на берегу моря, на время отдыха."
		return step_flippers()			#3
	return step_hotel()					#10

def step_hotel():
	global result
	question = "\n{}. Стоит ли снимать отель?\n".format(number_question)
	if asking_questions(question, 'конечно', 'нет'):
		result += "\nБудут снимать номер в отеле."
		return step_flippers()			#3
	print("\n\nСемье негде будет ночевать. С такими планами поездка отменяется. Дети расстроены.")
	return False						#выход


try:
	print("="*50,"\nOh My Duck\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")
	generateStartValue()
	print("\nСемья {}, состоящая из 4 человек уже собирается в отпуск на море, который состоится сразу после окончания коронавирусной инфекции covid-19.\nСостав семьи: отец, мать и сын с дочкой.\n".format(general_family))

	if step_car():
		print("\n\n" + "="*50 + "\n" + result + "\n" + "="*50 + "\nДо встречи, бро!\nNikel, 2021 ")


except KeyboardInterrupt:
	print("\033A\n\n" + "="*50 + "\nДо встречи, бро!\nNikel, 2021 ")