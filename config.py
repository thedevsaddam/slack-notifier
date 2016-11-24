#!/usr/bin/python
# -*- coding: utf-8 -*-

# Configuration
access_token = "ACCESS_TOKEN_HERE"
user_name = "USER_NAME_FOR_YOUR_SLACK_BOT"
channel = "CHANNEL_NAME_YOU_WANT_TO_POST"

# time format in 12 hours (AM/PM) or 24 hours
time_format = 12
# Get notified before X minutes, specify minutes if want to get notified multiple times, seperating by commas
notify_before = "5,3,1"
# Configure the time according to time format
events={
	'fajr': {
		'time': '5:30 AM',
		'message': "It's *`Fajr`* time."
	},
	'zuhr': {
		'time': '1:15 PM',
		'message': "It's *`Zuhr`* time."
	},
	'asr': {
		'time': '4:15 PM',
		'message': "It's *`Asr`* time."
	},
	'magrib': {
		'time': '5:20PM',
		'message': "It's *`Magrib`* time."
	},
	'isha': {
		'time': '6:45 PM',
		'message': "It's *`Isha`* time."
	},
	'standup':{
		'time': '11:15 AM',
		'message': "*`Stand up`* on meeting room. Everyone please come in time."
	}
}
