from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>T-Hola Mundo Dos</title>
  </head>
  <body>
    <h1>Hola gente de códigofacilito</h1>
  </body>
</html>
"""

def application(environ, start_response):
    headers = [ ('Content-type', 'text/html; charset=utf-8') ]

    start_response('200 OK', headers)

    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()


#
# Otra Parte
#Como no puedo enviar por ahora parametros... entonces

print('Vamos a Sumar dos Números')


def suma(a=0, b=0):
	"""  Este es la Suma."""
	print('Suma dos valores...')
	print(str(a) + ' + ' + str(b) + ' = ')
	return a + b

print(suma(4, 5))

# Fin