
from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/OrangeHrm/Utils/config.ini")
    return config.get(category, key)
    
