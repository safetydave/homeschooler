import numpy as np


class Evaluator:

    def __init__(self, tasks, n):
        self.tasks = tasks
        self.n = n
        self.target_efforts = [tasks.target_effort(n)] * n

    def loads(self, assignment):
        tks = self.tasks.keys_asc
        return tuple(sum([self.tasks.t[tks[i]] for i, t in enumerate(assignment) if t == c])
                     for c in range(self.n))

    def energy(self, assignment):
        deltas = np.array(self.loads(assignment)) - np.array(self.target_efforts)
        return sum(abs(deltas))

    def satisfies(self, assignment):
        return int(self.energy(assignment) > 0)

    def pretty_format(self, assignment):
        tks = self.tasks.keys_asc
        ls = self.loads(assignment)
        pretty_strings = []
        for i in range(self.n):
            ca = [j for j, c in enumerate(assignment) if c == i]
            ca_strings = ['Task {} ({} points)'.format(tks[j], self.tasks.t[tks[j]]) for j in ca]
            ca_str = ' + '.join(ca_strings)
            pretty_strings.append('Child {}: {} = {} points'.format(i + 1, ca_str, ls[i]))
        return '\n'.join(pretty_strings)
