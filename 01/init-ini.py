import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

db_host = config.get('database', 'host')
db_port = config.get('database', 'port')
db_username = config.get('database', 'username')
db_password = config.get('database', 'password')

print(db_host, db_port, db_username, db_password)


path_log = config.get('logs', 'path_log')
path_app = config.get('logs', 'path_app')

print(path_log, path_app)
