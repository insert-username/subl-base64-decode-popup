import unittest

from base64_decode_popup.EncodingAnalysis import EncodingAnalysis
from base64_decode_popup.EncodingDetails import EncodingDetails

class EncodingAnalysisTest(unittest.TestCase):

    def test_create_without_details(self):
        encoding_analysis = EncodingAnalysis(None)

        self.assertFalse(encoding_analysis.has_encoding_details())

    def test_create_with_details(self):
        encoding_details = EncodingDetails("name", "asdf", "bytes")

        encoding_analysis = EncodingAnalysis(encoding_details)

        self.assertTrue(encoding_analysis.has_encoding_details())
        self.assertEqual(encoding_analysis.get_encoding_details(),
            encoding_details)

if __name__ == "__main__":
    unittest.main()
