from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/PytestSelenium/config.ini")
    return config.get(category, key)
    
