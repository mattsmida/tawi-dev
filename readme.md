# TaWI

First write out your devotions.
Then, each day, set your intentions in service of each devotion.
At the end of the day, reflect on the actions you took.

## How?

Made a directory in this project called `./yourname`?
Have a devotions document like the one in `./sample`?
Installed `taskwarrior`?
Then you're ready.

At the beginning of the day, go into `./yourname`.
Run `../new_intentions.py`.
Write your intentions.
When done, run `../set_intentions.py`.

Then live your day.
Check off your tasks in `taskwarrior` as you go.
When it's over, from `./yourname`, run `../reflect.py`.
There, you'll write about your day.
