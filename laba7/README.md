# 7 лабораторная работа Методы оптимизации и принятия решений

## Задание



### 1. Написать декоратор, который подсчитывает время выполнения функции и выводит его на консоль

```python
def calc_duration(): pass


@calc_duration
def long_executing_task():   # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index}')
        sleep(random())
        
        
long_executing_task()  # print "elapsed time is about <> seconds"
```

### 2. Написать декоратор, пропускающий заданные исключения

> Декоратор не выбрасывает ошибку, если она возникла в декорируемой функции, вместо этого выводит сообщение на консоль

```python
def suppress_errors(): pass


@suppress_errors((
    KeyError,
    ValueError,
))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]


print(potentially_unsafe_func('name'))  # everything is ok
print(potentially_unsafe_func('last_name'))  # error is silented
```

### 3. Написать декоратор, выполняющий валидацию аргументов функции

> Декоратор выполняет валидацию входных данных или результатов функции.
> 
> Примеры проверок и соответственно декораторов:
> 
> - результат должен принадлежать определённому числовому интервалу, в противном случае ошибка ValueError
> 
> - строка должна иметь длину не менее N символов, в противном случае ошибка ValueError

```python
def result_between(value_min, value_max): pass


def len_more_than(s_len): pass


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(10)
def show_message(message: str) -> str:
    return f'Hi, you sent: {message}'


sum_of_values((1, 3, 5, 7))  # ValueError
show_message('Howdy, howdy my little friend')  # ValueError
```

### 4. Реализовать наложение декораторов

> Есть 2 декоратора:
> 
> 1. Заменяет знаки препинания (запятые, точки с запятой, двоеточия и т.д.) на пробелы
> 1. В каждом слове (последовательность букв и цифр, окружённая пробелами) делает первую и последнюю букву прописной

```python
def replace_commas(func): pass


def words_title(func): pass


@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')


@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')


print(process_text('the French revolution resulted in 3 concepts: freedom,equality,fraternity')) 
print(another_process('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))
```

### 5. Написать декоратор-кэш

> Декоратор "запоминает" результат выполнения функции для заданных аргументов.
> 
> Если функция вызывается вновь с указанной последовательностью аргументов, то берём результат кэша.


```python
def cache_result(func): pass


@cache_result
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'


some_func('shulyak', 'dmitry', 30)  # call
some_func('ivanov', 'ivan', 25)     # call
some_func('shulyak', 'dmitry', 30)  # cache
```




## Ход работы:
1. Скачать/стянуть репозиторий
1. Перейдите в папку репозитория и произведите переход в папку "laba7" при помощи команды `cd laba7`
1. Чтобы запустить выполнение кода, выполните команду `python3 decorators.py`

Результат выполнения кода приведен в файле `result.md`.

## Инструменты:
- **GIT** (устанавливается командой `sudo apt install git -y`)
- **Python** (устанавливается командой `sudo apt install python3 -y`)
- Установщик пакетов **Python PIP3** (устанавливается командой `sudo apt install python3-pip -y`)
- Установленные **модули**:
	+ **Flake8** `sudo pip3 install flake8`
    + **pytest** `sudo pip3 install pytest`
