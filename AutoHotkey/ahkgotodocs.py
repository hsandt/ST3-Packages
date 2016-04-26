import sublime, sublime_plugin
import subprocess
import os
from .utils import find_in_settings

class ahkgotodocs(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			word = self.view.substr(region)

			# If no selection, find word contained by whitespace
			if len(word) == 0:
				region = self.view.word(region)
				if region.a != 0:
					region.a = region.a - 1
				word = self.view.substr(region)
				if word[0] != '#':
					word = word[1:]

			if len(word) != 0:
				# Remove non-alpha characters
				wordalphaonly = ''
				for ch in word:
					if ch.isalpha() == True or ch == '#':
						wordalphaonly += ch
				word = wordalphaonly.replace('#', '_')
				sublime.status_message("AHKGOTODOCS Loading Documentation For: " + word)
				self.ahkgotodocs_hh(word)
				# self.ahkgotodocs_url(keyword)

	def ahkgotodocs_hh(self, keyword):
		AhkHelpPath = find_in_settings("AhkHelpPath")
		cmd = ["hh.exe", r"mk:@MSITStore:" + AhkHelpPath + r"::/docs/commands/%s.htm" % keyword]
		subprocess.Popen(cmd)

	def ahkgotodocs_url(self, keyword):
		url = "http://www.autohotkey.com/docs/commands/%s.htm" % keyword
		os.startfile(url)
