from time import sleep, time
from random import random
import string


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
def long_executing_task():  # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index + 1}')
        sleep(random())


def suppress_errors(list_errors):
    """
    a decorator that displays a message instead of an exception
    """
    def decorator(func):
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except list_errors as err:
                print(f"error: {err}")
        return decorated
    return decorator


@suppress_errors((
    KeyError,
    ValueError,
))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]


def result_between(value_min, value_max):
    """
    decorator validating by minimum and maximum value
    """
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if value_min <= result <= value_max:
                return result
            else:
                return ValueError
        return decorated
    return decorator


def len_more_than(s_len):
    """
    decorator validating by length string
    """
    def decorator(func):
        def decorated(*args, **kwargs):
            result_func = func(*args, **kwargs)
            if len(result_func) >= s_len:
                return result_func
            else:
                return ValueError
        return decorated
    return decorator


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(100)
def show_message(message: str) -> str:
    return f'Hi, you sent: {message}'


def replace_commas(func):
    """
    decorator that replaces punctuation marks with spaces
    """
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        for i in list(string.punctuation):
            result_func = result_func.replace(i, ' ')
        return result_func
    return decorated


def words_title(func):
    """
    the decorator, in each word (a sequence of characters on both sides surrounded by a space),
    makes the first and last letter uppercase
    """
    def decorated(*args, **kwargs):
        result_func = func(*args, **kwargs)
        whitespace_positions = []
        n = 0
        for i in result_func:
            if i == ' ':
                whitespace_positions.append(n)
            n += 1
        list_result = list(result_func)
        for i in range(whitespace_positions.__len__()):
            if i == 0:
                list_result[whitespace_positions[0] + 1] = str(list_result[whitespace_positions[0] + 1]).upper()
            elif i == whitespace_positions.__len__() - 1:
                list_result[whitespace_positions[whitespace_positions.__len__() - 1] - 1] = \
                    str(list_result[whitespace_positions[whitespace_positions.__len__() - 1] - 1]).upper()
            else:
                list_result[whitespace_positions[i] - 1] = str(list_result[whitespace_positions[i] - 1]).upper()
                list_result[whitespace_positions[i] + 1] = str(list_result[whitespace_positions[i] + 1]).upper()
        return ''.join(list_result)
    return decorated


@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')


@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')


def cache_result():
    """
    decorator-cache that stores the result of executing a function for the specified arguments and returns it
    if the function is called again with a certain set of arguments.
    """
    _cache_result = {}

    def decorator(func):
        def decorated(*args, **kwargs):
            if args not in _cache_result:
                _cache_result[args] = func(*args, **kwargs)
            return _cache_result[args]
        return decorated
    return decorator


@cache_result()
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'


if __name__ == '__main__':
    long_executing_task()  # print "elapsed time is about <> seconds"

    print('\n')
    print(potentially_unsafe_func('name'))  # everything is ok
    print(potentially_unsafe_func('last_name'))  # error is silented

    print('\n')
    print(sum_of_values((1, 3, 5, 7)))  # ValueError
    print(show_message('Howdy, howdy my little friend'))  # ValueError

    print('\n')
    print(process_text('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))
    print(another_process('the French revolution resulted in 3 concepts: freedom,equality,fraternity'))

    print('\n')
    print(some_func('shulyak', 'dmitry', 30))  # call
    print(some_func('ivanov', 'ivan', 25))     # call
    print(some_func('shulyak', 'dmitry', 30))  # cache
