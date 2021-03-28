import random

# It is a decoration of the program.
result = ''                             # variable for storing the resulting message for the selected user responses.
using_pre_word = False                  # variable that reflects the use of pre_word.
pre_word = "\nВозьмут с собой: "
SET_LASTNAMES = ('Ивановых', 'Петровых', 'Сидоровых', 'Смирновых', 'Зайцевых', 'Семёновых', 'Кузнецовых',)


def generating_family_name(second_family_name="") -> str:
    """Generating a family name from an existing set of surnames.
    The second_family_name variable is optional, and is only needed to generate a unique family name.
    Use it only when you need to generate a family name that is not equal to the one passed in the variable.
    Returns the selected family name."""
    family_name = random.choice(SET_LASTNAMES)
    while second_family_name == family_name:
        family_name = random.choice(SET_LASTNAMES)
    return family_name


def asking_questions(question: str, positive_answer: str, negative_answer: str):
    """The function of asking the transmitted context-question.
    The question variable must contain the question string.
    The positive_answer variable must contain the string value of the positive response that will be offered to the user.
    The negative_answer variable must contain the value of the negative response that will be offered to the user.
    Returns True if a positive response option is selected, and False if a negative response option is selected."""
    print(question)
    option = ''
    options = {positive_answer: True, negative_answer: False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input("Ваш ответ: ")
    return options[option]


def step_car(second_family: str, number_question=1):
    """First question - Starting question
    about choosing a car as a means of transportation.
    The second_family variable that will be passed to the underlying function."""
    global result
    question = "{}. Отец не может решить, стоит ли семье поехать на море на своей машине?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        result += "Семья поедет на море на своей машине. "
        return step_rent(number_question)                   # go next step - 4 question
    return step_join(second_family, number_question)        # go next step - 2 question


def step_join(second_family: str, number_question: int):
    """Second question
    is whether to go with another family in their car.
    The second_family variable accepts the last name of the family with which the first family will travel."""
    global result
    question = f"\n{number_question}. Может тогда им объединиться с семьей {second_family} и поехать в их minivan'е?\n"
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        result += "Семья поедет вместе с семьей {}. ".format(second_family)
        return step_rent(number_question)				    # go next step - 4 question
    return step_bus(number_question)					    # go next step - 3 question


def step_bus(number_question: int):
    """Third question
    Take the bus route."""
    global result
    question = "\n{}. Может тогда им воспользоваться автобусным маршрутом?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        result += "Семья поедет автобусом. "
        return step_rent(number_question)			        # go next step - 4 question
    print("\n\nПолучается, они не едут никуда. Теперь где-то грустят несколько детей.")
    return False						    # exit, because the family will not be able to travel.


def step_rent(number_question: int):
    """Fourth question
    The question of renting a house."""
    global result
    question = "\n{}. Стоит ли арендовать отдельный домик на берегу моря?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'конечно', 'нет'):
        result += "\nПомимо этого они арендуют домик на берегу моря, на время отдыха."
        return step_flippers(number_question)			    # go next step - 5 question
    return step_hotel(number_question)					    # go next step - 6 question


def step_hotel(number_question: int):
    """Fifth question
    The question of renting a hotel."""
    global result
    question = "\n{}. Стоит ли снимать отель?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'конечно', 'нет'):
        result += "\nБудут снимать номер в отеле."
        return step_flippers(number_question)			    # go next step - 6 question
    print("\n\nСемье негде будет ночевать. С такими планами поездка отменяется. Дети расстроены.")
    return False						    # exit, because the family has nowhere to spend the night.


def step_flippers(number_question: int):
    """Sixth question
    Should I take fins?"""
    global result
    global using_pre_word
    question = "\n{}. Стоит ли отцу взять с собой ласты для себя и сына?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        if not using_pre_word:
            result += pre_word
            using_pre_word = True
        result += "ласты"
    return step_lifeline(number_question)			        # go next step - 7 question


def step_lifeline(number_question: int):
    """Seventh question
    Should I take a lifeline?"""
    global result
    global using_pre_word
    question = "\n{}. Брать ли для дочки надувной круг?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        if not using_pre_word:
            result += pre_word
            using_pre_word = True
        else:
            result += ", "
        result += "надувной круг"
    return step_fridge(number_question)				    # go next step - 8 question


def step_fridge(number_question: int):
    """Eighth question
    Should I take a portable refrigerator?"""
    global result
    global using_pre_word
    question = "\n{}. Нужно ли брать с собой переносной холодильник для еды?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'нужно', 'нет'):
        if not using_pre_word:
            result += pre_word
            using_pre_word = True
        else:
            result += ", "
        result += "холодильник"
    return step_raft(number_question)                      # go next step - 9 question


def step_raft(number_question: int):
    """Ninth question
    Should I take an inflatable raft?"""
    global result
    global using_pre_word
    question = "\n{}. Стоит ли брать надувной плот?\n".format(number_question)
    number_question += 1
    if asking_questions(question, 'да', 'нет'):
        return step_availability(number_question)          # go next step - 10 question
    result += "."
    return True                             # exit, because completing the survey


def step_availability(number_question: int):
    """The tenth question
    Is there an inflatable raft or should I buy one?"""
    global result
    global using_pre_word
    question = "\n{}. А есть ли он дома? Или его нужно покупать?\n".format(number_question)
    if asking_questions(question, 'купить', 'есть'):
        if using_pre_word:
            result += "."
        result += " Еще необходимо купить надувной плот в магазине."
        return True
    if not using_pre_word:
        result += pre_word
        using_pre_word = True
    else:
        result += ", "
    result += "надувной плот."
    return True                                     # exit, because completing the survey


if __name__ == "__main__":
    try:
        print("="*50, "\nOh My Duck\nРазработчик: Nikel, М30-117М-20\n2021 Moscow.\n"+"="*50, "\n")
        final_phrase = "="*50 + "\nДо встречи, бро!\nNikel, 2021 "
        first_fam = generating_family_name()
        second_fam = generating_family_name(first_fam)
        history_message = """
Семья {}, состоящая из 4 человек уже собирается в отпуск на море, 
который состоится сразу после окончания коронавирусной инфекции covid-19.  
Состав семьи: отец, мать, сын и дочка.
""".format(first_fam)
        print(history_message)
        if step_car(second_fam):
            print("\n\n" + "="*50 + "\n" + result + "\n" + final_phrase)
        else:
            print("\n\n" + "="*50 + "\nИтог: Семья не едет на отдых.\n" + final_phrase)
    except KeyboardInterrupt:
        print("\033A\n\n" + final_phrase)
