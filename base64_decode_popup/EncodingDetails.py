

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