import unittest

from p5_Temes_Enrique import caesar_cipher, caesar_decipher, letter_frequency


class TestCaesarCipher(unittest.TestCase):
    def test_cipher_shifts_letters_and_preserves_case(self):
        self.assertEqual(caesar_cipher("Hello World", 3), "Khoor Zruog")

    def test_cipher_wraps_around_alphabet(self):
        self.assertEqual(caesar_cipher("XyZ", 3), "AbC")

    def test_cipher_preserves_non_letters(self):
        self.assertEqual(caesar_cipher("Hi, Bob! 123", 1), "Ij, Cpc! 123")

    def test_decipher_returns_original_message(self):
        original = "Meet me at 5:30 PM!"
        encrypted = caesar_cipher(original, 7)
        self.assertEqual(caesar_decipher(encrypted, 7), original)

    def test_decipher_handles_negative_shift(self):
        self.assertEqual(caesar_decipher("Bcd", -1), "Cde")


class TestLetterFrequency(unittest.TestCase):
    def test_frequency_ignores_case_and_non_letters(self):
        text = "Hello, HELLO! 123"
        expected = {"h": 2, "e": 2, "l": 4, "o": 2}
        self.assertEqual(letter_frequency(text), expected)

    def test_frequency_returns_empty_dictionary_without_letters(self):
        self.assertEqual(letter_frequency("123! ?"), {})


if __name__ == "__main__":
    unittest.main()
