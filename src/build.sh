pyinstaller \
    --add-data ~/projects/tawi/src/devotions.md:. \
    --add-data ~/projects/tawi/src/intentions.txt:. \
    --add-data ~/projects/tawi/src/reflections.txt:. \
    tawi.py
