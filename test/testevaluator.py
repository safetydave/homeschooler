import unittest

from homeschooler.assignment import Assignment
from homeschooler.evaluator import Evaluator
from homeschooler.tasks import Tasks


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.t2y = Tasks(Tasks.TASKS_2_YES)
        self.evaluator = Evaluator(self.t2y, 2)
        self.pos = Assignment((0, 1, 1))
        self.neg = Assignment((0, 0, 1))

    def test_loads(self):
        self.assertEqual(self.evaluator.loads(self.pos), (5, 5))
        self.assertEqual(self.evaluator.loads(self.neg), (6, 4))

    def test_energy(self):
        self.assertEqual(self.evaluator.energy(self.pos), 0)
        self.assertEqual(self.evaluator.energy(self.neg), 2)

    def test_satisfies(self):
        self.assertEqual(self.evaluator.satisfies(self.pos), 0)
        self.assertEqual(self.evaluator.satisfies(self.neg), 1)
