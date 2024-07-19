import re
import os


DISTRIBUTED = '_internal/' if '_internal' in os.listdir() else ''
DEVOTIONS_PATH = f'./{DISTRIBUTED}devotions.md'


def get_devotions():
    devotions = []
    with open(DEVOTIONS_PATH, 'r') as f:
        for line in f:
            if re.search(r'^##\s.*', line):
                shortcode = re.search(r'^##\s(.*):', line).group(1).lower()
                name = re.search(r'^##\s.*:\s(.*)$', line).group(1)
                devotions.append({'shortcode': shortcode, 'name': name})

    return devotions


def display_help():
    print("Valid commands: new, set, reflect")


def setup_prereqs():
    if 'reflections' not in os.listdir():
        os.mkdir('./reflections')
