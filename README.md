# homeschooler
ThoughtWorks Shokunin Challenge July 2020

Solves the homeschool task allocation problem, and more (see More section).

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

Designed with maximum ease and flexibility of homeschooling in mind:

* Children set to 3 but configurable 
* Two solvers available: breadth first search & simulated annealing

Also an exploratory [notebook](https://github.com/safetydave/homeschooler/blob/main/homeschooler.ipynb) with a third bonus brute force solver.

Todos:

0. Todos in `runner.py`
1. Satisfy more awesomeness criteria
2. Tune solver selection & parameters like temperature
3. Visualise search
