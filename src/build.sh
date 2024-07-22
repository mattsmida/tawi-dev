pyinstaller \
    --add-data ~/projects/tawi/src/devotions-template.md:. \
    --add-data ~/projects/tawi/src/intentions.txt:. \
    --add-data ~/projects/tawi/src/reflections.txt:. \
    --add-data ~/projects/tawi/src/help.txt:. \
    tawi.py
