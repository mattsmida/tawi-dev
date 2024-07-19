#!/usr/bin/env python3

import new_intentions
import set_intentions
import reflect
import tawi_utils
import sys

tawi_utils.setup_prereqs()
if not tawi_utils.check_valid_devotions():
    exit(1)

try:
    func = sys.argv[1]  # new, set, reflect
except IndexError:
    tawi_utils.display_help()
    func = ''

if __name__ == "__main__" and func == "new":
    new_intentions.main()

elif __name__ == "__main__" and func == "set":
    set_intentions.main()

elif __name__ == "__main__" and func == "reflect":
    reflect.main()
