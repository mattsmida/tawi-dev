#!/usr/bin/env python3
import subprocess
import json
import tawi_utils
import os

DISTRIBUTED = '_internal/' if '_internal' in os.listdir() else ''
TMP_REPORT_PATH = './.tmp-report.json'
REFLECTIONS_TEMPLATE_PATH = f'./{DISTRIBUTED}reflections.txt'
REFLECTIONS_OUTPUT_PATH = './reflections'
REFLECT_QUESTION = "*How was your effort in service of this devotion today?" \
                   + " From -2 to 2.*"
REFLECT_OPENENDED = "*More to say?* \n"

status_icons = {
    "completed": "✅",
    "deleted": "🗑",
    "pending": "❌"
}


def main():
    with open('.tawi.dat') as f:
        time_data = json.loads(f.read())
        today, set_time = time_data['set_time'].split('T')
        today = int(today)
        pretty_today = str(today)
        pretty_today = pretty_today[0:4] \
            + '-' + pretty_today[4:6] \
            + '-' + pretty_today[6:]

    if f'{pretty_today}.md' in os.listdir('./reflections'):
        subprocess.run(f"vim {REFLECTIONS_OUTPUT_PATH}/{pretty_today}.md",
                       shell=True)
        return

    subprocess.run(f'task export > {TMP_REPORT_PATH}', shell=True)

    with open(TMP_REPORT_PATH, 'r') as f:
        tasks_str = f.read()
        all_tasks = json.loads(tasks_str)
        set_time = int(set_time.strip('Z'))
        todays_tasks = []
        tolerance = 5
        for task in all_tasks:
            task_day, task_set_time = task['entry'].split('T')
            task_day = int(task_day)
            task_set_time = int(task_set_time.strip('Z'))
            if task_day == today and abs(task_set_time - set_time) < tolerance:
                todays_tasks.append(task)

    devotions = tawi_utils.get_devotions()

    with open(REFLECTIONS_TEMPLATE_PATH, 'r') as fin, \
            open(f'{REFLECTIONS_OUTPUT_PATH}/{pretty_today}.md', 'w') as fout:
        fout.write(f"# Reflection for {pretty_today} \n")
        for line in fin:
            fout.write(line)

        for devotion in devotions:
            fout.write(f"## {devotion['name']}\n")
            for task in todays_tasks:
                if devotion['shortcode'] in task['tags']:
                    fout.write(
                        f"  - {status_icons[task['status']]}: " +
                        f"{task['description']}\n")
            fout.write('\n')
            fout.write(REFLECT_QUESTION)
            fout.write('\n')
            fout.write(REFLECT_OPENENDED)
            fout.write('\n\n')

    subprocess.run(f"vim {REFLECTIONS_OUTPUT_PATH}/{pretty_today}.md",
                   shell=True)


if __name__ == "__main__":
    main()
