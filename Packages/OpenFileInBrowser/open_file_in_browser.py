import sublime_plugin
import webbrowser

class OpenFileInBrowserCommand(sublime_plugin.WindowCommand):

	def run(self):

		active_file = self.window.active_view().file_name()
		url = active_file.replace('C:\wamp\www\\', 'http://127.0.0.1/')
		webbrowser.open_new_tab(url)

		print 'Opening file', active_file, 'in browser...'