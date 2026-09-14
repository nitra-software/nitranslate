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
		wx.MessageBox(f_("Se tradujo correctamente el texto. La traducción se copió al portapapeles, y es la siguiente: {result}"), _("Traducción realizada con éxito"))
	except:
		wx.MessageBox(_("Se produjo un error al realizar la traducción. Verifica tu conexión a Internet y vuelve a intentarlo"), _("Error"))