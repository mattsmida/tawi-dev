import re
import os
import subprocess

DISTRIBUTED = '_internal/' if '_internal' in os.listdir() else ''
DEVOTIONS_TEMPLATE_PATH = f'./{DISTRIBUTED}devotions-template.md'
HELP_PATH = f'./{DISTRIBUTED}help.txt'
DEVOTIONS_PATH = './devotions.md'
EDITOR = os.environ.get('EDITOR', 'nano')


def get_devotions():
    devotions = []
    with open(DEVOTIONS_PATH, 'r') as f:
        for line in f:
            if re.search(r'^##\s.*', line):
                shortcode = re.search(r'^##\s(.*):', line).group(1).lower()
                name = re.search(r'^##\s.*:\s(.*)$', line).group(1)
                devotions.append({'shortcode': shortcode, 'name': name})

    return devotions


def edit_devotions():
    subprocess.run([EDITOR, DEVOTIONS_PATH])
    return


def display_help():
    text = subprocess.run(['cat', HELP_PATH], capture_output=True, text=True)
    print(text.stdout)
    return


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
        if 'delete this example' in devotion['name']:
            print(
                "Write your devotions in devotions.md to use tawi.",
                "\nMake sure to delete the example as well.", "\n"
            )
            return False
    return True
