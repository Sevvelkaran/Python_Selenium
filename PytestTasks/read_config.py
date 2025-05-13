from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config_path = "/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/PytestTasks/config.ini"
    config.read(config_path)
    return config.get(category, key)
