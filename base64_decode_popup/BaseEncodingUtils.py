import sys
import base64
import binascii
import codecs

from base64_decode_popup.Base64EncodingAnalyzer import Base64EncodingAnalyzer
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis
from base64_decode_popup.Base64UrlEncodingAnalyzer import Base64UrlEncodingAnalyzer

def analyze(encoded_string):
    """
    :returns: an EncodingAnalysis representing the supplied string.
    """

    # if the string is empty, it should be treated as not encoded.
    if not encoded_string:
        return EncodingAnalysis(None)

    analyzers = [
        Base64EncodingAnalyzer(),
        Base64UrlEncodingAnalyzer()
    ]

    for analyzer in analyzers:
        analysis = analyzer.analyze(encoded_string)

        if analysis.has_encoding_details():
            return analysis

    return EncodingAnalysis(None)
