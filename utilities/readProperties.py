import configparser
config = configparser.RawConfigParser()
config.read(".//utilities/config.ini")
class Readconfig:
    @staticmethod
    def getAppUrl():
        url = config.get("Common info", "base_url")
        return url
    @staticmethod
    def getAppUsername():
        app_username = config.get("Common info", 'user_name')
        return app_username
    @staticmethod
    def getAppPassword():
        app_password = config.get("Common info", 'user_password')
        return app_password









