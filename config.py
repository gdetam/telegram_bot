"""this is config parser for settings.ini file."""

import configparser


# create a parser object
config = configparser.ConfigParser()
# read the config
config.read('E:/Python/my_adult_telegram_bot/settings.ini')
PATH = config['PATH']['PATH']
BOT_TOKEN = config['BOT_TOKEN']['BOT_TOKEN']
CONNECTION_FOR_ENGINE = config['CONNECTION_FOR_ENGINE']['CONNECTION_FOR_ENGINE']
# flag for start db_inserter.py control and save in data base
inserter_flag = False
LIMIT = 2
