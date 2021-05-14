import pytest
import functional


def test_ilen_range():
    n = 17
    test_data = (x*2 for x in range(n))
    assert functional.ilen(test_data) == n


def test_ilen_list():
    test_data = [1, 2, 3, 4, 5, 6, 7]
    assert functional.ilen(test_data) == 7


def test_ilen_tuple():
    test_data = (1, 2, 3, 4, 5, 'fff',)
    assert functional.ilen(test_data) == 6


def test_ilen_string():
    test_data = 'qwertyuiop[]'
    assert functional.ilen(test_data) == 12


def test_flatten_list():
    test_data = [0, [1, [2, 3]]]
    assert list(functional.flatten(test_data)) == [0, 1, 2, 3]


def test_flatten_tuple():
    test_data = (1, 2, (3, 4, 5,), 6)
    assert tuple(functional.flatten(test_data)) == (1, 2, 3, 4, 5, 6,)


def test_flatten_combo():
    test_data = [1, 2, 3, 7, (4, 5, 6, 7,)]
    assert list(functional.flatten(test_data)) == [1, 2, 3, 7, 4, 5, 6, 7]


def test_flatten_to_tuple():
    test_data = (1, 2, 3)
    assert tuple(functional.flatten(test_data)) == (1, 2, 3, )


def test_flatten_string():
    test_data = 'string'
    assert list(functional.flatten(test_data)) == list(test_data)


def test_distinct_list():
    test_data = [1, 2, 0, 1, 3, 0, 2]
    assert list(functional.distinct(test_data)) == [1, 2, 0, 3]


def test_distinct_tuple():
    test_data = (1, 2, 4, 0, 1, 3, 0, 5, 4, 2,)
    assert tuple(functional.distinct(test_data)) == (1, 2, 4, 0, 3, 5,)


def test_distinct_not_repetitions():
    test_data = 'qwerty'
    assert list(functional.distinct(test_data)) == list(test_data)


def test_groupby_correct_key():
    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    out_data_gender = {
        'female': [
            {'gender': 'female', 'age': 33},
            {'gender': 'female', 'age': 21},
        ],
        'male': [{'gender': 'male', 'age': 20}],
    }
    out_data_age = {
        20: [
            {'age': 20, 'gender': 'male'}
        ],
        21: [
            {'age': 21, 'gender': 'female'}
        ],
        33: [
            {'age': 33, 'gender': 'female'}
        ]
    }
    assert functional.groupby('gender', users) == out_data_gender
    assert functional.groupby('age', users) == out_data_age


def test_groupby_key_error():
    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    with pytest.raises(KeyError):
        functional.groupby('list', users)


def test_chunks_with_none():
    test_data = [0, 1, 2, 3, 4]
    out_data = [(0, 1, 2), (3, 4, )]
    assert list(functional.chunks(3, test_data)) == out_data
    assert list(functional.chunks(5, list(x for x in range(8)))) == [(0, 1, 2, 3, 4), (5, 6, 7, )]


def test_chunks_without_none():
    test_data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    out_data = [(9, 8, 7), (6, 5, 4), (3, 2, 1)]
    assert list(functional.chunks(3, test_data)) == out_data


def test_first_list():
    test_data = [1, 2, 3, 4, 5]
    assert functional.first(test_data) == 1


def test_first_tuple():
    test_data = (1, 2, 3, 4, 5,)
    assert functional.first(test_data) == 1


def test_first_string():
    test_data = 'qwerty'
    assert functional.first(test_data) == 'q'


def test_first_none():
    test_data = range(0)
    assert functional.first(test_data) is None


def test_last_list():
    test_data = [1, 2, 3, 4, 5]
    assert functional.last(test_data) == 5


def test_last_tuple():
    test_data = (1, 2, 3, 4, 5,)
    assert functional.last(test_data) == 5


def test_last_string():
    test_data = 'qwerty'
    assert functional.last(test_data) == 'y'


def test_last_none():
    test_data = range(0)
    assert functional.last(test_data) is None

