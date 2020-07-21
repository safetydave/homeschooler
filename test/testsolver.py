import unittest

from homeschooler.assignment import assign_rro
from homeschooler.evaluator import Evaluator
from homeschooler.solver import bfs, sim_anneal
from homeschooler.tasks import Tasks


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        # few tasks
        # two children
        self.t2y = Tasks(Tasks.TASKS_2_YES)
        self.evaluator_2y = Evaluator(self.t2y, 2)
        self.initial_assignment_2y = assign_rro(self.t2y, 2)
        # three children
        self.evaluator_2_3n = Evaluator(self.t2y, 3)
        self.initial_assignment_2_3n = assign_rro(self.t2y, 3)
        # more tasks
        # three children
        self.t3y = Tasks(Tasks.TASKS_3_YES)
        self.evaluator_3y = Evaluator(self.t3y, 3)
        self.initial_assignment_3y = assign_rro(self.t3y, 3)
        # most tasks
        # two children
        self.t4y = Tasks(Tasks.TASKS_4_YES)
        self.evaluator_4_2y = Evaluator(self.t4y, 2)
        self.initial_assignment_4_2y = assign_rro(self.t4y, 2)
        # three children
        self.evaluator_4_3n = Evaluator(self.t4y, 3)
        self.initial_assignment_4_3n = assign_rro(self.t4y, 3)
        # four children
        self.evaluator_4_4y = Evaluator(self.t4y, 4)
        self.initial_assignment_4_4y = assign_rro(self.t4y, 4)


    def helper_test_function(self, solver_function):
        # few tasks
        # two children
        out = solver_function(self.evaluator_2y, self.initial_assignment_2y, 2000)
        self.assertTrue(out[0])
        out = solver_function(self.evaluator_2y, self.initial_assignment_2y, 0)
        self.assertFalse(out[0])
        # three children
        out = solver_function(self.evaluator_2_3n, self.initial_assignment_2_3n, 2000)
        self.assertFalse(out[0])
        # more tasks
        # three children
        out = solver_function(self.evaluator_3y, self.initial_assignment_3y, 2000)
        self.assertTrue(out[0])
        # most tasks
        # two children
        out = solver_function(self.evaluator_4_2y, self.initial_assignment_4_2y, 2000)
        self.assertTrue(out[0])
        # three children
        out = solver_function(self.evaluator_4_3n, self.initial_assignment_4_3n, 2000)
        self.assertFalse(out[0])
        # four children
        out = solver_function(self.evaluator_4_4y, self.initial_assignment_4_4y, 2000)
        self.assertTrue(out[0])

    def test_bfs(self):
        self.helper_test_function(bfs)

    def test_sim_anneal(self):
        self.helper_test_function(sim_anneal)
