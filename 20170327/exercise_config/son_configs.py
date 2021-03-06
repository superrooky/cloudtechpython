import os
try:
    from configparser import SafeConfigParser
except ImportError:
    # ConfigParser in python 2
    from ConfigParser import SafeConfigParser
    
    config_dir = [os.path.expanduser(os.path.join('~','.'+project)),
                  os.path.expanduser(os.path.join('~')),
                  os.path.join('/etc', project),
                  '/etc']
                  
    for d in config_dir:
        file_path = os.path.join(d, project+'.conf')
        if os.path.isfile(file_path):
            return file_path
            
CONF = SaveConfigParser()
CONF.read(find_config_file('son_project'))
    
