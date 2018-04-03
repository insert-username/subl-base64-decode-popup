import binascii

from base64_decode_popup.EncodingAnalysis import EncodingAnalysis
from base64_decode_popup.EncodingDetails import EncodingDetails

class Base64EncodingAnalyzer:


    VARIANTS = [
        "Url"
    ]


    def __init__(self, variant=None):
        if variant is not None and not (variant in Base64EncodingAnalyzer.VARIANTS):
            raise ValueError("Unknown Variant: " + variant)

        self.variant = variant


    def analyze(self, encoded_string):
        if self.variant == "Url":
            encoded_string = Base64EncodingAnalyzer.__base64url_to_base64(encoded_string)

        try:
            decoded_bytes = binascii.a2b_base64(encoded_string)

            variant_name = self.variant if self.variant else ""

            encoding_details = \
                EncodingDetails("Base64" + variant_name, encoded_string, decoded_bytes)
            return EncodingAnalysis(encoding_details)
        except binascii.Error:
            return EncodingAnalysis(None)


    @staticmethod
    def __base64url_to_base64(encoded_string):
        # Based off implementation found at: https://brockallen.com/2014/10/17/base64url-encoding/

        result = encoded_string \
            .replace("-", "+") \
            .replace("_", "/")

        lenMod4 = len(result) % 4

        if lenMod4 == 2:
            return result + '=='
        elif lenMod4 == 3:
            return result + '='
        else:
            return result
