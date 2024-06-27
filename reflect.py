#!/usr/bin/env python3
import subprocess
import json
import re
from datetime import datetime

TMP_REPORT_PATH = './tmp-report.json'
REFLECTIONS_TEMPLATE_PATH = '../templates/reflections.txt'
REFLECTIONS_OUTPUT_PATH = \
    f"./{datetime.today().strftime('%Y-%m-%d')}-reflections.md"
REFLECT_QUESTION = "How was your effort in service of this devotion today?" \
                   + " From -2 to 2."
REFLECT_OPENENDED = "More to say? \n"

icons = {
    "completed": "✅",
    "deleted": "🗑",
    "pending": "❌"
}


def main():
    subprocess.run(f'task export > {TMP_REPORT_PATH}', shell=True)
    with open('.tawi.dat') as f:
        time_data = json.loads(f.read())

    with open(TMP_REPORT_PATH, 'r') as f:
        tasks_str = f.read()
        all_tasks = json.loads(tasks_str)

        # Filter the task export to tasks that were set within 5 seconds
        # of set_intentions script running. That data is held in tawi.dat's
        # "set_time" attribute.

        today, set_time = time_data['set_time'].split('T')
        today = int(today)
        set_time = int(set_time.strip('Z'))
        todays_tasks = []
        tolerance = 5
        for task in all_tasks:
            task_day, task_set_time = task['entry'].split('T')
            task_day = int(task_day)
            task_set_time = int(task_set_time.strip('Z'))
            if task_day == today and abs(task_set_time - set_time) < tolerance:
                todays_tasks.append(task)

    # Get devotions TODO: combine this with same thing from new_intentions
    devotions_path = './devotions.md'
    devotions = []  # {"HCM": "Home Chef Mastery"}
    with open(devotions_path, 'r') as f:
        for line in f:
            if re.search(r'^##\s.*', line):
                shortcode = re.search(r'^##\s(.*):', line).group(1).lower()
                name = re.search(r'^##\s.*:\s(.*)$', line).group(1)
                devotions.append({'shortcode': shortcode, 'name': name})

    with open(REFLECTIONS_TEMPLATE_PATH, 'r') as fin, \
            open(REFLECTIONS_OUTPUT_PATH, 'w') as fout:
        pretty_today = str(today)
        pretty_today = pretty_today[0:4] \
            + '-' + pretty_today[4:6] \
            + '-' + pretty_today[6:]
        fout.write(f"# Reflection for {pretty_today} \n")
        for line in fin:
            fout.write(line)

        # Loop over all the devotions and write to the file
        # Devotion name
        # Devotion oneliner
        # Devotion tasks
        # ...
        # How was your effort in service of this devotion today, from -2 to 2?
        # More to say?

        for devotion in devotions:
            fout.write(f"## {devotion['name']}\n")
            for task in todays_tasks:
                if devotion['shortcode'] in task['tags']:
                    # fout.write(str(task) + '\n')
                    fout.write(
                        f"  - {icons[task['status']]}: {task['description']}")
            fout.write('\n')
            fout.write(REFLECT_QUESTION)
            fout.write('\n')
            fout.write(REFLECT_OPENENDED)
            fout.write('\n\n')

    subprocess.run(f"vim {REFLECTIONS_OUTPUT_PATH}", shell=True)


if __name__ == "__main__":
    main()
