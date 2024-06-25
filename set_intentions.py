import subprocess

def make_tags(line, lp_idx, rp_idx):
    """ Given a string and indexes of its right and left parens, return the 
    tags as a string. """
    tags = line[:rp_idx]
    tags = tags.split(',')
    tags = ["+" + tag.strip() for tag in tags]
    tags_str = ' '.join(tags)
    return tags_str


def main():
    with open('today.txt', 'r') as f:
        for line in f:
            lp_idx, rp_idx = line.find('('), line.find(')')
            if lp_idx > rp_idx or (lp_idx == -1 and rp_idx > 0):
                tags_str = make_tags(line, lp_idx, rp_idx)
                description = line[rp_idx+1:-1].strip()
                command = f'task add "{description}" {tags_str}'
                print(command)
                # subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()

