import click
import sys
from homeschooler.runner import Runner, parse_tasks


@click.command()
@click.option('--solver', default='bfs', help='Solver type. bfs or sa.')
@click.option('--children', default=3, help='Number of children.')
@click.option('--steps', default=2000, help='Maximum solver steps.')
def run_with_params(solver, children, steps):
    r = Runner()
    task_definition = sys.stdin.readlines()
    r.set_tasks(task_definition)
    r.run(solver, children, steps)


if __name__ == "__main__":
    run_with_params()
