#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from config import *
from pattern.en import singularize

BASE_URL = "https://slack.com/api/chat.postMessage"

# reformat notify before
notify_before = map(lambda minute: int(minute), filter(lambda x: x.strip() if len(x.strip()) else False, notify_before.split(",")))
# Need to make a copy of the notify before, otherwise, it becomes [] on very next call.
times = list(notify_before)

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
    global times
    format = "%H:%M"
    t1 = datetime.strptime(from_time, format)
    t2 = datetime.strptime(to_time, format)
    difference = (((t1 - t2).seconds) // 60)
    return [True, difference] if difference in times else [False, difference]

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

# Loop over all the events registered
for event, body in events.items():
    # check if the event body has time and message as key
    if 'time' not in body or 'message' not in body:
        raise Exception("The event '{}' doesn't contain the 'time' or 'message' or both as key.".format(event))

    # get the time from the event body, strip the whitespaces
    time = body.get('time').strip()
    # format the time if needed
    formatted_time = format_time(time) if time_format == 12 else time
    # is the given time is notifiable 
    notifiable = is_notifiable_difference(formatted_time, now)
    # if notifiable[0] == true, send notification
    if notifiable[0]:
        send_notification(body = "{}. *`{} {}`* to go".format(body.get('message').strip(' .'), notifiable[1], \
            singularize('minutes') if notifiable[1] == 1 else "minutes"))