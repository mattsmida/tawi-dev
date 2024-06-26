#!/usr/bin/env python3
import re
import subprocess


def main():
    devotions_path = './devotions.md'
    devotions = []  # {"HCM": "Home Chef Mastery"}
    with open(devotions_path, 'r') as f:
        for line in f:
            if re.search(r'^##\s.*', line):
                shortcode = re.search(r'^##\s(.*):', line).group(1).lower()
                name = re.search(r'^##\s.*:\s(.*)$', line).group(1)
                devotions.append({'shortcode': shortcode, 'name': name})

    max_len_devotion_shortcode = max([len(d['shortcode']) for d in devotions])
    intentions_template_path = '../templates/intentions.txt'
    intentions_output_path = './intentions.md'
    with open(intentions_template_path, 'r') as fin, \
            open(intentions_output_path, 'w') as fout:
        for line in fin:
            if "$YOUR_DEVOTIONS" not in line:
                fout.write(line)
            else:
                width = max_len_devotion_shortcode + 4
                for d in devotions:
                    fout.write(f"- {d['shortcode']}: ".ljust(width) +
                               f"{d['name']}\n")

    subprocess.run('vim +$ intentions.md', shell=True)


if __name__ == "__main__":
    main()
