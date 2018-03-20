# -*- coding: utf-8 -*- 
# Install by pip install -U wxpy and then run this script
# Game Rule:
# start the game by sending 'I am XXX', and exit the game by sending 'end'. Any message that you send to the host will be broadcast to the group with the temp name you used.
from wxpy import *
bot = Bot();

nameMap = {};

gameGroup = bot.groups().search('Test')[0];
#gameGroup.send('Entered robot mode. Please send me your message individually and i will broadcast your message in the group.');

if 'I am' in 'I am 多串':
	print('test chinese pass');
	
@bot.register()
def reply_my_friend(msg):
	messageSender = msg.sender;
	if (messageSender in gameGroup) :
		if 'I am' in msg.text:
			nameMap[messageSender.name] = msg.text.replace('I am', '').strip();
			bot.file_helper.send(nameMap);
			return 'Renamed. Start the game';
		elif 'end' == msg.text:
			del nameMap[messageSender.name];
			bot.file_helper.send(nameMap);
			return 'Exit the game';
		elif messageSender.name in nameMap: 
			gameGroup.send('{}: {}'.format(nameMap[messageSender.name], msg.text));

print('Entered robot mode');

embed();