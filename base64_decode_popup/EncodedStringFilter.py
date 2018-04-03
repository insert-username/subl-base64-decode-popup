import re

class EncodedStringFilter:


    def __init__(self, \
        min_encoded_string_length_inclusive=1, \
        max_encoded_string_length_exclusive=1000, \
        encoded_string_ignore_filter_regex="^$"):

        if min_encoded_string_length_inclusive < 0:
            raise ValueError("""min_encoded_string_length_inclusive must be greater than
                or equal to zero""")

        if max_encoded_string_length_exclusive <= min_encoded_string_length_inclusive:
            raise ValueError("""max_encoded_string_length_exclusive must be greater than
                or equal to min_encoded_string_length_inclusive""")

        self.length_range = range( \
            min_encoded_string_length_inclusive, \
            max_encoded_string_length_exclusive)

        self.pattern = re.compile(encoded_string_ignore_filter_regex)


    def should_evaluate_encoded_string(self, encoded_string):
        return (len(encoded_string) in self.length_range) and \
            (not self.pattern.match(encoded_string))
