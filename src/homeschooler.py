import sys
from homeschooler.runner import Runner, parse_tasks


if __name__ == "__main__":
    task_definition = sys.stdin.readlines()
    r = Runner()
    r.set_tasks(parse_tasks(task_definition))
    r.run()
