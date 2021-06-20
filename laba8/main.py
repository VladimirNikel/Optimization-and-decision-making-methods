import os
from time import time
import csv
import pandas
import numpy as np
import re
from datetime import datetime


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
    function for getting the maximum amount of time between site visits
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
        print(f"\ncompleted in about {time_to_finish - time_to_start} seconds")
        return result_func

    return decorated


@calc_duration
def prepare_train_set(ogs_path: str, session_length: int, window_size: int, max_duration: int):
    """
    function for processing files in a session
    """
    session_is_open = False
    time_start_session = datetime(2021, 6, 17, 0, 10, 36)
    data_headers = []
    data_dataframe = []
    #reason_for_finish_previous_session = ""

    "считываем файлы из директории __ogs_path__"
    # 1.8s на получение строк
    # 12.6s на вывод всех строк
    # 34.92 на обработку и вывод строк согласно сессиям в виде print()
    # 450 секунд на вывод вместе с использование pandas.DataFrame (вместе с профилированием)
    # 163 секунды - просто выполняя код из под python
    for file_name in os.listdir(ogs_path):
        #reason_for_finish_previous_session = ""
        current_name_file = ogs_path + "/" + file_name
        id_user = int(re.search('(\d\d*).csv$', file_name).group(1))

        # получен файл
        with open(current_name_file) as file:
            reader = csv.reader(file, delimiter=',')
            last_session = []

            if csv.Sniffer().has_header(file.read(1024)):
                file.seek(0)        # обнаружены заголовки, но возвращаемся в начало файла
                next(reader, None)  # отсечение первой строчки файла с заголовками
            else:
                file.seek(0)        # возвращаемся в начало файла
            """можно оптимизировать оставив только 
            next(reader, None)
            при условии, что все файлы начинаются с заголовков
            но я решил оставить данную проверку, на всякий случай"""

            current_session_length = 0

            for row_file in reader:
                # получена строчка из файла
                datetime_row = datetime.strptime(row_file[0], '%Y-%m-%d %H:%M:%S')
                site_row = row_file[1]

                if not session_is_open:
                    #print(reason_for_finish_previous_session)
                    session_is_open = True
                    current_session_length = 0
                    time_start_session = datetime_row

                # условия останова
                if session_is_open and current_session_length >= session_length:
                    session_is_open = False
                    """reason_for_finish_previous_session = "-- новая сессия из-за того, что\n" \
                                                         " - посетили session_length сайтов"
                                                         """
                    data_headers.append('user_id')
                    data_dataframe.append(id_user)

                if session_is_open and \
                        ((datetime_row - time_start_session).total_seconds() / 60 >= max_duration):
                    session_is_open = False
                    """reason_for_finish_previous_session = f"-- новая сессия из-за того, что\n" \
                                                         f" - следующий сайт посещен больше чем через {max_duration}" \
                                                         f" минут"
                                                         """
                    data_headers.append('user_id')
                    data_dataframe.append(id_user)

                # тут делаем основную работу
                if session_is_open:
                    #print(f"time: {datetime_row} & site: {site_row}")
                    data_headers.append('site' + str(current_session_length+1).zfill(2))
                    data_headers.append('time' + str(current_session_length+1).zfill(2))
                    data_dataframe.append(site_row)
                    data_dataframe.append(datetime_row)
                    current_session_length += 1

                    # реализация использования windows_size
                    # область применения пока не понятна
                    last_session.append([site_row, datetime_row])
                    while len(last_session) > window_size:
                        last_session.pop(0)

            session_is_open = False
            #reason_for_finish_previous_session = "-- новая сессия из-за того, что\n - записи кончились"

    #print(reason_for_finish_previous_session)
    return pandas.DataFrame(np.array([data_dataframe]), columns=data_headers)


if __name__ == "__main__":
    directory_path = get_directory_path()
    sess_len = get_session_length()
    wind_size = get_window_size()
    maximum_duration = get_max_duration()

    prepare_train_set(directory_path, sess_len, wind_size, maximum_duration)
