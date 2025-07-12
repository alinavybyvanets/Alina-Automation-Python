from lesson_12.homeworks12 import add_sum, multiplication_table, arefmetic, reverse_string, words_list
import unittest
class TestAddSum(unittest.TestCase):
    def test_add_sum(self):
        self.assertEqual(add_sum(2, 3), 5)
        self.assertNotEqual(add_sum(2,3), 6)
if __name__ == '__main__':
    unittest.main()

class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table_3(self):
        result = [
                "3 x 1 = 3",
                "3 x 2 = 6",
                "3 x 3 = 9",
                "3 x 4 = 12",
                "3 x 5 = 15",
                "3 x 6 = 18",
                "3 x 7 = 21",
                "3 x 8 = 24"
                  ]
        self.assertEqual(multiplication_table(3), result)

    def test_multiplication_table_3_last_element(self):
         result = multiplication_table(3)
         last_element = result[-1]
         value = int(last_element.split('=')[1].strip())
         self.assertLessEqual(value, 25)

class TestArefmetic(unittest.TestCase):
    def test_arefmetic(self):
        self.assertEqual(arefmetic([2, 4]), 3)

    def test_arefmetic_empty(self):
        self.assertIsNone(arefmetic([]))

    def test_arefmetic_zero(self):
        self.assertEqual(arefmetic([0, 0]), 0)

    def test_arefmetic_minus(self):
        self.assertEqual(arefmetic([-4, -6]), -5)

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_string_empty(self):
        self.assertIsNone(reverse_string(""))

class TestWordsList(unittest.TestCase):
    def test_words_list(self):
        self.assertEqual(words_list(["hello", "Alina", "Vybyvanets"]), "Vybyvanets")
    def test_words_list_empty(self):
        self.assertIsNone(words_list([]))