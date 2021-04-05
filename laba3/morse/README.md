# 3 лабораторная работа Методы оптимизации и принятия решений

## issue-01

### Задание

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

-----------


### Definition of Done

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* используется директива
* используется флаг
* тест с message = 'SOS'
* тест с исключением (Exception)
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и доктестами
* нет замечаний от `flake8`

-----------


### Выполнение</summary>

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
$ python3 -m doctest -o NORMALIZE_WHITESPACE -v ./morse/morse.py
```

Результаты выполнения указанной команды отображены в файле `doctest_result.md`.

-----------

## issue-02

### Задание

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

-----------


### Definition of Done

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 3 тестовых примера
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`

-----------


### Выполнение

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
pytest ./morse/morse_test.py
```

Результаты выполнения теста сведены в файл `paramtest_result.md`.
