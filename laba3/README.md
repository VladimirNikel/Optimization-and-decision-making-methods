# 3 лабораторная работа Методы оптимизации и принятия решений

## issue-01
<details>
<summary>Задание</summary>

Дана функция, кодирующая строку в соответствии с таблицей азбуки Морзе

```python
# полный код в файле morse.py
def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
```

Напишите на неё тесты с использованием `doctest`
</details>

<details>
<summary>Definition of Done</summary>

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* используется директива
* используется флаг
* тест с message = 'SOS'
* тест с исключением (Exception)
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и доктестами
* нет замечаний от `flake8`
</details>

<details>
<summary>Выполнение</summary>

Были дописаны доктесты:

```python
def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'

    >>> encode('TEST MESSAGE')
    '- . ... -   -- . ... ... .- --. .'

    >>> encode('Nikel') #doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    KeyError: 'i'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
```


Для выполнения доктестов, описанных в коде необходимо выполнить следующий код:

```bash
$ cd morse
$ python3 -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```

Результаты выполнения указанной команды отображены в файле `doctest_result.md`.

</details>

-----------

## issue-02
<details>
<summary>Задание</summary>

Дана функция, декодирующая строку из азбуки Морзе в английский

```python
# полный код в файле morse.py
def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)
```

Напишите на неё параметрический тест, используя `pytest.mark.parametrize`
</details>

<details>
<summary>Definition of Done</summary>

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 3 тестовых примера
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
</details>

<details>
<summary>Выполнение</summary>

Был написан отдельный файл `morse_test.py` тестирования, в котором реализовано параметрическое тестирование некоторым набором данных.
```python
import morse
import pytest


@pytest.mark.parametrize('s,exp', [
    ('... --- ...', 'SOS'),
    ('... . -.-. --- -. -..', 'SECOND'),
    ('--. --- --- -.. -....- .--- --- -...', 'GOOD-JOB'),
    ('--.- .-- . .-. - -.-- -....- -. .. -.- . .-.. -....- --... .---- -.... -....- -- .- .. -....- .---- .---- --...',
     'QWERTY-NIKEL-716-MAI-117')
])
def test_decode(s, exp):
    assert morse.decode(s) == exp
```

Чтобы выполнить тестирование при помощи библиотеки `pytest` необходимо выполнить команду:

```bash
$ cd morse
$ pytest morse_test.py
```

Результаты выполнения теста сведены в файл `paramtest_result.md`.

</details>

-----------

## issue-03
<details>
<summary>Задание</summary>

Дана функция, кодирующая значение в бинарное представление на основе порядкового номера первого встречаемого элемента\
Подробнее про `One Hot Encoding` можно прочитать тут - [How to One Hot Encode Sequence Data in Python](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/)

```python
# полный код в файле one_hot_encoder.py
def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows
```

Напишите на неё тесты с использованием `unittest`
</details>

<details>
<summary>Definition of Done</summary>

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 4 тестовых примера
* минимум 2 метода проверки (`assertEqual`, `assertNotIn`, ...)
* пример с перехватом исключения
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
</details>

<details>
<summary>Выполнение</summary>

Был написан файл, используемый для тестирования.
```python
# подробности в файле unitTestOneHotEncoder.py
import unittest
import one_hot_encoder

class MyTestCase(unittest.TestCase):
    def test_simple_sequence(self):
        ...
        self.assertEqual(correct_answer, answer_test_words)

    def test_with_one_repeat(self):
        ...
        self.assertIn(correct_answer[2], answer_test_words)
        self.assertEqual(correct_answer, answer_test_words)

    def test_with_multiple_repeats(self):
        ...
        self.assertEqual(correct_answer, answer_test_words)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()


if __name__ == '__main__':
    unittest.main()
```

Как видно из приведенного кода, в процессе тестирования выполняется 4 теста, в одном из которых присутствуют два метода проверки, также, есть тест на перехват исключения.

Чтобы выполнить тестирование при помощи библиотеки `unittest` необходимо выполнить команду:

```bash
$ cd OneHotEncoder
$ python3 -m unittest -v unitTestOneHotEncoder.py
```

Результат выполнения тестирования приведен в файле `unittest_result.md`.

</details>

-----------

## issue-04
<details>
<summary>Подробности</summary>

Дана функция, кодирующая значение в бинарное представление на основе порядкового номера первого встречаемого элемента\
Подробнее про `One Hot Encoding` можно прочитать тут - [How to One Hot Encode Sequence Data in Python](https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/)

```python
# полный код в файле one_hot_encoder.py
def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows
```

Напишите на неё тесты с использованием `pytest`
</details>

<details>
<summary>Definition of Done</summary>

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 4 тестовых примера
* пример с перехватом исключения
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
</details>

<details>
<summary>Выполнение</summary>

Был написан файл для тестирования при помощи pytest.
```python
# подробности в файле pyTestOneHotEncoder.py
import pytest
import one_hot_encoder


def test_simple_sequence():
    ...
    assert answer_test_words == correct_answer


def test_with_one_repeat():
    ...
    assert answer_test_words == correct_answer


def test_with_multiple_repeats():
    ...
    assert answer_test_words == correct_answer


def test_empty_args():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()
```

Как видно из приведенного кода, в процессе тестирования выполняется 4 теста, также, есть тест на перехват исключения.

Чтобы выполнить тестирование при помощи библиотеки `pytest` необходимо выполнить команду:

```bash
$ cd OneHotEncoder
$ python3 -m pytest pyTestOneHotEncoder.py
```

Результат выполнения тестирования приведен в файле `pyTest_result.md`.

</details>

-----------

## issue-05
<details>
<summary>Подробности</summary>

Дана функция, возвращающая текущий год. Дату и время получаем из API-worldclock

```python
# полный код в файле what_is_year_now.py
def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)
```

Напишите на неё тесты, проверяющие все сценарии работы
</details>

<details>
<summary>Definition of Done</summary>

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* добейтесь 100% покрытия кода тестами
* используйте unittest.mock для замены реального обращения к API
* предоставьте отчет о покрытии в виде директории с html файлами
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`
</details>

<details>
<summary>Выполнение</summary>

Был написан файл, содержащий тесты, с различными вариантами передачи даты в запросе.
```python
# полная версия кода приведена в файле testWhatIsYearNow.py
import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_format_v1(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"2021-04-09T19:29Z",\
        ... \
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_format_v2(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"09.04.2021T19:29Z",\
        ... \
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_exception_format(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",\
        "currentDateTime":"2021/04/09T19:29Z",\
        ... \
        "serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    with pytest.raises(Exception):
        what_is_year_now.what_is_year_now()
```

Чтобы увидеть процентное отношение покрытия кода тестами, необходимо выполнить команду:
```bash
$ cd WhatIsYearNow
$ python3 -m pytest --cov . testWhatIsYearNow.py
```

Чтобы сформировать HTML-отчет по покрытию тестами, необходимо выполнить команду:

```bash
$ cd WhatIsYearNow
$ python3 -m pytest --cov . --cov-report=html testWhatIsYearNow.py
```

Результат выполнения команд приведен в файле `result.md`.

</details>

-----------

## Ход работы:
1. Скачать/стянуть репозиторий
1. Перейдите в папку репозитория и произведите переход в папку `laba3`
1. Выполнить приведенные команды в README-файлах в каждой имеющейся папке, либо приведенные в этом `README.md`.

## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
	+ **Flake8** `sudo pip3 install flake8`
	+ **pytest** `sudo pip3 install pytest`
	+ **pytest-cov** `sudo pip3 install pytest-cov`
