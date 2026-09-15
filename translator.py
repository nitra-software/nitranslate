import wx
from pyperclip import copy
import requests
from urllib.parse import quote

# Mismo endpoint "no oficial" que usa la app/extensión oficial de Google
# Translate (y que usa translators.zip). No es scraping de HTML, así que
# no lo bloquea el mismo filtro anti-bot que golpea a deep_translator.
API_KEY = "AIzaSyDLEeFI5OtFBwYBIoK_jj5m32rZK5CkCXA"
TRANSLATE_URL = "https://translate-pa.googleapis.com/v1/translate"

HEADERS = {
	"Content-Type": "application/json+protobuf",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
}

session = requests.Session()
session.headers.update(HEADERS)
# Se deja por compatibilidad, en caso de que algo más del proyecto
# siga esperando poder pedir una requests.Session() "parcheada".
requests.Session = lambda: session

result = ""


def translate(source, target, text):
	global result
	try:
		# quote() es imprescindible aquí: text puede llevar espacios, "&",
		# "%", tildes, etc., y si los metemos tal cual en la url rompen la
		# petición (o incluso cambian sin querer los demás parámetros).
		texto_codificado = quote(text)
		url = (f"{TRANSLATE_URL}?params.client=gtx&query.source_language={source}&query.target_language={target}&query.text={texto_codificado}&key={API_KEY}&data_types=TRANSLATION&data_types=SENTENCE_SPLITS")
		response = session.get(url, timeout=15)
		response.raise_for_status()
		data = response.json()
		sentences = data[1] if len(data) > 1 else None
		if sentences:
			result = "".join(
				sentence[0] for sentence in sentences if sentence and sentence[0]
			)
		else:
			result = data[0] or ""
		copy(result)
		wx.MessageBox(_(f"Se tradujo correctamente el texto. La traducción se copió al portapapeles, y es la siguiente: {result}"), _("Traducción realizada con éxito"))
	except Exception:
		wx.MessageBox(_("Se produjo un error al realizar la traducción. Verifica tu conexión a Internet y vuelve a intentarlo"), _("Error"))
