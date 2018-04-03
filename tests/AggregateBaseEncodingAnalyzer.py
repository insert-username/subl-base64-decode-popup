import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from base64_decode_popup.AggregateBaseEncodingAnalyzer import AggregateBaseEncodingAnalyzer
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis

class AggregateBaseEncodingAnalyzerTest(unittest.TestCase):

    def test_delegates_called_until_successful_analysis(self):
        delegate0 = Mock()
        delegate0.analyze = MagicMock(return_value=EncodingAnalysis(None))

        delegate1 = Mock()
        delegate1.analyze = MagicMock(return_value=EncodingAnalysis(Mock()))

        delegate2 = Mock()
        delegate2.analyze = MagicMock(return_value=EncodingAnalysis(Mock()))

        delegates = [
            delegate0,
            delegate1,
            delegate2
        ]

        AggregateBaseEncodingAnalyzer(delegates).analyze("")

        delegate0.analyze.assert_called_with("")
        delegate1.analyze.assert_called_with("")
        delegate2.analyze.assert_not_called()


if __name__ == "__main__":
    unittest.main()
