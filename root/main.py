from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def antes_request():
	print (" Mensaje Antes de Responder la Petición")

@app.after_request
def despues_reques(response):
	print (" Mensaje despues de Resolver la Solicitud en el Servidor")
	return response

@app.route('/')
def index():
	titulo = 'Python-Web'
	name = 'Dieguito'
	curso= 'De Codigo Facilito Python-Web'
	is_premium = False
	listado_cursos = ('Python' , 'Perl' , 'Java' , 'Django')
	
	return render_template('index.html', username=name,
										title=titulo,
										name_curso=curso,
										is_premium=is_premium,
										list_cursos=listado_cursos)

# Ejemplo URLs dynamicas										
@app.route('/usuario/<Apellido>/<Nombre>/<int:edad>')
def usuario(Apellido, Nombre, edad):
	return 'Hola ' + Nombre + ' ' + Apellido + ' de: ' + str(edad) + ' Año'

# Funcion
def suma(val1, val2):
    return val1 + val2

# Intancia + Funcion
@app.route('/suma')
def suma_template():
	titulo = 'Python-Web-Suma'
	name = 'Dieguito'
	
	return render_template('suma.html', val1=10,
										val2=30, 
										funcion=suma,
										title=titulo,
										username=name)

# Intancia Ruta
@app.route('/datos')
def	Datos():
	nombre = request.args.get('nombre' , '') # Dicc + un dafault
	name_curso = request.args.get('curso' , '')
	
	return	'Listado Pasado : ' + nombre + ' ' + name_curso


# Intancia About + funcion
@app.route('/about')
def	about():
	print (" Mensaje desde la función ABOUT")
	return	render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True, port=9000)
