# homeschooler
ThoughtWorks Shokunin Challenge July 2020

Solves the homeschool task allocation problem.

## Running Submission

### Set up Environment and Dependencies

1. Clone this repo (to `./homeschooler`)
2. Create and activate a Python 3.7+ Virtual Environment (`virtualenv -p python3 homeschooler`
   then `source homeschooler/bin/activate`
3. From repo base directory (`cd homeschooler`)
4. Run `pip install .`

### To Execute

```
python src/homeschooler.py < sample_tasks.txt
```

### To Run Tests

```
cd test
python -m unittest discover .
```

## Results

Sample results:

```
Yes
Child 1: Task D (2 points) + Task F (8 points) = 10 points
Child 2: Task E (7 points) + Task G (3 points) = 10 points
Child 3: Task A (5 points) + Task B (4 points) + Task C (1 points) = 10 points
```

## More

Run the [notebook](https://github.com/safetydave/homeschooler/blob/main/homeschooler.ipynb) to execute the solution and extensions.

Solution is stochastic. Best heuristics (see comparison in notebook) solve sample problem in median ~36 steps (is that "quick" as per problem statement?)

Todos:

1. Satisfy more awesomeness criteria
2. Reduce the search space for better performance, by...
3. ... exclude visited from candidates
4. ... exclude infeasible (eg not every child has a task) from candidates
5. ... exploit symmetry of assignments, eg swapping assignments between two children is equivalent state
6. ... exploit symmetry of tasks (not relevant above) where tasks of equal size can be swapped
7. ... then it probably looks more like BFS :D
