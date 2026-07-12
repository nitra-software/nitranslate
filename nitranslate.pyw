from pyperclip import copy
import landict
import wx
import translator
import threading
idiomas = landict.idiomas_naturales
diccionario=landict.idiomas

class Ventana(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title="Nitranslate, versión 26.1.3")
		panel=wx.Panel(self)
		trad1_label = wx.StaticText(panel, label="Selecciona el idioma de origen")
		self.idioma_origen = wx.Choice(panel, choices=idiomas)
		self.idioma_origen.SetSelection(0)
		entertext = wx.StaticText(panel, label="Escribe aquí el texto que quieres traducir: ")
		self.entrada_texto = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)
		trad2_label = wx.StaticText(panel, label="Selecciona el idioma de destino")
		self.idioma_destino = wx.Choice(panel, choices=idiomas)
		self.idioma_destino.SetSelection(1)
		btn_trad = wx.Button(panel, label="&Traducir")
		btn_trad.Bind(wx.EVT_BUTTON, self.on_translate)
		self.Show()

	def on_translate(self, event):
		self.origen = self.idioma_origen.GetStringSelection()
		idioma_origen=diccionario[self.origen]
		if idioma_origen=="":
			wx.MessageBox("No se ha seleccionado ningún idioma de origen", "Error", wx.ICON_ERROR)
			return
		self.Destino = self.idioma_destino.GetStringSelection()
		self.destino=diccionario[self.Destino]
		if self.destino=="":
			wx.MessageBox("No se ha seleccionado ningún idioma de destino", "Error", wx.ICON_ERROR)
			return
		texto = self.entrada_texto.GetValue()
		if texto=="":
			wx.MessageBox("No se ha introducido nada en el cuadro de edición para realizar la traducción", "Error", wx.ICON_ERROR)
			return
		if idioma_origen==self.destino:
			wx.MessageBox("No es posible realizar la traducción si los idiomas de origen y destino coinciden", "Error", wx.ICON_ERROR)
			return
		hilo=threading.Thread(target=translator.translate, args=(idioma_origen, self.destino, texto,))
		hilo.start()
app=wx.App()
Ventana()
app.MainLoop()
