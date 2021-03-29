from faker import Faker
import random
import os
import csv

""" It is a decoration of the program. """
joke = False


def get_count_departments() -> int:
    """Function for getting the number of departments from the user.
    Errors from entering non-numbers are handled, and the number is checked for matching the range from 1 to 9."""

    joke_string = [
        'Это не число. Попробуй снова:',
        'Ну вот опять: ну не число это. Понимаешь? НЕ ЧИСЛО! Давай по новой:',
        'Никогда такого не было, и вот опять... Ты смеешься?',
        'Ну всё! Крайний шаг: перевожу на китайский!',
        'Выйди и зайди нормально!']
    count_joke_moment = 5
    global joke

    """далее код проверок написан в личных интересах (чисто поржать)"""
    while True:
        try:
            my_count_departments = int(input('Введите количество отделов в фирме: '))
            if 0 < my_count_departments < 10:
                return my_count_departments
            else:
                print("Давай это число будет от 1 до 9... А то что это за фирма такая?)\n")

        # catching the error of entering a non-number
        except ValueError:
            print("{}\n".format(joke_string.pop(0)))
            if count_joke_moment == 2:
                joke = True
            elif count_joke_moment == 1:
                exit(0)
            count_joke_moment -= 1


if __name__ == "__main__":
    start_message = "=" * 50 + """
Генератор CSV-файлов 3000.
Предназначен для генерации CSV-файлов, использующихся для тестирования.
Разработчик: Nikel, М30-117М-20\n2021 Moscow.\n""" + "="*50 + "\n"
    finally_word = "=" * 50 + "\nДо встречи, бро!\nNikel, 2021"
    list_departments = []
    name_file = 'test.csv'
    new_name_file = 'test-old.csv'
    separator = ';'

    try:
        fake = Faker('ru_RU')					        # initializing the Faker generator
        if joke:
            fake = Faker('zh_CN')				        # initializing the joke Faker generator
        print(start_message)                            # print start_message - it's menu
        count_departments = get_count_departments()     # request for the count of departments

        # filling in the list of departments with data from the Faker
        for i in range(count_departments):
            list_departments.append(fake.bs())

        # checking for a file with the specified name
        if os.path.exists(name_file):
            os.rename(name_file, new_name_file)
            print("\nДля сохранения предыдущих результатов, имеющийся файл {} был переименован в {}.".format(
                name_file,
                new_name_file))

        with open(name_file, 'w', newline='') as open_file:
            count_record_in_file = random.randint(100, 140)
            for i in range(count_record_in_file):
                set_param = (
                    fake.name(),											# full name
                    fake.job(),												# job
                    random.choice(list_departments),						# one of departments
                    str(fake.random_int(min=1, max=5)),						# quarterly assessment
                    str(fake.random_int(min=25000, max=150000, step=500))   # current salary
                )
                writer = csv.writer(open_file, delimiter=separator)
                writer.writerow(set_param)

            print(f"\nУспешно создан файл {name_file} с количеством записей: {count_record_in_file}\n{finally_word}")
            exit(0)

        print("Не удалось открыть/создать файл. Программа завершается." + finally_word)
        exit(0)

    except KeyboardInterrupt:
        print("\033A\n\n" + finally_word)
