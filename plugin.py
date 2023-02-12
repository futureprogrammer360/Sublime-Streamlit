import string
import os
import json
import webbrowser

import sublime_plugin
import sublime


def plugin_loaded():
    global links
    with open(os.path.join(sublime.packages_path(), "Streamlit", "links.json")) as f:
        links = json.load(f)


class StreamlitDocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        if region.begin() == region.end():
            selection = self.view.substr(self.view.word(region))
        else:
            selection = self.view.substr(region)

        if selection in string.whitespace:
            return

        selection = selection.strip()
        for name in links:
            command = name.split(" - ")[0].lower()
            if selection.lower() == command or selection.lower() == command.replace("st.", ""):
                link = links[name]
                webbrowser.open(link)
                break
        else:
            sublime.status_message("Streamlit doc not found for `{}`".format(selection))


class StreamlitSearchDocCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_quick_panel(
            items=list(links.items()),
            on_select=self.on_select
        )

    def on_select(self, i):
        if i == -1:
            return

        link = list(links.values())[i]
        webbrowser.open(link)
