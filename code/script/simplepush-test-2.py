# import DaVinciResolveScript as dav
# resolve = dav.scriptapp('Resolve')
import os

# build the command
# cmd = "/usr/bin/python3 '/Users/ethanvosburg/Documents/git/Davinci Render Notifications/test.py'"
# run the command
# os.system(cmd)
os.system("Say Render Finish")
os.system("curl https://api.simplepush.io/send -d '{\"key\": \"pNWzrp\", \"title\": \"title\", \"msg\": \"message\", \"actions\": [\"yes\", \"no\", \"maybe\", \"option 4\"]}'")