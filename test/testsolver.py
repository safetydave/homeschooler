import unittest

from homeschooler.assignment import assign_rro
from homeschooler.evaluator import Evaluator
from homeschooler.solver import bfs
from homeschooler.tasks import Tasks


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.n = 2
        self.t2y = Tasks(Tasks.TASKS_2_YES)
        self.evaluator = Evaluator(self.t2y, self.n)
        self.initial_assignment = assign_rro(self.t2y, self.n)

    def test_bfs(self):
        out = bfs(self.evaluator, self.initial_assignment, 2000)
        self.assertTrue(out[0])
