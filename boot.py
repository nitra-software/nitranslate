import json
import main_window
import translations_handler
import no_language_selected
import wx
app=wx.App()

with open("default_language.json", "r") as archivo:
	try:
		content = json.load(archivo)
	except json.decoder.JSONDecodeError:
		content = ""
	if content == "":
		ventana = no_language_selected.Ventana()
	else:
		translations_handler.set_language(content)
		ventana = main_window.Ventana()
app.MainLoop()