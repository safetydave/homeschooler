# homeschooler
ThoughtWorks Shokunin Challenge July 2020

Solves the homeschool task allocation problem with simulated annealing. Run the [notebook](https://github.com/safetydave/homeschooler/blob/main/homeschooler.ipynb) to execute the solution and extensions.

Solution is stochastic. Best heuristics (see comparison in notebook) solve sample problem in median ~36 steps (is that "quick" as per problem statement?)

Sample results:

```
Yes
Child 1: Task D (2 points) + Task F (8 points) = 10 points
Child 2: Task E (7 points) + Task G (3 points) = 10 points
Child 3: Task A (5 points) + Task B (4 points) + Task C (1 points) = 10 points
```

Todos:

1. Satisfy more awesomeness criteria
2. Reduce the search space for better performance, by...
3. ... exclude visited from candidates
4. ... exploit symmetry of assignments, eg swapping assignments between two children is equivalent state
5. ... exploit symmetry of tasks (not relevant above) where tasks of equal size can be swapped
