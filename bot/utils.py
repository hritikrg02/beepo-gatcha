# file:         utils.py
# description:  contains utility functions used by the bot
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

from PIL import Image
from random import choice


def get_token(token_file):
    with open(token_file, "r") as f:
        token = f.read().rstrip()
    return token


def generate_image(base_images: list[Image.Image], accessory_images: list[Image.Image]):
    background = choice(base_images)
    foreground = choice(accessory_images)

    background.paste(foreground, (0, 0), foreground)
    background.save("composite/test.png")
