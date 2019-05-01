import unittest

from src.challenge_2 import o


class TestChallenge1(unittest.TestCase):
    def test_whenEmptyWordToFind_thenReturnsBaseString(self):
        to_find = ''
        base = 'hello'

        result = c(base, to_find)
        self.assertEqual(base, result)