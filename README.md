### Purpose
This bot was created as a part of RIT GSO's 2024 April Fools event. 

### Info
The main file assumes a few things:
- There is a file called `token.txt` present within the `bot_root` directory.
- There is a directory called `images` on the same level as `bot_root`, which itself contains two directories: `accessory` and `base`.

`base` contains the basis images (such as PNGs of instruments and musical equipment) and `accessory` contains some artifact to overlay on top of a base image.
When the bot is run, use anyone with the 'Eboard' role can call `$roll` which will pick a random base image and accessory, and send the resulting image in whatever channel the command was issued in.

#### Usage
You may run this bot in either a docker container or locally.

##### Docker Container
Assuming you have the latest version of docker installed, you can simply run `docker compose up --build` from the `beepo-gatcha` directory.

#### Local
Assuming that you have some form of `conda` installed, use the `environment.yml` file to create a new environment. Once this is done, simply run `conda activate gso-april-fools-2024` followed by `python3 bot_root/main.py` run from the `beepo-gatcha` directory. 