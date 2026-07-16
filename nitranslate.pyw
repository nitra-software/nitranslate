from pyperclip import copy
import landict
import wx
import translator
import threading
idiomas = landict.idiomas_naturales
diccionario=landict.idiomas

class Ventana(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title="Nitranslate, versión 26.1.4")
		panel=wx.Panel(self)
		sizer=wx.BoxSizer(wx.HORIZONTAL)
		trad1_label = wx.StaticText(panel, label="Selecciona el idioma de origen")
		sizer.Add(trad1_label, 0, wx.ALL, 5)
		self.idioma_origen = wx.Choice(panel, choices=idiomas)
		sizer.Add(self.idioma_origen, 0, wx.ALL, 5)
		self.idioma_origen.SetSelection(0)
		entertext = wx.StaticText(panel, label="Escribe aquí el texto que quieres traducir: ")
		sizer.Add(entertext, 0, wx.ALL, 5)
		self.entrada_texto = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)
		sizer.Add(self.entrada_texto, 0, wx.ALL, 5)
		trad2_label = wx.StaticText(panel, label="Selecciona el idioma de destino")
		sizer.Add(trad2_label, 0, wx.ALL, 5)
		self.idioma_destino = wx.Choice(panel, choices=idiomas)
		sizer.Add(self.idioma_destino, 0, wx.ALL, 5)
		self.idioma_destino.SetSelection(1)
		btn_trad = wx.Button(panel, label="&Traducir")
		sizer.Add(btn_trad, 0, wx.ALL, 5)
		btn_trad.Bind(wx.EVT_BUTTON, self.on_translate)
		panel.SetSizer(sizer)
		self.Show()

	def on_translate(self, event):
		self.origen = self.idioma_origen.GetStringSelection()
		idioma_origen=diccionario[self.origen]
		if idioma_origen=="":
			wx.MessageBox("No se ha seleccionado ningún idioma de origen", "Error")
			return
		self.Destino = self.idioma_destino.GetStringSelection()
		self.destino=diccionario[self.Destino]
		if self.destino=="":
			wx.MessageBox("No se ha seleccionado ningún idioma de destino", "Error")
			return
		texto = self.entrada_texto.GetValue()
		if texto=="":
			wx.MessageBox("No se ha introducido nada en el cuadro de edición para realizar la traducción", "Error")
			return
		if idioma_origen==self.destino:
			wx.MessageBox("No es posible realizar la traducción si los idiomas de origen y destino coinciden", "Error")
			return
		hilo=threading.Thread(target=translator.translate, args=(idioma_origen, self.destino, texto,))
		hilo.start()
app=wx.App()
Ventana()
app.MainLoop()
