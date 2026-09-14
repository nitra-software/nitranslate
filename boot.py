import main_window
import translations_handler
import no_language_selected
import wx
app=wx.App()

with open("default_language.txt", "r") as archivo:
	content=archivo.read()
	if content == "":
		ventana = no_language_selected.Ventana()
	else:
		translations_handler.set_language(content)
		ventana = main_window.Ventana()
app.MainLoop()