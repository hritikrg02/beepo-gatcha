# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

import discord
from os import listdir
from utils import get_token

TOKEN_FILE = "bot/token.txt"
TOKEN = get_token(TOKEN_FILE)

BASE_IMAGES_DIR = "images/base/"
ACCESSORY_IMAGES_DIR = "images/accessory/"

BASE_IMAGES = listdir(BASE_IMAGES_DIR)
ACCESSORY_IMAGES = listdir(ACCESSORY_IMAGES_DIR)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$roll"):
        await message.channel.send(file=discord.File("images/base/clarinet.png"))


client.run(TOKEN)
