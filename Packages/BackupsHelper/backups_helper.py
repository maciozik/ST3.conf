import sublime_plugin
import os
import shutil

class BackupsHelperCommand(sublime_plugin.WindowCommand):

    def run(self):

        active_file = self.window.active_view().file_name()
        save_dir = os.path.dirname(active_file) + '/.save/'

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        shutil.copy(active_file, save_dir)