#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from config import *

BASE_URL = "https://slack.com/api/chat.postMessage"

# reformat notify before
notify_before = map(lambda minute: int(minute), filter(lambda x: x.strip() if len(x.strip()) else False, notify_before.split(",")))

if time_format not in [12, 24]:
    raise Exception('Time format should either be 12 or 24')

def get_current_time():
    now = datetime.now()
    return "{}:{}".format(now.hour, now.minute)

def format_time(utime):
    lower = utime.lower()
    if "am" in lower:
        return lower.replace('12', '0')[:-2].strip() if "12" in lower and lower.index('12') == 0 else lower[:-2].strip()
    elif "pm" in lower:
        utime = utime.lower().replace('pm', '')
        splited = utime.split(':')
        new_time = 12 + int(splited[0])
        return "{}:{}".format(new_time, splited[1]).strip()

def is_notifiable_difference(from_time, to_time):
    global notify_before
    format = "%H:%M"
    t1 = datetime.strptime(from_time, format)
    t2 = datetime.strptime(to_time, format)
    difference = (((t1 - t2).seconds) // 60)
    return [True, difference] if difference in notify_before else [False, difference]

def send_notification(body = "It's salat time"):
    params = {
        "text": body,
        "channel": channel,
        "token": access_token,
        "username": user_name
    }
    requests.get(BASE_URL, params)

# current time
now = get_current_time()

#looping over the listed salat times and send notifications
for salat, time in salat_times.items():
    time = time.strip()
    formatted_time = format_time(time) if time_format == 12 else time
    notifiable_salat = is_notifiable_difference(formatted_time, now)
    if notifiable_salat[0]:
        send_notification(body = "It's *`{}`* prayer time. {} minutes to go.".format(salat.capitalize(), notifiable_salat[1]))
