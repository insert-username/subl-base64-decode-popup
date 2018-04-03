import sys
import sublime
import sublime_plugin

from base64_decode_popup.EncodedStringFilter import EncodedStringFilter
from base64_decode_popup.Base64EncodingAnalyzer import Base64EncodingAnalyzer
from base64_decode_popup.AggregateBaseEncodingAnalyzer import AggregateBaseEncodingAnalyzer
from base64_decode_popup.FilteredBaseEncodingAnalyzer import FilteredBaseEncodingAnalyzer
from base64_decode_popup.SettingDefaults import SETTING_DEFAULTS


class Base64DecodePopupEventListener(sublime_plugin.EventListener):


    def on_selection_modified(self, view):
        delegates = [ Base64EncodingAnalyzer(), Base64EncodingAnalyzer(variant="Url") ]

        analyzer = FilteredBaseEncodingAnalyzer(
                AggregateBaseEncodingAnalyzer(delegates), \
                Base64DecodePopupEventListener.__get_encoded_string_filter(view))

        selected_text = Base64DecodePopupEventListener.__get_selected_text(view)

        encoding_analysis = analyzer.analyze(selected_text)


        if encoding_analysis.has_encoding_details():
            Base64DecodePopupEventListener.__display_encoding_details(
                encoding_analysis.get_encoding_details(),
                view)


    @staticmethod
    def __get_settings(view):
        view_settings = view.settings().get("base64_decode_popup") or {}

        result = {}

        for setting_name in SETTING_DEFAULTS:
            result[setting_name] = view_settings.get(setting_name) or SETTING_DEFAULTS.get(setting_name)

        return result


    @staticmethod
    def __get_encoded_string_filter(view):
        settings = Base64DecodePopupEventListener.__get_settings(view)

        return EncodedStringFilter( \
            min_encoded_string_length_inclusive=settings.get("min_encoded_string_length_inclusive"), \
            max_encoded_string_length_exclusive=settings.get("max_encoded_string_length_exclusive"), \
            encoded_string_ignore_filter_regex=settings.get("encoded_string_ignore_filter_regex"))



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

        if decoded_bytes_as_utf8 is None and \
            (not Base64DecodePopupEventListener.__get_settings(view).get("display_non_utf8_byte_arrays")):
            return

        display_string = decoded_bytes_as_utf8 \
            if decoded_bytes_as_utf8 is not None \
            else encoding_details.get_decoded_bytes_as_hex_string()

        view.show_popup(
            '<h3>' + encoding_scheme_name + '</h3>' +
            '<code>' + display_string + '</code>',
            max_width=600)
