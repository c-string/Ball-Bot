import discord
import asyncio
import re
import csvt
from random import randint

# creates a bot object that has access to Discord's events
bot = discord.Client()

#--------------------------------------------
# Events 
#--------------------------------------------

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
    print('------------------')
    channel = discord.Object(id='channel_id')
    yield from bot.send_message(channel,'Ohayou!')

@bot.event
@asyncio.coroutine
def on_message(message):
    msg_content = message.content

    # User responses
    if message.author == bot.user:
        # prevents the bot from responding to itself
        return
      
    if (message.content.lower() == 'ping'):
        if (message.author.id == 'specific_user_id'):
            msg = '{0.author.mention} gnop!'.format(message)
            yield from bot.send_message(message.channel, msg)
        else:
            # other people
            msg = ('{0.author.mention} %s' % Random_Message(bot.r_response_list)).format(message)
            yield from bot.send_message(message.channel, msg)

    if (re.match('snek\,? (should|would|could|can|will|did|do|are|is|was|am|does|what|have)[\,\ ]? (.+)', message.content.lower())):
            # magic eight ball check
            msg = ('{0.author.mention}, %s' % Random_Message(bot.eight_ball_response_list)).format(message)
            yield from bot.send_message(message.channel, msg)
            
    # Substring responses
    for key, value in bot.substring_list.items():
        if key in msg_content.lower():
            # checks if the key is in the input string
            yield from bot.send_message(message.channel, value)
            break
            
    # Admin commands
    # commands in this section should only be executed if called by a specific user (hopefully the bot's owner)
    if (message.author.id == 'admin_id'):
        if (message.content == '!kill'):
            # disconnects fromt the discord server and ends the script
            yield from bot.send_message(message.channel, 'Oyasumi!')
            yield from bot.close()
            exit()   
        elif (message.content == '!reload'):
            bot.substring_list = csvt.CSV_To_Dict('responses.csv')
            bot.r_response_list = csvt.CSV_To_List('ping_responses.csv')
            bot.eight_ball_response_list = csvt.CSV_To_List('eight_ball_responses.csv')

def Random_Message(response_list):
    # pulls a random response from the global list and returns it as a string
    random = randint(0,(len(response_list)-1))
    return response_list[random]
 
def main():
    print('\nLoading scripts...')
    bot.r_response_list = csvt.CSV_To_List('ping_responses.csv')

    # dict of users that can be used for getting specific responses to specific users
    bot.eight_ball_response_list = csvt.CSV_To_List('eight_ball_responses.csv')

    # dict of substrings that the bot can respond to
    bot.substring_list = csvt.CSV_To_Dict('responses.csv')
    print('\nAttempting to log in...')
    # Bot token, do not change this. This allows the bot to login to the discord server
    bot.run("bot_token")

main()