import unittest
from resume_tasks import braces_valid_check


class Tests(unittest.TestCase):
    def test1(self):
        self.assertTrue(braces_valid_check("d{a[sd(as)]s}"))

    def test2(self):
        self.assertTrue(braces_valid_check("I love braces!"))

    def test3(self):
        self.assertTrue(braces_valid_check(""))

    def test3(self):
        self.assertFalse(braces_valid_check("d}a(sd(as))"))

    def test4(self):
        self.assertFalse(braces_valid_check("d{a[sd(as)]} {"))

    def test5(self):
        self.assertFalse(braces_valid_check("d{a[sd(as])s}"))

    def test6(self):
        self.assertFalse(braces_valid_check('da({(sd(as))dsa}'))


if __name__ == "__main__":
    unittest.main()
