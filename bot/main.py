# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

import discord

from utils import get_token

TOKEN_FILE = "token.txt"
TOKEN = get_token(TOKEN_FILE)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)
