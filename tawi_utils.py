import re

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
