#!/usr/bin/python
import requests
import time
from config import *

BASE_URL = "https://slack.com/api/chat.postMessage"
_hour = time.strftime('%H')
_minute = time.strftime('%M')


def is_prayer_available(hour, minute):
    current_time_minutes = int(hour) * 60 + int(minute)
    for prayer_name, prayer_time in prayer_times.items():
        prayer_time_ = (str(prayer_time)).split(":")
        prayer_time_minutes = ((int(prayer_time_[0]) * 60) + int(prayer_time_[1]))
        if current_time_minutes in range((prayer_time_minutes - 5), prayer_time_minutes + 1):
            return prayer_name, (prayer_time_minutes - current_time_minutes)

    return None


if is_prayer_available(_hour, _minute):
    params = {
        "text": "*" + str(is_prayer_available(_hour, _minute)[0]) + "* prayer will be held within " + str(
            is_prayer_available(_hour, _minute)[1]) + " minutes",
        "channel": channel,
        "token": access_token,
        "username": user_name
    }
    requests.get(BASE_URL, params)
