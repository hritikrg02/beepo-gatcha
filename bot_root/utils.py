# file:         utils.py
# description:  contains utility functions used by the bot.
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

from loguru import logger
from PIL import Image
from random import choice


def get_token(token_file):
    logger.debug("Initiating token get.")
    try:
        with open(token_file, "r") as f:
            token = f.read().rstrip()

    except Exception:
        logger.error("Issue when reading token file.")
        return

    logger.success("Token successfully parsed.")
    return token


def generate_image(base_images: list[Image.Image], accessory_images: list[Image.Image]):
    background = choice(base_images).convert('RGBA')
    foreground = choice(accessory_images).convert('RGBA')

    background_size = background.size
    placement = background_size[0] // 4, background_size[1] // 4

    composite = background.copy()
    composite.paste(foreground, placement, foreground)
    # composite.save("images/composite/test.png")

    return composite
