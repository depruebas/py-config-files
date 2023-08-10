import configparser
import json

class ConfigClass:

  def Get( file, section, value):

    config_file = file.split(".")

    if config_file[1] == 'ini':
      config = configparser.ConfigParser()
      config.read(file)

      try: 
        return config.get( section, value) 
      except: 
        return "nothing1" 
    
    elif config_file[1] == 'json':
      with open( file) as config_json_file:
        config = json.load( config_json_file)
      
      try:
        return config[ section][ value]
      except: 
        return "nothing2" 
    
    else:
      return "nothing3"

