# assignment heuristic for a good place to start - round robin oscillating
def assign_rro(tasks, n):
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


# neighbours have just one task assigned to a different child
def neighbours(assignment, n):
    return [tuple((a + r * (i == j)) % n for i, a in enumerate(assignment))
            for r in range(1, n) for j, _ in enumerate(assignment)]
