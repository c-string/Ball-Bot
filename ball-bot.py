import discord
import asyncio

bot = discord.Client()

@bot.event
@asyncio.coroutine
# both the above lines are need for python 3.4.2
# this would be different for newer versions of python
def on_ready():

	# event for when the bot is is done preparing the data received from discord
	# prints out the name and id of the bot to the termainal
	# and makes the bot send a ready message to the discord text channel
	print('Login succesful')
	print("Bot username: %s" % bot.user.name)
	print("Bot id: %s" % bot.user.id)
	print('------')
	channel = discord.Object(id='token')
	yield from bot.send_message(channel,'Ohayou!')

@bot.event
@asyncio.coroutine
def on_message(message):

	# prevents the bot from responding to itself
	if message.author == bot.user:
		return
	
	if (message.content == 'ping'):
		if (message.author.id == 'token'):
			# BEEEEEES message
			msg = '{0.author.mention} gnop!'.format(message)
			yield from bot.send_message(message.channel, msg)
		else:
			# other people
			msg = '{0.author.mention} pong!'.format(message)
			yield from bot.send_message(message.channel, msg)


	# kill command
	# it should only accept this command from my account
	if (message.content == '!kill' and  message.author.id == 'token'):
		yield from bot.send_message(message.channel, 'Oyasumi!')
		yield from bot.close()
		exit()

# bot token, do not change this
bot.run("token")
