
import zipfile
from datetime import datetime
from celery import Celery

app = Celery( 'tasks' , broker = 'redis://localhost:6379/0' )

# Creamos una tarea llamada sumar_numeros usando el decorador @app.task
# Se imprime un mensaje con la fecha simulando un LOG
@app.task
def sumar_numeros(x, y):
    print ("-> Se generó una tarea [{}]: {} + {}".format(datetime.now(), x, y))
    return x + y

# Creamos una tarea llamada hola
@app.task
def hola(nombre):
        return 'Hola %s' % nombre

@app.task
def comprimir(filename, zipname, new_path):
    print ('\n-> Se va a comprimir el archivo: {}'.format(filename))
    zfile = zipfile.ZipFile(new_path + '/' + zipname, 'w')
    zfile.write(filename, compress_type = zipfile.ZIP_DEFLATED)
    zfile.close()
    print ('\n-> El archivo comprimido se copió a : {}'.format(new_path))

