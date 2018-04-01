import unittest

from base64_decode_popup.Base64EncodingAnalyzer import Base64EncodingAnalyzer

class Base64EncodingAnalyzerTest(unittest.TestCase):

    def test_decode_base64_string(self):
        encoded = "Zm9vIGJhciBiYXo="

        analysis = Base64EncodingAnalyzer().analyze(encoded)

        self.assertTrue(analysis.has_encoding_details())

        encoding_details = analysis.get_encoding_details()

        self.assertEquals(encoding_details.get_encoding_scheme_name(), "Base64")

if __name__ == "__main__":
    unittest.main()