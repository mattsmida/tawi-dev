#!/usr/bin/env python3
import subprocess
import tawi_utils
import os

DISTRIBUTED = '_internal/' if '_internal' in os.listdir() else ''
EDITOR = tawi_utils.EDITOR


def main():
    devotions = tawi_utils.get_devotions()

    max_len_devotion_shortcode = max([len(d['shortcode']) for d in devotions])
    intentions_template_path = f'./{DISTRIBUTED}intentions.txt'
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

    subprocess.run([EDITOR, 'intentions.md'])


if __name__ == "__main__":
    main()
