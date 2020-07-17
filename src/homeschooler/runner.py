from homeschooler.tasks import Tasks


# todo validate input
def parse_tasks(task_definition):
    t = {}
    for line in task_definition:
        for token in line.split():
            kv = token.split(':')
            t[kv[0]] = int(kv[1])
    return t


class Runner:
    NUM_CHILDREN = 3

    def __init__(self):
        self.tasks = None

    def set_tasks(self, t):
        self.tasks = Tasks(t)

    def run(self):
        print(self.tasks.t)
