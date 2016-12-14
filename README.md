# Python Flask + PyCrypto

## Descripción

Microservicio Python Flask + PyCrypto para codificar y decodificar. Hay que considerar que la llave de encriptación debe ser un string de longitud de 16, 24 o 32.

## Test

http://localhost:5000/encode?key=1234567890123456&texto=textodeprueba

## Instalaciones

Instalación de Flask

	$ sudo apt-get update
	$ sudo apt-get install python-dev -y
	$ sudo apt-get install python-pip
	$ sudo pip install Flask
	$ sudo pip install -U flask-cors	

Instalación de PyCrypto

Descargar el archivo pycrypto-2.6.1.tar.gz, descomprimir, entrar al directoro e instalar:

	$ sudo python setup.py install

---

Fuentes :

+ http://flask.pocoo.org
+ https://flask-cors.readthedocs.io/en/latest/
+ https://pypi.python.org/pypi/pycrypto