# importamod el modulo para leer ficheros de configuración .INI
import configparser

# Instanciamos la calse ConfigParser
config = configparser.ConfigParser()

# Leemos el fichero .ini
config.read('config.ini')

# y con el método get de ConfigParser leemos los valores que queremos
# del fichero de configuración pasandole la sección y la clave
db_host = config.get('database', 'host')
db_port = config.get('database', 'port')
db_username = config.get('database', 'username')
db_password = config.get('database', 'password')

# lo mostramos por pantalla
print(db_host, db_port, db_username, db_password)


path_log = config.get('logs', 'path_log')
path_app = config.get('logs', 'path_app')

print(path_log, path_app)
