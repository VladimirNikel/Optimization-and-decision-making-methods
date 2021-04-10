# 3 лабораторная работа Методы оптимизации и принятия решений

## issue-05

### Задание

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

-----------


### Definition of Done

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* добейтесь 100% покрытия кода тестами
* используйте unittest.mock для замены реального обращения к API
* предоставьте отчет о покрытии в виде директории с html файлами
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`

-----------


### Выполнение</summary>

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
$ python3 -m pytest --cov . testWhatIsYearNow.py
```

Чтобы сформировать HTML-отчет по покрытию тестами, необходимо выполнить команду:

```bash
$ python3 -m pytest --cov . --cov-report=html testWhatIsYearNow.py
```

Результат выполнения команд приведен в файле `result.md`.