import wx
from languages import lang, lista_de_idiomas
import translations_handler

class setLanguage(wx.Dialog):
	def __init__(self, parent=None):
		super().__init__(parent, title=_("Seleccionar idioma de la aplicación"))
		panel=wx.Panel(self)
		label1=wx.StaticText(panel, label=_("Selecciona un idioma"))
		self.selector=wx.Choice(panel, choices=list(lista_de_idiomas))
		accept=wx.Button(panel, label=_("&Aceptar"))
		accept.Bind(wx.EVT_BUTTON, self.cambiar_idioma)
		self.Show()
	def cambiar_idioma(self, event):
		selected_language=self.selector.GetStringSelection()
		selected_language_code=lang[selected_language]

		with open("default_language.txt", "r") as data:
			languages=data.read()
			languages=selected_language_code
		with open("default_language.txt", "w") as new:
			newlang=new.write(languages)
		wx.MessageBox(_("El idioma ha sido establecido. Reinicia la aplicación para aplicarlo."))
		self.Destroy()