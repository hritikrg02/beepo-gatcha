# file:         main.py
# description:  contains the main implementation for the bot.
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

import discord
from glob import glob
from io import BytesIO
from PIL import Image
from utils import get_token, generate_image

TOKEN_FILE = "bot/token.txt"
TOKEN = get_token(TOKEN_FILE)

BASE_IMAGES_DIR = "images/base/"
ACCESSORY_IMAGES_DIR = "images/accessory/"
EXTENSION = "*.png"

COMPOSITE_FILENAME = "composite.png"

BASE_IMAGES = [Image.open(img) for img in glob(f"{BASE_IMAGES_DIR}{EXTENSION}")]
ACCESSORY_IMAGES = [Image.open(img) for img in glob(f"{ACCESSORY_IMAGES_DIR}{EXTENSION}")]

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

    composite = generate_image(BASE_IMAGES, ACCESSORY_IMAGES)
    buffer = BytesIO()
    composite.save(buffer, format="PNG")
    buffer.seek(0)
    f = discord.File(buffer, filename=COMPOSITE_FILENAME)

    if message.content.startswith("$roll"):
        await message.channel.send(file=f)


client.run(TOKEN)
