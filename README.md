# Ball-Bot
## What is it?
A Python 3.4.2+ Discord Bot. Right now, its main use is to listen for messages and respond to certain keywords.

## Requirements
* Python 3.4.2+
* aiohttp library
* websockets library
* [discord.py](https://github.com/Rapptz/discord.py)

All these libraries can be installed with pip. Pip should handle grabbing all the required packages if you grab discord.py.

## Features
* Admin command interface
* Respond to keywords with random messages
* Respond if a post contains certian keywords
* "Magic eight ball" function that lets the user ask a question and get a random respsonse

## Usage
* ping:
Case insenstive. The bot will respond to the ping with a random message.

* !kill:
Causes the bot to disconnect and the script to exit. This can only be executed if the message comes from a user id

* !reload: 
rereads the script files and updates the structures the bot stores them in. This is useful if you want to add or remove responses without restarting the whole bot.

## Other helpful things
Some of these links might be helpful if you want to contribute or work on the bot yourself.

The discord.py documention: https://discordpy.readthedocs.io/en/latest/
The official documentation for the discord api: https://discordapp.com/developers/docs/intro
