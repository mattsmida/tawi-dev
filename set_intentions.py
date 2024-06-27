#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime


def make_tags(line, lp_idx, rp_idx):
    """ Given a string and indexes of its right and left parens, return the
    tags as a string. """
    tags = line[:rp_idx]
    tags = tags.split(',')
    tags = ["+" + tag.strip() for tag in tags]
    tags_str = ' '.join(tags)
    return tags_str


def main():
    with open('./intentions.md', 'r') as f:
        listen = False
        for line in f:
            lp_idx, rp_idx = line.find('('), line.find(')')
            if "## Write below" in line:
                listen = True
            if listen and (lp_idx > rp_idx or (lp_idx == -1 and rp_idx > 0)):
                tags_str = make_tags(line, lp_idx, rp_idx)
                description = line[rp_idx + 1:-1].strip()
                # TODO: escape characters like apostrophe in command
                command = f'task add {description} {tags_str}'
                subprocess.run(command, shell=True)

    with open('./.tawi.dat', 'w') as f:
        data = {}
        set_time = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        data['set_time'] = set_time
        f.write(json.dumps(data))


if __name__ == "__main__":
    main()
