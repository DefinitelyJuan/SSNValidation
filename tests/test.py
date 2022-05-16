import unittest
from SSN import ValidateSSN
class validationTest(unittest.TestCase):
    def testSSN(self):
        self.assertEqual(ValidateSSN("111-@3-2!3$"), False)
        self.assertEqual(ValidateSSN("123456789"), False)
        self.assertEqual(ValidateSSN("000-11-2345"), False)
        self.assertEqual(ValidateSSN("666-11-2345"), False)
        self.assertEqual(ValidateSSN("900-11-2345"), False)
        self.assertEqual(ValidateSSN("916-11-2345"), False)
        self.assertEqual(ValidateSSN("445-00-2345"), False)
        self.assertEqual(ValidateSSN("445-24-0000"), False)
        self.assertEqual(ValidateSSN(""), False)
        self.assertEqual(ValidateSSN("13-331-2345"), False)
        self.assertEqual(ValidateSSN("1333-331-234"), False)
        self.assertEqual(ValidateSSN("326-31-2376"), True)