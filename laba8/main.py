import os
from time import time
import csv
import pandas


def get_directory_path() -> str:
    """
    function of getting a path from the user and checking its existence
    output of the function: we get the correct path to the directory
    """
    default_path = "./data/train/other_user_logs"
    dir_path = input("Введите пожалуйста путь до директории с файлами: ")
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            print(f"Обнаружено в директории {len(os.listdir(dir_path))} файлов")
            return dir_path
    print(f"(info) Объект не найден. Выставлен путь: {default_path}")
    return default_path


def get_session_length() -> int:
    """
    function for getting the maximum number of sites per session
    """
    message = "Введите пожалуйста максимальное количество посещенных сайтов, отображенных в одной сессии: "
    default_length = 10
    session_len = input(message)
    if session_len.isdigit():
        if 0 < int(session_len):
            return int(session_len)
    print(f"(info) Вы ввели не число. Размер сессии равен {default_length}")
    return default_length


def get_window_size() -> int:
    """
    function for getting the session window size
    """
    default_window_size = 10
    message = "Введите пожалуйста размер окна сессии: "
    window_size = input(message)
    if window_size.isdigit():
        if 0 < int(window_size):
            return int(window_size)
    print(f"(info) Вы ввели не число. Размер окна сессии равен {default_window_size}")
    return default_window_size


def get_max_duration() -> int:
    """

    """
    default_duration = 30
    message = "Введите пожалуйста максимальное кол-во минут между посещенными сайтами в разных сессиях: "
    max_duration = input(message)
    if max_duration.isdigit():
        if 0 < int(max_duration):
            return int(max_duration)
    print(f"(info) Вы ввели не число. Размер окна сессии выставлен в {default_duration} минут.")
    return default_duration


def calc_duration(func):
    """
    a decorator that outputs the execution time of a function
    """
    def decorated(*args, **kwargs):
        time_to_start = time()
        result_func = func(*args, **kwargs)
        time_to_finish = time()
        print(f"elapsed time is about {time_to_finish-time_to_start} seconds")
        return result_func

    return decorated


@calc_duration
def prepare_train_set(ogs_path: str, session_length: int, window_size: int, max_duration: int):
    "считываем файлы из директории __ogs_path__"
    """собсна чтение"""

    """
    # 1.8 на получение строк
    # 12.6 на вывод всех строк
    count_row = 0   # временно
    for file_name in os.listdir(ogs_path):
        current_name_file = ogs_path + "/" + file_name
        # получен файл
        with open(current_name_file) as file:
            reader = csv.reader(file, delimiter=',')
            for row_file in reader:
                # получена строчка из файла
                print(row_file)
                count_row += 1  # временно

    print(f"Было перебрано {count_row} строк")
    

    """
    # 5.71 на получение строк из файлов
    # 12.8 на вывод строк всех
    count_row = 0  # временно
    for file_name in os.listdir(ogs_path):
        current_name_file = ogs_path + "/" + file_name
        # получен файл
        with open(current_name_file) as file:
            df = pandas.read_csv(file)
            for rows in df.itertuples():
                count_row += 1

    print(f"Было перебрано {count_row} строк")


    "разбиваем строки на сессии"
    "  Содержит максимум __session_length__"

    ...


if __name__ == "__main__":
    directory_path = get_directory_path()
    sess_len = get_session_length()
    wind_size = get_window_size()
    maximum_duration = get_max_duration()
    print()     # вывод пустой строки

    prepare_train_set(directory_path, sess_len, wind_size, maximum_duration)
