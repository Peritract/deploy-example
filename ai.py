from random import choice

with open("options.txt", 'r') as f_obj:
    options = [x.strip() for x in f_obj.readlines()]

def make_ai_decision():
    return choice(options)
