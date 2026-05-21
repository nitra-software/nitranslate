import speech_recognition as sr

def dictado(idioma, tiempo_espera):
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		audio = recognizer.listen(source, timeout=tiempo_espera)
	try:
		result = recognizer.recognize_google(audio, language=idioma)
		return result
	except sr.UnknownValueError:
		raise Exception("Algo salió mal")
	except sr.RequestError:
		raise Exception("No se pudo conectar con el servicio de reconocimiento")