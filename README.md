# homeschooler
ThoughtWorks Shokunin Challenge July 2020

Solves the homeschool task allocation problem.

## Set up

1. Clone this repo (to `./homeschooler`)
2. Create and activate a Python 3.6+ Virtual Environment (`virtualenv -p python3 homeschooler`
   then `source homeschooler/bin/activate`
3. From repo base directory (`cd homeschooler`)
4. Run `pip install .`

## Run

You can run the submission as below.

```
python src/homeschooler.py < sample_tasks.txt
```

### Input

Input is read from stdin, terminated by EOF. Input format is a list of uniquely labelled task efforts (`label:effort`), over one or more lines, with individual tasks separated by whitespace. For example:

```
A:5 B:4 C:1 D:2 E:7 F:8 G:3
```

### Options

Note you can specify solver (breadth first search or simulated annealing), number of children, and max number of solution steps via command line options.

```
Options:
  --solver TEXT       Solver type. bfs or sa.
  --children INTEGER  Number of children.
  --steps INTEGER     Maximum solver steps.
  --help              Show this message and exit.
``` 

### Results

Sample results:

```
Yes
Child 1: Task D (2 points) + Task F (8 points) = 10 points
Child 2: Task E (7 points) + Task G (3 points) = 10 points
Child 3: Task A (5 points) + Task B (4 points) + Task C (1 points) = 10 points
```

## Test

```
cd test
python -m unittest discover .
```

## More

### Highlights

Designed for the discerning homeschooler:

* Children set to 3 but configurable, for whenever a different configuration of children is appealing
* Two solvers available - breadth first search & simulated annealing - to suit your homeschooling mood. Whether you feel like you're on the frontier, or it's just a roll of the dice
* Max number of solve steps is configurable, if you need an answer, any answer, quick

### Notes

Here's how I landed on this implementation:

* I first thought of some sort of swapping algorithm to balance pairs of tasks, but realised there were scenarios requiring complex multi-swaps, taking us further away from the solution in the process
* Thinking about optimisation, I was keen to try simulated annealing, so defined states & neighbours
* I played around with different hyperparams for simulated annealing, and compared it to brute force approach
* Decided instead to implement breadth first search as it was looking more like a graph problem and I had all the ingredients
* Some of this in the exploratory [notebook](https://github.com/safetydave/homeschooler/blob/main/homeschooler.ipynb), which also includes the bonus brute force solver, for those days you know which

What I would do next:

* Write a go script
* Experiment more with symmetry (n! symmetrical solutions for n children?) & limiting state space
* Visualise state space and search
