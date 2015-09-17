import os
import time
import random
import re
from slackclient import SlackClient

# DO_ALY_CHAN = "D0AQXL0CX"

imageList = ["http://i.imgur.com/gbwgfw6.jpg", 
			  "http://i.imgur.com/gbwgfw6.jpg",
			  "http://i.imgur.com/gbwgfw6.jpg"]

class slackbot(object):
	# a class for fun slackbots

	def __init__(self, token):
		self.token = token
		self.slack_client = None

	def connect(self):
		# setup the SlackClient and connect to the RTM API

		self.slack_client = SlackClient(self.token)
		self.slack_client.rtm_connect()

	def get_events(self):
		# get all events from the RTM API
		# Is drunkoctopus or a keyword mentioned?

		while True:
			new_evts = self.slack_client.rtm_read()
			for evt in new_evts:
				print evt
				if evt.get('type') == 'message':
					message = evt.get('text')
					if 'catbot' in message:
						channel = evt.get('channel')
						self.reply(message, channel)
				time.sleep(1)

	def reply(self, message, channel):
		# when drunkoctopus is mentioned, return a message
		# look message words up in the drunkoctopus dictionary
		
		if "STAT" in message:
			reply = "HERES YOURS CAT FAST"
			self.slack_client.rtm_send_message(channel, reply)
		
		else: 
			reply = random.choice(imageList)
			self.slack_client.rtm_send_message(channel, reply)
			
if __name__ == "__main__":
	
	TOKEN = os.environ['SLACK_TOKEN']
	drunkoctopus = slackbot(TOKEN)
	drunkoctopus.connect()
	drunkoctopus.get_events()