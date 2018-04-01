import binascii

from base64_decode_popup import BaseEncodingUtils
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis
from base64_decode_popup.EncodingDetails import EncodingDetails

class Base64EncodingAnalyzer:

    def analyze(self, encoded_string):
        try:
            decoded_bytes = binascii.a2b_base64(encoded_string)
            encoding_details = \
                EncodingDetails("Base64", encoded_string, decoded_bytes)
            return EncodingAnalysis(encoding_details)
        except binascii.Error:
            return EncodingAnalysis(None)