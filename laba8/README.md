# 8 лабораторная работа Методы оптимизации и принятия решений

## Задание


Для решения соревнования на kaggle ["Catch Me If You Can"](https://inclass.kaggle.com/c/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2/overview) нужно построить обучающую выборку на основе данных, находящихся в архиве [train.zip/other_user_logs](https://inclass.kaggle.com/c/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2/data)

Напишите функцию `prepare_train_set(logs_path: str, session_length: int, window_size: int, max_duration: int)`
Функция должна:
* считывать файлы из директории `logs_path`
* разбивать строки на сессии. Сессия - это одна строка в выходной матрице:
    * содержит максимум `session_length` посещенных сайтов
    * каждый посещенный сайт сохраняется в виде 2-х полей: `site01`, `time01`. Если подходящих данных нет, то ставим `None`
    * поля `time01` - это объекты `datetime`, а не просто строки
    * каждая сессия содержит `ID` пользователя в виде поля `user_id`
    * `window_size` - размер смещения для подсчета следующей сессии
    * `max_duration` - максимальное кол-во минут между посещенными сайтами в разных сессиях
    * пример сессии
    
        | site01              | time01              | site02              | time02              | site03             | time03              | user_id |
        |---------------------|---------------------|---------------------|---------------------|--------------------|---------------------|---------|
        | khm1.googleapis.com | 2014-02-13 13:32:02 | maps.googleapis.com | 2014-02-13 13:32:03 | mt1.googleapis.com | 2014-02-13 13:32:03 | 237     |


* возвращать [pandas датафрейм](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) из сессий
* подсказка-01: при написании функции не используйте все файлы, возьмите 2-3 файла и запускайте функцию на них
* подсказка-02: пандас умеет [читать csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) в датафрейм, но делает это не очень быстро, так что лучше ищите другой путь
* подсказка-03: пример разделения лога посещенных сайтов на сессии, который можно использовать для написания тестов
    * имеем лог в файле `user01.csv` посещенных сайтов пользователем с `ID = 1`
    ```csv
    timestamp,site
    2013-11-15 09:28:17,vk.com
    2013-11-15 09:33:04,oracle.com
    2013-11-15 09:52:48,oracle.com
    2013-11-15 11:37:26,geo.mozilla.org
    2013-11-15 11:40:32,oracle.com
    2013-11-15 11:40:34,google.com
    2013-11-15 11:40:35,accounts.google.com
    2013-11-15 11:40:37,mail.google.com
    2013-11-15 11:40:40,apis.google.com
    2013-11-15 11:41:35,plus.google.com
    ```
    * разделить данный лог на сессии с параметрами `session_length = 4`, `window_size = 2`, `max_duration = 30` можно так
    ```csv
    timestamp,site
    2013-11-15 09:28:17,vk.com
    2013-11-15 09:33:04,oracle.com
    2013-11-15 09:52:48,oracle.com
    -- новая сессия из-за того, что
     - следующий сайт посещен более чем через 30 минут
    2013-11-15 09:52:48,oracle.com
    -- новая сессия из-за того, что 
     - следующий сайт посещен более чем через 30 минут
     - сместились на window_size сайтов вперед и по этому начали с oracle.com
    2013-11-15 11:37:26,geo.mozilla.org
    2013-11-15 11:40:32,oracle.com
    2013-11-15 11:40:34,google.com
    2013-11-15 11:40:35,accounts.google.com
    -- новая сессия из-за того, что 
     - посетили session_length сайтов
     - сместились на window_size сайтов вперед, но в предыдущую сессию не вошел geo.mozilla.org и по этому он не учитывается в смещении на window_size
    2013-11-15 11:40:34,google.com
    2013-11-15 11:40:35,accounts.google.com
    2013-11-15 11:40:37,mail.google.com
    2013-11-15 11:40:40,apis.google.com
    -- новая сессия из-за того, что 
     - посетили session_length сайтов
    2013-11-15 11:40:37,mail.google.com
    2013-11-15 11:40:40,apis.google.com
    2013-11-15 11:41:35,plus.google.com
    -- новая сессия из-за того, что 
     - записи закончились
    ```

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* произведено профилирование при помощи `сProfile` и создан файл `program.prof` с отчетом
* отрабатывает для всех файлов в `other_user_logs` не дольше 1 минуты (у меня вышло 43 секунды) с параметрами `session_length=10`, `window_size=10`, `max_duration=30`
* как минимум 4 осмысленных тестов
* файл `README.m`d с описанием шагов для запуска тестов к заданию
* файл `result` с командами и результатами запуска тестов к заданию
* нет замечаний от `flake8`





## Ход работы:
1. Скачать/стянуть репозиторий
1. Перейдите в папку репозитория и произведите переход в папку "laba8" при помощи команды `cd laba8`
1. Чтобы запустить выполнение кода, выполните команду `python3 main.py`
1. Чтобы запустить профилирование кода, выполните команду 
    ```bash 
    pyhon3 -m cProfile -o program.prof main.py
    snakeviz program.prof 
    ```

Результат выполнения кода приведен в файле `result.md`.

## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
	+ **Flake8** `sudo pip3 install flake8`
    + **pytest** `sudo pip3 install pytest`
    + **snakeviz** `sudo pip3 install snakeviz`
