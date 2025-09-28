import random

def get_funny_caption():
    templates = [
        "When {thing} is life...",
        "{thing}? More like my entire personality 😎",
        "I run on {thing} and regrets",
        "404: {thing} not found",
        "Me trying to be productive: *opens {thing}*",
        "Dark mode + {thing} = happiness",
    ]
    things = ["Python", "coffee ☕", "WiFi", "memes", "sleep", "bug fixes"]

    template = random.choice(templates)
    thing = random.choice(things)
    return template.format(thing=thing)