import sys
import re
import base64
import binascii
import codecs

from base64_decode_popup.EncodingAnalyzer import EncodingAnalyzer
from base64_decode_popup.Base64EncodingAnalyzer import Base64EncodingAnalyzer
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis
from base64_decode_popup.Base64UrlEncodingAnalyzer import Base64UrlEncodingAnalyzer


class AggregateBaseEncodingAnalyzer(EncodingAnalyzer):
    """
    Delegates to other analyzers, returning the first
    successfully analyzed result.
    """


    def __init__(self, delegates):
        self.delegates = delegates


    def analyze(self, encoded_string):
        """
        :returns: an EncodingAnalysis representing the supplied string.
        """

        for analyzer in self.delegates:
            analysis = analyzer.analyze(encoded_string)

            if analysis.has_encoding_details():
                return analysis

        return EncodingAnalysis(None)
