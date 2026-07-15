from deep_translator import GoogleTranslator
import wx
from pyperclip import copy
result=""
def translate(source, target, text):
	global result
	try:
		traductor = GoogleTranslator(source, target)
		result=traductor.translate(text)
		copy(result)
		wx.MessageBox(f"Se tradujo correctamente el texto. La traducción se copió al portapapeles, y es la siguiente: {result}")
	except:
		wx.MessageBox("Se produjo un error al realizar la traducción. Verifica tu conexión a Internet y vuelve a intentarlo")