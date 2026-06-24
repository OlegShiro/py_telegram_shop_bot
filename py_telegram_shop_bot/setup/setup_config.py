import config
import configparser


def setup_config():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    
    cfg_bot = cfg["BOT"]
    config.BOT_TOKEN = cfg_bot["token"]

    cfg_logger = cfg["LOGGING"]
    config.LOG_FORMAT = cfg_logger["format"]
    config.LOG_PATH = cfg_logger["log_path"]
    config.LOG_LEVEL_FILE = cfg_logger["level_file"]
    config.LOG_LEVEL_OUTPUT = cfg_logger["level_output"]

    print("Файл конфигурации загружен.")
