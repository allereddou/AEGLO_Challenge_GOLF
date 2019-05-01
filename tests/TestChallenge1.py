import unittest

from src.challenge_1 import c


class TestChallenge1(unittest.TestCase):

    def test_whenEmptyWordToFind_thenReturnsBaseString(self):
        to_find = ''
        base = 'hello'

        result = c(base, to_find)
        self.assertEqual(base, result)

    def test_whenWordToFindIsBaseString_thenReturnsBaseString(self):
        to_find = 'snek'
        base = 'snek'
        answer = '[' + base + ']'
        result = c(base, to_find)
        self.assertEqual(answer, result)

    def test_whenBaseContainsSpaces_thenReturnCorrectAnswer(self):
        to_find = 'world'
        base = 'Hello world'
        answer = base.split(' ')[0] + ' ' + str.format('{0}' + base.split(' ')[1] + '{1}', '[', ']')
        result = c(base, to_find)
        self.assertEqual(answer, result)

    def test_whenWordToFindContainsRepetingLetters_thenReturnsCorrectAnswer(self):
        to_find = 'hellllo'
        base = to_find + 'There'
        answer = '[' + to_find + ']There'
        result = c(base, to_find)
        self.assertEqual(answer, result)

    def test_whenWordToFindContainsSpaces_thenReturnsCorrectAnswer(self):
        to_find = 'hello johnny'
        base = 'hello my name is johnny'
        answer = '[hello] my name is [johnny]'

        result = c(base, to_find)
        self.assertEqual(answer, result)

    def test_whenWordToFindContainsUppercase_thenReturnsCorrectAnswer(self):
        to_find_string = 'Pee'
        base_string = 'Pedofile'
        answer_string = '[Pe]dofil[e]'
        result = c(base_string, to_find_string)
        self.assertEqual(result, answer_string)


if __name__ == '__main__':
    unittest.main()
