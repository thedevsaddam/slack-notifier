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

# get the fajr prayer time
fajr = fajr.strip()
formatted_fajr = format_time(fajr) if time_format == 12 else fajr

# get the zuhr prayer time
zuhr = zuhr.strip()
formatted_zuhr = format_time(zuhr) if time_format == 12 else zuhr

# get the asr prayer time
asr = asr.strip()
formatted_asr = format_time(asr) if time_format == 12 else asr

# get the magrib prayer time
magrib = magrib.strip()
formatted_magrib = format_time(magrib) if time_format == 12 else magrib

# get the isha prayer time
isha = isha.strip()
formatted_isha = format_time(isha) if time_format == 12 else isha

# current time
now = get_current_time()

notifiable_fajr = is_notifiable_difference(formatted_fajr, now)
notifiable_zuhr = is_notifiable_difference(formatted_zuhr, now)
notifiable_asr = is_notifiable_difference(formatted_asr, now)
notifiable_magrib = is_notifiable_difference(formatted_magrib, now)
notifiable_isha = is_notifiable_difference(formatted_isha, now)

if notifiable_fajr[0]:
    send_notification(body = "It's *`Fajr`* prayer time. {} minutes to go.".format(notifiable_fajr[1]))
elif notifiable_zuhr[0]:
    send_notification(body = "It's *`Zuhr`* prayer time. {} minutes to go.".format(notifiable_zuhr[1]))
elif notifiable_asr[0]:
    send_notification(body = "It's *`Asr`* prayer time. {} minutes to go.".format(notifiable_asr[1]))
elif notifiable_magrib[0]:
    send_notification(body = "It's *`Magrib`* prayer time. {} minutes to go.".format(notifiable_magrib[1]))
elif notifiable_isha[0]:
    send_notification(body = "It's *`Isha`* prayer time. {} minutes to go.".format(notifiable_isha[1]))

