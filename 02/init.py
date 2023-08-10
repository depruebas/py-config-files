from config.ConfigClass import ConfigClass


print( ConfigClass.Get ( 'config.ini', 'database', 'host'))
print( ConfigClass.Get ( 'config.ini', 'database', 'username'))

print( ConfigClass.Get ( 'config.json', 'database', 'password'))
print( ConfigClass.Get ( 'config.json', 'logs', 'perro'))


print( ConfigClass.Get ( 'config.txt', 'logs', 'path_app'))
