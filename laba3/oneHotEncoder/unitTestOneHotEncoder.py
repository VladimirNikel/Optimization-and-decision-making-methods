import unittest
import one_hot_encoder


class MyTestCase(unittest.TestCase):
    def test_simple_sequence(self):
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
        self.assertEqual(correct_answer, answer_test_words)

    def test_with_one_repeat(self):
        test_words = ['first', 'second', 'first', 'third', 'fourth']
        answer_test_words = one_hot_encoder.fit_transform(test_words)
        correct_answer = [
            ('first', [0, 0, 0, 1]),
            ('second', [0, 0, 1, 0]),
            ('first', [0, 0, 0, 1]),
            ('third', [0, 1, 0, 0]),
            ('fourth', [1, 0, 0, 0])
        ]
        self.assertIn(correct_answer[2], answer_test_words)
        self.assertEqual(correct_answer, answer_test_words)

    def test_with_multiple_repeats(self):
        test_word = ['first', 'second', 'first', 'second', 'first']
        answer_test_words = one_hot_encoder.fit_transform(test_word)
        correct_answer = [
            ('first', [0, 1]),
            ('second', [1, 0]),
            ('first', [0, 1]),
            ('second', [1, 0]),
            ('first', [0, 1])
        ]
        self.assertEqual(correct_answer, answer_test_words)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()


if __name__ == '__main__':
    unittest.main()
