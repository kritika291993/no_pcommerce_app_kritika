import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod  # can access class function without creating obj
    def getApplicationURL():
        return config.get('common data', 'BaseURL')

    @staticmethod
    def getUserEmail():
        return config.get('common data', 'Username')

    @staticmethod
    def getUserPassword():
        return config.get('common data', 'Password')
