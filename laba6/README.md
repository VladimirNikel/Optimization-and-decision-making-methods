# 6 лабораторная работа Методы оптимизации и принятия решений

## Задание

- делать все на функциях
- должно работать со всеми Iterable: списки, генераторы, проч.
- по возможности возвращать генератор (ленивый объект)
- тесты на pytest + pytest-doctest, покрыть как можно больше кейсов
- в помощь: itertools, collections, funcy, google

### 1. Написать функцию получения размера генератора

```python
def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
```

### 2. Написать функцию flatten, которая из многоуровневого массива сделает одноуровневый

```python
def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
```

### 3. Написать функцию, которая удалит дубликаты, сохранив порядок

```python
def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
```

### 4. Неупорядоченная последовательность из словарей, сгруппировать по ключу, на выходе словарь

```python
def groupby(key, iterable: Iterable):
    """
    >>> users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20}, 
        {'gender': 'female', 'age': 21},
    ]
    >>> groupby('gender', users)
    {
        'female': [
            {'gender': 'female', 'age': 33},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    # Или так:
    >>> groupby('age', users)
    """
```

### 5. Написать функцию, которая разобьет последовательность на заданные куски

```python
def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
```

### 6. Написать функцию получения первого элемента или None

```python
def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
```

### 7. Написать функцию получения последнего элемента или None

```python
def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
```





## Ход работы:
1. Скачать/стянуть репозиторий
1. Перейдите в папку репозитория и произведите переход в папку "laba6" при помощи команды `cd laba6`
1. Чтобы провести тестирование при помощи написанных кейсов, выполните команду `python3 -m pytest -v .`

Результат выполнения тестов приведен в файле `result.md`.

## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
	+ **Flake8** `sudo pip3 install flake8`
    + **pytest** `sudo pip3 install pytest`
