import wx
from languages import lang, lista_de_idiomas

class Ventana(wx.Dialog):
	def __init__(self, parent=None):
		super().__init__(parent, title="Select a language")
		panel=wx.Panel(self)
		maininfo=wx.StaticText(panel, label="It looks like this is the first time you have oppened the program. Please, select a language to continue, you can change it in the app's main window.")
		label1=wx.StaticText(panel, label="Choose a language")
		self.selector=wx.Choice(panel, choices=list(lista_de_idiomas))
		accept=wx.Button(panel, label="&OK")
		accept.Bind(wx.EVT_BUTTON, self.set_default)
		self.Show()

	def set_default(self, event):
		selected_language=self.selector.GetStringSelection()
		selected_language_code=lang[selected_language]

		with open("default_language.txt", "r") as data:
			languages=data.read()
			languages=selected_language_code
		with open("default_language.txt", "w") as new:
			newlang=new.write(languages)

		wx.MessageBox("The default language has been establised. Restart the program to aply the new language")