import logging
class LogGen:
    @staticmethod
    def log():
        logger =logging.basicConfig(filename= "C:/Users/Owner/Desktop/NopCommerce/LogAutomation.log" )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
