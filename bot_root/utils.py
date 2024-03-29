# file:         utils.py
# description:  contains utility functions used by the bot.
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

from loguru import logger
from PIL import Image
from random import choice


def get_token(token_file):
    logger.info("Initiating token get.")
    try:
        with open(token_file, "r") as f:
            token = f.read().rstrip()

    except Exception:  # yes ik this is too broad, no I don't care enough to fix it
        logger.error("Issue when reading token file.")
        return

    logger.success("Token successfully parsed.")
    return token


def generate_image(base_images: list[Image.Image], accessory_images: list[Image.Image]):
    logger.info("Generate image initiated.")

    background = choice(base_images)
    foreground = choice(accessory_images)

    bg_name = background.filename
    fg_name = foreground.filename

    logger.debug(f"Background: {bg_name}, foreground: {fg_name}.")

    background_size = background.size
    placement = background_size[0] // 4, background_size[1] // 4

    composite = background.copy()
    composite.paste(foreground, placement, foreground)

    logger.success("Composite image generated successfully.")
    return composite
