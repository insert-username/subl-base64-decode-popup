import sys
import sublime
import sublime_plugin

from base64_decode_popup.BaseEncodingUtils import analyze

class Base64DecodePopupEventListener(sublime_plugin.EventListener):


    def on_selection_modified(self, view):
        selected_text = Base64DecodePopupEventListener.__get_selected_text(view)

        encoding_analysis = analyze(selected_text)

        if encoding_analysis.has_encoding_details():
            Base64DecodePopupEventListener.__display_encoding_details(
                encoding_analysis.get_encoding_details(),
                view)



    @staticmethod
    def __get_selected_text(view):
        selection = view.sel()

        selected_text = ""
        for region in selection:
            selected_text += view.substr(region)

        return selected_text


    @staticmethod
    def __display_encoding_details(encoding_details, view):
        encoding_scheme_name = encoding_details.get_encoding_scheme_name()
        decoded_bytes = encoding_details.get_decoded_bytes()

        decoded_bytes_as_utf8 = \
            encoding_details.get_decoded_bytes_as_utf8_string()

        encoded_string = encoding_details.get_encoded_string()

        display_string = decoded_bytes_as_utf8 \
            if decoded_bytes_as_utf8 is not None \
            else encoding_details.get_decoded_bytes_as_hex_string()

        view.show_popup(
            '<h3>' + encoding_scheme_name + '</h3>' +
            '<code>' + display_string + '</code>',
            max_width=600)
