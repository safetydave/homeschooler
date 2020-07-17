# heuristic for a good place to start
def assign_round_robin_oscillating(tasks, n):
    assignment = [-1] * len(tasks.t)
    i = 0
    di = 1
    for k in tasks.t_efforts_desc:
        j = tasks.keys_asc.index(k)
        assignment[j] = i
        i = i + di
        if i >= n:
            i = i - di
            di = -1
        if i <= 0:
            i = i - di
            di = 1
    return tuple(assignment)


class Assignment:

    def __init__(self, a):
        self.a = a

    # Neighbours have just one task assigned to a different child
    def neighbours(self, n):
        return [tuple((a + r * (i == j)) % n for i, a in enumerate(self.a))
                for r in range(1, n) for j, _ in enumerate(self.a)]
