from homeschooler.assignment import neighbours


# breadth first search traversing neighbours from initial assignment
def bfs(evaluator, assignment, steps):
    visited = []
    queue = []
    visited.append(assignment)
    queue.append(assignment)

    solved = False
    candidate = None
    k = 0
    while queue and k < steps:
        candidate = queue.pop(0)
        solved = evaluator.satisfies(candidate) == 0
        if solved:
            break
        k = k + 1
        for n in neighbours(candidate, evaluator.n):
            if n not in visited:
                visited.append(n)
                queue.append(n)

    return solved, candidate, k
