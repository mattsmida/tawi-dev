#!/usr/bin/env python3
import subprocess
import json

TMP_REPORT_PATH = './tmp-report.json'


def main():
    subprocess.run(f'task export > {TMP_REPORT_PATH}', shell=True)
    with open(TMP_REPORT_PATH, 'r') as f:
        tasks_str = f.read()
        tasks = json.loads(tasks_str)
        print(tasks)


if __name__ == "__main__":
    main()
