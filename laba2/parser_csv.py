import os
import numpy
import csv


def get_str_from_file(name_file: str, delimiter=';') -> list:
    """Function for getting a list of "cell" values by lines from a file.
    The name_file variable is required. It is used to pass the full path of the file in question.
    Output value: list of data by row."""
    str_from_file = []
    with open(name_file, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            str_from_file.append(row)
    return str_from_file


def get_unique_list_department(name_file: str, delimiter=';') -> list:
    """Function for getting a list of only unique values from a list of departments.
    The name_file variable is required and is used to pass the path of the file under investigation.
    The delimiter variable is optional and stores the delimiter character used in the file.
    Output value: a unique list of departments that were listed in the file."""
    list_department = []
    for item in get_str_from_file(name_file, delimiter):
        list_department.append(item[2])
    return list(set(list_department))


def get_list_data_department(name_file: str, department: str, delimiter=';') -> list:
    """Function for getting a list of values (full name, quarterly estimate, and current salary) of employees
    for a specific department from the input file.
    The name_file variable is required and is used to pass the path to the file under investigation.
    The department variable is required and is used to pass a string value for the department name.
    The delimiter variable is optional and stores the delimiter character used in the file.
    Output value: a list of values (full name, quarterly estimate, and current salary) of the employee
    for a specific department from the input file."""
    out_list = []
    input_date = get_str_from_file(name_file, delimiter)
    for line in input_date:
        if line[2] == department:
            out_list.append([line[0], line[3], line[4]])    # full name, quarterly estimate, and current salary
    return out_list


def asking_questions(question: str, positive_answer: str, negative_answer: str) -> bool:
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


def get_departments(name_file: str, delimiter=';') -> str:
    """The called script for displaying the list of departments that are listed in the input file.
    The name_file variable is required and is used to pass the path to the file under investigation.
    The delimiter variable is optional and stores the delimiter character used in the file.
    A string value is returned - the generated response of the function."""
    out_data = "***************Вывод*списка*отделов***************"
    unique_list_department = get_unique_list_department(name_file, delimiter)
    out_data += "\nВ файле {} были перечислены следующие отделы:".format(name_file)
    for n, item in enumerate(unique_list_department, 1):
        out_data += "\n\t{}) {}".format(n, item)
    return out_data


def get_report(name_file: str, delimiter=';') -> str:
    """The called script for displaying a summary report on the departments that are listed in the input file.
    The name_file variable is required and is used to pass the path to the file under investigation.
    The delimiter variable is optional and stores the delimiter character used in the file.
    The output is a generated report in the form of str."""

    print("*********Вывод*сводного*отчета*по*отделам*********\n")
    out_data = f"Отчёт по файлу {name_file}\n"
    tmp = (f"Название отдела", "Численность", "min-max зарплата", "Средняя зарплата")
    out_data += (separator.join(tmp)+'\n')

    # Crawling the entire file by department
    for n, department in enumerate(get_unique_list_department(name_file, delimiter), 1):
        count_worker = 0
        list_salary = []

        """ Calculating the required data (number of employees, minimum-maximum salary, and average salary) within 
        a single department."""
        for item_in_department in get_list_data_department(name_file, department):
            count_worker += 1
            list_salary.append(int(item_in_department[2]))

        fork_salary = "{}-{}".format(min(list_salary), max(list_salary))
        average_salary = str(int(numpy.average(list_salary)))

        print("Название {} отдела: {}\n\tЧисленность: {}\n\tДиапазон зарплат: {}\n\tСредняя зарплата: {}\n".format(
            n,                      # номер отдела
            department,             # название
            count_worker,           # численность
            fork_salary,            # min-max
            average_salary          # средняя зарплата
        )
        )
        tmp = (department, str(count_worker), fork_salary, average_salary)
        out_data += (separator.join(tmp)+'\n')
    return out_data


def get_name_output_file() -> str:
    """Function for getting the output file name from the user."""
    question = "\n\t\t!!!ВНИМАНИЕ!!!\nТакой файл уже существует! Вы хотите перезаписать файл?"
    while True:
        name_output_file = input("\nВведите название выходного файла: ")
        if name_output_file[-4:] != ".csv":
            name_output_file += ".csv"
        if not os.path.exists(name_output_file):
            break               # there is no file at the specified path (this is a new file)
        if asking_questions(question, "да", "нет"):
            break               # a file exists at the specified path, but it can be overwritten
        print("\tТогда необходимо повторить операцию.")
    return name_output_file


def save_report_in_csv(name_output_file: str, data_report: str) -> str:
    """Function for saving a summary report to a CSV file."""
    out_data = "\n*******Сохранение*сводного*отчёта*в*CSV-файл******"
    if data_report == "":
        out_data += "\n\t\t!!!ВНИМАНИЕ!!!\nВы не сформировывали сводный отчёт. Операция прервана.\n"
        return out_data
    with open(name_output_file, 'w', newline='') as open_file:
        open_file.write(data_report)
    out_data += "\n\nИмеющийся отчет записан в файл: {}\n".format(name_output_file)
    return out_data


def change_file_name() -> str:
    """Function for changing the path of the input / analyzed file."""
    print("************Смена*пути*входного*файла*************")
    while True:
        tmp = input("Введите полный путь до csv-файла: ")
        if tmp[-4:] == ".csv":
            if os.path.exists(tmp):
                return tmp
            print("\n\t\t!!!ВНИМАНИЕ!!!\nТакого файла не существует. Проверьте правильность ввода.\n")
        print("\n\t\t!!!ВНИМАНИЕ!!!\nЭто не CSV-файл. Проверьте правильность ввода.\n")


if __name__ == "__main__":
    start_message = "=" * 50 + """
Парсер CSV-файлов 3000.
Предназначен для анализа CSV-файлов.
Разработчик: Nikel, М30-117М-20
2021 Moscow.\n""" + "=" * 50 + "\n"
    menu = """==================Меню=действий===================
    Меню действий:
    1. Вывести все отделы
    2. Вывести сводный отчёт по отделам
    3. Сохранить сводный отчёт в CSV-файл
    4. Изменить название/путь входного файла
    5. Выйти из программы\n""" + "=" * 50
    finally_word = "=" * 50 + "\nДо встречи, бро!\nNikel, 2021"
    input_file_name = 'test.csv'
    report = ""
    separator = ';'

    try:
        print(start_message)
        action_code = 0
        while True:
            try:
                print("Для анализа используется файл: {}\n\n{}".format(input_file_name, menu))
                action_code = int(input("Ваш выбор: "))
                if action_code == 1:
                    print(get_departments(input_file_name, separator))
                elif action_code == 2:
                    report = get_report(input_file_name, separator)
                elif action_code == 3:
                    output_file = get_name_output_file()
                    print(save_report_in_csv(output_file, report))
                elif action_code == 4:
                    input_file_name = change_file_name()
                elif action_code == 5:
                    print("\n{}".format(finally_word))
                    break
                print("*"*50, "\n")
            except ValueError:
                print("Вы ввели не число. Попробуйте снова.\n")
    except KeyboardInterrupt:
        print("\033A\n\n" + finally_word)
