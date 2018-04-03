from base64_decode_popup.EncodingAnalyzer import EncodingAnalyzer
from base64_decode_popup.EncodingAnalysis import EncodingAnalysis


class FilteredBaseEncodingAnalyzer(EncodingAnalyzer):
    """
    Analyzer which considers only results passing the
    supplied string filter.
    """


    def __init__(self, delegate, encoded_string_filter):
        self.delegate = delegate
        self.encoded_string_filter = encoded_string_filter


    def analyze(self, encoded_string):
        if self.encoded_string_filter.should_evaluate_encoded_string(encoded_string):
            return self.delegate.analyze(encoded_string)
        else:
            return EncodingAnalysis(None)
