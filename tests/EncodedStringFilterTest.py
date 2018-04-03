import unittest

from base64_decode_popup.EncodedStringFilter import EncodedStringFilter

class EncodedStringFilterTest(unittest.TestCase):


    def test_min_length_may_be_zero(self):
        EncodedStringFilter(min_encoded_string_length_inclusive=0)


    def test_min_length_may_not_be_negative(self):
        try:
            EncodedStringFilter(min_encoded_string_length_inclusive=-1)
            self.fail()
        except ValueError as e:
            pass


    def test_max_length_exclusive_must_be_greater_than_min_length(self):
        try:
            EncodedStringFilter(max_encoded_string_length_exclusive=1)
            self.fail()
        except ValueError as e:
            pass


    def test_string_length_filter(self):
        filter = EncodedStringFilter(min_encoded_string_length_inclusive=10, \
                                     max_encoded_string_length_exclusive=21)

        self.assertFalse(filter.should_evaluate_encoded_string('a' * 3))

        self.assertFalse(filter.should_evaluate_encoded_string('a' * 9))

        self.assertTrue(filter.should_evaluate_encoded_string('a' * 10))

        self.assertTrue(filter.should_evaluate_encoded_string('a' * 20))

        self.assertFalse(filter.should_evaluate_encoded_string('a' * 21))


    def test_string_regex_filter(self):
        filter = EncodedStringFilter(min_encoded_string_length_inclusive=10, \
                                     max_encoded_string_length_exclusive=21, \
                                     encoded_string_ignore_filter_regex="l+")

        self.assertTrue(filter.should_evaluate_encoded_string('a' * 10))
        self.assertTrue(filter.should_evaluate_encoded_string('a' * 20))


        self.assertFalse(filter.should_evaluate_encoded_string('l' * 10))
        self.assertFalse(filter.should_evaluate_encoded_string('l' * 20))


if __name__ == "__main__":
    unittest.main()
