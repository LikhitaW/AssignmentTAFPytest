from configparser import ConfigParser



def ReadConfigProperty(category,key):
    config = ConfigParser()
    config.read(".\\Configurations\\config.ini")
    return config.get(category, key)