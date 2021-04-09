import pytest
import one_hot_encoder


def test_simple_sequence():
    test_words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    answer_test_words = one_hot_encoder.fit_transform(test_words)
    correct_answer = [
        ('first', [0, 0, 0, 0, 0, 1]),
        ('second', [0, 0, 0, 0, 1, 0]),
        ('third', [0, 0, 0, 1, 0, 0]),
        ('fourth', [0, 0, 1, 0, 0, 0]),
        ('fifth', [0, 1, 0, 0, 0, 0]),
        ('sixth', [1, 0, 0, 0, 0, 0])
    ]
    assert answer_test_words == correct_answer


def test_with_one_repeat():
    test_words = ['first', 'second', 'first', 'third', 'fourth']
    answer_test_words = one_hot_encoder.fit_transform(test_words)
    correct_answer = [
        ('first', [0, 0, 0, 1]),
        ('second', [0, 0, 1, 0]),
        ('first', [0, 0, 0, 1]),
        ('third', [0, 1, 0, 0]),
        ('fourth', [1, 0, 0, 0])
    ]
    assert answer_test_words == correct_answer


def test_with_multiple_repeats():
    test_word = ['first', 'second', 'first', 'second', 'first']
    answer_test_words = one_hot_encoder.fit_transform(test_word)
    correct_answer = [
        ('first', [0, 1]),
        ('second', [1, 0]),
        ('first', [0, 1]),
        ('second', [1, 0]),
        ('first', [0, 1])
    ]
    assert answer_test_words == correct_answer


def test_empty_args():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()