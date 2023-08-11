# Incluimos nuestro modulo para leer ficheros de configuración
from config.ConfigClass import ConfigClass

# Leemos los datos que queremos del fichero de configuración con la
# clase ConfigClass y el método Get, los parametros que se pasan son
# el fichero de configuración, la sección y la clave del valor que 
# queremos recuperar.
print( ConfigClass.Get ( 'config/config.ini', 'database', 'host'))
print( ConfigClass.Get ( 'config/config.ini', 'database', 'username'))

print( ConfigClass.Get ( 'config/config.json', 'database', 'password'))
print( ConfigClass.Get ( 'config/config.json', 'logs', 'perro'))

# comprobamos resultado si ponemos un fichero de configuracion que no existe
print( ConfigClass.Get ( 'config.txt', 'logs', 'path_app'))


