# 3 лабораторная работа Методы оптимизации и принятия решений

## issue-03

### Задание

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

-----------


### Definition of Done

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 4 тестовых примера
* минимум 2 метода проверки (`assertEqual`, `assertNotIn`, ...)
* пример с перехватом исключения
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`

-----------


### Выполнение</summary>

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
$ python3 -m unittest -v unitTestOneHotEncoder.py
```

Результат выполнения тестирования приведен в файле `unittest_result.md`.

-----------

## issue-04

### Задание

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

-----------


### Definition of Done

**DoD (Definition of Done) - критерии, позволяющие понять, что задача сделана, как ожидается**:
* минимум 4 тестовых примера
* пример с перехватом исключения
* файл README.md с описанием шагов для запуска
* файл result с командами и результатами запуска
* файл *.py с функцией и тестами
* нет замечаний от `flake8`

-----------


### Выполнение

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
$ python3 -m pytest pyTestOneHotEncoder.py
```

Результат выполнения тестирования приведен в файле `pyTest_result.md`.

