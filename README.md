# Davinci Resolve Render Notifications

_This project is currently in progress and missing files after a computer transfer. I will be working on it again soon._

This is a simple script that will send a notification to your phone when a Davinci Resolve render is complete.

## Features

- Sends a notification to your phone when a Davinci Resolve render is complete
- Checks the render queue every minute
- Can be run in the background
- Integrated logging

## To Do

- [ ] Add support for multiple renders with fleet monitoring
- [ ] Add support for multiple phones
- [ ] Add support for multiple notifications
- [ ] Improve render detection


## Requirements

- Python 3
- [Simple Push](https://www.simplepush.io/) account
- Davinci Resolve
- Runs in crontab or other task automation service
- IFTTT account 

## Basic Operating Principle

The script will check the Davinci Resolve render queue every minute. If there is a render in progress, it will begin checking constantly untill the render has finished. When the render finishes or there is a problem with the render, it will send a notification to your phone informing you of the state of the render.