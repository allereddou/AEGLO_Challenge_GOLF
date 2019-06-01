import unittest

from src.challenge_5 import c


class TestChallenge1(unittest.TestCase):

    def test_whenMatchingEmptyWords_thenEditDistanceIsZero(self):
        a = ''
        b = ''

        result, distance = c(a, b)
        self.assertEqual(distance, 0)

    def test_whenMatchingWithEmptyWord_thenEditDistanceIsWordLength(self):
        a = 'test'
        b = ''

        result, distance = c(a, b)
        self.assertEqual(distance, len(a))

    def test_whenMatchingSimilarWords_thenEditDistanceIsZero(self):
        a = 'hello'
        b = a

        result, distance = c(a, b)
        self.assertEqual(distance, 0)

    def test_whenMatchingWordsWithNoSimilarLetters_thenEditDistanceIsLongestWordLength(self):
        shortest_word = 'qqq'
        longest_word = 'aaaaa'

        result, distance = c(shortest_word, longest_word)
        self.assertEqual(distance, len(longest_word))


if __name__ == '__main__':
    unittest.main()
