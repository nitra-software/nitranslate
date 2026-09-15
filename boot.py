import gettext
gettext.install("lang")
from pathlib import Path
import translations_handler
import no_language_selected
import wx

app=wx.App()
if Path("default_language.txt").exists():
	with open("default_language.txt", "r") as archivo:
		content=archivo.read()
		if content == "":
			ventana = no_language_selected.Ventana()
		else:
			translations_handler.set_language(content)
			import main_window
			ventana = main_window.Ventana()
else:
	with open("default_language.txt", "w") as creado:
		ventana = no_language_selected.Ventana()
app.MainLoop()