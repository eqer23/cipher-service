from django.test import TestCase
from .ciphers import caesar_encode

class CipherTest(TestCase):
    def test_caesar_encoded_1(self):
        plain_text = 'hello'
        shift = 1
        expected = 'ifmmp'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caesar_encoding_2(self):
        plain_text = 'winter'
        shift = 3
        expected = 'zlqwhu'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)


    def test_caesar_encoding_FLAW(self):
        #initial version doesn't take into account letters at the end
        plain_text = 'zoo'
        shift = 3
        expected = 'crr'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)
    
    def test_caesar_encoding_FLAW_2(self):
        #initial version doesn't take into account letters at the end
        plain_text = 'Winter'
        shift = 3
        expected = 'zlqwhu'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)
# Create your tests here.
