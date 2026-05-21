import os
from api import copyToClip as copy
import landict
import voz
import winsound
import wx
import ui
import gui
from deep_translator import GoogleTranslator
import threading
import json
idiomas = landict.idiomas_naturales
diccionario=landict.idiomas

class Ventana(wx.Dialog):
	def __init__(self):
		try:
			with open("settings.json", "r") as f:
				settings=json.load(f)
				self.duration_time=settings["tiempo"]
		except:
			self.duration_time=10
		super().__init__(parent=gui.mainFrame, title="Nitranslate")
		panel=wx.Panel(self)
		trad1_label = wx.StaticText(panel, label="Selecciona el idioma de origen")
		self.idioma_origen = wx.Choice(panel, choices=idiomas)
		self.idioma_origen.SetSelection(1)
		btn_dictar=wx.Button(panel, label="&Dictar")
		btn_dictar.Bind(wx.EVT_BUTTON, self.iniciar_dictado)
		entertext = wx.StaticText(panel, label="Escribe aquí el texto que quieres traducir: ")
		self.entrada_texto = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.HSCROLL)
		trad2_label = wx.StaticText(panel, label="Selecciona el idioma de destino")
		self.idioma_destino = wx.Choice(panel, choices=idiomas)
		self.idioma_destino.SetSelection(5)
		btn_trad = wx.Button(panel, label="&Traducir")
		btn_trad.Bind(wx.EVT_BUTTON, self.on_translate)

	def on_translate(self, event):
		self.origen = self.idioma_origen.GetStringSelection()
		idioma_origen=diccionario[self.origen]
		if idioma_origen=="":
			ui.message("No se ha seleccionado ningún idioma de origen")
			return
		self.Destino = self.idioma_destino.GetStringSelection()
		self.destino=diccionario[self.Destino]
		if self.destino=="":
			ui.message("No se ha seleccionado ningún idioma de destino")
			return
		texto = self.entrada_texto.GetValue()
		if texto=="":
			ui.message("No se ha introducido nada en el cuadro de edición para realizar la traducción")
			return
		if idioma_origen==self.destino:
			ui.message(f"Es imposible traducir del {idioma_origen} al {self.destino}. Pillaste la indirecta, ¿No?")
			return
		try:
			traductor = GoogleTranslator(source=idioma_origen, target=self.destino)
			self.traducido = traductor.translate(texto)
			copy(self.traducido)
			ui.message(f"Texto traducido: {self.traducido}")
		except Exception as e:
			ui.message(f"No es posible realizar la traducción. Aquí tienes la traza, contacta al desarrollador si hay algún problema. {e}.")
			copy(e)

	def iniciar_dictado(self, event):
		try:
			idioma_natural=self.idioma_origen.GetStringSelection()
			idioma_voz=diccionario[idioma_natural]
			tiempo_voz=self.duration_time
			def manejador(idioma_voz, tiempo_voz):
				directorio = os.path.dirname(os.path.abspath(__file__))
				ruta_sonidos=os.path.join(directorio, "sounds")
				inicio=os.path.join(ruta_sonidos, "inicio.wav")
				fin=os.path.join(ruta_sonidos, "fin.wav")
				winsound.PlaySound(inicio, winsound.SND_FILENAME)
				obtenido=voz.dictado(idioma_voz, tiempo_voz)
				wx.CallAfter(self.entrada_texto.SetValue, obtenido)
				winsound.PlaySound(fin, winsound.SND_FILENAME)
			hilo=threading.Thread(target=manejador, args=(idioma_voz, tiempo_voz))
			hilo.start()
		except:
				ui.message("Se produjo un error durante el reconocimiento de voz")