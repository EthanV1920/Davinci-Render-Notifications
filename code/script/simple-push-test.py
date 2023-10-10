# pip install simplepush

import configparser
from simplepush import send, send_encrypted

config = configparser.ConfigParser()

config.read("config.ini")
prod = config['PROD']

# Send notification
# send (prod["KEY"], "Render Complete", "Your render is done", "event", ["yes", "no", "maybe", "option 4"])
send ("pNWzrp", "Render Complete", "Your render is done", "event", ["yes", "no", "maybe", "option 4"])

# curl https://api.simplepush.io/1/feedback/56d38bf99a124e9fb81a0c62805f57f1 
# curl https://api.simplepush.io/send -d '{"key": "pNWzrp", "title": "title", "msg": "message", "actions": ["yes", "no", "maybe", "option 4"]}'