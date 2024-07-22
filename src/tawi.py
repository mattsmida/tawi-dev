#!/usr/bin/env python3

import new_intentions
import set_intentions
import reflect
import tawi_utils
import sys


def main():
    tawi_utils.setup_prereqs()

    try:
        func = sys.argv[1]
        if func not in ['new', 'set', 'reflect', 'devotions', 'help']:
            print('Commands: new, set, reflect, devotions, help')
            return
    except IndexError:
        print('Commands: new, set, reflect, devotions, help')
        return

    if __name__ == "__main__" and func == "devotions":
        tawi_utils.edit_devotions()
        return

    if not tawi_utils.check_valid_devotions():
        tawi_utils.display_help()
        return

    if __name__ == "__main__" and func == "new":
        new_intentions.main()
        return

    elif __name__ == "__main__" and func == "set":
        set_intentions.main()
        return

    elif __name__ == "__main__" and func == "reflect":
        reflect.main()
        return

    elif __name__ == "__main__" and func == "help":
        tawi_utils.display_help()
        return


if __name__ == "__main__":
    main()
