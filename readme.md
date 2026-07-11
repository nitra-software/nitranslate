# Nitranslate
## 1. Introducción
Nitranslate es un programa cuya función principal es permitirte traducir textos de una forma sencilla y rápida.

## 2. Modo de uso
* Al ejecutar la aplicación, el foco caerá sobre el cuadro combinado para seleccionar el idioma origen. Puedes seleccionarlo con las flechas arriba y abajo.
* luego, encontrarás un cuadro de edición, en el que introducirás el texto que quieres traducir.
* El siguiente control es un botón, como, cuyo nombre indica, se utiliza para realizar la traducción y copiarla al portapapeles.
### Nota para los usuarios de Linux
Para aquellos que utilizéis Linux, es necesario tener el paquete xclip para copiar el texto al portapapeles.

## Empaquetar el programa para que sea un ejecutable
En este apartado explicaremos como empaquetar este programa en un .binario ejecutable (Linux) o un archivo .zip (Windows):
### Windows
* Para empezar, la versión de python que usamos es la 3.13 para nuestro flujo de trabajo
* Creamos un entorno virtual (python3 -m venv env) y entramos a él
* instalamos los siguientes paquetes: deep-translator, wxPython, pyperclip y pyinstaller
* Luego, en la raíz del repositorio, ejecutamos pyinstaller nitranslate.pyw, y tendremos una carpeta con el programa y todas sus dependencias

### Linux
En Linux la cosa es muy similar. Ten en cuenta que la versión de python que use tu distribución tiene que ser compatible con pyinstaller, deep-translator y wxPython.  
Dado que hay gran variedad de distribuciones, opté por explicaros como empaquetar el programa en [Debian](https://debian.org).  
* En primer lugar, actualizamos todos los paquetes: sudo apt update && sudo apt upgrade -y
* Instalaremos wxPython desde los repositorios de apt (dado que al instalarlo con pip da error) con el siguiente comando: sudo apt install python3-wxgtk4.0
* Luego, creamos un entorno virtual con los paquetes del sistema incluidos: python3 -m venv env --system-site-packages
* Entramos a él con el siguiente comando: source env/bin/activate
* Instalamos los paquetes desde pip: pip install pyinstaller pyperclip deep-translator
* Por último, creamos el archivo ejecutable, que en este caso será de un único archivo para su fácil integración, por ejemplo, con archivos .deb de debian: pyinstaller --onefile nitranslate.pyw
