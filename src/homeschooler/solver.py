import math
import random
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


# simulated annealing solver stochastic exploring neighbours with reducing temp
def sim_anneal(evaluator, assignment, steps):
    solved = False
    candidate = assignment
    e0 = evaluator.energy(candidate)
    k = 0
    for k in range(steps):
        t = (k + 1.0) / steps
        if e0 == 0:
            solved = True
            break
        alternative = random.choice(neighbours(candidate, evaluator.n))
        e1 = evaluator.energy(alternative)
        prob_accept = 1 if e1 < e0 else math.exp(-(e1 - e0) / t)
        if prob_accept >= random.random():
            candidate = alternative
            e0 = e1

    return solved, candidate, k