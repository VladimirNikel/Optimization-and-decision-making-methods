from collections.abc import Iterable
from collections import deque


def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return len(list(iterable))


def get_one_layout(iterable: Iterable):
    """
    Recursive function for getting a one-dimensional object from a multidimensional object
    """
    output_iterable = deque()
    for x in iterable:
        if isinstance(x, (list, tuple)):
            output_iterable += get_one_layout(x)
        else:
            output_iterable.append(x)
    return output_iterable


def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    return get_one_layout(iterable)


def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    output_iterable = deque()
    for x in iterable:
        if x not in output_iterable:
            output_iterable.append(x)
    return output_iterable


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
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    # Или так:
    >>> groupby('age', users)
    """
    output_iterable = {}
    for x in iterable:
        if x[key] not in output_iterable:
            output_iterable[x[key]] = []
        output_iterable[x[key]].append(x)

    return output_iterable


def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, )]
    """
    for x in range(0, ilen(iterable), size):
        output_iterable = iterable[x: size + x]
        """
        # if you need to add None in the case when the last tuple is not complete
        if ilen(output_iterable) < size:
            output_iterable = output_iterable + [None for y in range(size - ilen(output_iterable))]
        """
        yield tuple(output_iterable)


def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    return next(iter(iterable), None)


def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    return next(reversed(iterable), None)
