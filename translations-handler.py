import gettext
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')
DOMAIN = 'lang'

_active_translation = gettext.NullTranslations()

def set_language(lang_code):
    """Carga el idioma solicitado e instala la función global _()"""
    global _active_translation
    try:
        _active_translation = gettext.translation(
            domain=DOMAIN, 
            localedir=LOCALE_DIR, 
            languages=[lang_code]
        )
    except FileNotFoundError:
        _active_translation = gettext.NullTranslations()
    
    # Inyecta _() globalmente en todos los módulos de Python
    _active_translation.install()
    return _active_translation.gettext
