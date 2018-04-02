from base64_decode_popup.EncodingAnalyzer import EncodingAnalyzer
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis


class Base64UrlEncodingAnalyzer(EncodingAnalyzer):


    def analyze(self, encoded_string):
        return EncodingAnalysis(None)
