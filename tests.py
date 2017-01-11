import unittest
from format_price import format_price


class FormatPriceCase(unittest.TestCase):
    def test_zero_point(self):
        result = format_price('200.0')
        self.assertEqual(result, '200')

    def test_zero_comma(self):
        result = format_price('200,0')
        self.assertEqual(result, '200')

    def test_round_point(self):
        result = format_price('200.079')
        self.assertEqual(result, '200.08')

    def test_round_comma(self):
        result = format_price('200,079')
        self.assertEqual(result, '200.08')

    def test_four_digits(self):
        result = format_price('2270.02')
        self.assertEqual(result, '2 270.02')

    def test_five_digits(self):
        result = format_price('22270.02')
        self.assertEqual(result, '22 270.02')

    def test_six_digits(self):
        result = format_price('222270.02')
        self.assertEqual(result, '222 270.02')

    def test_letter_in_number(self):
        result = format_price('2w70')
        self.assertEqual(result, 'Ошибка')

    def test_no_numbers(self):
        result = format_price('Price')
        self.assertEqual(result, 'Ошибка')

    def test_empty_input(self):
        result = format_price('')
        self.assertEqual(result, 'Ошибка')


if __name__ == '__main__':
    unittest.main()
