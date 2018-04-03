import unittest

from base64_decode_popup.Base64EncodingAnalyzer import Base64EncodingAnalyzer

class Base64EncodingAnalyzerTest(unittest.TestCase):

    def test_decode_base64_string(self):
        encoded = "Zm9vIGJhciBiYXo="

        analysis = Base64EncodingAnalyzer().analyze(encoded)

        self.assertTrue(analysis.has_encoding_details())

        encoding_details = analysis.get_encoding_details()

        self.assertEqual(encoding_details.get_decoded_bytes_as_utf8_string(), "foo bar baz")
        self.assertEqual(encoding_details.get_encoding_scheme_name(), "Base64")


    def test_decode_base64url_string(self):
        encoded = "aGVsbG8gZGFya25lc3MsIG15IG9sZCBmcmllbmQ"

        analysis = Base64EncodingAnalyzer(variant="Url").analyze(encoded)

        self.assertTrue(analysis.has_encoding_details())

        encoding_details = analysis.get_encoding_details()

        self.assertEqual(encoding_details.get_decoded_bytes_as_utf8_string(),
            "hello darkness, my old friend")
        self.assertEqual(encoding_details.get_encoding_scheme_name(), "Base64Url")


if __name__ == "__main__":
    unittest.main()
