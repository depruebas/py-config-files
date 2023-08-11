# Importamos el modulo para trabajar con ficheros JSON
import json

# Leemos y carganos en una varible los datos del fichero json
with open('config.json') as config_file:
    config = json.load(config_file)

# Leemos la clave de la sección que queremos
db_host = config['database']['host']
db_port = config['database']['port']
db_username = config['database']['username']
db_password = config['database']['password']

print(db_host, db_port, db_username, db_password)

path_log = config['logs']['path_log']
path_app = config['logs']['path_app']

print(path_log, path_app)
