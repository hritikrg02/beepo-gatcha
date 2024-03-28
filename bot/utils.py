# file:         utils.py
# description:  contains utility functions used by the bot
# author:       Hritik "Ricky" Gupta | hritikrg02@gmail.com

def get_token(token_file):
    with open(token_file, 'r') as f:
        token = f.read().rstrip()
    return token


def generate_image():
    pass
