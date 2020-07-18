from homeschooler.assignment import assign_rro
from homeschooler.evaluator import Evaluator
from homeschooler.solver import bfs, sim_anneal
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

    def set_tasks(self, task_definition):
        t = parse_tasks(task_definition)
        self.tasks = Tasks(t)

    def run(self):
        evaluator = Evaluator(self.tasks, Runner.NUM_CHILDREN)
        initial_assignment = assign_rro(self.tasks, Runner.NUM_CHILDREN)
        out = bfs(evaluator, initial_assignment, 2000)
        if out[0]:
            print('Yes')
            print(evaluator.pretty_format(out[1]))
        else:
            print('No')
