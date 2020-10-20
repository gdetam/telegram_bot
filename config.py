"""this is config parser for settings.ini file."""

import configparser


# create a parser object
config = configparser.ConfigParser()
# read the config
config.read('E:/Python/my_adult_telegram_bot/settings.ini')

bot_token = config['bot_token']['bot_token']
connection_for_engine = config['connection_for_engine']['connection_for_engine']
