import wx
from languages import lang, lista_de_idiomas
import translations_handler
import json
class setLanguage(wx.Dialog):
	def __init__(self, parent=None):
		super().__init__(parent, title=_("Seleccionar idioma de la aplicación"))
		panel=wx.Panel(self)
		label1=wx.StaticText(_("Selecciona un idioma"))
		self.selector=wx.Choice(panel, choices=lista_de_idiomas)
		accept=wx.Button(panel, label=_("&Aceptar"))
		accept.Bind(wx.EVT_BUTTON, self.cambiar_idioma)
		self.Show()
	def cambiar_idioma(self, event):
		selected_language=self.selector.GetStringSelection()
		selected_language_code=lang[selected_language]
		with open("default_language.json", "r") as data:
			languages=json.load(data)
			languages=selected_language_code
		with open("default_language.json", "w") as new:
			newlang=json.dump(languages, new)
		wx.MessageBox(_("El idioma ha sido establecido. Reinicia la aplicación para aplicarlo."), wx.OK)