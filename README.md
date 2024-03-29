### Purpose
This bot was created as a part of RIT GSO's 2024 April Fools event. 

### Usage
The main file assumes a few things:
- There is a file called `token.txt` present within the `bot_root` directory.
- There is a directory called `images` on the same level as `bot_root`, which itself contains two directories: `accessory` and `base`.

`base` contains the basis images (such as PNGs of instruments and musical equipment) and `accessory` contains some artifact to overlay on top of a base image.
When the bot is run, use anyone with the 'Eboard' role can call `$roll` which will pick a random base image and accessory, and send the resulting image in whatever channel the command was issued in.