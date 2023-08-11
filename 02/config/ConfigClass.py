# Importamos las clase que vamos a utilizar para leer los ficheros
# de configuración, en este caso .INI y .JSON
import configparser
import json

class ConfigClass:

  # Método para leer los datos del un fichero de configuración.
  # Recibe los parametros:
  #
  #     file: fichero de configuración: formato = 'path/config.ini'
  #     section: sección del fichero de configuración, en el ejemplo database o logs
  #     key: Clave de la que queremos obtener su valor, ejem.: username
  #
  # Devuelve el valor asociado a la seccion/clave o un error.
  #
  def Get( file, section, key):

    # Obtenemos la extensión para saber el tipo de fichero a procesar
    config_file = file.split(".")

    # Si el fichero es tipo .INI
    if config_file[1] == 'ini':
      # Cargamos el ConfigParser y leemos el fichero
      config = configparser.ConfigParser()
      config.read(file)

      # Obtenemos el valor de la clave pasado y lo encerramos en un 
      # try ... except para poder tratar el error si no existe la clave o seccion
      try: 
        return config.get( section, key) 
      except: 
        return "nothing1" 
    
    # hacemos lo mismo con los fichero .json
    elif config_file[1] == 'json':
      with open( file) as config_json_file:
        config = json.load( config_json_file)
      
      try:
        return config[ section][ key]
      except: 
        return "nothing2" 
    
    # Devolvemos un error o lo que queramos si el fichero de configuracion no existe
    else:
      return "nothing3"

