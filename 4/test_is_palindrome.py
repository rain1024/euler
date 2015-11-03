from unittest import TestCase
from solution import is_palindrome

__author__ = 'rain'


class TestIs_palindrome(TestCase):
    def test_is_palindrome_1(self):
        self.assertTrue(is_palindrome(1))

    def test_is_palindrome_2(self):
        self.assertTrue(is_palindrome(1001))

    def test_is_palindrome_3(self):
        self.assertTrue(is_palindrome(12021))

    def test_is_palindrome_4(self):
        self.assertFalse(is_palindrome(1201))

    def test_is_palindrome_5(self):
        self.assertTrue(is_palindrome(906609))

