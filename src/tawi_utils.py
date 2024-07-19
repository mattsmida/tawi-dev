import re
import os


DISTRIBUTED = '_internal/' if '_internal' in os.listdir() else ''
DEVOTIONS_TEMPLATE_PATH = f'./{DISTRIBUTED}devotions-template.md'
DEVOTIONS_PATH = './devotions.md'


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

    if 'devotions.md' not in os.listdir():
        with open(DEVOTIONS_TEMPLATE_PATH, 'r') as fi, \
             open('./devotions.md', 'w') as fo:
            text = fi.read()
            fo.write(text)


def check_valid_devotions():
    """ Determine whether the user has made their own devotions yet.
    Returns true if so, false if not. """

    devotions = get_devotions()
    for devotion in devotions:
        if 'you should delete this example' in devotion['name']:
            print("Write your devotions in devotions.md to use tawi. \
                  Delete the example too.")
            return False
    return True
