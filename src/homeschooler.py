import sys
from homeschooler.runner import Runner, parse_tasks


if __name__ == "__main__":
    r = Runner()
    task_definition = sys.stdin.readlines()
    r.set_tasks(task_definition)
    r.run()
