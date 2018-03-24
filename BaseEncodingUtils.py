import sys
import base64
import binascii
import codecs


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


class EncodingDetails:


    def __init__(self, encoding_scheme_name, encoded_string, decoded_bytes):
        self._encoding_scheme_name = encoding_scheme_name
        self._encoded_string = encoded_string
        self._decoded_bytes = decoded_bytes


    def get_encoding_scheme_name(self):
        """
        :returns: the string name representation of the encoding scheme used to
        encode the bytes.
        """

        return self._encoding_scheme_name


    def get_encoded_string(self):
        return self._encoded_string


    def get_decoded_bytes(self):
        return self._decoded_bytes


    def get_decoded_bytes_as_utf8_string(self):
        """
        Attempts to convert the decoded_bytes into their corresponding UTF-8
        string.
        :returns: the decoded bytes as a UTF-8 string, or None if conversion is
        not possible.
        """
        try:
            return self._decoded_bytes.decode("utf-8")
        except:
            return None


    def get_decoded_bytes_as_hex_string(self):
        return " ".join(format(e, 'x') for e in self._decoded_bytes)


def analyze(encoded_string):
    """
    :returns: an EncodingAnalysis representing the supplied string.
    """

    # if the string is empty, it should be treated as not encoded.
    if not encoded_string:
        return EncodingAnalysis(None)

    try:
        decoded_bytes = binascii.a2b_base64(encoded_string)
        encoding_details = \
            EncodingDetails("Base64", encoded_string, decoded_bytes)
        return EncodingAnalysis(encoding_details)
    except binascii.Error:
        return EncodingAnalysis(None)
