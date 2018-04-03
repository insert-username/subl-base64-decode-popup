import unittest
from unittest.mock import Mock

from base64_decode_popup.FilteredBaseEncodingAnalyzer import FilteredBaseEncodingAnalyzer

class FilteredBaseEncodingAnalyzerTest(unittest.TestCase):

    def test_delegates_when_filter_passes(self):
        delegate = Mock()
        encoded_string_filter = Mock()
        encoded_string_filter.should_evaluate_encoded_string = lambda s: True

        FilteredBaseEncodingAnalyzer(delegate, encoded_string_filter).analyze("")

        delegate.analyze.assert_called_with("")


    def test_does_not_delegate_when_filter_fails(self):
        delegate = Mock()
        encoded_string_filter = Mock()
        encoded_string_filter.should_evaluate_encoded_string = lambda s: False

        FilteredBaseEncodingAnalyzer(delegate, encoded_string_filter).analyze("")

        delegate.analyze.assert_not_called()


if __name__ == "__main__":
    unittest.main()
