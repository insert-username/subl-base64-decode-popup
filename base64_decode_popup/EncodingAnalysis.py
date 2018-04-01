

class EncodingAnalysis:


    def __init__(self, encoding_details):
        """
        :param encoding_details: may be None.
        """
        self._encoding_details = encoding_details


    def has_encoding_details(self):
        """
        :returns: true if encoding details are available after analysis. False
        if no encoding details could be found.
        """
        return self._encoding_details is not None


    def get_encoding_details(self):
        """
        :returns: encoding details found for this analysis.
        :raises ValueError: if no encoding details are available.
        """
        if not self.has_encoding_details():
            raise ValueError("No encoding details available.")

        return self._encoding_details
