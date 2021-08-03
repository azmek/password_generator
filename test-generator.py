import unittest
import generator
import random


class TestGenerator(unittest.TestCase):
    def test_is_repeating_with_repeated_characters(self):
        repeated_password = "abccdefgh"
        total = len(repeated_password)
        self.assertEqual(generator.is_repeating(
            repeated_password, total), False)

    def test_is_repeating_with_unique_characters(self):
        unique_password = "abcdefghi"
        total = len(unique_password)
        self.assertEqual(generator.is_repeating(unique_password, total), False)

    def test_create_random_string(self):
        random_string = "abcdefg23?"
        return False

    def test_generate_random_password(self):
        random_password = random.randint(6, 30)

        return False


if __name__ == "__main__":
    unittest.main()
