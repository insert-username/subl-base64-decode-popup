import sublime
import sublime_plugin


class Base64DecodePopupEventListener(sublime_plugin.EventListener):


    def on_selection_modified(self, view):
        selected_text = Base64DecodePopupEventListener.__get_selected_text(view)

        view.show_popup("<p>" + selected_text + "</p>")


    @staticmethod
    def __get_selected_text(view):
        selection = view.sel()

        selected_text = ""
        for region in selection:
            selected_text += view.substr(region)

        return selected_text
